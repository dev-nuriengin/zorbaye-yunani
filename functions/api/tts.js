// Cloudflare Pages Function — same-origin TTS proxy for the Zorba book.
// Keeps the KurdishTTS key server-side (set TTS_API_KEY as a Pages secret).
// Browser POSTs { text } to /api/tts ; we add the fixed Kurmanji v4 voice +
// word timestamps, convert the raw PCM to WAV, and return base64 audio + timing.
//
// Adapted from the tts-kurdi proxy. Same-origin => no CORS needed.

const MAX_CHARS = 2000;          // a single book sentence is tiny; guard anyway
const COOLDOWN_MS = 1_000;       // gentle pacing between *new* fetches (cache => no call)
const DAILY_CAP = 400;           // generous per-IP daily ceiling for one reader
const SPEAKER_ID = 'kurmanji_236';
const MODEL_VERSION = 'v4';      // v4 required for word timestamps

function createWavHeader(pcmLength) {
  const sampleRate = 22050, numChannels = 1, bitsPerSample = 16;
  const byteRate = sampleRate * numChannels * (bitsPerSample / 8);
  const blockAlign = numChannels * (bitsPerSample / 8);
  const header = new ArrayBuffer(44);
  const view = new DataView(header);
  view.setUint32(0, 0x52494646, false);  // "RIFF"
  view.setUint32(4, 36 + pcmLength, true);
  view.setUint32(8, 0x57415645, false);  // "WAVE"
  view.setUint32(12, 0x666d7420, false); // "fmt "
  view.setUint32(16, 16, true);
  view.setUint16(20, 1, true);
  view.setUint16(22, numChannels, true);
  view.setUint32(24, sampleRate, true);
  view.setUint32(28, byteRate, true);
  view.setUint16(32, blockAlign, true);
  view.setUint16(34, bitsPerSample, true);
  view.setUint32(36, 0x64617461, false); // "data"
  view.setUint32(40, pcmLength, true);
  return new Uint8Array(header);
}

// Per-isolate rate limit (resets on cold start — good enough for one reader).
const rateLimitMap = new Map();

function checkRateLimit(key, now, today) {
  let entry = rateLimitMap.get(key);
  if (!entry || entry.day !== today) {
    entry = { day: today, count: 0, lastRequest: 0 };
    rateLimitMap.set(key, entry);
  }
  if (now - entry.lastRequest < COOLDOWN_MS) {
    const waitSec = Math.ceil((COOLDOWN_MS - (now - entry.lastRequest)) / 1000);
    return { ok: false, error: `Hêdî bisekine — ${waitSec}s`, status: 429 };
  }
  if (entry.count >= DAILY_CAP) {
    return { ok: false, error: `Sînorê rojane temam bû (${DAILY_CAP})`, status: 429 };
  }
  entry.count++;
  entry.lastRequest = now;
  return { ok: true, remaining: DAILY_CAP - entry.count };
}

export async function onRequestPost(context) {
  const { request, env } = context;

  let body;
  try { body = await request.json(); } catch { body = {}; }
  const text = (body.text || '').trim();

  if (!text) {
    return Response.json({ error: 'Deqa vala' }, { status: 400 });
  }
  if (text.length > MAX_CHARS) {
    return Response.json({ error: `Deq pir dirêj e (${text.length}/${MAX_CHARS})` }, { status: 400 });
  }

  const now = Date.now();
  const today = new Date().toISOString().slice(0, 10);
  const rlKey = request.headers.get('cf-connecting-ip')
    || request.headers.get('x-forwarded-for') || 'unknown';
  const rl = checkRateLimit(rlKey, now, today);
  if (!rl.ok) {
    return Response.json({ error: rl.error }, { status: rl.status, headers: { 'Retry-After': '2' } });
  }

  const apiKey = env.TTS_API_KEY;
  if (!apiKey) {
    return Response.json({ error: 'TTS_API_KEY nehatiye danîn' }, { status: 500 });
  }

  const upstream = await fetch('https://www.kurdishtts.com/api/tts-proxy', {
    method: 'POST',
    headers: { 'x-api-key': apiKey, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      speaker_id: SPEAKER_ID,
      model_version: MODEL_VERSION,
      include_timestamps: true,
    }),
  });

  if (!upstream.ok) {
    const errorText = await upstream.text();
    return Response.json({ error: `KurdishTTS: ${upstream.status} — ${errorText}` }, { status: upstream.status });
  }

  const data = await upstream.json();
  const base64Audio = data.audio;
  if (!base64Audio) {
    return Response.json({ error: 'Bersiv bê deng e' }, { status: 500 });
  }

  // base64 -> raw PCM bytes -> prepend WAV header -> base64 WAV for JSON transport
  const binary = atob(base64Audio);
  const pcm = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i++) pcm[i] = binary.charCodeAt(i);

  const wavHeader = createWavHeader(pcm.length);
  const wav = new Uint8Array(wavHeader.length + pcm.length);
  wav.set(wavHeader, 0);
  wav.set(pcm, wavHeader.length);

  let wavBase64 = '';
  const chunk = 8192;
  for (let i = 0; i < wav.length; i += chunk) {
    wavBase64 += String.fromCharCode(...wav.subarray(i, i + chunk));
  }
  wavBase64 = btoa(wavBase64);

  return Response.json(
    { audio: wavBase64, timestamps: data.timestamps || [], audio_duration: data.audio_duration || null },
    { status: 200, headers: { 'X-RateLimit-Remaining': String(rl.remaining) } }
  );
}
