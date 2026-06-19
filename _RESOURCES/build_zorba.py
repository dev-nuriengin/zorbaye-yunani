# -*- coding: utf-8 -*-
import html, re, io, sys, os

CH10 = r"""
##PG 72
##FIRST
«Vêca çi ev afirand: ev labîrenta dudiliyê, ev perestgeha pozbilindiyê, ev cêra gunehan, ev zeviya ku hezar xap tê de hatine çandin, ev deriyê dojehê, ev selîka ku ji fêlbaziyê tije ye, ev jehra ku tama wê wek hingiv e, ev zincîra ku mirovan bi erdê ve girê dide: jin?» ||| "What then created this labyrinth of hesitation, this temple of presumption, this pitcher of sin, this field sown with a thousand deceptions, this gateway to Hell, this basket overflowing with artfulness, this poison which tastes like honey, this bond which chains mortals to the earth: woman?"
Min hêdî hêdî, bêdeng ev strana Bûdayî ji nû ve dinivîsî, li ser erdê li nêzî mangalê rûniştî bûm. ||| I was slowly, silently copying this Buddhist song, sitting on the ground near the brazier.
Min efsûn li ser efsûnê diceriband, dixwest wêneyê laşê jinekê yê ji baranê şilbûyî ji hişê xwe biavêjim — ew wêneyê ku her şev di wê payîzê de di hewaya şil de li ber çavên min diçû û dihat, bi hejîna ranan. ||| I was trying exorcism upon exorcism, bent on casting out from my mind the image of a woman's body soaked by the rain, which every night that fall passed in the humid air to and fro before my eyes with swaying hips.
Ji wê rojê ku gal hilweşiya û jiyana min hema hema qut bû ve, min jinebî di xwîna xwe de hîs dikir. ||| Ever since the collapse of the gallery, when my life had nearly been cut short, I sensed the widow in my blood.
Wek heywanekî hov gazî min dikir, bi lez û bi gilî. ||| She called to me like a wild animal, pressingly and reproachfully.

«Were! Were!» diqîriya. ||| "Come! Come!" she cried.
«Jiyan wek birûskê derbas dibe. Bi lez were, were, were, berî ku pir dereng bibe!» ||| "Life passes in a flash. Come quickly, come, come, before it is too late!"

Min baş dizanî ku ev Mara bû, ruhê Xerabiyê, di şiklê jinekê de bi ran û qûnên bihêz. ||| I was well aware that it was Mara, the spirit of the Evil One, in the shape of a woman with powerful thighs and buttocks.
Min li dijî wî şer dikir. ||| I fought against him.
Min xwe da nivîsandina Bûda, çawa ku mirovên hov di şkeftên xwe de bi kevirekî tûj heywanên birçî û dirinde yên ku li dora wan digeriyan dikolan an bi sor û spî dinexşandin. ||| I applied myself to writing Buddha in the same way that savages in their caves engraved with a pointed stone or painted in red and white the famished and ferocious beasts who prowled around them.
Wan jî hewl dida ku bi kolan û nexşandina van heywanan, wan li ser zinaran bi cih bikin. ||| They, too, endeavored, by engraving and painting these beasts, to fix them fast on the rock.
Eger wan wisa nekira, dê heywanan xwe bavêtina ser wan. ||| If they had not done so, the beasts would have leapt upon them.

Ji roja ku ez hema hema bin axê de nemam ve, jinebî bê navber di hewaya agirîn a tenêtiya min de derbas dibû, gazî min dikir û ranên xwe bi şehwet dihejand. ||| From the day I had just missed being crushed to death, the widow passed ceaselessly in the fiery air of my solitude, beckoning to me and voluptuously swaying her hips.
Bi roj ez bihêz bûm, hişê min şiyar bû û min karî ku wê biavêjim. ||| During the day I was strong, my mind was alert and I managed to cast her out.
Min dinivîsî ka Ceribkar bi çi awayî li ber Bûda xuya bû, çawa şiklê jinekê girt, çawa memikên xwe yên hişk li çokên zahid pêçandin, çawa Bûda metirsî dît, hemû hêza xwe kom kir û Xerabî têk bir. ||| I wrote in what guise the Tempter appeared to Buddha, how he took on the shape of a woman, how he pressed his firm breasts against the knees of the ascetic, how Buddha saw the danger, mobilized all his powers and routed the Evil One.

Her hevokek ku min dinivîsî rihetiyeke nû dida min, min wêrekî digirt, min hîs dikir ku Xerabî paşde diçû, bi efsûna hêzdar a peyvê hatibû avêtin. ||| Each sentence I wrote brought me fresh relief, I took courage, I felt the Evil One was withdrawing, cast out by the all-powerful exorcism of the word.
##PG 73
Bi roj min bi hemû hêza xwe şer dikir, lê bi şev hişê min çekên xwe datanîn, deriyên hundir vedibûn û jinebî dikete hundir. ||| I fought during the daytime with all my strength, but at night my mind laid down its arms, the inner doors opened and the widow entered.
Sibehê ez westiyayî û têkçûyî hişyar dibûm, û têkoşîn ji nû ve dest pê dikir. ||| In the morning I awoke exhausted and vanquished, and the struggle began afresh.

Çaxê min serê xwe ji kaxezê bilind dikir, dawiya êvarê bû; ronahî dihate qewirandin; tarî ji nişkê ve bi ser min de dadiket. ||| When I raised my head from my paper, it was the end of the afternoon; the light was being chased away; darkness suddenly fell upon me.
Roj kurt dibûn, Sersal nêzîk dibû. ||| The days were shortening, Christmas was approaching.
Min xwe bi hemû hêza xwe avêt nav têkoşînê. ||| I threw myself with all my might into the struggle.
Min ji xwe re digot: ez ne tenê me. ||| I said to myself: I am not alone.
Hêzeke mezin, ronahiya rojê, jî şer dike. ||| A great force, the light of day, is also fighting.
Ew jî carinan têk diçe, carinan bi ser dikeve. ||| It, too, is sometimes vanquished, sometimes victorious.
Lê hêviya xwe winda nake. ||| But it does not despair.
Ez bi ronahiyê re têkoşîn dikim û hêvî dikim! ||| I struggle and hope together with the light!

Wisa dihat ber min, û ev fikir wêrekî dida min, ku di şerê li dijî jinebiyê de ez jî bi ahengeke mezin a gerdûnî re hevdeng bûm. ||| It seemed to me, and this thought gave me courage, that in fighting against the widow I, too, was obeying a great universal rhythm.
Min fikirî: maddeya fêlbaz vî laşî hilbijartiye, da ku hêdî hêdî wî agirê azad ê ku di hundirê min de dibiriqe vemirîne. ||| Guileful matter has chosen this body, I thought, slowly to dampen and extinguish the free flame which flickers within me.
Min ji xwe re got: hêza nemir a ku maddeyê dike ruh, ya xwedayî ye. ||| I said to myself: The imperishable force which transforms matter into spirit is divine.
Her mirovekî di hundirê xwe de hêmaneke ji wî bagerê xwedayî heye, û bi vî awayî dikare nan, av û goşt veguherîne fikir û kar. ||| Each man has within him an element of the divine whirlwind and that is how he can convert bread, water and meat into thought and action.
Zorba rast digot: «Bibêje min tu bi tiştê ku dixwî çi dikî, ezê bibêjim tu kî yî!» ||| Zorba was right: "Tell me what you do with what you eat and I will tell you who you are!"
Û wisa min bi zehmetî hewl dida ku wê daxwaza tund a goşt veguherînim Bûda. ||| And so I was painfully endeavoring to transform that violent desire of the flesh into Buddha.

«Tu li ser çi difikirî, axa? Tu ne wek xwe yî,» Zorba di şeva berî Sersalê de got. ||| "What are you thinking about, boss? You don't seem to be quite yourself," Zorba said to me on Christmas Eve.
Wî texmîneke jîr dikir ka ez li dijî kîjan cinî şer dikim. ||| He had a shrewd idea as to what demon I was fighting.
Min xwe wisa nîşan da ku min nebihîst. ||| I pretended not to hear.
Lê Zorba ne ew kes bû ku wisa hêsanî dest jê berde. ||| But Zorba did not give up so easily.

«Tu ciwan î, axa,» got. ||| "You're young, boss," he said.
Û ji nişkê ve dengê wî tehl û bi hêrs bû. ||| And suddenly his voice assumed a bitter and angry tone.
«Tu ciwan î û pir saxlem î, baş dixwî, baş vedixwî, hewaya behrê ya geş dikişînî hundir, û hêz kom dikî — lê tu bi vê hemûyê çi dikî? ||| "You're young and pretty tough, eating well, drinking well, breathing exhilarating sea air, and storing up energy -- but what are you doing with it all?
Tu bi tenê radizê, û ev heyf e ji wê hêzê re! ||| You sleep alone, and it's just too bad for the energy!
Îşev here wir — erê, wextê xwe winda neke! ||| You get along there tonight -- yes, lose no time!
Axa, her tişt di vê dinyayê de hêsan e. ||| Boss, everything's simple in this world.
Çend caran divê ez ji te re bibêjim? ||| How many times must I tell you?
Loma neçe û tiştan tevlihev neke!» ||| So don't go and complicate things!"

Destnivîsa Bûda li ber min vekirî bû û min pelên wê diqulibandin dema ku ez li gotinên Zorba guhdarî dikim, û min fêm dikir ku ew rêyeke piştrast, dilkêş û pir mirovî nîşanî min didin. ||| The manuscript of Buddha was open in front of me and I turned over its leaves as I listened to Zorba's words and realized that they showed me a sure, attractive and very human path to tread.
Dîsa ruhê Mara bû, ew dehfdarê fêlbaz, ku gazî dikir. ||| It was again the spirit of Mara, the crafty pander, who was calling.
Min bê tu peyvê guhdarî dikir û hêdî hêdî pelên destnivîsê diqulibandin. ||| I listened without saying a word and continued slowly to turn the pages of the manuscript.
Min fîk lê dixist da ku hestên xwe veşêrim. ||| I whistled to conceal my emotion.

Lê Zorba, çaxê dît ku ez napeyivim, ji nişkê ve teqiya: «Ev şeva berî Sersalê ye, hevalê min, lezê bike, berî ku ew here dêrê xwe bigihîne wê. Îşev Îsa dê çêbibe, axa; tu jî here û keramata xwe bike!» ||| But Zorba, seeing I did not speak, suddenly burst out: "This is Christmas Eve, my friend, hurry up, get to her before she goes to church. Christ will be born tonight, boss; you go and perform your miracle, too!"

Ez bi acizî rabûm. ||| I rose, irritated.
«Bes e, Zorba,» min got. ||| "That's enough, Zorba," I said.
«Her kes li gor xwesleta xwe diçe. ||| "Every one follows his own bent.
Mirov wek darekê ye. ||| Man is like a tree.
Tu tu caran bi dara hêjîrê re pev neçûyî ji ber ku gêlas nade, ne wisa? ||| You've never quarrelled with a fig tree because it doesn't bear cherries, have you?
Vêca, bes e! ||| Well then, that'll do!
Hema hema nîvê şevê ye. ||| It's nearly midnight.
Em herin dêrê û em bi xwe bibînin ka Îsa çawa çêdibe.» ||| Let us go to the church and see Christ born ourselves."

Zorba kumê xwe yê stûr ê zivistanê li serê xwe kişand. ||| Zorba pulled his thick winter cap over his head.
«Baş e, vêca!» bi xemgînî got. ||| "All right, then!" he said unhappily.
«Em herin! ||| "Let's go!
Lê ez dixwazim tu bizanî ku Xwedê dê pir bêtir kêfxweş bûya eger tu îşev mîna Cebraîlê milyaket biçûya ba jinebiyê. ||| But I want you to know that God would have been much more pleased if you'd gone to the widow's tonight, like Archangel Gabriel.
Eger Xwedê jî heman rê wek te bigirta, axa, ew tu caran neçûya ba Meryemê ||| If God had followed the same path as you, boss, he'd never have gone to Mary's
##PG 74
û Îsa tu caran çênedibû. ||| and Christ would never have been born.
Eger tu ji min bipirsî ka Xwedê li ser kîjan rê dimeşe, ezê bibêjim: ya ku diçe ba Meryemê. ||| If you asked me what path God follows, I'd say: the one leading to Mary's.
Meryem ew jinebî ye.» ||| Mary is the widow."

Bê fêde û bêdeng li bersiva min sekinî. ||| He waited in silence and in vain for my reply.
Derî bi hêz vekir û derket. ||| He thrust the door open, and he went out.
Bi serê gopalê xwe bi hêrs li keviran dixist. ||| He angrily struck at the pebbles with the end of his stick.
«Erê,» bi israr dubare kir, «Meryem ew jinebî ye!» ||| "Yes," he repeated persistently, "Mary is the widow!"

«Vêca, em herin!» min got. «Neqîre!» ||| "Now, let's get along!" I said. "Don't shout!"

Em di şeva zivistanê de bi lezeke baş dimeşiyan. ||| We strode along at a good pace in the winter night.
Ezman bi temamî zelal bû, stêrk mezin xuya dikirin û nizm li ezmanan daleqandî bûn wek gûyên agir. ||| The sky was perfectly clear, the stars looked big and hung low in the sky like balls of fire.
Şev, dema ku em li ber peravê diçûn, dişibiya heywanekî reş ê mezin ê ku li ber lêva avê dirêj bûyî. ||| The night, as we made our way along the shore, resembled a great black beast lying along the water's edge.

«Ji îşev ve,» min ji xwe re got, «ronahiya ku zivistanê paşde avêtibû, dê dest bi şereke serketî bike. Mîna ku ev şev bi xwedayê pitik re çêbûbe.» ||| "From tonight," I said to myself, "the light which winter has forced back will begin to fight victoriously. As if it were born this night together with the infant god."

Hemû gundî li hundirê dêrê yê germ û bîhnxweş kom bûbûn. ||| All the villagers had crowded into the warm and scented hive of the church.
Mêr li pêş sekinîbûn û jin, bi destên girêdayî, li paş. ||| The men stood in front and the women, with clasped hands, behind.
Keşîşê dirêj, Stefanos, piştî rojiya çil rojan di rewşeke pir aciz de bû. ||| The tall priest, Stephanos, was in an exasperated state after his forty-days' fast.
Bi rîda xwe ya zêrîn a giran, bi gavên mezin vir û wê de direvî, bixûrdana xwe dihejand, bi dengê herî bilind distira û pir bilez bû ku bibîne Îsa çêdibe û here malê ji bo şorbeyeke stûr, sosîsên bîhnxweş û goştên dûkêşkirî.... ||| Clad in his heavy gold chasuble, he was running hither and thither in great strides, swinging his censer, singing at the top of his voice and in a great hurry to see Christ born and get home to a thick soup, savory sausages and smoked meats....

Eger di pirtûkên pîroz de hatibûya gotin: «Îro, ronahî çêdibe,» dilê mirov dê neperikiya. ||| If the scriptures had said: "Today, light is born," man's heart would not have leapt.
Ev fikir dê nebûya efsane û dê dinya dest nexista. ||| The idea would not have become a legend and would not have conquered the world.
Wan tenê dê diyardeyeke fizîkî ya asayî teswîr bikira û dê xeyala me — yanî ruhê me — neşewitanda. ||| They would merely have described a normal physical phenomenon and would not have fired our imagination -- I mean our soul.
Lê ronahiya ku di dilê zivistanê de çêdibe bûye zarok û zarok bûye Xwedê, û bîst sedsalan e ku ruhê me wê dimije.... ||| But the light which is born in the dead of winter has become a child and the child has become God, and for twenty centuries our soul has suckled it....

Merasîma nepenî demek piştî nîvê şevê bi dawî bû. ||| The mystic ceremony came to an end shortly after midnight.
Îsa çêbûbû. ||| Christ had been born.
Gundiyên birçî û bextewar bi bezê çûn malê, da ku xwarinekê bixwin û di kûrahiya hinava xwe de razê bedenbûnê hîs bikin. ||| The famished and happy villagers ran home, to have a feast and feel in the depths of their bowels the mystery of incarnation.
Zik bingehê hişk e; nan, şerab û goşt tiştên herî pêwîst in; tenê bi nan, şerab û goşt mirov dikare Xwedê biafirîne. ||| The belly is the firm foundation; bread, wine and meat are the first essentials; it is only with bread, wine and meat that one can create God.

Stêrk mezin wek milyaketan li ser qubeya spî ya dêrê dibiriqîn. ||| The stars were shining as large as angels above the white dome of the church.
Rêya Kadîz wek çemekî ji aliyekî ezman heta yê din diherikî. ||| The milky way was flowing like a stream from one side of the heavens to the other.
Stêrkeke kesk li jorê me wek zimrûdekê dibiriqî. ||| A green star was twinkling above us like an emerald.
Min axîn kişand, dîlê hestên xwe. ||| I sighed, a prey to my emotions.

Zorba berê xwe da min. ||| Zorba turned to me.
«Axa, tu bawer dikî? Ku Xwedê bûye mirov û di tewleyekê de çêbûye? Tu bawer dikî, an tu tenê me dixapînî?» ||| "Boss, d'you believe that? That God became man and was born in a stable? Do you believe it, or are you just pulling our legs?"

«Zehmet e mirov bibêje, Zorba,» min bersiv da. ||| "It's difficult to say, Zorba," I replied.
«Ez nikarim bibêjim ez bawer dikim, ne jî ku nakim. Tu çawa?» ||| "I can't say I believe it, nor that I don't. What about you?"

«Ez jî nikarim bibêjim ez dikim. ||| "I can't say I do either.
Bi tu awayî nikarim. ||| I can't for the life of me.
Binêre, dema ez zarok bûm û dapîra min çîrok ji min re digotin, min peyvek jî bawer nedikir. ||| You see, when I was a kid and my grandma told me tales, I didn't believe a word of them.
Û dîsa jî ez ji heyecanê dilerizîm, ez dikeniyam û ez digiriyam, mîna ku min bawer dikira. ||| And yet I trembled with emotion, I laughed and I cried, just as if I did believe them.
Çaxê rî li çenê min hat, min ew berdan, min heta pê dikeniya jî; lê niha, di pîrbûna xwe de — texmîn dikim ez nerm dibim, ne wisa axa? — bi awayekî ez dîsa bawer dikim.... ||| When I grew a beard on my chin, I just dropped them, and I even used to laugh at them; but now, in my old age -- I suppose I'm getting soft, eh, boss? -- in a kind of way I believe in them again....
Mirov sirr e!» ||| Man's a mystery!"

Me rêya ku diçû mala Madam Hortans girtibû û em wek du hespên birçî yên ku bîhna tewleyê digirin dest bi bezê kirin. ||| We had taken the path leading to Dame Hortense's and we started galloping along like two hungry horses who can smell the stable.
«Bavên pîroz pir fêlbaz in, tu dizanî!» Zorba got. ||| "The holy fathers are pretty crafty, you know!" Zorba said.
«Bi rêya zikê te xwe digihînin te, vêca tu çawa ji wan xilas dibî? ||| "They get at you through your belly, so how can you escape them?
Çil rojan, dibêjin, ||| For forty days, they say,
##PG 75
goşt naxwî, şerabê venaxwî; tenê rojî bigire. ||| you shan't eat meat, you shan't drink wine; just fast.
Çima? ||| Why?
Da ku tu ji bo goşt û şerabê bikevî hesretê. ||| So that you'll pine for meat and wine.
Ax, berazên qelew, ew hemû fêlên lîstikê dizanin!» ||| Ah, the fat hogs, they know all the tricks of the game!"

Wî hê bileztir dest bi meşê kir. ||| He started going even faster.
«Em bilezînin, axa,» got. ||| "Let's get moving, boss," he said.
«Divê elok niha tam pijiyabe!» ||| "The turkey must be done to a turn!"

Çaxê em gihîştin odeya xanima me ya delal, bi nivîna xwe ya mezin a dilkêş, me mase bi qumaşekî spî nixumandî dît, û li ser wê elok germ-germ li ser pişta xwe rakirî bû, lingên wê ji hev vekirî. ||| When we arrived in our good lady's room, with its great tempting bed, we found the table covered with a white cloth, and on it the steaming turkey lying on its back with its legs apart.
Mangal germahiyeke nerm belav dikir. ||| The brazier was giving off a gentle heat.
Madam Hortans porê xwe lewitandibû û kirasekî dirêj ê pembeyê çilmisî yê bi destikên mezin û tevneyên qetiyayî li xwe kiribû. ||| Dame Hortense had curled her hair and was wearing a long dressing gown of faded pink color with enormous sleeves and frayed lacework.
Li dora situyê xwe yê qermiçandî bendeke teng a zer-kenarî, qasî bejna du tiliyan, hebû. ||| Round her wrinkled neck was a tight, canary-yellow ribbon, about the width of two fingers.
Wê bi camêrî ava kulîlka pirteqalê li xwe reşandibû. ||| She had sprayed herself generously with orange-blossom water.

Çiqas her tişt li ser vê erdê bi temamî li hev tê, min fikirî. ||| How perfectly everything is matched on this earth, I thought.
Çiqas erd bi dilê mirov re li hev tê! ||| How well the earth is matched to the human heart!
Va ye ev stranbêja kabareyê ya pîr a ku jiyaneke pir bilez derbas kiriye, û niha, li vê peravê tenê hatî avêtin, di vê odeya reben de hemû xema pîroz û germahiya jinaniyê kom dike. ||| Here is this old cabaret singer who has led a thoroughly fast life, and now, cast up on this lonely coast, she concentrates in this miserable room all the sacred solicitude and warmth of womanhood.
Xwarina bol û bi baldarî amadekirî, mangala dişewite, laşê boyaxkirî û xemilandî, bîhna kulîlka pirteqalê — bi çi lezê û bi çi sadetiyê ev hemû kêfên biçûk, bedenî û pir mirovî diguherin nav şahiyeke mezin a ruhanî! ||| The copious and carefully prepared repast, the burning brazier, the painted and pennanted body, the orange-blossom scent -- with what rapidity and what simplicity all these very human, little, corporeal pleasures are transformed into a great spiritual joy!

Dilê min ji nişkê ve di sîngê min de perikî. ||| My heart suddenly leaped in my breast.
Min di wê êvara bi rûmet de hîs kir ku ez li vir li ser vê peravê vala ne bi tena serê xwe me. ||| I felt, on that solemn evening, that I was not quite alone here on this deserted seashore.
Afirîdek tije dilsoziya jinanî, dilovanî û sebir ber bi min de dihat: ew dê, xwişk û jin bû. ||| A creature full of feminine devotion, tenderness and patience was coming toward me: she was the mother, the sister, the wife.
Û ez, ê ku digot pê re ne hewceyî tiştekî me, ji nişkê ve hîs kir ku ez hewceyî her tiştî me. ||| And I, who thought I needed nothing, suddenly felt I needed everything.

Diviya Zorba jî hesteke wisa hîs kiribe, çimkî hema em ketin odeyê, ew bezî ber bi stranbêja xemilandî ve û hembêz kir. ||| Zorba must have felt a like emotion, for scarcely had we entered the room than he rushed to the bedecked cabaret-singer and hugged her.
«Îsa çêbû!» qîriya. ||| "Christ is born!" he cried.
«Silav li te, mêya cinsê me!» ||| "Greetings to you, female of the species!"
Berê xwe da min, dikeniya. ||| He turned to me, laughing.
«Binêre, axa, jin çi afirîdeke fêlbaz e! Ew dikare Xwedê jî li dora tiliya xwe ya biçûk bipêçe!» ||| "See, boss, what a cunning creature is woman! She can even twist God round her little finger!"

Em li ber masê rûniştin; me xwarin bi birçîtî xwarin û şerab vexwar. ||| We sat down at table; we hungrily devoured the dishes and drank the wine.
Laşên me têr bûn û ruhên me ji kêfê diricifîn. ||| Our bodies were satisfied and our souls thrilled with pleasure.
Zorba dîsa geş bû. ||| Zorba became lively once more.
«Bixwe û vexwe,» bê navber diqîriya. ||| "Eat and drink," he continually shouted.
«Bixwe û vexwe, axa, û germ bibe! Tu jî bistirê, kuro, wek şivanan bistirê: ‹Rûmet ji yê herî jor re!... Rûmet ji yê herî nizm re...› ||| "Eat and drink, boss, and get warmed up! You sing too, my boy, sing like the shepherds: 'Glory to the highest!... Glory to the lowest...'
Îsa çêbû, ev tiştekî ecêb e, tu dizanî. ||| Christ is born, that's a terrific thing, you know.
Stranê bilind bike û bila Xwedê te bibihîze û şa bibe.» ||| Pipe up with your song and let God hear you and rejoice."

Wî bi temamî kêfa xwe vegerandibû, û rawestandina wî tune bû. ||| He had quite recovered his spirits, and there was no stopping him.
«Îsa çêbû, Silêmanê min ê zana, mirîzê min ê reben ê qeleman! ||| "Christ is born, my wise Solomon, my wretched pen-pusher!
Tiştan bi derziyê hilnede! ||| Don't go picking things over with a needle!
Çêbûye an çênebûye? ||| Is He born or isn't He?
Helbet çêbûye, dîn nebe. ||| Of course He's born, don't be daft.
Eger tu camekê bigirî û li ava vexwarina xwe binêrî — endezyarekî rojekê ev ji min re got — tê bibînî, got, av tije kurmikên biçûk e ku tu bi çavê tazî nikarî bibînî. ||| If you take a magnifying-glass and look at your drinking water -- an engineer told me this, one day -- you'll see, he said, the water's full of little worms you couldn't see with your naked eye.
Tê kurmikan bibînî û tê venexwî. ||| You'll see the worms and you won't drink.
Tê venexwî û tê ji tîbûnê bibirûzî. ||| You won't drink and you'll curl up with thirst.
Camê bişkêne, axa, û kurmikên biçûk dê winda bibin û tê bikarî vexwî û rehet bibî!» ||| Smash your glass, boss, and the little worms'll vanish and you can drink and be refreshed!"

##PG 76
Berê xwe da hevala me ya xemilandî, qedeha xwe ya tije bilind kir û got: «Bûbûlîna min a pir delal, hevala min a kevn a şer, ez dixwazim li ser tenduristiya te vexwim! ||| He turned towards our gaudy companion, raised his full glass and said: "My very dear Bouboulina, my old comrade-in-arms, I'm going to drink to your health!
Min di jiyana xwe de gelek peykerên pêşiya keştiyê dîtine; ew li serê keştiyê hatine mîxkirin, memikên xwe di destên xwe de digirin, û rû û lêvên wan bi sorahiyeke agirîn boyaxkirî ne. ||| I've seen many figureheads in my life; they're nailed to the ship's prow, they hold their breasts in their hands, and the cheeks and lips are painted a fiery red.
Wan li ser hemû behran rê kiriye, ketine her benderê, û çaxê keştî ket perçe-perçe, ew tên ser hişkayê û, heta dawiya rojên xwe, li dîwarê meyxaneyeke masîgirekî paldayî dimînin, ku kaptan tên wir vedixwin. ||| They've sailed over all the seas, they've entered every port, and when the ship falls to bits they come on dry land and, till the end of their days, stay leaning against the wall of a fisherman's tavern where the captains go to drink.
Bûbûlîna min, îşev, dema ku ez te li ser vê peravê dibînim, niha ku zikê min tije tiştên xweş e û çavên min vekirî ne, tu ji min re wek peykera keştiyeke mezin xuya dikî. ||| My Bouboulina, tonight, as I see you on this shore, now my belly's full of good things and my eyes are wide open, you look to me like the figurehead of a great ship.
Û ez bendera te ya dawî me, ez ew meyxane me ku kaptanên behrê tên vedixwin. ||| And I am your last port, I am the tavern where the sea captains come to drink.
Were, xwe bide ser min, kelekên xwe daxe! ||| Come, lean on me, strike your sails!
Ez vê qedeha şeraba Krêtayî li ser tenduristiya te vedixwim, sîrena min!» ||| I drink this glass of Cretan wine to your health, my siren!"

Bi hest û bê hêz, Madam Hortans dest bi giriyê kir û xwe da ser milê Zorba. ||| Touched and overcome, Dame Hortense started to cry, and leaned on Zorba's shoulder.
«Tu ê bibînî, axa,» Zorba di guhê min de pist-pist kir, «axaftina min a xweş dê min têxe nav hin derdan. ||| "You just see, boss," Zorba whispered in my ear, "my fine speech is going to land me into some trouble.
Ev dê îşev nexwaze min berde. ||| The jade won't want to let me go tonight.
Lê, ev e, dilê min bi vê afirîdê reben dişewite, erê, ez dilovaniya wan dikim!» ||| But, there you are, I'm sorry for the poor creatures, yes, I pity them!
«Îsa çêbû!» bi dengekî bilind ji sîrena xwe re qîriya. «Li ser tenduristiya me!» ||| "Christ is born!" he shouted loudly to his siren. "To our health!"
Wî milê xwe xiste bin milê xanima me û wan bi hev re qedehên xwe vexwarin, mil di mil de, û bi heyecan li hev dinêrîn. ||| He slipped his arm under that of our lady and they quaffed their glasses together, arms entwined, and looking enraptured at each other.

Spêde ne dûr bû dema ku min ew her du li wê odeya razanê ya germ a biçûk bi nivîna wê ya mezin hiştin û rêya malê girt. ||| Dawn could not have been far off when I left the two of them in the warm little bedroom with its great bed and took the road home.
Gundiyan baş xwaribû û vexwaribû, û niha gund radiza bi derî û pencereyên girtî, di bin stêrkên mezin ên zivistanê de. ||| The villagers had eaten and drunk well, and now the village was sleeping with doors and windows closed, under the great winter stars.
Sar bû, behr dixuriya, Zuhre bi şeytanetî li rojhilatê dans dikir. ||| It was cold, the sea was booming, Venus was dancing roguishly in the east.
Ez li ber lêva avê dimeşiyam û bi pêlan re dilîstim. ||| I walked along the water's edge playing a game with the waves.
Ew dibezîn da ku min şil bikin û ez direviyam. ||| They ran up to try and wet me and I ran away.
Ez bextewar bûm û min ji xwe re got: «Ev bextewariya rastîn e: ku tu tu armanc nebî û dîsa wek hespekî bixebitî mîna ku hemû armancên te hebin. ||| I was happy and said to myself: "This is true happiness: to have no ambition and to work like a horse as if you had every ambition.
Ku tu dûrî mirovan bijî, ne hewceyî wan bî û dîsa jî ji wan hez bikî. ||| To live far from men, not to need them and yet to love them.
Ku tu beşdarî cejna Sersalê bibî û, piştî ku te baş xwar û vexwar, bi tena serê xwe ji hemû xefkan bireviyî, stêrk li jorê te, erd li milê çepê û behr li milê rastê te bin: û ji nişkê ve fêm bikî ku, di dilê te de, jiyanê keramata xwe ya dawî pêk aniye: ew bûye çîroka periyan.» ||| To take part in the Christmas festivities and, after eating and drinking well, to escape on your own far from all the snares, to have the stars above, the land to your left and the sea to your right: and to realize of a sudden that, in your heart, life has accomplished its final miracle: it has become a fairy tale."

Roj derbas dibûn. ||| The days were passing by.
Min hewl dida ku rûyekî wêrek nîşan bidim, ez diqîriyam û dînîtiyê dikim, lê di kûrahiya dilê xwe de min dizanî ku ez xemgîn im. ||| I tried to put a brave face on it, I shouted and played the fool, but in my heart of hearts I knew I was sad.
Di vê heftiya cejnan de, bîranîn şiyar bûbûn û sîngê min bi muzîkeke dûr û bi ezîzan tije kiribûn. ||| During all this week of festivities, memories had been aroused and filled my breast with distant music and loved ones.
Dîsa rastiya wê gotina kevn li min ket: dilê mirov çalek e tije xwîn. ||| I was once more struck by the truth of the ancient saying: Man's heart is a ditch full of blood.
Ezîzên ku mirine xwe diavêjin ser kêleka vê çalê da ku xwînê vexwin û wisa dîsa zindî bibin; çiqas ji te re ezîztir bin, ewqas xwîna te bêtir vedixwin. ||| The loved ones who have died throw themselves down on the bank of this ditch to drink the blood and so come to life again; the dearer they are to you, the more of your blood they drink.

Şeva Sersalê. ||| New Year's Eve.
Komeke zarokên gundê ku keştiyeke mezin a kaxezî hildigirtin hatin koxika me û bi dengên xwe yên tûj û şa dest bi stranên Sersalê kirin: «Aziz Vasîlê Mezin ji Qeyseriyê, bajarê xwe yê zikmakî, hat...» ||| A band of village children carrying a large paper boat came to our hut and started to sing kalanda in their shrill and merry voices: Saint Basil the Great arrived from Caesarea, his native city...
##PG 77
Ew li vir li ser vê peravê biçûk a Krêtayî li ber behra şîn a tarî sekinîbû. ||| He was standing here on this little Cretan beach by the indigo-blue sea.
Xwe da ser gopalê xwe û gopalê wî ji nişkê ve bi pel û kulîlkan nixumî. ||| He leaned on his staff and his staff was suddenly covered with leaves and flowers.
Strana Sersalê bilind bû: ||| The New Year's carol rang out:

##VERSE
Sala we ya nû pîroz be, Xiristiyanno!<br>Axa, bila mala te bi genim, zeyt û şerabê tije bibe;<br>bila jina te bibe stûneke mermerî ji banê mala te re;<br>bila keça te bizewice û neh kur û keçek bîne;<br>bila van kuran Konstantînopolîsê, bajarê padîşahên me, azad bikin! ||| A happy new year to you, Christians! Master, may your house be filled with corn, olive-oil and wine; May your wife be a marble pillar to the roof of your house; May your daughter marry and beget nine sons and one daughter; May these sons liberate Constantinople, the city of our kings!

Zorba bi heyecan guhdarî dikir. ||| Zorba listened, entranced.
Wî defa zarokan girtibû û bi dînîtî lê dixist. ||| He had seized the children's tambourine and was banging it frenziedly.
Min temaşe dikir û guhdarî dikir bê tu gotin. ||| I watched and listened without saying anything.
Min hîs dikir ku pelek din ji dilê min dikeve, derbasbûna saleke din. ||| I could feel another leaf falling from my heart, the passing of another year.
Ez gaveke din ber bi çalê reş ve dimeşiyam. ||| I was taking another step toward the black pit.
«Çi bi serê te hat, axa?» Zorba pirsî, di navbera stranê de ku bi dengê herî bilind bi zarokan re distira û li defê dixist. ||| "What's come over you, boss?" Zorba asked, in between singing at the top of his voice, together with the children, and striking the tambourine.
«Çi bi serê te hat, kuro? Tu bi salan kal xuya dikî, û rûyê te gewr bûye. ||| "What's come over you, man? You look years older, and your face is grey.
Ev ew dem e ku ez dîsa dibim kurikekî biçûk; ez ji nû ve çêdibim, wek Îsa. ||| This is when I turn into a little boy again; I'm reborn, like Christ.
Ma ew her sal çênabe? Ez jî wisa!» ||| Isn't he born every year? So am I!"

Ez li ser nivîna xwe razam û çavên xwe girtin. ||| I lay down on my bed and shut my eyes.
Dilê min wê şevê di hewayekî hov de bû; min nedixwest bipeyivim. ||| My heart was in a wild mood that night; I did not wish to speak.
Min nikaribû razêm. ||| I could not sleep.
Min hîs dikir ku divê ez heman şevê hesabê karên xwe bidim. ||| I felt I had to account for my acts that very night.
Min tevahiya jiyana xwe ji ber çavan re derbas kir, ku bêtam, bêhevseng û dudilî, wek xewnekê xuya dikir. ||| I went over my whole life, which appeared vapid, incoherent and hesitating, dreamlike.
Min bi bêhêvîtî lê nihêrî. ||| I contemplated it despairingly.
Wek ewrekî hirî ku ji ber bayên ji bilindahiyan tê êrişkirin, jiyana min bê navber şikil diguhert. ||| Like a fleecy cloud attacked by the winds from the heights, my life constantly changed shape.
Diket perçe-perçe, ji nû ve çêdibû, diguherî — bi dorê, qûyek, kûçikek, cinek, dûpişkek, meymûnek bû — û ewr her dem dihate qetandin. ||| It came to pieces, reformed, was metamorphosed -- it was, by turns, a swan, a dog, a demon, a scorpion, a monkey -- and the cloud was forever being frayed and torn.
Bi bayên ezman dihate ajotin û bi keskesorê dihate ronîkirin. ||| It was driven by the winds of heaven and shot with the rainbow.

Roj hilat. ||| Day broke.
Min çavên xwe venekirin. ||| I did not open my eyes.
Min hewl dida ku hemû hêza xwe li ser daxwaza xwe ya geş kom bikim — ku qalikê hiş bişkênim û têkevim wê kanala tarî û metirsîdar ku her dilopa mirovî pê tê birin da ku bi okyanusê re tev bibe. ||| I was trying to concentrate all my strength on my ardent desire to break through the crust of the mind and penetrate to the dark and dangerous channel down which each human drop is carried to mingle with the ocean.
Min dixwest perdeyê biçirînim û bibînim ka Sala Nû dê çi ji min re bîne.... ||| I was eager to tear the veil and see what the New Year would bring me....

«Sibe baş, axa. Sala te pîroz be!» ||| "Morning, boss. Happy New Year!"
Dengê Zorba ez bi hovîtî vegerandim erdê. ||| Zorba's voice brought me back brutally to earth.
Min çavên xwe vekirin tam di wextê de ku min dît Zorba hinarekî mezin avêt nav deriyê koxikê. ||| I opened my eyes just in time to see Zorba throw into the doorway of the hut a big pomegranate.
Tovên wê, wek yaqûtên zelal, heta nivîna min belav bûn. ||| Its seeds, like clear rubies, shot as far as my bed.
Min çend hilanîn û xwarin, û qirika min rehet bû. ||| I picked up a few and ate them, and my throat was refreshed.

«Ez hêvî dikim em pereyên gelek qezenc bikin û keçên bedew dilê me bibin!» Zorba bi kêfxweşî qîriya. ||| "I hope we make a pile and are ravished by beautiful maidens!" Zorba cried good-humoredly.
Xwe şuşt, rîya xwe taşt û cilên xwe yên herî baş li xwe kirin — şalekî kesk ê qumaş û çakêtekî ku li malê hatibû çêkirin, ku li ser wî kurkekî nîv-astarî yê ji çermê bizinê avêt. ||| He washed, shaved and put on his best clothes -- green cloth trousers and rough home-spun jacket, over which he threw a half-lined, goat-skin coatee.
Kumê xwe yê rûsî yê astraxan li xwe kir û simbêlên xwe badan. ||| He put on his Russian astrakhan cap and twirled his moustaches.
«Axa,» got, «ezê wek nûnerê Şirketê xwe li dêrê nîşan bidim. ||| "Boss," he said, "I'm going to put in an appearance at church as a representative of the Company.
Ne di berjewendiya kanê de ye ku ew bifikirin em farmason in. ||| It wouldn't be in the interest of the mine for them to think we're freemasons.
Ev tiştekî ji min naxwaze û dê wextê derbas bike.» ||| It'll cost me nothing and it'll pass the time."
Xwe xwar kir û çavê xwe qirpand. ||| He bent over and winked.
«Belkî ez jinebiyê jî li wir bibînim,» pist-pist kir. ||| "Maybe I'll see the widow there, too," he whispered.

Xwedê, berjewendiyên Şirketê û jinebî bi awayekî hevaheng di hişê Zorba de tev bûbûn. ||| God, the interests of the Company and the widow blended harmoniously in Zorba's mind.
Min dengê gavên wî yên sivik bihîst ku dûr dibûn. ||| I heard his light footsteps departing.
Ez rabûm ser xwe. ||| I leaped up.
Efsûn şikest, ruhê min ji nû ve di girtîgeha goşt de hat girtin. ||| The spell was broken, my soul was shut in the prison of the flesh anew.
Min cilên xwe li xwe kirin û çûm xwarê ber lêva avê. ||| I dressed and went down to the water's edge.
Ez bilez dimeşiyam. ||| I walked quickly.

##PG 78
Ez şa bûm, mîna ku ez ji metirsiyekê an ji gunehekî reviyabim. ||| I was gay, as if I had escaped from a danger or a sin.
Daxwaza min a bêedeb a wê sibehê — ku berî ku pêşeroj çêbibe têkevim navê û wê bizanim — ji nişkê ve ji min re wek kufrekê xuya bû. ||| My indiscreet desire of that morning to pry into and know the future before it was born suddenly appeared to me a sacrilege.
Min bîr anî sibehekê ku min di qalikê darekê de pîlek dît, tam dema ku perperok di doxa xwe de qulek çêdikir û xwe amade dikir ku derkeve. ||| I remembered one morning when I discovered a cocoon in the bark of a tree, just as the butterfly was making a hole in its case and preparing to come out.
Ez demekê li bendê mam, lê pir dirêj dikişand û ez bêsebir bûm. ||| I waited a while, but it was too long appearing and I was impatient.
Xwe xwar kirim û bi bîhna xwe lê kir da ku germ bikim. ||| I bent over it and breathed on it to warm it.
Min wek ku ji destê min dihat zû germ kir û keramat li ber çavên min dest pê kir, bileztir ji jiyanê. ||| I warmed it as quickly as I could and the miracle began to happen before my eyes, faster than life.
Dox vebû, perperok hêdî hêdî dest bi xişînê kir ku derkeve, û ez tu caran tirsa xwe ji bîr nakim çaxê min dît ka baskên wê çawa paşde pêçandî û qermiçandî bûn; perperoka reben bi tevahiya laşê xwe yê dilerizî hewl dida ku wan veke. ||| The case opened, the butterfly started slowly crawling out and I shall never forget my horror when I saw how its wings were folded back and crumpled; the wretched butterfly tried with its whole trembling body to unfold them.
Min xwe xwar kir, hewl da ku bi bîhna xwe alîkariya wê bikim. ||| Bending over it, I tried to help it with my breath.
Bê fêde. ||| In vain.
Diviya bû ew bi sebir derketa û vebûna baskan diviya bû di tavê de hêdî hêdî bûya. ||| It needed to be hatched out patiently and the unfolding of the wings should be a gradual process in the sun.
Niha pir dereng bû. ||| Now it was too late.
Bîhna min perperok mecbûr kiribû ku xuya bibe, hemû qermiçî, berî wextê xwe. ||| My breath had forced the butterfly to appear, all crumpled, before its time.
Bi bêhêvîtî têkoşiya û, çend saniye şûnde, di kefa destê min de mir. ||| It struggled desperately and, a few seconds later, died in the palm of my hand.

Ew laşê biçûk, ez bawer dikim, giraniya herî mezin e ku li ser wijdana min heye. ||| That little body is, I do believe, the greatest weight I have on my conscience.
Çimkî ez îro fêm dikim ku binpêkirina qanûnên mezin ên xwezayê gunehekî kujer e. ||| For I realize today that it is a mortal sin to violate the great laws of nature.
Divê em lez nekin, divê em bêsebir nebin, lê divê em bi piştrastî li ahenga herheyî guhdarî bikin. ||| We should not hurry, we should not be impatient, but we should confidently obey the eternal rhythm.
Ez li ser zinarekî rûniştim da ku vê fikra Sala Nû hilmijim. ||| I sat on a rock to absorb this New Year's thought.
Ax, eger tenê ew perperoka biçûk her dem li ber min bifiriya da ku rê nîşanî min bide. ||| Ah, if only that little butterfly could always flutter before me to show me the way.
"""

CH11 = r"""
##PG 78
##FIRST
Ez wek ku diyariyên Sersalê standibim wisa bextewar rabûm. ||| I rose as happy as if I had received my New Year presents.
Ba sar bû, ezman zelal bû, behr dibiriqî. ||| The wind was cold, the sky clear, the sea gleaming.
Min rêya gund girt. ||| I took the path to the village.
Niha dibû ku ayîn xilas bûbe. ||| Mass would have ended by now.
Dema ez dimeşiyam, bi hesteke ehmeq, min ji xwe dipirsî ka di vê sala nû de yê pêşî ku ezê pê re rûbirû bibim — bextiyar an bêbext — dê kî be. ||| As I walked along, I wondered, with an absurd emotion, who would be the first person -- lucky or unlucky -- I should meet this new year.
Min ji xwe re digot, xwezî ew zarokekî biçûk bûya ku destên wî tije lîstokên Sersalê bin; an pîrekî çalak ê bi kirasekî spî yê bi destikên fireh û neqişandî, ku ji ber bi wêrekî erkê xwe yê li ser rûyê erdê bi cih aniye dilxweş û serbilind e. ||| If only, I said to myself, it could be a small child with its arms loaded with its New Year toys; or an active old man in a white shirt with full, embroidered sleeves, content and proud that he had fulfilled his duty on earth with courage.
Çiqas ez bêtir diçûm û nêzîkî gund dibûm, ewqas bêtir aciz dibûm. ||| The further I went and the closer I came to the village the more troubled I became.
Ji nişkê ve çokên min di bin min de şikiyan. ||| Suddenly my knees gave way beneath me.
Di bin daran zeytûnê de, bi gavên bazdayî li ser rêya gund, bi sor, bi laçikeke reş li ser serê xwe, rûçikê delal û navqemçî yê jinebiyê xuya bû! ||| Under the olive trees, walking with a springing step along the village road, appeared in red, with a black kerchief over her head, the graceful, slender-waisted figure of the widow!
Meşa wê ya xelek-xelek bi rastî wek a piling reş bû, û wisa dihat ber min ku bîneke tûj a miskê di hewayê de belav dibû. ||| Her sinuous gait was really that of a black panther, and it seemed to me that an acrid scent of musk was distilled in the air.

Xwezî min bikariya birevim! ||| If only I could escape!
Min hîs dikir ku çaxê hêrs bibe ev heywan dê tu dilovaniyê neke û tişta yekane ya ku divê bê kirin ev bû ku mirov bireve. ||| I felt that when angry this beast would have no mercy and that the only thing to do was to run away.
Lê çawa? ||| But how?
Jinebî hêdî hêdî nêzîk dibû. ||| The widow was steadily approaching.
Wisa dihat ku rîzik diqîçirî, mîna ku leşkerek li serê dimeşiya. ||| The gravel seemed to be crunching as if an army were marching over it.
Ew min dît, serê xwe hejand, laçika wê xwar bû û porê wê xuya bû, reş wek şebeqê û biriqok. ||| She saw me, shook her head, her kerchief slipped down and her hair appeared, black as jet and shining.
Nêrîneke nazdar avêt min û bişirî. ||| She cast me a languorous look and smiled.
Çavên wê şîrîniyeke hov hebû. ||| Her eyes had a wild sweetness.
Bi lez laçika xwe rast kir, mîna ku şerm bike ku hiştiye ez yek ji sirên herî kûr ên jinê bibînim: porê wê. ||| Hastily she adjusted her kerchief, as though she were ashamed at having let me see one of woman's deepest secrets: her hair.
Min dixwest ez pê re bipeyivim, Sersala wê pîroz bikim, lê qirika min pir teng bû, wek wê rojê ku gal hilweşiya û jiyana min di metirsiyê de bû. ||| I wanted to speak to her, wish her a happy New Year, but my throat was too tight, as on the day when the gallery fell in and my life had been in danger.

##PG 79
Qamîşên ku dora baxçeyê wê girtibûn di bayê de dihejiyan, tava zivistanê li ser leymûnên zêrîn û pirteqalên bi pelên xwe yên tarî diket. ||| The reeds surrounding her garden stirred in the wind, the winter sun fell on the golden lemons and the oranges with their dark foliage.
Tevahiya baxçe wek bihiştekê dibiriqî. ||| The entire garden was resplendent like a paradise.
Jinebî sekinî, milê xwe dirêj kir û dergeh bi hêz vekir. ||| The widow stopped, stretched out her arm and thrust the gate open.
Ez tam di wê kêliyê de ji ber wê derbas dibûm. ||| I was passing her just at that moment.
Li dora xwe nihêrî û, biruyên xwe bilind kirin, nêrîna xwe da ser min. ||| She looked round and, raising her eyebrows, turned her gaze on me.
Dergeh vekirî hişt û min dît ku ew li paş daran pirteqalê winda bû, dema diçû ranên xwe dihejand. ||| She left the gate open and I saw her disappear behind the orange trees, swaying her hips as she went.

Ku mirov têkeve wî dergehî û wî bigire, li pey wê bibeze, wê ji navqemê bigire û, bê tu peyvê, wê bikişîne ber nivîna wê ya mezin a jinebiyê — ev bû ya ku tu jê re dibêjî mêrbûn! ||| To enter that gate and bolt it, to run after her, take her by the waist and, without a word, drag her to her large widow's bed, that was what you would call being a man!
Ev ew tişt bû ku bapîrê min dê bikira, û ya ku ez hêvî dikim neviyê min dê bike! ||| That was what my grandfather would have done, and what I hope my grandson will do!
Lê ez li wir wek stûnekê sekinîm, tiştan dikêşim û difikirim.... ||| But I stood there like a post, weighing things up and reflecting....
«Di jiyaneke din de,» min bi tehlî bişirî û pist-pist kir, «di hin jiyaneke din de ezê ji vê çêtir tevbigerim!» ||| "In another life," I murmured, smiling bitterly, "in some other life I'll behave better than this!"

Ez ketim nav geliyê kesk, giraniyek li ser ruhê xwe hîs dikir mîna ku min gunehekî kujer kiribe. ||| I plunged into the green defile, feeling a weight on my soul as if I had committed a mortal sin.
Ez jor û jêr geriyam. ||| I wandered up and down.
Sar bû û ez dilerizîm. ||| It was cold and I was shivering.
Bê fêde bû ku ez ji bîrên xwe ranên hejok ên jinebiyê, bişirîna wê, çavên wê, memikên wê biqewirînim; ew her vedigeriyan — ez dixeniqîm. ||| It was no use my chasing from my thoughts the widow's swaying hips, her smile, her eyes, her breasts, they always returned -- I was suffocating.
Hê pelên daran tunebûn, lê gomik tije av bûn û jixwe diwerimîn û diteqiyan. ||| The trees had no leaves as yet, but the buds were full of sap and already swelling and bursting.
Di her gomikê de te dikarî hebûna kombûyî ya şivikên ciwan, kulîlk û fêkiyên-bê-çêbûyî hîs bikira, ku li benda derketinê bûn û amade bûn ku ber bi ronahiyê biteqin. ||| In every bud you could feel the concentrated presence of young shoots, flowers, fruits-to-be, lying in wait and ready to burst out to the light.
Roj û şev di nîvê zivistanê de, keramata mezin a biharê bêdeng û bi dizî di bin qalikê hişk de dihat amadekirin. ||| Day and night in the middle of winter, the great miracle of spring was silently, secretly being prepared beneath the dry bark.

Ji nişkê ve min qîrîneke şahiyê kir. ||| Suddenly I gave a cry of joy.
Dara behîvê ya wêrek li hember min di kortikeke parastî de di nîvê zivistanê de gulvedabû, rê nîşanî hemû daran did da û mizgîna biharê dida. ||| A bold almond tree opposite me in a sheltered hollow had burst into flower in midwinter, leading the way to all the other trees and heralding the spring.
Ew zextê ku min hîs dikir ji min veqetiya. ||| The oppression I felt left me.
Min bîna wê ya hineke bîberî kûr kişand. ||| I took a deep breath of its somewhat peppery scent.
Ez ji rê derketim û li bin çiqilên wê yên bi gul rûniştim. ||| I left the road and sat down beneath its flowering branches.
Ez demeke dirêj li wir mam, li ser tu tiştî nedifikirîm, bêxem û bextewar. ||| I stayed there a long time, thinking of nothing, care-free and happy.
Ev herheyî bû û ez li bin darekê di Bihiştê de rûniştî bûm. ||| This was eternity and I was sitting beneath a tree in Paradise.

Ji nişkê ve dengekî bilind û dijwar ez ji vê bihiştê avêtim derve. ||| Suddenly a loud rough voice ejected me from this paradise.
«Ka tu li wir vehewiyayî çi dikî, axa? Ez li jor û jêr li te digerim. Nêzîkî diwanzdehan e, were!» ||| "Now what might you be doing tucked away in there, boss? I've been looking high and low for you. It's close on twelve, come on!"
«Kuderê?» ||| "Where?"
«Kuderê? Tu ji min dipirsî kuderê? Bê guman, ba diya kal a Berxê Şîrmij! Ma tu birçî nî? Berazê şîrmij ji firnê derket! Çi bîn... devê te av tê! Were!» ||| "Where? You ask me where? To old mother Sucking Pig, of course! Aren't you hungry? The sucking pig's out of the oven! What a smell... makes your mouth water! Come on!"

Ez rabûm, destê xwe li qurmê hişk ê dara behîvê xist, ya ku ewqas sir di xwe de dihewand û ev keramata gulvedanê derxistibû. ||| I rose, stroked the hard trunk of the almond tree containing so many mysteries and which had produced this miracle of blossom.
Zorba li pêş diçû, sivikpê, tije coş û birçîbûn. ||| Zorba went on ahead, light-footed, full of zest and hunger.
Hewcedariyên bingehîn ên mirov — xwarin, vexwarin, jin û govend — di laşê wî yê saxlem û dilxwaz de tu caran neqediyan an kêm nebûn. ||| The fundamental needs of man -- food, drink, women and dance -- were never exhausted or dulled in his robust and eager body.
Di destê xwe de pakêteke pehn digirt, bi kaxezê pembe pêçayî û bi benê rengê zêr girêdayî. ||| He was holding in his hand a flat parcel wrapped in pink paper and tied with golden-colored string.
«Diyariya Sersalê?» min bi bişirîn pirsî. ||| "A New Year's gift?" I asked with a smile.
Zorba keniya, hewl dida ku hesta xwe veşêre. ||| Zorba laughed, trying to hide his emotion.

##PG 80
«Ka, tenê da ku cihê gilîkirinê jê re nemîne, jina belengaz!» got, bê ku berê xwe bizivirîne. ||| "Well, just so she's no room for complaint, poor woman!" he said, without turning round.
«Da ku ew mezinahiya xwe ya berê bîne bîra xwe.... Ew jinek e — ma me ev têra xwe negotiye? — û loma afirîdeke ku her dem li ser çarenûsa xwe şîn digire....» ||| "So she'll remember her past grandeur.... She's a woman -- haven't we said so often enough? -- and therefore a creature always mourning over her lot...."
«Wêneyek?» ||| "A photograph?"
«Tê bibînî... tê bibînî; ewqas lez neke! Min bi xwe çêkir. Were, çêtir e em bilezin.» ||| "You'll see... you'll see; don't be in so great a hurry! I made it myself. Come on, we'd better get a move on."

Tava nîvro wisa bû ku heta hestiyên te jî şa dikir. ||| The midday sun was such as to gladden your very bones.
Behr jî, bi kêfxweşî di tavê de xwe germ dikir. ||| The sea, too, was happily warming itself in the sun.
Li dûr, girava biçûk a bêmirov, di mijeke sivik de pêçayî, wisa xuya dikir mîna ku xwe ji behrê rakiribe û li ser avê biçe. ||| In the distance the tiny uninhabited island, shrouded in light mist, looked as if it had raised itself out of the sea and was floating.
Em nêzîkî gund bûn, û Zorba nêzîkî min bû û dengê xwe nizm kir. ||| We approached the village, and Zorba came close to me and lowered his voice.

«Tu dizanî, axa,» got, «ew kesa ku behsa wê dikim li dêrê bû. Ez li pêş li ba stranbêj sekinî bûm dema ku ji nişkê ve min dît îkonên pîroz ronî bûn. Îsa, Meryema Pîroz, Diwanzdeh Şandî, her tişt biriqî.... ‹Çi diqewime?› min got, û xaç li xwe kir. ‹Ma ev tav e?› Min berê xwe zivirand — ew jinebî bû!» ||| "You know, boss," he said, "the person in question was at church. I was standing in front by the cantor when I suddenly saw the sacred icons light up. Christ, the Holy Virgin, the Twelve Apostles, everything shone.... 'Whatever's happening?' I said, crossing myself. 'Is it the sun?' I turned round -- it was the widow!"
«Baş e, Zorba. Bes e,» min got, û bi lez çûm pêş. ||| "All right, Zorba. That'll do," I said, hurrying on.
Lê Zorba li pey min bezî. ||| But Zorba ran after me.
«Min ew ji nêzîk ve dît, axa. Li ser hinarika rûyê wê xalek heye ku têra dînkirina te dike. Sirek din ji wan siran — xalên li ser hinarikên jinan!» ||| "I saw her close to, boss. She's got a beauty spot on her cheek that's enough to send you crazy. Another of those mysteries -- beauty spots on women's cheeks!"

Çavên xwe bi awayekî heyirî vekir. ||| He opened wide his eyes with an air of stupefaction.
«Ma te ferq kir, axa? Çerm hemû nerm û hilû ye, û paşê, ji nişkê ve, xalek reş! Ka, ew bes e! Te dîn dike! Ma tu vê fêm dikî, axa? Pirtûkên te li ser vê çi dibêjin?» ||| "Have you noticed, boss? The skin's all soft and smooth, and then, all of a sudden, a black spot! Well, that's all that's needed! It sends you crazy! D'you understand that, boss? What d'your books say about it?"
«Bila şeytan wan bibe!» ||| "The devil take them!"
Zorba keniya, ji xwe razî. ||| Zorba laughed, pleased with himself.
«Ev e mesele!» qîriya. «Ev e mesele. Tu dest pê dikî fêm bikî....» ||| "That's the stuff!" he exclaimed. "That's the stuff. You're beginning to realize...."

Em li qehwexaneyê nesekinîn; em çûn pêş. ||| We did not stop at the café; we pressed on.
Xanima me ya delal ji me re di firnê de berazekî şîrmij pijandibû û li ber deriyê xwe li benda me bû. ||| Our good lady had cooked a sucking pig for us in the oven and was waiting for us on her doorstep.
Wê dîsa bendeke zer-kenarî li dora situyê xwe kiribû, û dîtina wê bi vî awayî — bi pûdra giran, lêvên bi qatekî stûr ê sor sîwaxkirî — têra tirsandina her kesî dikir. ||| She had put a canary-yellow ribbon round her neck once more, and, to see her like that -- heavily powdered, lips plastered with a thick layer of crimson -- was enough to dismay anyone.
Ma ew, bi rastî, peykera pêşiya keştiyekê bû? ||| Was she, in fact, a ship's figurehead?
Hema ku çavê wê bi me ket, wisa xuya bû ku hemû goştê wê şa bû û hat livandin, çavên wê yên biçûk bi şeytanetî di serê wê de dans kirin û li ser simbêlên badayî yên Zorba sekinîn. ||| As soon as she caught sight of us her whole flesh seemed to be gladdened and set in motion, her small eyes danced naughtily in her head and came to rest fixed on Zorba's curled-up moustache.

Hema ku deriyê derve li pişt me girt, Zorba ew ji navqemê girt. ||| As soon as the outer door had closed behind us, Zorba took her by the waist.
«Sersala te pîroz be, Bûbûlîna min!» got. «Binêre me ji te re çi anî!» ||| "Happy New Year, my Bouboulina!" he said. "Look what we brought you!"
Û situyê wê yê qelew û qermiçandî maç kir. ||| And he kissed her plump and wrinkled neck.
Sîrena pîr bo kêliyekê kêfxweş bû, lê serê xwe winda nekir. ||| The old siren was tickled for a moment, but did not lose her head.
Çavên wê li ser diyariyê mîxkirî bûn. ||| Her eyes were clamped on the present.
Wê ew girt, benê zêrîn vekir, li hundir nihêrî û qîrîneke şahiyê kir. ||| She seized it, undid the golden string, looked inside and uttered a cry of joy.

Ez ber bi pêş ve xwar bûm da ku bibînim ew çi bû: li ser parçeyekî stûr ê mukewayê wî qeşmerê Zorba bi çar rengan — sor, zêr, gewr û reş — çar keştiyên şer ên mezin, bi alên xemilandî, li ser behreke şîn a tarî dikişandin. ||| I leaned forward to see what it was: on a thick piece of cardboard that rascal Zorba had drawn in four colors -- red, gold, grey and black -- four huge battleships, decked with flags, sailing on an indigo-blue sea.
Li pêşiya keştiyên şer, li ser pêlan diherikî, hemû tazî û spî, bi porê belavbûyî, memik di hewayê de, û dûvikê masî yê xelek-xelek, sîrenek hebû — Madam Hortans, bi bendika zer a li dora situyê xwe ve temam! ||| In front of the battleships, floating on the waves, all naked and white, with hair flowing, breasts in the air, and a spiral fish-tail, was a siren -- Dame Hortense, complete with yellow ribbon round her neck!
Wê çar ben digirtin û li pey xwe çar keştiyên şer ên ku alên Îngilîstan, Rûsya, Fransa û Îtalyayê hildigirtin dikişandin. ||| She was holding four strings and pulling behind her the four battleships flying the flags of England, Russia, France and Italy.
##PG 81
Li her quncikê wêneyê rîyek daleqandî bû, yek zer, yek sor, yek gewr, û yek reş. ||| In each corner of the picture hung a beard, one fair, one red, one grey, and one black.

Stranbêja pîr yekser fêm kir. ||| The old singer understood immediately.
«Ez!» got, bi serbilindî sîrenê nîşan da. ||| "Me!" she said, pointing proudly to the siren.
Axîn kişand. «Ax! Ez jî carekê Hêzeke Mezin bûm, demekê!» ||| She sighed. "Ah! I used to be a Great Power, too, once upon a time!"
Neynikeke biçûk a girover ji ser nivîna xwe, li nêzî qefesa papaganê, rakir û, li şûna wê, wêneyê Zorba daliqand. ||| She moved a small round mirror from over her bed, near to the parrot's cage, and, in its place, hung Zorba's picture.
Di bin rûnê xwe yê stûr de divê ew zer bûbe. ||| Beneath her thick make-up she must have gone pale.

Zorba, di vê navberê de, xwe xistibû metbexê. Ew birçî bû. ||| Zorba, meanwhile, had slipped into the kitchen. He was hungry.
Wî firaqa bi berazê şîrmij anî, şûşeyeke şerabê li ber xwe danî ser masê û sê qedeh dagirtin. ||| He brought in the dish with the sucking pig, placed a bottle of wine on the table in front of him and filled three glasses.
«Were! Bixwe, bixwe!» qîriya, destên xwe li hev xistin. «Em ji bingehê dest pê bikin — ji zik. Piştî wê, şîrîna min, emê li ya jêrî binêrin!» ||| "Come! Eat, eat!" he cried, clapping his hands together. "Let's begin with the foundation -- the belly. After that, my sweet, we'll take care of what's below!"

Lê hewa bi axînên sîrena pîr aciz bû. ||| But the atmosphere was troubled by the old siren's sighs.
Her Sersalê, ew jî Roja Qiyametê ya xwe ya biçûk hebû... li jiyana xwe vedinihêrî, dikêşa û kêm didît. ||| Each New Year, she, too, had a little Doomsday of her own... she looked back on her life, weighed it up and found it wanting.
Di bin porê hindikbûyî yê vê jina pîr de, di hemû rojên bi rûmet de, bajarên mezin, mêr, kirasên hevirmiş, şûşeyên şampanyayê û rîyên bîhnxweş ji goristanên bîranîna wê radibûn. ||| Beneath this old woman's thinning hair, big cities, men, silk dresses, bottles of champagne and scented beards rose from the graves of her memory on all solemn occasions.
«Işteha min tune,» bi nazikî pist-pist kir. «Qet... qet....» ||| "I've no appetite," she murmured coyly. "None at all... none at all...."
Li ber mangalê çû ser çokan û komirên germ tev dan. ||| She kneeled down before the brazier and poked the hot coals.
Hinarikên wê yên şilbûyî ronahiya agir vedidan. ||| Her flabby cheeks reflected the light of the fire.
Çîçeke por ji eniya wê xwar bû û bi pêtekê hat şewitandin. ||| A lock of hair slipped from her brow and was singed by a flame.
Bîna nexweş a porê şewitî ode girt. ||| The nauseating smell of burnt hair permeated the room.
«Ez naxwim... ez naxwim...» dîsa pist-pist kir, dema dît ku em qet bala xwe nadinê. ||| "I won't eat... I won't eat..." she muttered once more, seeing we were taking no notice of her at all.

Zorba bi bêsebirî mistên xwe gurç kirin. Bo kêliyekê bêbiryar ma. ||| Zorba clenched his fists impatiently. He remained for a moment undecided.
Dikaribû bihêle ku ew bi qasî ku bixwaze ji xwe re pist-pist bike, dema em bi berazê biraştî mijûl dibin — an dikaribû xwe biavêje ser çokan, wê hembêz bike û bi peyvên xweş wê aram bike. ||| He could let her mutter to herself as much as she chose, while we got on with the roast pig -- or he could throw himself on his knees, take her in his arms and calm her down with kind words.
Min li rûyê wî yê ezisî nihêrî û dît, ku li ser sîmayên wî yên livok pêlên hêzên dijber derbas dibûn. ||| I watched his tanned face and saw, passing over his mobile features, waves of contradictory impulses.
Ji nişkê ve sîmaya wî sekinî. Ew gihîştibû biryarekê. ||| Suddenly his expression set. He had come to a decision.
Li tenişta wê çû ser çokan û çokên sîrenê girtin. ||| He knelt beside her and seized the siren's knees.
«Eger tu naxwî, efsûngera min a biçûk,» bi dengekî dilşewat got, «ev dawiya her tiştî ye. Dilovaniya berazê belengaz bike, delala min, û vî lingikê şîrîn bixwe!» ||| "If you don't eat, my little charmer," he said in heart-rending tones, "it's the end of everything. Have pity on the poor pig, my lovely, and eat this sweet little trotter!"
Û lingikê qiriqî yê bi rûn nixumandî da devê wê. ||| And he pushed into her mouth the crackling trotter covered with butter.
Wê hembêz kir, ji erdê rakir, û bi nermî danî ser kursiya wê di navbera me herduyan de. ||| He took her in his arms, raised her from the ground, and placed her gently on her chair between the two of us.

«Bixwe,» got, «bixwe, gencîneya min, da ku Aziz Vasîl bê gundê me! Eger tu naxwî, tu dizanî, ew dê neyê ba me! Ewê vegere welatê xwe, Qeyseriyê. Ewê hibirdank û kaxez, Kêka Diwanzdehan, diyariyên Sersalê, lîstokên zarokan, heta vî berazê biçûk ê şîrmij jî hilde û bi hemûyan re biçe! Loma devikê xwe veke, Bûbûlîna min, û bixwe!» ||| "Eat," he said, "eat, my treasure, so that Saint Basil will come to our village! If you don't, you know, he won't come to us! He'll go back to his own country, to Caesarea. He'll pick up the inkhorn and paper, the Twelfth Cake, the New Year gifts, the children's toys, even this little sucking pig, and away with them all! So open your little mouth, my Bouboulina, and eat!"
Du tilî dirêj kirin û ew di bin destî de qurçumî. ||| He put out two fingers and tickled her under the arm.
Sîrena pîr ji kêfê qîqî kir, çavên xwe yên biçûk û sorbûyî paqij kirin û bi xîret dest bi cûtina lingikê qiriqî kir.... ||| The old siren clucked with pleasure, wiped her small, reddened eyes and started busily to chew over the crackly trotter....

##PG 82
Tam di wê kêliyê de du pisîkên evîndar li ser banê li ser serê me dest bi qîrînê kirin. ||| Just at that moment two amorous cats began to howl on the roof over our heads.
Bi awazeke kerb a nayê vegotin diqîriyan, dengên wan bi gefdar bilind dibûn û dadiketin. ||| They howled in an indescribable tone of hatred, their voices rising and falling, threateningly.
Ji nişkê ve me bihîst ku ew bi hovî li ser banê li hev diqelibin, hev perçe-perçe dikin. ||| Suddenly we heard them scrambling wildly on the roof, tearing one another to pieces.
«Mîaw... mîaw...» got Zorba, çavê xwe li sîrena pîr qirpand. ||| "Miaow... miaow..." said Zorba, winking at the old siren.
Ew bişirî û destê wî di bin masê de pelçiqand. ||| She smiled and pressed his hand under the table.
Qirika wê rehet bû û bi îşteha dest bi xwarinê kir. ||| Her throat relaxed and she began to eat with appetite.

Tav zivirî, ji pencereya biçûk ket hundir û li ser lingên xanima delal ronî da. ||| The sun moved round, came in through the small window and shone on the good lady's feet.
Şûşe vala bû, Zorba simbêlên xwe wek ên pisîkeke hov badabûn û nêzîkî «mêya cinsê» bûbû. ||| The bottle was empty, Zorba had twisted up his moustaches like those of a wild cat and moved close to the "female of the species."
Madam Hortans, kombûyî, serê wê di milên wê de daketî, lerizî dema ku bîhna wî ya germ û şerabî li ser xwe hîs kir. ||| Dame Hortense, huddled up, her head sunk into her shoulders, shuddered as she felt his warm, vinous breath on her.

«Ka, ev sira din çi ye, axa?» got Zorba, berê xwe da min. ||| "Now, what's this other mystery, boss?" said Zorba, looking round at me.
«Bi min re her tişt berevajî diçe. Çaxê ez zarok bûm, wisa xuya dibe, ez wek pîrê biçûk dixuyam. Ez sergiran bûm, pir nedipeyivîm lê dengekî zilamekî mezin hebû. Dibêjin ez wek bapîrê xwe bûm! ||| "Everything goes backwards with me. When I was a kid, so it seems, I looked like a little old man. I was dense, didn't talk much but had a big fellow's voice. They say I was like my grandad!
Lê çiqas ez pîrtir dibûm, ewqas sersemtir dibûm. Çaxê ez bîst salî bûm min dest bi tiştên hov kir. Ox, tiştekî taybet na, tenê wek lawên din ên di wî temenî de. ||| But the older I grew, the more harum-scarum I became. I began doing wild things when I was twenty. Oh, nothing special, just the same as other fellows at that age.
Çaxê ez çil salî bûm min dest pê kir bi rastî xwe ciwan hîs bikim û ketim macerayên herî dîn. Û niha ez ji şêst salî mezintir im — şêst û pênc, axa, lê wê veşêre — ka, niha ku ez ji şêst mezintir im, ez çawa rave bikim? Bi rastî, dinya ji bo min pir biçûk bûye!» ||| When I was forty I began to feel really young and went off on the maddest escapades. And now I'm over sixty -- sixty-five, boss, but keep that dark -- well, now I'm over sixty, how can I explain? Honestly, the world's grown too small for me!"

Qedeha xwe bilind kir û bi dilrehmî berê xwe da xanima xwe. ||| He raised his glass and turned with compunction to his lady.
«Tenduristiya te, Bûbûlîna,» bi rûmet got. «Bila Xwedê bike ku îsal hin diran û hin biruyên xweşik li te şîn bin, û çermekî nû yê bi bîna xox! Û bila tu van bendikên ne'eyran hemûyan ji holê rakî! Û bila li Krêtayê şoreşeke din çêbibe û çar Hêzên Mezin dîsa vegerin, Bûbûlîna, delala min, bi keştiyên xwe yên şer... û bila her fîloyek admîralê xwe hebe û her admîral rîyê xwe yê badayî û bîhnxweş. Û bila tu dîsa ji pêlan rabî, sîrena min, strana xwe ya xweş bistirê. Û bila fîlo li van her du zinarên girover û hov perçe-perçe bibin!» ||| "Your good health, Bouboulina," he said solemnly. "May God see to it that this year you grow some teeth and some neat eyebrows, and a new skin scented like a peach! And that you do away with all these beastly little ribbons! And that there's another revolution in Crete and the four Great Powers come back again, Bouboulina, my dear, with their fleets... and that each fleet has its admiral and each admiral his curled and scented beard. And may you rise from the waves once more, my siren, singing your lovely song. And may the fleets break to pieces on these two round and savage rocks!"
Li ser vê yekê wî destên xwe yên mezin danîn ser memikên şilbûyî û daleqandî yên xanima delal.... ||| Whereupon he placed his big hands on the good lady's flabby, hanging breasts....

Zorba dîsa geş dibû, dengê wî ji daxwazê xerexerî bû. Ez keniyam. ||| Zorba was getting lively again, his voice was hoarse with desire. I laughed.
Rojekê, li sînemayê, min paşayekî tirk dîtibû ku li kabareyeke Parîsê dilîst. Keçeke ciwan a porzer li ser çonga xwe digirt. ||| One day, at the cinema, I had seen a Turkish pasha frolicking in a Paris cabaret. He was holding a fair-haired young midinette on his lap.
Paşa coş dibû; rîşiya li ser fesê wî hêdî hêdî dest bi rabûnê kir, bo kêliyekê dema asoyî bû sekinî, paşê ji nişkê ve rast ber bi jor ve di hewayê de zîq bû. ||| The pasha was getting excited; the tassel on his fez began to rise slowly, stopped for a moment when it was horizontal, then suddenly stuck straight up in the air.
«Tu bi çi dikenî, axa?» Zorba pirsî. ||| "What are you laughing at, boss?" Zorba asked.

Lê belê xanima delal hê li ser ya ku Zorba gotibû difikirî. ||| The good lady, however, was still thinking of what Zorba had been saying.
«Ox,» got, «tu difikirî ku gengaz e, Zorba? Lê çaxê ciwanî diçe, ew tu caran venagere....» ||| "Oh," she said, "d'you think it's possible, Zorba? But when youth goes it never comes back...."
Zorba hê nêzîktir bû; her du kursî bi hev ve zeliqîn. ||| Zorba moved closer still; the two chairs stuck together.
«Guhdariya min bike, qazika min,» got, di heman demê de hewl dida ku bişkoka sêyem, ya biryardar a kirasê wê veke. ||| "Listen to me, ducky," he said, trying at the same time to undo the third, the decisive button of her bodice.
«Guhdarî bike, bila ez behsa wê diyariya xweş bikim ku ezê ji te re bînim. Bijîşkekî nû heye — Voronof — ku dibêjin keramatan dike. Ew dermanekî dide te — dilop an toz, ez nizanim kîjan — û tu di kêliyekê de dîsa dibî bîst salî — herî xerab bîst û pênc! Negirî, delala min, ezê hinekî ji Ewrûpayê ji te re bînim....» ||| "Listen, let me tell you about the fine present I'm going to get you. There's a new doctor -- Voronoff -- who performs miracles, they say. He gives you a medicine of some kind -- drops or powder, I don't know which -- and you become twenty again in a trice -- twenty-five at the worst! Don't cry, my dear, I'll have some sent from Europe for you...."

Sîrena pîr ji cî hejiya. Serçermê wê yê sorgewr di navbera porê hindikbûyî de dibiriqî. ||| The old siren started. Her reddish scalp was gleaming between the thinning hair.
Milên xwe yên qelew û goştî avêtin dora situyê Zorba. ||| She threw her fat, fleshy arms round Zorba's neck.
##PG 83
«Eger dilop be, şîrîna min,» pist-pist kir, xwe wek pisîkekê li Zorba dixiste, «tê ji min re fîçiyekê sîpariş bikî, ne wisa? Û eger toz be...» ||| "If it's drops, my sweetie," she murmured, rubbing herself against Zorba like a cat, "you'll order a demijohn for me, won't you? And if it's powder..."
«Tûrekek tije!» got Zorba, bişkoka sêyem vekir. ||| "A sackful!" said Zorba, undoing the third button.

Pisîkên ku demekê bêdeng bûbûn, dîsa dest bi qîrîna xwe kirin. Yek ji dengan giliyok û lavakar bû, yê din bi hêrs û gefdar. ||| The cats, who had been quiet for a time, started their howling again. One of the voices was plaintive and appealing, the other angry and threatening.
Xanima me ya delal bêhneke fireh kişand û çavên wê nazdar bûn. ||| Our good lady yawned and her eyes became languorous.
«Ma tu wan pisîkên kirêt dibihîzî?» pist-pist kir. «Şerma wan tune!» ||| "D'you hear those horrid cats?" she muttered. "They've no shame!"
Û li ser çonga Zorba rûnişt. Serê xwe paşde da ser situyê wî û axîneke mezin kişand. ||| And she sat on Zorba's knee. She leaned her head back against his neck and heaved a great sigh.
Wê hineke zêde vexwaribû û çavên wê dibûn dûman. ||| She had drunk a little too much and her eyes were growing misty.

«Tu li ser çi difikirî, Bûbûlîna min?» Zorba pirsî, memikên wê hişk girtin. ||| "What are you thinking about, my Bouboulina?" Zorba asked, clutching hold of her breasts.
«Îskenderiye...» pist-pist kir sîrena pîr, ya ku gelek li dinyayê geriyabû. «Îskenderiye... Beyrût... Konstantînopolîs... tirk, ereb, şerbet, solên zêrîn, fesên sor....» ||| "Alexandria..." murmured the old siren, who had trundled about the world quite a bit. "Alexandria... Beirut... Constantinople... the Turks, the Arabs, sherbet, golden sandals, red fezes...."
Axîneke din kişand. ||| She heaved another sigh.

«Çaxê Elî Beg şeva xwe bi min re derbas dikir — çi simbêl, çi birû, çi mil hebûn wî! — gazî lêxerên def û bilûrê dikir û ji pencereyê pere davêtin wan, da ku heta spêdeyê li hewşa min lê bixin. Û cîran ji çavnebariyê dibûn kesk: ‹Elî Beg dîsa li wir e bi wê re!› bi hêrs digotin. ||| "When Ali Bey stayed the night with me -- what a moustache, what eyebrows, what arms he had! -- he'd call to the tambourine and flute players and throw them money through the window, so that they'd play in my courtyard until dawn. And the neighbors used to go green with envy: 'Ali Bey's there with her again!' they'd say in a rage.
Paşê, li Konstantînopolîsê, Silêman Paşa tu caran nedihişt ez roja înê qet derkevim derve. Ditirsiya ku Siltan li ser rêya mizgeftê min bibîne û ji bedewiya min ewqas heyirî bibe ku min birevîne. Her sibe çaxê ji malê derdiket sê reşikên mezin li ber derî datanîn da ku hemû mêran ji min dûr bixin.... Ax! Silêmanê min ê biçûk!» ||| "Afterwards, in Constantinople, Suleiman Pasha would never let me go out at all on Fridays. He was afraid the Sultan might see me on the way to the mosque and be so dazzled by my beauty he'd have me kidnapped. Every morning when he left the house he'd put three big negroes at the door to keep all males away from me.... Ah! my little Suleiman!"
Destmaleke mezin a çareçar ji kirasê xwe derxist û eniya xwe pê girt, mîna kûsiyekî fîz dikir. ||| She took a large, checked handkerchief from her bodice and bit it, hissing like a turtle.

Zorba ew danî ser kursiya tenişta xwe û jê xilas bû, û bi acizî rabû ser xwe. ||| Zorba got rid of her by placing her on the chair next to him, and stood up, annoyed.
Carekê du caran jor û jêr meşiya û wî jî dest bi fîzkirinê kir; ode ji nişkê ve ji wî re pir teng bû. ||| He walked up and down once or twice and he began hissing as well; the room was suddenly too cramped for him.
Gopalê xwe hilda û bi lez derket hewşê, û min dît ku derince da ser dîwêr û bi hêrs, her carê du pêpelûk, hilkişiya jor. ||| He picked up his stick and rushed out into the yard, and I saw him lean the ladder against the wall and clamber up, two steps at a time, in a fury.
«Tê li kê bidî, Zorba?» min qîriya. «Silêman Paşa?» ||| "Who are you going to thrash, Zorba?" I shouted. "Suleiman Pasha?"
«Wan pisîkên lanetî!» qîriya. «Ma nikarin bo kêliyekê jî me bi tena bihêlin?» ||| "Those damned cats!" he shouted. "Can't they leave us for a single moment?"
Û bi lotikekê ew li ser banî bû. ||| And in one bound he was on the roof.

Madam Hortans, baş serxweş, porê wê tevlihev, niha çavên xwe yên werimî girtibûn, û xirexireke dizî ji devê wê yê bêdiran dihat. ||| Dame Hortense, quite drunk, her hair dishevelled, had now closed her inflamed eyes, and a discreet snore came from her toothless mouth.
Xew ew rakiribû û biribû bajarên mezin ên Rojhilatê — nav baxçeyên girtî û heremên tarî yên paşayên evîndar. ||| Sleep had lifted her up and transported her to the great cities of the East -- into the closed gardens and dim harems of amorous pashas.
Xewê hişt ku ew ji dîwaran derbas bibe û xewn ji wê re şandin. ||| Sleep let her pass through walls and sent her dreams.
Wê dikaribû xwe bibîne ku masî digire; çar ben avêtibûn û çar keştiyên şer ên mezin girtibûn. ||| She could see herself fishing; she had thrown out four lines and caught up four great battleships.
Bi xirexir û bi bêhneke giran, sîrena pîr di xewa xwe de bi kêfxweşî bişirî, û diyar bû ku ji ber serşûştina xwe ya di behrê de teze bûye. ||| Snoring and breathing heavily, the old siren smiled happily in her sleep, and seemingly refreshed by her bathe in the sea.

Zorba vegeriya, gopalê xwe dihejand. ||| Zorba came back, swinging his stick.
«Razayî, ha?» got dema ku ew dît. «Pîrê razayî ye, ne wisa?» ||| "Sleeping, eh?" he said as he saw her. "The jade's asleep, is she?"
##PG 84
«Erê, Zorba Paşa,» min bersiv da. «Ew ji aliyê Bijîşk Voronof ê ku pîran dîsa ciwan dike ve hatiye birin — xew. Ew tenê bîst salî ye, û li Îskenderiye û Beyrûtê digere....» ||| "Yes, Zorba Pasha," I answered. "She's been carried off by the Doctor Voronoff who makes old people young again -- sleep. She's only twenty, and she's strolling about Alexandria and Beirut...."
«Bila here ba şeytan, pîra qehpik!» Zorba kurîn, û tif kir erdê. «Ka temaşe bike ka çawa diçirpîne! Ez meraq dikim ji kê re diçirpîne, dêûsa bêrû? Were, axa, em herin!» ||| "Let her go to the devil, the old slut!" Zorba growled, and spat on the floor. "Just look at the way she's grinning! I wonder who she's grinning at, the brazen bitch? Come on, boss, let's go!"
Kumê xwe danî serê xwe û derî vekir. ||| He slapped on his cap and opened the door.
«Ew ne bi tena serê xwe ye,» qîriya Zorba; «ew bi Silêman Paşa re ye. Ma tu nabînî? Ew di esmanê heftan de ye, çêleka qirêj! ... Were. Em bizdin!» ||| "She's not all on her own," cried Zorba; "she's with Suleiman Pasha. Can't you see? She's in her seventh heaven, the dirty cow! ... Come on. Let's beat it!"

Em derketin hewaya sar. Heyv li ezmanekî aram dikişiya. ||| We went out into the cold air. The moon was sailing across a calm sky.
«Jin!» got Zorba bi nefret. «Tu! Lê dîsa jî, ev ne sûcê te ye, ev sûcê sersemên bêmêjî yên wek Silêman û Zorba ye!» ||| "Women!" said Zorba in disgust. "Ugh! Still, it's not your fault, it's the fault of hare-brained harum-scarums like Suleiman and Zorba!"
Û piştî bêhnvedaneke kurt: «Na, ev qet ne sûcê me ye jî,» bi hêrs berdewam kir. «Hebûnek heye ku sedema her tiştî ye, û tenê yek — Sersemê Mezin ê Bêmêjî, Silêman Paşayê Mezin... tu dizanî kî!» ||| And after a moment's pause: "No, it's not even our fault," he went on furiously. "There's one being who's the cause of it all, and one alone -- the Grand Hare-brained Harum-scarum, the Grand Suleiman Pasha... you know who!"
«Eger ew hebe,» min bersiv da. ||| "If he exists," I answered.
«Ma eger tunebe?» ||| "What if he doesn't?"
«Xwedêyê Mezin, vêca em qediyane!» ||| "God Almighty, then we're done for!"

Demekê em bê tu peyvê meşiyan. Bê guman Zorba di hişê xwe de hin fikrên hov diqulibandin, çimkî hema her saniyê bi gopalê xwe li keviran dixist û tif dikir erdê. ||| For some time we strode along without a word. Zorba was certainly going over some wild ideas in his mind, because every second or so he would lash out at the pebbles with his stick and spit on the ground.
Ji nişkê ve berê xwe da min. «Bila Xwedê hestiyên bapîrê min pîroz bike!» got. «Ew tiştek du tişt li ser jinan dizanî. Ji wan pir hez dikir, belengaz, û wan ew di jiyana wî de baş gerand. ||| Suddenly he turned to me. "May God sanctify my grandad's bones!" he said. "He knew a thing or two about women. He liked them a lot, poor wretch, and they led him a regular dance in his lifetime.

‹Bi hemû xêrên ku ez ji te re dixwazim, Alexîs, lawê min,› digot, ‹xwe ji jinan biparêze! Çaxê Xwedê parsûya Adem derxist da ku jinê biafirîne — bila ew kêlî nifirî be! — şeytan bû mar, û pif! parsû qeland û pê re reviya.... ||| 'By all the good things I wish you, Alexis, my boy,' he'd say, 'beware of women! When God took Adam's rib out to create woman -- curse that minute! -- the devil turned into a serpent, and pff! he snatched the rib and ran off with it....
Xwedê li pey wî bezî û ew girt, lê ji tiliyên wî xişiya derket û tenê strûyên şeytan di destên Xwedê de man. ||| God dashed after him and caught him, but he slipped out of his fingers and God was left with just the devil's horns in his hands.
‹Kedbanûyeke baş,› got Xwedê, ‹dikare bi kefçiyekî jî bidirûye. Ka, ezê jinê bi strûyên şeytan biafirînim!› ||| "A good housekeeper," said God, "can sew even with a spoon. Well, I'll create a woman with the devil's horns!"
Û wî çêkir; û şeytan bi vî awayî em hemû xistin destê xwe, Alexîsê lawê min. Tu li kuderê jinê bigirî, tu strûyên şeytan digirî. ||| And he did; and that's how the devil got us all, Alexis my boy. No matter where you touch a woman, you touch the devil's horns.
Xwe ji wê biparêze, lawê min! Wê sêvên di baxçeyê Eden de jî dizîn; ew xistin nav kirasê xwe, û niha derdikeve û digere, li her derê bi pozbilindî dimeşe. Bila bela li wê be! ||| Beware of her, my boy! She also stole the apples in the garden of Eden; she shoved them down her bodice, and now she goes out and about, strutting all over the place. A plague on her!
Ji wan sêvan bixwî tu winda yî; tu nexwî jî tê dîsa winda bî! Vêca ez çi şîretê dikarim li te bikim, lawê min? Çawa dilê te bixwaze wisa bike!› ||| Eat any of those apples and you're lost; don't eat any and you'll still be lost! What advice can I give you, then, my boy? Do as you please!'
Ev e ya ku bapîrê min ê kal ji min re got. Lê tu çawa dixwazî ez bi aqil mezin bibim? Min heman rê wek wî girt — ez çûm ba şeytan!» ||| That's what my old grandad said to me. But how could you expect me to grow up sensible? I went the same way as he did -- I went to the devil!"

Em bi lez di gund re derbas bûn. Ronahiya heyvê aciz dikir. ||| We hurried through the village. The moonlight was disturbing.
Bifikire ka dê çawa be eger te vexwaribe û tu derketibî ji bo gerê û dinya ji nişkê ve guherî bibînî. ||| Imagine how it would be if you had been drinking and came out for a walk and found the world suddenly transformed.
Rê bûbûn çemên şîr, kortikên rê û şopên çerxan bi kilsê tije bûbûn, gir bi berfê nixumî bûn. ||| The roads had turned into rivers of milk, the holes in the road and the ruts overflowed with chalk, the hills were covered with snow.
Destên te, rûyê te û situyê te ronî didan, wek dûvikê kurmê şewqdar. ||| Your hands, face and neck were phosphorescent, like a glowworm's tail.
Û heyv li ser sîngê te wek medalyayeke girover a ecêb daleqandî bû. ||| And the moon hung on your chest like an exotic round medal.

Em bi lez, bêdeng dimeşiyan. Ji ronahiya heyvê û ji şerabê serxweş, em hema hîs nedikir ku lingên me bi erdê dikevin. ||| We were walking along briskly, in silence. Intoxicated by the moonlight as well as by the wine, we hardly felt our feet touch the ground.
##PG 85
Li pişt me, di gundê razayî de, kûçik li ser banan rabûbûn û li heyvê diewtiyan. ||| Behind us, in the sleeping village, the dogs had got up on the roofs and were howling at the moon.
Û me jî, bê tu sedem, hesta xwestina ku situyê xwe ber bi heyvê dirêj bikin û dest bi ewtînê bikin hîs kir.... ||| And we, for no reason at all, also felt a desire to stretch our necks towards the moon and begin to howl....

Em gihîştin baxçeyê jinebiyê. Zorba sekinî. ||| We came to the widow's garden. Zorba stopped.
Şerab, xwarina baş û heyvê serê wî zivirandibû. ||| Wine, good food and the moon had turned his head.
Situyê xwe dirêj kir û, bi dengê xwe yê mezin ê wek kerê, dest bi zûrîna malikeke bêedeb kir ku, di rewşa xwe ya coşbar de, di cih de honand. ||| He craned his neck and, in his big ass's voice, began to bray a bawdy couplet which, in his excited state, he composed on the spur of the moment.
«Ew jî yek ji strûyên şeytan e!» got. «Em herin, axa!» ||| "She's another of the devil's horns!" he said. "Let's go, boss!"

Spêde li ber çêbûnê bû dema ku em gihîştin koxikê. Min xwe avêt ser nivîna xwe, westiyayî. ||| Dawn was about to break when we arrived at the hut. I threw myself on my bed, worn out.
Zorba xwe şuşt, soba pêxist û hinek qehwe çêkir. ||| Zorba washed, lit the stove and made some coffee.
Li ber derî li erdê çemiya, cigareyek pêxist û bi aramî dest bi cigarekêşanê kir, laşê wî rast û bêliv dema ku li behrê dinihêrî. ||| He crouched on the floor by the door, lit a cigarette and began to smoke placidly, his body straight and motionless as he looked out at the sea.
Rûyê wî giran û fikarî bû. ||| His face was grave and thoughtful.

Ew tabloyeke japonî ya ku ez jê hez dikim anî bîra min: zahidekî ku li ser lingên xwe yên bi hev ve rûniştî û di kincekî dirêj ê rengê pirteqalê de pêçayî; rûyê wî wek neqşek di darê hişk de dibiriqî, ji baranê reşbûyî; situyê wî zîq, dibişire dema ku, bê tirs, li şeva tarî dinihêre.... ||| He reminded me of a Japanese painting I like: an ascetic sitting on his crossed legs and wrapped in a long orange-colored robe; his face shining like a carving in hard wood, blackened by the rain; his neck erect, smiling as he gazes, without fear, into the dark night....

Min di ronahiya heyvê de li Zorba nihêrî û ji wê coş û sadetiya ku pê xwe li dinyaya dora xwe diguncand heyirî mam, ji awayê ku laş û ruhê wî tevahiyeke hevaheng pêk dianîn, û her tişt — jin, nan, av, goşt, xew — bi kêfxweşî bi goştê wî re tev dibû û dibû Zorba. ||| I looked at Zorba in the light of the moon and admired the jauntiness and simplicity with which he adapted himself to the world around him, the way his body and soul formed one harmonious whole, and all things -- women, bread, water, meat, sleep -- blended happily with his flesh and became Zorba.
Min tu caran lihevhatineke wisa dostane di navbera mirovekî û gerdûnê de nedîtibû. ||| I had never seen such a friendly accord between a man and the universe.

Heyv dê niha di demeke nêz de biçûya ava. Girover bû û kesketeke vemirî bû. ||| The moon would soon be setting now. It was round and of a pale green.
Aşitiyeke nayê vegotin li ser behrê belav bû. ||| An indescribable peacefulness spread across the sea.
Zorba cigareya xwe avêt û dest dirêjî selikekê kir. ||| Zorba threw away his cigarette and reached out for a basket.
Tê de geriya û hin ben, çerxik û perçeyên biçûk ên dar derxistin; çiraya neftê pêxist û dîsa dest bi ceribandina hesinrêya xwe ya hewayî kir. ||| He fumbled in it and pulled out some string, pulleys and little pieces of wood; he lit the oil-lamp and once more started to experiment with his overhead railway.
Li ser lîstoka xwe ya seretayî çemiyayî, dest bi hesaban kir ku divê pir aloz û dijwar bûbin, çimkî hema her saniyê bi hêrs serê xwe dixurand û nifir dikir. ||| Stooping over his primitive toy, he began to make calculations which must have been extremely complicated and difficult, for every other second he scratched his head furiously and swore.
Ji nişkê ve jê bêzar bû. Lêpekek li modelê da û ew bi erdê ket û perçiqî. ||| Suddenly he had had enough of it. He aimed one kick at the model and it crashed to the ground.
"""

CH12 = r"""
##PG 85
##FIRST
Xew bi ser min de hat, û çaxê ez hişyar bûm Zorba çûbû. ||| Sleep overcame me, and when I awoke Zorba had gone.
Sar bû û qet daxwaza min a rabûnê tunebû. ||| It was cold and I did not have the slightest desire to rise.
Min dest dirêjî çend refên pirtûkan ên li jor serê min kir û pirtûkek daxist ku min bi xwe re anîbû û ji wê hez dikir: helbestên Malarme. ||| I reached up to some bookshelves above my head and took down a book which I had brought with me and of which I was fond: the poems of Mallarmé.
Min hêdî hêdî û bê tertîb xwend. ||| I read slowly and at random.
Min pirtûk girt, dîsa vekir, û di dawiyê de avêt. ||| I closed the book, opened it again, and finally threw it down.
Cara yekem di jiyana min de hemû bê xwîn, bê bîn, û ji her madeyeke mirovî vala xuya dikir. ||| For the first time in my life it all seemed bloodless, odorless, void of any human substance.
Peyvên kesk-şîn, vala di valahiyê de. ||| Pale-blue, hollow words in a vacuum.
Ava parzûnkirî ya bi temamî zelal bê tu bakterî, lê her wiha bê tu madeyên xwêdar. Bê jiyan. ||| Perfectly clear distilled water without any bacteria, but also without any nutritive substances. Without life.

Di olên ku çirûska xwe ya afirîner winda kirine de, xweda di dawiyê de ji motîfên helbestî an xemlên ji bo xemilandina tenêtî û dîwarên mirovan pê ve tiştekî din namînin. ||| In religions which have lost their creative spark, the gods eventually become no more than poetic motifs or ornaments for decorating human solitude and walls.
Tiştekî wisa bi vê helbestê re jî qewimîbû. ||| Something similar had happened to this poetry.
Xwestekên geş ên dil, ên barkirî bi ax û tov, bûbûn lîstikeke aqilî ya bê kêmasî, mîmariyeke jîr, hewayî û aloz. ||| The ardent aspirations of the heart, laden with earth and seed, had become a flawless intellectual game, a clever, aerial and intricate architecture.

##PG 86
Min pirtûk ji nû ve vekir û dîsa dest bi xwendinê kir. ||| I reopened the book and began reading again.
Çima van helbestan ewqas salan ez girtibûm? ||| Why had these poems gripped me for so many years?
Helbesta pak! ||| Pure poetry!
Jiyan bûbû lîstikeke zelal û şefaf, ku bi qasî dilopeke xwînê jî giran nebûbû. ||| Life had turned into a lucid, transparent game, unencumbered by even a single drop of blood.
Hêmana mirovî hov, qels û ne pak e — ew ji evînê, ji goşt û ji qîrîneke êşê pêk tê. ||| The human element is brutish, uncouth, impure -- it is composed of love, the flesh and a cry of distress.
Bila ew bibe fikreke razber, û, di pota ruh de, bi pêvajoyên cûrbecûr ên kîmyaya kevn, bila zirav bibe û bifûre. ||| Let it be sublimated into an abstract idea, and, in the crucible of the spirit, by various processes of alchemy, let it be rarefied and evaporate.
Hemû van tiştên ku berê min ewqas heyirî dikirin, vê sibehê ji akrobatiya mêjî û şarlatanetiyeke nazik pê ve tiştekî din xuya nedikirin! ||| All these things which had formerly so fascinated me appeared this morning to be no more than cerebral acrobatics and refined charlatanism!

Di hilweşîna şaristaniyekê de her wiha ye. ||| That is how it always is at the decline of a civilization.
Êşa mirov bi vî awayî diqede — di fêlbaziyên hostayî de: helbesta pak, muzîka pak, fikra pak. ||| That is how man's anguish ends -- in masterly conjuring tricks: pure poetry, pure music, pure thought.
Mirovê dawî — ê ku xwe ji hemû baweriyan, ji hemû xeyalan azad kiriye û tiştekî din ji bo hêvîkirin an tirsê nemaye — dibîne ku herriya ku jê hatiye çêkirin bûye ruh, û ji vî ruhî re tu ax nemaye ji bo rehên xwe, ku jê ava xwe bikişîne. ||| The last man -- who has freed himself from all belief, from all illusions and has nothing more to expect or to fear -- sees the clay of which he is made reduced to spirit, and this spirit has no soil left for its roots, from which to draw its sap.
Mirovê dawî xwe vala kiriye; êdî ne tov, ne rîx, ne xwîn. ||| The last man has emptied himself; no more seed, no more excrement, no more blood.
Her tişt bûye peyv, her komek peyv bûye lîstikbaziya muzîkî, mirovê dawî hê pêdetir diçe: di tenêtiya xwe ya temam de rûdine û muzîkê hildiweşîne nav hevkêşeyên bêdeng ên matematîkî. ||| Everything having turned into words, every set of words into musical jugglery, the last man goes even further: he sits in his utter solitude and decomposes the music into mute, mathematical equations.

Ez ji cî hejiyam. «Bûda ew mirovê dawî ye!» min qîriya. ||| I started. "Buddha is that last man!" I cried.
Ev wateya wî ya veşartî û tirsnak e. ||| That is his secret and terrible significance.
Bûda ew ruhê «pak» e ku xwe vala kiriye; di hundirê wî de valahî heye, ew bi xwe Valahî ye. ||| Buddha is the "pure" soul which has emptied itself; in him is the void, he is the Void.
«Laşê xwe vala bike, ruhê xwe vala bike, dilê xwe vala bike!» diqîre. ||| "Empty your body, empty your spirit, empty your heart!" he cries.
Li ku derê lingê xwe bi cih bike, av êdî naherike, tu giya naşîn dibe, tu zarok nayê dinyayê. ||| Wherever he sets his foot, water no longer flows, no grass can grow, no child be born.

Min fikirî, divê ez peyvan û hêza wan a sêrbaz bilivînim, ahengên efsûnî gazî bikim; dora wî bigirim, efsûnê li wî bikim û wî ji hinavên xwe biqewirînim! ||| I must mobilize words and their necromantic power, I thought, invoke magic rhythms; lay siege to him, cast a spell over him and drive him out of my entrails!
Divê ez tora wêneyan li ser wî biavêjim, wî bigirim û xwe azad bikim! ||| I must throw over him the net of images, catch him and free myself!

Nivîsandina Bûda, bi rastî, êdî nedima temrîneke edebî. ||| Writing Buddha was, in fact, ceasing to be a literary exercise.
Ew têkoşîneke jiyan-û-mirinê bû li dijî hêzeke mezin a wêrankirinê ya ku di hundirê min de xwe veşartibû, dûelek bi NA-yeke mezin re ku dilê min dixwar, û rizgariya ruhê min bi encama vê dûelê ve girêdayî bû. ||| It was a life-and-death struggle against a tremendous force of destruction lurking within me, a duel with a great NO which was consuming my heart, and on the result of this duel depended the salvation of my soul.
Bi lez û bi biryardarî min destnivîs girt. ||| With briskness and determination I seized the manuscript.
Min armanca xwe keşf kiribû, niha min dizanî li ku derê bidim! ||| I had discovered my goal, I knew now where to strike!
Bûda mirovê dawî bû. ||| Buddha was the last man.
Em hê tenê li destpêkê ne; me têra xwe ne xwariye, ne vexwariye, ne jî hez kiriye; em hê nejiyane. ||| We are only at the beginning; we have neither eaten, drunk, nor loved enough; we have not yet lived.
Ev pîrê nazik, ê kêm-bîhn, pir zû hatiye ba me. ||| This delicate old man, scant of breath, has come to us too soon.
Divê em wî bi qasî ku ji destê me tê zû bavêjin! ||| We must oust him as quickly as possible!

Wisa min bi xwe re xeber da û min dest bi nivîsandinê kir. ||| So I spoke to myself and I began to write.
Lê na, ev ne nivîsandin bû: ev şerekî rastîn bû, nêçîreke bê dilovanî, dorpêçek, efsûnek ji bo derxistina cinawir ji şûna wî ya veşartî. ||| But no, this was not writing: it was a real war, a merciless hunt, a siege, a spell to bring the monster out of its hiding place.
Huner, bi rastî, efsûnek e. ||| Art is, in fact, a magic incantation.
Hêzên tarî yên mirovkuj di hinavên me de xwe vedişêrin, daxwazên kujer ji bo kuştin, wêrankirin, kerb û bêrûmetkirinê. ||| Obscure homicidal forces lurk in our entrails, deadly impulses to kill, destroy, hate, dishonor.
Hingê huner bi bilûra xwe ya şîrîn xuya dibe û me xilas dike. ||| Then art appears with its sweet piping and delivers us.

Min nivîsî, da pey, têkoşiya tevahiya rojê. ||| I wrote, pursued, struggled the whole day through.
Êvarê ez westiyayî bûm. ||| In the evening I was exhausted.
Lê min hîs dikir ku min pêşveçûn kiriye, çend mevzîên pêşîn ên dijmin bi dest xistine. ||| But I felt I had made progress, had mastered a few advance posts of the enemy.
Niha ez bêhntengiya vegera Zorba dikişandim, da ku ez bixwim, razêm û hêza xwe ava bikim ku spêdeyê dîsa dest bi şer bikim. ||| I was now anxious for Zorba to return, so that I could eat, sleep and build up my strength to resume the fight at dawn.

Jixwe tarî bû dema ku Zorba ket hundir. ||| It was already dark when Zorba came in.
Sîmayeke biriqdar li rûyê wî hebû. ||| He had a radiant expression on his face.
Min fikirî, wî jî bersiva tiştekî dîtiye. Û ez li bendê mam. ||| He has found the answer to something, too, I thought. And I waited.
Min dest pê kiribû ku ez jê bêsebir bibim û, tenê çend roj berê, min bi hêrs gotibû: ||| I had begun to grow impatient with him and, only a few days before, I had said angrily:

##PG 87
«Zorba, drav ê me kêm dibe. Çi divê bê kirin, zû bike! Bila em vê hesinrêyê bidin xebitandin; eger em bi komirê serfiraz nebin, bila em hemû hêza xwe bidin daran. Wekî din em qediyan!» ||| "Zorba, our funds are getting low. Whatever has to be done, do it quickly! Let's get this railway going; if we're not successful with the coal, let's go all out for the timber. Otherwise we've had it!"
Zorba serê xwe xurandibû. «Drav kêm dibe, ne wisa, axa? Ev xerab e!» got. ||| Zorba had scratched his head. "Funds getting low, are they, boss? That's bad!" he said.
«Çûne, Zorba. Me hemû daqurtand. Tiştekî bike! Ceribandinên te çawa diçin? Hê bextê te venebû?» ||| "They're gone, Zorba. We've swallowed up the lot. Do something! How are your experiments going? No luck yet?"
Zorba serê xwe daxistibû û tu bersiv neda. Wê êvarê şerm kiribû. ||| Zorba had hung his head and made no reply. He had felt ashamed that evening.
«Ew berwara lanetî!» bi hêrs got. «Ezê hê jî serî li wê bigirim!» ||| "That damned slope!" he said furiously. "I'll get the better of it yet!"

Û niha ew ketibû hundir, rûyê wî bi serkeftinê ronî bûbû. ||| And now he had come in, his face lit up with success.
«Min kir, axa!» qîriya. «Min goşeya rast dît! Ji destên min direviya, dixwest ji min bireve, lê min ew girt û mîx kir, axa!» ||| "I've done it, boss!" he shouted. "I've found the right angle! It was slipping through my hands, trying to get away from me, but I held on and pinned it down, boss!"
«Ka, lezê bike û wê tiştê bide xebitandin! Berde, Zorba! Tu çi din lazim î?» ||| "Well, hurry up and get the thing working! Fire away, Zorba! What else do you need?"
«Sibê zû divê ez biçim bajêr û amûran bikirim: têlekî stûr ê pola, çerxik, bilî, bizmar, çengal.... Xem neke, ezê hema berî ku tu bibînî ez çûm vegerim!» ||| "Early tomorrow morning I must go to town and buy the tackle: a thick steel cable, pulleys, bearings, nails, hooks.... Don't worry, I'll be back almost before you've seen me go!"

Demek şûnde wî agir pêxist, xwarina me amade kir û me bi îşteheke ji rêzê xwar û vexwar. Me herduyan jî wê rojê baş xebitîbû. ||| He lit the fire shortly afterwards, prepared our meal and we ate and drank with excellent appetites. We had both worked well that day.

Sibeha din ez bi Zorba re heta gund çûm. ||| The next morning I went with Zorba as far as the village.
Em wek mirovên cidî û pratîkî li ser xebata komirê axivîn. ||| We talked like serious and practical-minded people about the working of the lignite.
Dema ku em ji berwarekê dadiketin, Zorba lingê xwe li kevirekî xist, ku gindirî ber bi jêr ve çû. ||| While going down a slope, Zorba kicked against a stone, which went rolling downhill.
Bo kêliyekê bi heyret sekinî, mîna ku cara yekem di jiyana xwe de vê dîmena ecêb dibîne. ||| He stopped for a moment in amazement, as if he were seeing this astounding spectacle for the first time in his life.
Berê xwe da min, û di nêrîna wî de min tirseke sivik ferq kir. ||| He looked round at me, and in his look I discerned faint consternation.
«Axa, ma te ew dît?» di dawiyê de got. «Li ser berwaran, kevir dîsa zindî dibin.» ||| "Boss, did you see that?" he said at last. "On slopes, stones come to life again."

Min tiştek negot, lê min şahiyeke kûr hîs kir. ||| I said nothing, but I felt a deep joy.
Min fikirî, dîtbar û helbestvanên mezin her tiştî bi vî awayî dibînin — mîna ku cara yekem. ||| This, I thought, is how great visionaries and poets see everything -- as if for the first time.
Her sibe dinyayeke nû li ber çavên xwe dibînin; bi rastî wê nabînin, wê diafirînin. ||| Each morning they see a new world before their eyes; they do not really see it, they create it.
Gerdûn ji bo Zorba, wek ji bo mirovên yekem ên li ser rûyê erdê, dîmenek giran û tûj bû; stêrk li ser wî dişemitîn, behr li ser eniya wî dişikiya. ||| The universe for Zorba, as for the first men on earth, was a weighty, intense vision; the stars glided over him, the sea broke against his temples.
Wî erd, av, heywan û Xwedê dijiya, bê destwerdana xerakar a aqil. ||| He lived the earth, water, the animals and God, without the distorting intervention of reason.

Madam Hortans hatibû agahdarkirin û li ber deriyê xwe li benda me bû. ||| Dame Hortense had been informed and she was waiting for us on her doorstep.
Boyaxkirî, bi pûdrayê girtî, û bêhntengî bû. ||| She was painted, caulked with powder, and uneasy.
Xwe wek lûnaparkeke şeva şemiyê xemilandibû. ||| She had got herself up like a fun fair on a Saturday night.
Hêstir li ber dergehê wê bû; Zorba bazda ser pişta wê û gem girtin. ||| The mule was in front of her gate; Zorba jumped on its back and seized the reins.
Sîrena pîr bi tirs nêzîk bû û destê xwe yê biçûk û qelew danî ser sîngê heywên, mîna ku bixwaze nehêle evîndarê wê biçe. ||| The old siren came up timidly and placed her plump little hand on the animal's breast, as if she wanted to prevent her beloved from leaving.
«Zorba....» bi nazî kir, xwe li ser tiliyên lingan rakir. «Zorba....» ||| "Zorba...." she cooed, raising herself on tiptoe. "Zorba...."
Zorba serê xwe zivirand aliyekî. ||| Zorba turned his head away.
Jê nefret dikir ku li nava rê neçar bimîne ku guhdariya gefûgotên evîndaran ên wiha bike. ||| He hated having to listen to lovers' nonsense like this in the middle of the road.
Jina belengaz nêrîna wî dît û tirsiya. ||| The poor woman saw his look and was terrified.
Lê destê wê hê li ser sîngê hêstir dimat, tije lavayeke nerm. ||| But her hand still pressed on the mule's breast, full of tender entreaty.
«Tu çi dixwazî?» Zorba bi hêrs pirsî. ||| "What do you want?" Zorba asked angrily.
«Zorba,» lava kir, «baş be.... Min ji bîr neke, Zorba.... Baş be....» ||| "Zorba," she pleaded, "be good.... Don't forget me, Zorba.... Be good...."
Zorba bê bersiv gem hejand. Hêstir bi rê ket. ||| Zorba shook the reins without replying. The mule started off.
«Bextê te vebe, Zorba!» min qîriya. «Sê roj, tu dibihîzî? Ne zêdetir!» ||| "Good luck, Zorba!" I cried. "Three days, do you hear? No more!"

##PG 88
Berê xwe zivirand, destê xwe yê mezin dihejand. ||| He turned round, waving his big hand.
Sîrena pîr digiriya û hêsirên wê di pûdraya li ser rûyê wê de cobar vedikirin. ||| The old siren was weeping and her tears washed furrows in the powder on her face.
«Min soz da te, axa!» Zorba qîriya. «Bi xatirê te!» ||| "I gave you my word, boss!" Zorba shouted. "Goodbye!"
Û li bin daran zeytûnê winda bû. ||| And he disappeared beneath the olive trees.
Madam Hortans giriya berdewam kir, lê çavên xwe li ser wî lekeyê rengîn dihişt ku ji berkêşa sor a şa çêbûbû, ya ku wê bi baldarî ji bo evîndarê xwe danîbû da ku ew bi rehetî rûne. ||| Dame Hortense went on crying, but she kept her eyes on the splash of color made by the gay red rug which she had placed so carefully for her beloved so that he should be comfortably seated.
Ew bê navber li pişt pelên zîvîn ên daran vedişart. Di demeke kurt de ew jî winda bû. ||| It was constantly being hidden by the silver foliage of the trees. Soon even that had disappeared.
Madam Hortans li dora xwe nihêrî. Dinya vala bû. ||| Dame Hortense looked round her. The world was empty.

Ez negeriyam paş ber bi peravê. Ez xemgîn bûm û ber bi çiyan ve meşiyam. ||| I did not go back to the beach. I felt sad and walked towards the mountains.
Çaxê ez gihîştim rêça çiyê, min dengê borîyekê bihîst. ||| As I reached the mountain track, I heard a trumpet sound.
Postevanê gund hatina xwe ya gund îlan dikir. ||| The country postman was announcing his arrival in the village.
«Mamoste!» gazî min kir, destê xwe dihejand. ||| "Master!" he called to me, waving his hand.
Ew hat û pakêtek rojname, çend kovarên edebî û du name dan min: yek min yekser xiste berîka xwe da ku êvarê bixwînim, çaxê roj diqede û ruh aram e. ||| He came over and gave me a packet of newspapers, some literary reviews and two letters: one I immediately put away in my pocket to read in the evening, when day is done and the spirit is calm.
Min dizanî kê ew nivîsiye û min dixwest şahiya xwe paşde bavêjim da ku ew bêtir bidome. ||| I knew who had written it and I wanted to defer my joy so that it should last longer.
Nameya din min ji nivîsa wê ya tûj û çikçikî û ji pûlên wê yên ecêb nas kir: ew ji yekî ji hevalên min ên kevn ên xwendekariyê, Karayanîs, hatibû. ||| The other letter I recognized from its sharp, jerky writing and the exotic stamps: it came from one of my old fellow students, Karayannis.

Ew ji çiyayekî hov ê Afrîkayê, li nêzî Tanganîkayê, bû. ||| It was from a wild African mountainside, near Tanganyika.
Ew zilamekî ecêb, hişk-hereket û esmer bû bi diranên pir spî. ||| He was a strange, impulsive, dark man with very white teeth.
Yek ji didanên wî yên tûj wek ên berazê kûvî derketibû derve. ||| One of his canines stuck out like a wild boar's.
Tu caran nedipeyivî, diqîriya. Tu caran gotûbêj nedikir, pev diçû. ||| He never talked, he shouted. He never discussed, he quarrelled.
Welatê xwe, Krêta, ku lê mamosteyekî ciwan ê teolojiyê û keşîşek bû, terikandibû. ||| He had left his own country, Crete, where he had been a young theology teacher and a monk.
Bi yek ji xwendekarên xwe re lehîstibû evînê, û rojekê ew li deşt û zeviyan dema hev maç dikirin hatibûn dîtin. Xelkê bi qêrîn ew şermezar kiribûn. ||| He had flirted with one of his students, and they had been surprised one day kissing out in the fields. They had been booed.
Heman rojê mamosteyê ciwan kincê keşîşiyê ji xwe avêt û li keştiyekê siwar bû. ||| The same day the young teacher threw off the cowl and took a boat.
Çû ba apekî xwe li Afrîkayê û bi dil û can dest bi xebatê kir. ||| He went to an uncle in Africa and started to work with a will.
Karxaneyeke werîs vekir û gelek pere qezenc kir. ||| He opened a rope factory and made a lot of money.
Carna ji min re dinivîsî û vedixwend ku ez biçim û şeş mehan li ba wî bimînim. ||| From time to time he wrote to me and invited me to go and stay with him for six months.
Her gava min yek ji nameyên wî vedikir, heta berî ku bixwînim, min dikaribû hîs bikira, ku ji rûpelên qelebalix, ên ku her dem bi benî bi hev ve hatibûn dirûtin, bayekî tund radibû ku porên min radiwestand. ||| Whenever I opened one of his letters, even before I read it, I could feel, arising from the crowded pages, which were always sewn together with string, a violent breath which made my hair stand on end.
Min her dem biryar dida ku ezê biçim wî li Afrîkayê bibînim, lê tu caran neçûm. ||| I was always deciding I would go and see him in Africa, but never went.

Ez ji rêçê derketim, li ser kevirekî rûniştim, ev name vekir û dest bi xwendinê kir: ||| I left the track, sat on a stone, opened and began reading this letter:

Tu kengê dê biryara xwe bidî ku werî vir ba min, lo kovika lanetî ya bi zinarên Yûnanîstanê ve zeliqî? ||| When are you going to make up your mind to come here to me, you damned limpet clamped to the rocks of Greece?
Tu jî bûyî Yûnaniyekî kêçî yê ji rêzê, meyxane-gerek, kesê ku di jiyana qehwexaneyan de digevize. ||| You, too, have turned into a typical lousy Greek, a tavern-loafer, a wallower in café-life.
Çimkî divê tu nefikirî ku tenê qehwexane qehwexane ne; pirtûk jî qehwexane ne, û edet jî, û îdeolojiyên te yên hêja jî. Ew hemû qehwexane ne. ||| Because you need not think only cafés are cafés; books are, too, and habits, and your precious ideologies. They are all cafés.
Îro yekşem e û tu karê min tune: ez li mîlkê xwe me û ez li te difikirim. ||| It is Sunday today and I have nothing to do: I am on my estate and I'm thinking of you.
Tav wek kuçik e, û qet dilopek baran nebariye. ||| The sun is like a furnace, and there has not been a drop of rain.
Li vir, çaxê baran dibare, di nîsan, gulan û hezîranê de, ew tofaneke rast e. ||| Here, when the rain does fall, in April, May and June, it's an absolute deluge.
Ez bi tena serê xwe me, û ji wê hez dikim. ||| I'm all alone, and I like that.
Li vir gelek Yûnaniyên kêçî hene (Ma cihek heye ku ev kurmik nagihîjinê?) lê ez naxwazim bi wan re tev bibim. Ew min bêzar dikin. ||| There are quite a lot of lousy Greeks here (Is there anywhere this vermin doesn't get to?) but I don't want to mix with them. They disgust me.
Heta li vir jî, lo meyxane-gerên lanetî — bila Şeytan we bibe — we kotîbûna xwe, paşgotina xwe ya reben ji me re şandiye. ||| Even here, you damned tavern-loafers -- may the Devil take you -- you've sent us your leprosy, your miserable back-biting.
Ev e ya ku Yûnanîstanê hildiweşîne — siyaset! Bê guman, lîstina qaxizan jî heye, û nezanî, û gunehên goşt. ||| That's what is ruining Greece -- politics! There's card-playing, too, of course, and ignorance, and the sins of the flesh.

##PG 89
Ez ji Ewrûpiyan nefret dikim; loma ez li vir di çiyayên Usumbara de digerim. ||| I detest Europeans; that's why I am wandering about here in the mountains of Usumbara.
Ez ji Ewrûpiyan nefret dikim, lê herî zêde ez ji Yûnaniyên kêçî û ji her tiştê Yûnanî nefret dikim. ||| I hate Europeans, but most of all I hate the lousy Greeks and everything Greek.
Ez êdî tu caran lingê xwe naxim Yûnanîstanê. Li vir e ku ezê biqedim. ||| I'll never set foot in Greece again. This is where I'll finish up.
Min jixwe gora xwe çêkiriye, li ber koxika xwe, li vir li ser çiyayê hov. ||| I've had my tomb made already, in front of my hut, here on the wild mountainside.
Min heta kevir jî daniye û bi destê xwe ev peyv bi tîpên girover ên mezin neqişandine: LI VIR YÛNANIYEK RAZAYE KU JI YÛNANIYAN NEFRET DIKE ||| I've even put up the stone and myself carved these words in large capitals: HERE LIES A GREEK WHO HATES THE GREEKS
Ez diteqim ji kenê, tif dikim, nifir dikim û digirîm her gava ku ez li Yûnanîstanê difikirim. ||| I burst out laughing, spit, swear and weep whenever I think of Greece.
Da ku ez tu Yûnaniyan û tu tiştê Yûnanî nebînim, min welat her û her terikand. ||| So as to see no Greeks and nothing Greek, I left the country forever.
Ez hatim vir, çarenûsa xwe bi xwe re anî — ne çarenûsa min bû ku ez anîm: mirov ya ku dibijêre dike! — min çarenûsa xwe anî vir û min wek koleyekî xebitî û hê jî dixebitim. ||| I came here, brought my destiny with me -- it was not my destiny which brought me: man does what he chooses! -- I brought my destiny here and I've worked and still am working like a slave.
Ez bi satilan xwêdan dirijînim û dê berdewam jî bikim. ||| I've been sweating and will continue to sweat by the bucketful.
Ez bi erd, ba, baran û bi karkeran, koleyên min ên sor û reş re şer dikim. ||| I am fighting with the earth, the wind, the rain, and with the workmen, my red and black slaves.
Tu kêfên min tune. Erê, yek: xebat. Bedenî û aqilî, lê bi taybetî bedenî. ||| I have no pleasures. Yes, one: work. Physical and mental, but preferably physical.
Ez hez dikim ku xwe biwestînim, xwêdan birijînim, dengê şikîna hestiyên xwe bibihîzim. ||| I like to exhaust myself, sweat, hear my bones crack.
Nîvê dravê xwe ez diavêjim, çawa û li ku bixwazim wî bi fîro dibim. ||| Half my money I throw away, waste it however and wherever I feel inclined.
Ez ne koleyê pere me: pere koleyê min e. ||| I'm not a slave to money: money is my slave.
Ez koleyê xebatê me, û ez pê serbilind im. ||| I am a slave to work, and I'm proud of it.
Ez daran dibirim; bi Brîtanyayê re peymaneke min heye. Ez werîs çêdikim; û niha min dest bi çandina pembû jî kiriye. ||| I fell trees; I have a contract with the British. I make rope; and now I've started planting cotton, too.

Şeva borî, di nav reşikên min de, du eşîr — Wa'yao û Wa'ngonî — li ser jinekê — li ser qehpikekê dest bi şer kirin. ||| Last night, among my negroes, two tribes -- the Wa'yao and the Wa'ngoni -- began fighting over a woman -- over a whore.
Tenê serbilindiyeke birîndar, tu dizanî. Tam wek li Yûnanîstanê. ||| Just hurt pride, you know. Just the same as in Greece.
Çêr, şer, û paşê gop derdikevin. Wan li ser wê serên hev şikandin. ||| Insults, brawls, and then out come the clubs. They broke one another's heads over her.
Jinan di nîvê şevê de bezîn ku min bînin, û bi qîrîna xwe ez hişyar kirim, da ku ez biçim hekemiyê bikim. ||| The women ran to fetch me in the middle of the night, and woke me with their yapping, to go and arbitrate.
Ez hêrs bûm, ji wan hemûyan re got ku herin ba şeytan, paşê ba polîsê Brîtanî. ||| I was angry, told them all to go to the devil, then to the British police.
Lê ew tevahiya şevê li ber deriyê min man û diqîriyan. ||| But they stayed there howling in front of my door the whole night.
Bi spêdeyê ez derketim û hekemî kir. ||| At dawn I went out and arbitrated.
Sibê, zû, ezê hilkişim çiyayên Usumbara, bi daristana xwe ya qalind, avên xwe yên teze û kesahiya xwe ya herheyî. ||| Tomorrow, early, I am going to scale the Usumbara mountains, with their dense forest, fresh waters and everlasting greenness.
Ka, lo Yûnaniyê kêçî yê Babîlî, tu kengê dê xwe ji Ewrûpayê vekî? «...ew qehpika mezin a ku li ser gelek avan rûdine, ya ku padîşahên erdê pê re zînayê kirine...!» ||| Well, you lousy Babylonian Greek, when will you cut adrift from Europe? "... that great whore that sitteth upon many waters, with whom the kings of the earth have committed fornication...!"
Tu kengê dê werî, da ku em bi hev re hilkişin van çiyayên pak û hov? ||| When will you come, so that we can climb these pure and wild mountains together?

Zarokek min ji jineke reş heye: keçek. ||| I have a child by a black woman: a girl.
Min diya wê şand: wê ez li ber çavên xelkê di ronahiya tava nîvro de, di bin her dareke kesk a derdorê de, bê rûmet kirim. ||| I've sent her mother away: she cuckolded me in public in the full glare of the midday sun, under every green tree in the neighborhood.
Ez jê têr bûm, û ew avêtim derve. ||| I had enough of her, and threw her out.
Lê min keçik hişt; ew du salî ye. Dikare bimeşe, û dest bi axaftinê dike. ||| But I kept the girl; she's two. She can walk, and she's beginning to talk.
Ez Yûnanî hîn dikim wê; hevoka yekem a ku min hîn kir ev bû: «Ez tif dikim li we, lo Yûnaniyên kêçî, ez tif dikim li we, lo Yûnaniyên kêçî!» ||| I'm teaching her Greek; the first sentence I taught her was: "I spit on you, you lousy Greeks, I spit on you, you lousy Greeks!"
Ew wek min e, qeşmera biçûk; tenê pozê diya xwe yê fireh û pehn jê girtiye. ||| She looks like me, the little scamp; she's only got her mother's broad, flat nose.
Ez ji wê hez dikim, lê tenê wek ku tu ji kûçik an pisîkekê hez dikî. ||| I love her, but just as you love a dog or a cat.
Were vir û ji jineke Usumbarayî kurekî çêbike. Emê rojekê wan herduyan bizewicînin, tenê ji bo ku em xwe şa bikin, û da ku wan jî şa bikin! ||| Come out here and get a boy by a Usumbara woman. We'll marry the two of them one day, just to amuse ourselves, and to amuse them, too!
Bi xatirê te! Bila şeytan bi te re be, û bi min re jî, hevalê hêja! Karayanîs, Servus diabolicus Dei. ||| Goodbye! May the devil go with you, and with me, dear friend! Karayannis, Servus diabolicus Dei.

Min name li ser çokên xwe vekirî hişt. ||| I left the letter open on my knees.
Daxwazeke geş a çûyînê dîsa ez girtim. ||| An ardent desire to go took possession of me once more.
Ne ji ber ku min dixwest biçim — ez li ser vê peravê Krêtayî gelek baş bûm, û ez li vir bextewar û azad hîs dikir û ne hewceyî tiştekî bûm — lê ji ber ku ez her dem bi daxwazekê dişewitîm: berî ku ez bimirim bi qasî ku ji destê min tê erd û behrê bidestînim û bibînim. ||| Not because I wanted to leave -- I was quite all right on this Cretan coast, and I felt happy and free here and I needed nothing -- but because I have always been consumed with one desire: to touch and see as much as possible of the earth and the sea before I die.

##PG 90
Ez rabûm ser xwe, biryara xwe guhert, û li şûna ku hilkişim girê, bi lez ber bi peravê ve çûm. ||| I stood up, changed my mind, and instead of climbing the hill went hurriedly towards the beach.
Min nameya din di berîka jorîn a çakêtê xwe de hîs kir, û êdî nikaribû li bendê bimînim. ||| I felt the other letter in the upper pocket of my coat, and could not wait any more.
Ew pêşçêjeya şîrîn û nayê ragirtin a şahiyê têra xwe dirêj kiribû. ||| That sweet, unbearable foretaste of joy had lasted long enough.
Ez gihîştim koxikê, agir pêxist, hineke çay çêkir, hineke nan û hingiv û pirteqal xwar. ||| I reached the hut, lit the fire, made some tea, ate some bread and honey and oranges.
Cilên xwe ji xwe kirin, li ser nivîna xwe dirêj bûm û name vekir: ||| I undressed, stretched out on my bed and opened the letter:

Mamoste û şagirt — Silav! ||| Master and neophyte -- Greetings!
Li vir karekî pir mezin û dijwar ê min heye, "Xwedê" şikir — ez peyva metirsîdar dixim nav nîşanên ginavkê (wek heywanekî hov li pişt mîlan) da ku tu hema ku nameya min vekî coş nebî. ||| I have a tremendous and difficult job here, thank "God" -- I enclose the dangerous word in inverted commas (like a wild beast behind bars) so that you do not get excited as soon as you open my letter.
Ka, karekî pir dijwar, pesnê "Xwedê" be! ||| Well, a very difficult job, "God" be praised!
Nîv milyon Yûnanî li başûrê Rûsyayê û li Kafkasyayê di metirsiyê de ne. ||| Half a million Greeks are in danger in the south of Russia and the Caucasus.
Gelek ji wan tenê bi tirkî an rûsî dipeyivin, lê dilên wan bi tundî bi Yûnanî dipeyivin. Ew ji nijada me ne. ||| Many of them speak only Turkish or Russian, but their hearts speak Greek fanatically. They are of our race.
Tenê ku tu li wan binêrî — awayê ku çavên wan diçirisin, çavbirçî, rovîçav, jîrî û şehweta lêvên wan dema dibişirin, awayê ku wan karîbûye bibin axa û cotkarên rûs ji bo wan li vî welatê fireh ê Rûsyayê bixebitin — têra wê dike ku te qanih bike ku ew nevîyên Odîsewsê te yê hezkirî ne. ||| Just to look at them -- the way their eyes flash, rapacious, ferrety, the cunning and sensuality of their lips when they smile, the way they have managed to become bosses and have moujiks working for them in this immense territory of Russia -- it's quite enough to convince you that they are descendants of your beloved Odysseus.
Loma mirov dest pê dike ji wan hez dike û nikare bihêle ku ew helak bibin. Çimkî ew di xetereya helakbûnê de ne. ||| So one comes to love them and cannot let them perish. For they are in danger of perishing.
Wan hemû tiştê xwe winda kiriye, birçî û tazî ne. ||| They have lost all they had, are hungry and naked.
Ji aliyekî Bolşewîk wan diêşînin; ji aliyê din Kurd. ||| From one side they are harried by the Bolsheviks; from the other by the Kurds.
Penaber ji her aliyî bi peq hatine da ku li vî an wî bajarî li Gurcistan û Ermenistanê bi cih bibin. ||| Refugees have swarmed in from every direction to settle in one town or another in Georgia and Armenia.
Ne xwarin, ne derman, ne cil heye. ||| There's no food, medicine, or clothing.
Li benderan kom dibin, bi bêhntengî li asoyê digerin li hêviya keştiyên Yûnanî yên ku werin wan vegerînin ba Dayika wan — Yûnanîstanê. ||| They gather in the ports, scan the horizon anxiously for Greek ships coming to take them back to their Mother -- Greece.
Beşek ji nijada me — ev tê wateya beşek ji ruhê me — ketiye panîkê. ||| One part of our race -- that means one part of our soul -- is panic-stricken.
Eger em wan li ber çarenûsa wan bihêlin, ew dê helak bibin. ||| If we leave them to their fate, they will perish.

Pêdiviya me bi gelek hezkirin û têgihiştin, coş û aqilê pratîkî heye — wan taybetmendiyên ku tu ewqas hez dikî ku bi hev re bibînî — eger em bixwazin wan rizgar bikin û wan vegerînin wê beşa welatê me yê azad ku ew tê de herî bi kêr bên — yanî, li sînorên Makedonyayê, û, hê dûrtir, li sînorên Trakyayê. ||| We need a lot of love and understanding, enthusiasm and practical sense -- those qualities which you like so much to see united -- if we are going to save them and get them back to the part of our own free land where they will be of most use -- that is, on the frontiers of Macedonia, and, further afield, on the frontiers of Thrace.
Ev tenê rê ye ku em ê sed hezaran Yûnaniyan rizgar bikin, û xwe jî bi wan re rizgar bikin. ||| That is the only way we shall save hundreds of thousands of Greeks, and save ourselves with them.
Çimkî hema ku ez gihîştim vir min xelekek kişand, bi awayê ku te hîn ez kiribû, û min ji wê xelekê re got "erkê min." ||| For as soon as I arrived here I drew a circle, in the way you taught me, and called that circle "my duty."
Min got: «Eger ez vê xeleka tevahî rizgar bikim, ez rizgar im; eger ez wê rizgar nekim, ez winda me!» ||| I said: "If I save this entire circle, I am saved; if I do not save it, I am lost!"
Ka, di hundirê wê xelekê de pênc sed hezar Yûnanî hene! ||| Well, inside that circle there are five hundred thousand Greeks!

Ez diçim bajar û gundan, hemû Yûnaniyan kom dikim, rapor dinivîsim, telegram dişînim, hewl didim ku karbidestên me yên li Atînayê keştî, xwarin, cil û derman bişînin, û van afirîdên belengaz biguhêzînin Yûnanîstanê. ||| I go to towns and villages, collect all the Greeks together, write reports, send telegrams, try to make our officials in Athens send boats, food, clothes, and medicine, and transport these poor creatures to Greece.
Eger têkoşîna bi kel û hişkî tê wateya bextewarbûnê, vêca ez bextewar im. ||| If to struggle with zeal and obstinacy is to be happy, then I am happy.
Ez nizanim ka min, ji bo ku gotina te bi kar bînim, bextewariya xwe li gorî bejna xwe biriye an na. ||| I do not know whether I have cut my happiness to my stature, to use your phrase.
Hêvîdar im ku min kiribe, çimkî hingê ezê bibûma kesekî mezin. ||| Please heaven I have, because then I would be a great person.
Ez dixwazim bejna xwe bigihînim wê tiştê ku ez difikirim dê min bextewar bike; yanî, heta sînorên herî dûr ên Yûnanîstanê! ||| I would like to increase my stature to what I think would make me happy; that is, to the farthest frontiers of Greece!

Lê ev teorî bes e! Tu li ser peravê xwe yê Krêtayî dirêjbûyî, guhdariya dengê behrê û santûriyê dikî — wextê te heye, yê min tune. ||| But that's enough theory! You are lying on your Cretan beach, listening to the sound of the sea and the santuri -- you have time, I have not.
Ez di nav çalakiyê de hatime daqurtandin û ez pê kêfxweş im. ||| I am swallowed up by activity and I am glad of it.
Kar, mamosteyê min ê hêja yê bêkar, kar; rizgariyeke din tune. ||| Action, dear inactive master, action; there is no other salvation.

Mijara ramanên min, bi rastî, pir sade û yekpare ye. ||| The subject of my meditations is, in fact, very simple and all of a piece.
##PG 91
Ez dibêjim: Ev rûniştiyên Pontos û Kafkasyayê, cotkarên Karsê, bazirganên mezin û biçûk ên Tîflîs, Batûm, Novo Rosîsk, Rostov, Odessa û Krîmyayê, yên me ne, ew ji xwîna me ne; ji wan re, wek ji me re, paytexta Yûnanîstanê Konstantînopolîs e. ||| I say: These inhabitants of the Pontus and the Caucasus, peasants of Kars, big and small merchants of Tiflis, Batum, Novo Rossisk, Rostov, Odessa and the Crimea, are ours, they are of our blood; for them, as for us, the capital of Greece is Constantinople.
Hemûyên me heman serek heye. ||| We all have the same chief.
Tu jê re dibêjî Odîsews, yên din Konstantînos Paleologos — ne ew ê ku li bin sûrên Bîzansê hat kuştin, lê yê din, yê efsanewî, ê ku bû mermer û hê jî rast disekine li hêviya Milyaketê Azadiyê. ||| You call him Odysseus, others Constantinos Palaeologos -- not the one who was killed beneath the walls of Byzantium, but the other, the legendary one, who was changed into marble and still stands erect waiting for the Angel of Liberty.
Bi destûra te, ez ji vî serekê nijada me re dibêjim Akrîtas. Ez ji wî navî bêtir hez dikim; ew hişktir û şeranetir e. ||| With your permission, I call this chief of our race Acritas. I like that name better; it is more austere and warlike.
Hema ku tu wê dibihîzî, di hundirê te de wêneyê Yewnaniyê herheyî radibe, bi tev çek, bê navber û bê bêhnvedan li ser tixûb û sînoran şer dike. ||| As soon as you hear it, there rises within you the image of the eternal Hellene, fully armed, fighting without cease or respite on the boundaries and frontiers.
Li ser her sînorî: neteweyî, aqilî, û ruhanî. ||| On every frontier: national, intellectual, and spiritual.
Û eger tu Dîgenes lê zêde bikî, tu hê bi temamtir wê senteza ecêb a Rojhilat û Rojavayê ku nijada me ye teswîr dikî. ||| And if you add Digenes, you describe even more completely that marvellous synthesis of East and West which is our race.

Ez niha li Karsê me; ez hatim ku hemû Yûnaniyên gundên dorê kom bikim. ||| I am in Kars now; I came to assemble all the Greeks of the neighboring villages.
Roja hatina min, Kurdan li herêmê mamosteyekî û keşîşekî Yûnanî girtibûn û nalên hespan li lingên wan mîx kiribûn. ||| On the day of my arrival the Kurds had seized a Greek teacher and priest in the district and nailed horse-shoes to their feet.
Giregir tirsiyabûn û penaberî mala ku ez lê dimînim bûbûn. ||| The notables were horrified and took refuge in the house where I am staying.
Em dikarin bibihîzin ku çekên Kurdan her dem nêzîktir tên. ||| We can hear the Kurds' guns coming closer all the time.
Hemû van Yûnaniyan çavên xwe li ser min mîx kirine, mîna ku ez yê tenê bim ê ku hêza wî heye ku wan rizgar bike. ||| All these Greeks have their eyes fixed on me, as if I were the only one with the strength to save them.

Min hesab dikir ku sibê ji bo Tîflîsê biçim, lê niha, li hember vê metirsiyê, ez şerm dikim ku biçim. Loma ez dimînim. ||| I was counting on leaving tomorrow for Tiflis, but now, in the face of this danger, I am ashamed to leave. So I am staying.
Ez nabêjim ku ez natirsim; ez ditirsim, lê ez şerm dikim. ||| I don't say I am not afraid; I am afraid, but I'm ashamed.
Ma Şervanê Rembrandt, Şervanê min, dê heman tişt nekira? ||| Wouldn't Rembrandt's Warrior, my Warrior, have done the same thing?
Ew dê bimaya; loma ez jî dimînim. ||| He would have stayed; so I am staying, too.
Eger Kurd bikevin bajêr, ev tenê xwezayî û rast e ku ez bibim yê yekem ê ku nal lê tên xistin. ||| If the Kurds come into the town it is only natural and just that I should be the first to be shoed.
Ez piştrast im, mamoste, te tu caran nedifikirî ku şagirtê te dê wisa biqede! ||| I am sure, master, you never thought your pupil would end like this!

Piştî yek ji wan gotûbêjên Yûnanî yên bêdawî, me biryar da ku her kes îşev bi hêstir, hesp, dewar, jin û zarokan kom bibe, û bi spêdeyê em ê hemû bi hev re ber bi bakur ve bi rê kevin. ||| After one of those interminable Greek discussions we decided that everyone should assemble this evening with mules, horses, cattle, women and children, and at dawn we will all start out together for the north.
Ezê li pêş bimeşim, beranê ku rê li keriyê dike. ||| I shall walk in front, the ram guiding the flock.
Koçeke bavkanî ya gelekî li ser zincîreyên çiya û deştên bi navên efsanewî! ||| A patriarchal emigration of a people over chains of mountains and plains with legendary names!
Û ez ê bibim cûreyekî Mûsa — Mûsayekî teqlîdî — ku nijada bijartî ber bi Welatê Soz ve dibe, wek ku ev gelê sade ji Yûnanîstanê re dibêjin. ||| And I shall be a sort of Moses -- an imitation Moses -- leading the chosen race to the Promised Land, as these naive people are calling Greece.

Bê guman, ji bo ku ez bi rastî hêjayî vê peywira Mûsayî bim û te rezîl nekim, divê min ew gore-pijamayên xwe yên xweşik ên ku tu pê min tinazan dikî ji holê rakira û lingên xwe bi postê pez pêçabûya. ||| Of course, to be really worthy of this Mosaic mission and not disgrace you, I should have done away with my elegant leggings which you tease me about and wrapped my legs in sheepskin.
Divê her wiha rîyeke dirêj, bi rûn û şepelî hebûya, û, berî her tiştî, cotek strûyên mezin. ||| I should also have a long, greasy, wavy beard, and, above all, a large pair of horns.
Lê biborîne, ez nikarim wê kêfê bidim te. ||| But I'm sorry, I can't give you that pleasure.
Hêsantir e ku ez ruhê xwe biguherim ne ku cilê xwe. ||| It's easier to get me to change my soul than my costume.
Ez gore-pijaman li xwe dikim; ez wek qurmê keleman hilû taştî me; û ez ne zewicî me. ||| I wear leggings; I am as smooth shaven as a cabbage stump; and I'm not married.

Mamoste, hêvî dikim ku tu vê nameyê bistînî, çimkî dibe ku ya dawî be. Tu kes nikare bibêje. ||| Master, I hope you get this letter, for it may be the last. No one can say.
Ez baweriya xwe bi wan hêzên veşartî yên ku tê gotin mirovan diparêzin nayînim. ||| I have no confidence in the secret forces which are said to protect men.
Ez bi hêzên kor bawer dikim ku rast û çep lê dixin, bê kîn, bê armanc, ku her kesê ku rêûberê wan be dikujin. ||| I believe in the blind forces which hit out right and left, without malice, without purpose, killing whoever happens to be in their way.
Eger ez vê erdê biterikînim (ez dibêjim "biterikînim" da ku te an xwe bi peyva rast netirsînim), eger ez vê erdê biterikînim, ez dibêjim, hêvî dikim ku tu sax û bextewar bimînî, mamosteyê hêja! ||| If I leave this earth (I say "leave" so as not to frighten you or myself with the proper word), if I leave this earth, I say, I hope you keep well and happy, dear master!

##PG 92
Ez şerm dikim ku divê wê bibêjim, lê divê, loma bibore: min jî, ji te pir bi dilovanî hez kiribû. ||| I am embarrassed at having to say it, but I must, so please excuse me: I, too, have loved you very dearly.
Paşê li jêr, bi lez bi qelemê reşîn nivîsandî, ev paşnivîs hebû: ||| Then underneath, written hurriedly in pencil, was this postscriptum:
ps. Min ew lihevkirina ku me roja çûyîna min li keştiyê kiribû ji bîr nekiriye. ||| ps. I haven't forgotten the agreement we made on the boat the day I left.
Eger ez neçar bibim ku vê erdê "biterikînim", ezê te hişyar bikim, bîne bîra xwe, li ku derê bî; nehêle ku ew te bitirsîne. ||| If I have to "leave" this earth, I shall warn you, remember, wherever you are; don't let it scare you.
"""

CH13 = r"""
##PG 92
##FIRST
Sê roj, çar roj, pênc roj derbas bûn, û hê Zorba tune. ||| Three days, four days, five days went by, and still no Zorba.
Roja şeşan min ji Kandiyayê nameyek bi çend rûpelan, hemûyek qise-mise, stand. ||| On the sixth day I received from Candia a letter several pages long, a whole lot of rigmarole.
Li ser kaxezê pembe yê bîhnxweş hatibû nivîsandin û, li quncikê rûpelê, dilekî ku bi tîrekê hatibû qul kirin hebû. ||| It was written on scented pink paper and, in the corner of the page, was a heart pierced by an arrow.
Min ew bi baldarî parast û ez wê bi dilsozî vediguhêzim, gotinên zehmet ên ku li vir û wir tê dîtin diparêzim. ||| I kept it carefully and am copying it faithfully, retaining the labored expressions to be found here and there.
Min tenê rastnivîsa wê ya delal sererast kir. ||| I have merely corrected the charming spelling.
Zorba qelem wek kazmeyekê digirt; pê bi tundî êrîşî kaxezê dikir, û loma di kaxezê de çend qul hebûn û bi lekeyan nixumî bû. ||| Zorba held a pen like a pickaxe; he attacked the paper violently with it, and that is why the paper had a number of holes in it and was covered with blots.

Axayê hêja! Birêz Sermayedar! ||| Dear Boss! Mister Capitalist!
Ez qelemê hildidim da ku bipirsim ka tenduristiya te baş e. Em jî gelek baş in, pesnê Xwedê be! ||| I take up the pen to ask if your health is favorable. We are quite well, too, God be praised!
Demek e min fêm kiriye ku ez nehatime vê dinyayê da ku bibim hesp, an ga. ||| I have realized for some time I didn't come into this world to be a horse, or an ox.
Tenê heywan dijîn da ku bixwin. ||| Only animals live to eat.
Ji bo ku ez ji wê sûcdarkirina jorîn xilas bibim, ez roj û şev ji xwe re karan diafirînim. ||| To escape the above accusation, I invent jobs for myself day and night.
Ez nanê xwe yê rojane ji bo fikrekê dixim xetereyê, ez gotina pêşiyan berevajî dikim û dibêjim: «Çêtir e mirov mirîşkavîyeke zeyf li ser golekê be ji çûçikê qelew ê di qefesekê de.» ||| I risk my daily bread for an idea, I turn the proverb round and say: "Better be a lean moorhen on a pond than a fat sparrow in a cage."
Gelek mirov welatparêz in bê ku tiştekî li wan bikeve. ||| Lots of people are patriots without it costing them anything.
Ez ne welatparêz im, û ne jî ez ê bibim, çi li min bikeve bila bikeve. ||| I am not a patriot, and will not be, whatever it costs me.
Gelek mirov bi bihiştê bawer dikin û li wir kerekî girêdayî dihêlin. Kerê min tune, ez azad im! ||| Lots of people believe in paradise and they keep an ass tethered there. I have no ass, I am free!
Ez ji dojehê natirsim ku kerê min lê bimire. Ez hesreta bihiştê jî nakişînim, ku ew lê xwe bi nefelê têr bike. ||| I am not afraid of hell where my ass would die. I don't long for paradise either, where he would stuff himself with clover.
Ez kafê nezan im, ez nizanim çawa tiştan rave bikim, lê tu min fêm dikî, axa. ||| I am an ignorant blockhead, I don't know how to put things, but you understand me, boss.

Gelek mirov ji betaliya tiştan tirsiyane! Min ew têk bir. ||| Lots of people have been afraid of the vanity of things! I've overcome it.
Gelek kûr difikirin; ez ne hewceyî fikirînê me. ||| Lots reflect hard; I have no need to reflect.
Ez bi qenciyê şa nabim û bi xirabiyê bêhêvî nabim. ||| I don't rejoice over the good and don't despair over the bad.
Eger ez bibihîzim ku Yûnaniyan Konstantînopolîs girtiye, ev ji bo min tam wek e ku tirk Atînayê digirin. ||| If I hear that the Greeks have taken Constantinople, it's just the same to me as if the Turks were taking Athens.
Eger tu ji vê qise-misa ku ez dikim difikirî ku serê min nerm dibe, ji min re binivîse. ||| If you think from the balderdash I talk I'm going soft in the head, write to me.

Ez li vir li Kandiyayê dikevim dikanan, hewl didim têl bikirim, û ez dikenim. ||| I go into the shops here in Candia, trying to buy cable, and I laugh.
«Tu bi çi dikenî, birawo?» her dipirsin. ||| "What are you laughing at, brother?" they keep asking.
Lê ez çawa dikarim ji wan re bibêjim? ||| But how can I tell them?
Ez dikenim ji ber ku, tam dema ku ez destê xwe dirêj dikim da ku bibînim ka têlê pola baş e, ez li ser wê difikirim ka mirovahî çi ye û çima qet hat ser vê erdê û çi feyda wî heye.... ||| I laugh because, just when I hold out my hand to see if the steel cable is good, I think about what mankind is and why he ever came onto this earth and what good he is....
Qet tu feyde, eger tu ji min bipirsî. ||| No good at all, if you ask me.
Ferq nake ka jineke min heye an na, ka ez rastgo me an na, ka ez paşa me an hammalê kuçeyan. ||| It makes no difference whether I have a woman or whether I don't, whether I'm honest or not, whether I'm a pasha or a street-porter.
Tişta yekane ya ku ferqê çêdike ev e ka ez sax im an mirî. ||| The only thing that makes any difference is whether I'm alive or dead.
Çi şeytan an Xwedê gazî min bike (û tu dizanî çi, axa? ez difikirim şeytan û Xwedê eynî ne), ez ê bimirim, bibim cendekê bîngenî, û bîna mirovan bibirim. ||| Whether the devil or God calls me (and do you know what, boss? I think the devil and God are the same), I shall die, turn into a reeking corpse, and stink people out.
Ew ê neçar bibin ku min bi kêmî çar lingan di bin axê de bitepisînin, da ku nexeniqin! ||| They'll be obliged to shove me at least four feet down in the earth, so that they won't get choked!

Bi awayekî, ez ê li ser tiştekî ji te bipirsim ku min hineke ditirsîne — tişta yekane, bala xwe bide — û ne bi şev ne bi roj aramiyê nade min. ||| By the way, I'm going to ask you about something that rather scares me -- the only thing, mind -- and it leaves me no peace, night or day.
Tişta ku min ditirsîne, axa, kalbûn e. ||| What scares me, boss, is old age.
##PG 93
Bila ezman me jê biparêze! ||| Heaven preserve us from that!
Mirin tiştek nîne — tenê pif! û find vedimire. ||| Death is nothing -- just pff! and the candle is snuffed out.
Lê kalbûn rezîlî ye. ||| But old age is a disgrace.
Ez wê rezîliyeke kûr dihesibînim ku ez qebûl bikim ku ez pîr dibim, û ez her tiştê ji destê min tê dikim da ku xelk nebîne ku ez pîr bûme: ez bazdidim, dans dikim, pişta min diêşe lê ez berdewamî dans dikim. ||| I consider it a deep disgrace to admit I'm getting on, and I do all I can to stop people seeing I've grown old: I hop about, dance, my back aches but I keep dancing.
Ez vedixwim, serê min digêre, her tişt dizivire, lê ez rûnanim, ez tenê xwe wisa nîşan didim ku her tişt çiqas baş e. ||| I drink, get dizzy, everything spins round, but I don't sit down, I just act as if everything's hunky-dory.
Ez xwêdan dirijînim, loma xwe diavêjim behrê, sermayê digirim û dixwazim bikuxim — gûh! gûh! — da ku xwe rehet bikim lê ez şerm dikim, axa, û kuxikê bi zorê paşde dixim. ||| I sweat, so I plunge into the sea, catch cold and want to cough -- gooh! gooh! -- to relieve myself but I feel ashamed, boss, and force back the cough.
Ma te tu caran ez kuxînim bihîstime? Qet! ||| Have you ever heard me cough? Never!
Û ne, wek ku tu dibe ku bifikirî, tenê dema ku mirovên din li dora min in, lê dema ku ez bi tena serê xwe me jî! ||| And not, as you might think, just when there are other people about, but when I'm by myself, too!
Ez li ber Zorba şerm dikim — tu li ser wê çi difikirî, axa? Ez li ber wî şerm dikim! ||| I feel ashamed in front of Zorba -- what do you think of that, boss? I'm ashamed in front of him!

Rojekê li Çiyayê Athos — çimkî ez lê bûme, û çêtir bûya ku min destê xwe yê rastê biqut bikira! — ez rastî keşîşekî hatim, Bavê Lavrentio, ji Çîosê. ||| One day on Mount Athos -- because I've been there, and I'd have done better to cut off my right hand! -- I met a monk, Father Lavrentio, a native of Chios.
Ew, belengaz, bawer dikir ku şeytanek di hundirê wî de heye û heta navek jî lê danîbû: jê re digot Xoce. ||| He, poor fellow, believed he had a devil inside him and he'd even given him a name: he called him Hodja.
«Xoce dixwaze roja Înîya Pîroz goşt bixwe!» Lavrentioyê belengaz dikuriya, serê xwe li dîwarê dêrê dixist. ||| "Hodja wants to eat meat on Good Friday!" poor Lavrentio used to roar, beating his head on the church wall.
«Xoce dixwaze bi jinekê re raze. Xoce dixwaze serkeşîş bikuje. Ev Xoce ye, Xoce ye, ne ez im!» ||| "Hodja wants to sleep with a woman. Hodja wants to kill the Abbot. It's Hodja, Hodja, it isn't me!"
Û serê xwe li kêvir dixist. ||| And he'd bang his head on the stone.
Cûreyekî şeytan di hundirê min de jî heye, axa, û ez jê re dibêjim Zorba! ||| I've a kind of devil inside me, too, boss, and I call him Zorba!

Zorbayê hundirîn naxwaze pîr bibe, qet, û ew pîr nebûye, ew tu caran pîr nabe. ||| The inner Zorba doesn't want to grow old, not at all, and he hasn't grown old, he never will grow old.
Ew dêwek e, porê wî reş wek şebeqê ye, sî û du (bi reqeman: 32) diran, û qerenfîleke sor li pişt guhê wî. ||| He's an ogre, he's got hair as black as jet, thirty-two (figures: 32) teeth, and a red carnation behind his ear.
Lê Zorbayê derîn, belengaz, hineke zik girtiye û çend porên spî peyda kirine. ||| But the outer Zorba, poor devil, has got a bit of a corporation and quite a few white hairs.
Ew çilmisî û qermiçî bûye; diranên wî dikevin û guhê wî yê mezin tije porê spî yê kalbûnê ye, porê dirêj ê kerî! ||| He's shrivelled and gone wrinkled; his teeth fall out and his big ear is full of the white hair of old age, long ass's hair!
Ew çi dikare bike, axa? Ev her du Zorba dê heta kengê li hev bidin? Kîjan dê bi ser bikeve? ||| What can he do, boss? How long will these two Zorbas fight each other? Which one will win?
Eger ez di demeke nêz de bimirim, dê baş be, ez ne li ser im. ||| If I kick the bucket soon, it'll be all right, I don't care.
Lê eger ez hê demeke dirêj bijîm, ez qediyam. Qediyam, axa! ||| But if I go on living for a long time yet, I'm done. Done, boss!
Ew roj dê bê ku ez ê rezîl bibim. Ez ê azadiya xwe winda bikim: bûka min û keça min dê emir li min bikin ku ez çavdêriya pitikekê bikim, cinawirekî wan ê biçûk ê tirsnak, da ku xwe neşewitîne, an nekeve, an xwe qirêj neke. ||| The day will come when I'll be disgraced. I'll lose my liberty: my daughter-in-law and daughter will order me to keep watch on some infant, a fearful little monster of theirs, so that he doesn't burn himself, or fall over, or dirty himself.
Û eger ew xwe qirêj bike, pûf! dê min mecbûr bikin ku wî paqij bikim! ||| And if he does dirty himself, pooh! they'll make me clean him up!
Tu jî dê neçar bibî ku heman cûreyê şermê derbas bikî, axa, her çend tu ciwan î. Bala xwe bide. ||| You'll have to go through the same sort of shame, boss, although you're young. You watch out.
Guhdariya ya ku ez ji te re dibêjim bike, heman rê wek min bigire, rizgariyeke din tune: bila em hilkişin çiyan, ji bo komir, sifir, hesin û kelemînê wan bikolin; bila em sermayeya xwe çêkin da ku xizm rêzê li me bigirin û heval solên me bilîsin û hemû dewlemend kumên xwe ji me re rakin. ||| Listen to what I tell you, follow the same road as me, there's no other salvation: let's go up into the mountains, mine them for coal, copper, iron and calamine; let's make our pile so that relatives respect us and friends lick our boots and all the well-to-do raise their hats to us.
Eger em serfiraz nebin, axa, çêtir e ku em bar bikin, ji aliyê guran, an hirçan, an her heywanekî hov ê ku em bibînin ve bên kuştin — û bila ji wan re pir xêr be! ||| If we don't succeed, boss, we might as well pack up, be killed by wolves, or bears, or any wild beast we can find -- and much good may it do them!
Loma Xwedê heywanên hov şandin ser erdê: da ku çend mirovên wek me biqedînin, da ku ew pir nizm nekevin. ||| That's why God sent wild beasts on earth: to finish off a few people like us, so they don't fall too low.

Li vir Zorba bi qelemên rengîn zilamekî dirêj û zeyf kişandibû, ku di bin hin daran kesk de direvî, bi heft gurên sor li pey wî, û li jora wêneyê, bi tîpên mezin, hatibû nivîsandin: «Zorba û Heft Gunehên Kujer.» ||| Here Zorba had drawn with colored pencils a tall, lean man, fleeing under some green trees, with seven red wolves at his heels, and at the top of the picture, in big letters, was written: "Zorba and the Seven Deadly Sins."
Paşê berdewam kir: ||| Then he went on:

Divê tu ji vê nameyê bibînî ku ez çi mirovekî bêbext im. ||| You must see from this letter what an unhappy man I am.
Tenê dema ez bi te re me, bi axaftina bi te re, derfeta min heye ku ji rewşa xwe ya hişê nexweş hineke rehet bibim. ||| It's only when I'm with you that I have any chance, through talking to you, of getting some relief from my morbid state of mind.
Çimkî tu jî wek min î, tenê tu wê nizanî. ||| Because you're like me, too, only you don't know it.
##PG 94
Şeytanek di hundirê te de jî heye, lê tu hê navê wî nizanî, û, ji ber ku tu wê nizanî, tu dikarî bêhna xwe bistînî. ||| You've got a devil inside you, as well, but you don't know his name yet, and, since you don't know that, you can breathe.
Wî vaftîz bike, axa, û tê xwe çêtir hîs bikî! ||| Baptize him, boss, and you'll feel better!

Min digot ku ez çiqas bêbext im. ||| I was saying how unhappy I am.
Ez bi zelalî dibînim ku hemû aqilê min ehmeqî ye û tiştekî din nîne. ||| I can see clearly that all my intelligence is stupidity and nothing more.
Lê dem hene, ku bo rojên tev fikrên mezin tên hişê min, û xwezî min bikariya ya ku ew Zorbayê hundirîn ji min re dibêje bikim, dinya dê heyirî bimaya! ||| There are times, though, when for whole days great thoughts occur to me, and if only I could do what that inside Zorba tells me to do the world would be amazed!
Ji ber ku di peymana min a bi jiyanê re tu bendeke dem-sînor tune, ez frênan berdidim çaxê digihîjim berwarên herî metirsîdar. ||| Seeing as how I have no time-limit clause in my contract with life, I let the brakes off when I get to the most dangerous slopes.
Jiyana mirov rêyek e bi hevraz û nişîvên zîq. ||| The life of man is a road with steep rises and dips.
Hemû mirovên bi aqil frênên xwe bi kar tînin. ||| All sensible people use their brakes.
Lê — û li vir e, axa, dibe ku ez nîşan bidim ez ji çi hatime çêkirin — min ji mêj ve frênên xwe bi temamî ji holê rakirine, çimkî ez qet ji şokekê natirsim. ||| But -- and this is where, boss, maybe I show what I'm made of -- I did away with my brakes altogether a long time ago, because I'm not at all scared of a jolt.
Çaxê makîneyek ji rê derdikeve, em mekanîk jê re dibêjin «şok!» ||| When a machine goes off the rails we mechanics call that "a jolt!"
Û şeytan dizane ka ez bala xwe didim wan şokên ku ez distînim. ||| And the devil knows if I take any notice of the jolts I get.
Roj û şev, ez bi temamî hêz diçim pêş, tenê ya ku ji dilê min e dikim; bila xerabtir be eger ez bişkêm û perçe-perçe bibim. ||| Day and night, I go full steam ahead, doing just what I like; so much the worse if I fold up and get smashed to pieces.
Ez çi heye ku winda bikim? Tu tişt. ||| What have I got to lose? Nothing.
Heta eger ez hêdî jî bibim, ma ez ê heman awayî neqedim? Bê guman ez ê biqedim! Loma bila em bi lez bişewitin diçin! ||| Even if I do take it easy, won't I end up just the same? Of course I will! So let's scorch along!

Ez piştrast im ku ez niha te dikenînim, axa, lê ez qise-misa xwe dinivîsim, an, eger tu bixwazî, ramanên xwe, an lawaziyên xwe — ferqa di navbera her sêyan de çi ye? — ez bi rastî nikarim bibêjim — ez ji te re dinivîsim, û tu baş bikene eger tu aciz nebî. ||| I'm sure I'm making you laugh now, boss, but I'm writing down my blather, or, if you like, my reflections, or my weaknesses -- what's the difference between the three? -- I really couldn't say -- I'm writing to you, and you have a good laugh if you're not bored.
Ez bi fikra te ya ku dikenî dikenim, û bi vî awayî ken li ser vê erdê tu caran nasekine. ||| I'm laughing at the thought of you laughing, and that's how laughing never stops on this earth.
Her mirovî dînitiya xwe heye, lê dînitiya herî mezin a hemûyan, bi dîtina min, ev e ku mirov yekê nebe. ||| Every man has his folly, but the greatest folly of all, in my view, is not to have one.

Loma tu dikarî bibînî ku ez li vir li Kandiyayê cûreyê xwe yê dînitiyê rêz dikim, û ez her tiştî ji te re vedibêjim, axa, çimkî ez dixwazim şîreta te bipirsim. ||| So you can see I'm sorting out my own brand of folly here in Candia, and I'm giving you the whole shoot, boss, because I want to ask your advice.
Tu hê ciwan î, bê guman, lê te pirtûkên kevn ên hîkmetê xwendine û tu bûyî, eger tu xeyidî nebî ji vê gotinê, hineke kevneşop; loma ez şîreta te dixwazim. ||| You're still young, of course, but you have read the old books of wisdom and you've become, if you don't mind my saying so, a bit old fashioned; so I'd like your advice.
Ka, ez difikirim her mirovî bîna xwe ya taybet heye. ||| Well, I think every man has his own smell.
Em wê pir ferq nakin çimkî bîn hemû tev li hev dibin û em bi rastî nikarin bibêjin kîjan ya te ye û kîjan ya min.... ||| We don't notice it much because smells mingle all together and we can't tell which is yours and which is mine, really....
Tiştê ku em dizanin ev e ku bîneke genî heye û ev e ya ku em jê re dibêjin «mirovahî»... mebesta min «bîngenîya mirovî» ye. ||| All we know is that there's a foul smell and that's what we call "humanity"... I mean "the human stench."
Mirov hene ku wê wisa bîn dikin mîna ku ew lavanta be. Ew min tê vereşînê. ||| There are people who sniff at it as if it was lavender. It makes me want to spew.
Çi dibe bila bibe, bila em biçin pêş, ew çîrokeke din e.... ||| Anyway, let's get on, that's another story....

Min dixwest bibêjim — ez tam dîsa li ber berdana frênê bûm — ku jin, ew pîrek, pozên wan şil in, wek dêlikan, û yekser bîna mêrê ku wan dixwaze û yê ku naxwaze dikin. ||| I wanted to say -- I was just going to let off the brake again -- that women, the jades, have wet noses, like bitches, and straight away smell out a man who desires them and one who doesn't.
Loma li her bajarê ku min lingê xwe lê daniye, heta niha ku ez pîr im, kirêt wek meymûnekê û tu cilên xweşik tunene, her dem yek an du jin li pey min bezîne. ||| That's why in every town I've ever set foot in, even now when I'm old, ugly as an ape and got no smart clothes, I've always had one or two women running after me.
Ew bîna min dikin, ew dêlik! Xwedê wan bihêle! ||| They sniff me out, the bitches! God bless 'em!

Çi dibe bila bibe, roja yekem a ku ez bi silametî gihîştim Kandiyayê, êvar bû. ||| Anyway, the first day I arrived safely in Candia, it was dusk.
Ez rast bezîm dikanan, lê ew hemû girtî bûn. ||| I rushed straight to the shops, but they were all closed.
Ez çûm xanekê, hineke alif da hêstir, xwe xwar û xwe paqij kir. ||| I went to an inn, gave the mule some fodder, ate myself and had a clean-up.
Cigareyek pêxist û derketim ku li dora xwe binêrim. ||| I lit a cigarette and went out for a look-around.
Min tu kes li bajêr nas nedikir û tu kesî ez nas nedikir; ez bi temamî azad bûm. ||| I didn't know a soul in the town and no one knew me; I was absolutely free.
Min dikaribû li kuçeyê fîk lêxim, bikenim, bi xwe re bipeyivim. ||| I could whistle in the street, laugh, talk to myself.
Min hineke passa-tempo (tovên kundirê yên şor ên biraştî) kirî, hûr-hûr xwar, tif kir û li gor dilê xwe geriyam. ||| I bought some passa-tempo (salted roast pumpkin seeds), nibbled, spat and wandered to my heart's content.
Çirayên kuçeyê vêketî bûn, mêran vexwarinên xwe yên berî-xwarinê dixwarin, jin diçûn malê, hewa bi pûdra, sabûna destşûştinê, anîset û souvlakia (goştê li ser şîşê biraştî) bîhnxweş bûbû. ||| The street-lamps were lit, men were having their aperitifs, women were going home, the air was scented with powder, toilet-soap, anisette, and souvlakia (grilled meat on a skewer).
Min ji xwe re got: «Guhdarî bike, Zorba, tu dê heta kengê bi wan kunên poz ên ricifok bijî? Pir wext ji te re nemaye, ku bîna hewayê bikî. Berde, kalo, bi qasî ku ji destê te tê wê kûr bikişîne hundir!» ||| I said to myself: "Listen, Zorba, how long do you expect to live with those quivering nostrils? You haven't got very long left, to sniff the air. Go on, old chap, breathe it in as deep as you can!"

##PG 95
Ev e ya ku min digot dema ku ez li meydana mezin jor û jêr dimeşiyam — tu wê dizanî. ||| That's what I was saying as I walked up and down the big square -- you know the one.
Ji nişkê ve — pesnê Xwedê be — min qîrîn, dans, lêxistina defekê û hin stranên rojhilatî bihîst. ||| Suddenly -- praise be to God -- I heard shouts, dancing, a tambourine playing and some oriental songs.
Min guhên xwe bel kir û bezîm ber bi cihê ku deng jê dihat. ||| I pricked up my ears and ran to where the noise was coming from.
Ew qehwexaneyek bi kabareyek bû. Ew tam ya ku min dixwest bû. ||| It was a café with a cabaret. That was just what I wanted.
Ez ketim hundir. Li maseyeke biçûk, baş li pêş, rûniştim. ||| I went in. I sat down at a little table, well to the front.
Çima ez nebim wêrek? Wek ku ez dibêjim, tu kesî ez nas nedikir, ez bi temamî azad bûm. ||| Why shouldn't I be bold? As I say, nobody knew me, I was absolutely free.
Jineke mezin û şêt li ser sehnê dans dikir, dora xwe radikir, lê min bala xwe nedayê. ||| A big gawk of a woman was dancing on the platform, lifting her skirts up, but I didn't pay any attention.
Min şûşeyeke bîrayê sîpariş kir, û paşê afirîdeke biçûk a şîrîn û esmer hat û li maseya min rûnişt. ||| I ordered a bottle of beer, and then a sweet, dusky little creature came and sat down at my table.
Wê boyaxa xwe bi malê li xwe sîwax kiribû. ||| She'd plastered on her paint with a trowel.
«Ma tu napejirînî, bapîro?» pirsî, dikeniya. ||| "Do you mind, grandad?" she asked, laughing.
Li ser vê yekê xwîn bi serê min de hilkişiya. Min daxwazeke tirsnak hîs kir ku situyê wê bişkînim, ya bêrû! ||| The blood rushed up to my head at this. I felt a terrible urge to wring her neck, the hussy!
Lê min xwe girt, dilê min bi «mêya cinsê» şewitî loma min gazî garsonekî kir. ||| But I held myself back, I was sorry for the "female of the species" so I called a waiter.
«Du şûşe şampanya!» ||| "Two bottles of champagne!"

Bibore, axa! Min hineke ji dravê te xerc kir, lê ew ewqas heqareteke tirsnak bû, diviya min rûmeta me, ya te jî wek ya min, biparasta, diviya min ew zarokoka biçûk li ber me biçemandiba, bi rastî diviya min. ||| Forgive me, boss! I've spent some of your money, but it was such a terrible insult, I had to save our honor, yours as well as mine, I had to bring that little brat to her knees before us, I really had to.
Ez dizanim te tu caran ez wisa bê parastin, di kêliyeke dijwar de, nedihiştim! ||| I know you would never have left me defenseless, like that, at a difficult moment!
Loma, «Du şûşe şampanya, garson!» ||| So, "Two bottles of champagne, waiter!"
Şampanya hat, û min kek jî sîpariş kir, paşê hineke şampanya zêdetir. ||| The champagne arrived, and I ordered cakes as well, then some more champagne.
Mirovekî bi hineke yasemînê hat û min selika tije kirî û ew li hembêza wê keça biçûk a ku wêrekî kiribû me heqaret bike vala kir. ||| A man with some jasmine came up and I bought the basketful and emptied it into the lap of the little bit of fluff who'd dared insult us.
Me vexwar û vexwar, lê bi sonda min, axa, min heta ew nequçand jî. ||| We drank and drank, but on my oath, boss, I didn't even pinch her.
Ez karê xwe dizanim. ||| I know my stuff.
Çaxê ez ciwan bûm tişta yekem a ku min dikir ev bû ku ez wan biquçînim û bi wan re bilîzim. ||| When I was young the first thing I did was to pinch and play with them.
Niha ez pîr im, tişta yekem a ku ez dikim ev e ku ez pere xerc bikim, comerd bim, destvekirî bim. ||| Now I'm old, the first thing I do is to spend money, be gallant, open-fisted.
Jin jê hez dikin ku wisa bi wan re bê reftarkirin. ||| Women adore being treated like that.
Ew pîrek li ser te dîn dibin; û tu dikarî pişt-xûz bî, kavilekî pîr, kirêt wek spîkê, û ew ê wê hemûyê ji bîr bikin. ||| The jades go crazy about you; and you can be hump-backed, an old ruin, as ugly as a louse, and they'll forget all that.
Ew nikarin tu tiştî din bibînin, ew dêlik, ji bilî destê ku pere derdixe û dihêle ew biherike wek selikeke ku qulek tê de heye. ||| They can't see anything else, the bitches, but the hand that brings out the money and lets it flow away like a basket with a hole in it.

Loma, wek ku min digot, min serwetek xerc kir — bila Xwedê te bihêle, axa, û sed qatî wê ji te re vegerîne — û keça navborî bi min ve hişk zeliqî. ||| So, as I was saying, I spent a fortune -- may God bless you, boss, and return it to you a hundred-fold -- and the abovementioned girl stuck tight to me.
Ew her nêzîktir dibû; çonga xwe ya biçûk li hember kerikên min ên mezin ên hestî dimat. ||| She came closer and closer; she pressed her little knee up against my big bony stumps.
Lê ez tenê wek pareyekî qeşayê bûm, her çend ez ji hundir germ û bêhntengî bûm. ||| But I was just like a block of ice, although inside I was hot and bothered.
Ev e ya ku jinan serê wan winda dike; çêtir e tu wê hîn bibî, heke tu xwe di heman rewşê de bibînî, dibe ku bi kêrî te bê: bihêle ku ew hîs bikin tu ji hundir dişewitî û lê tu wan nadestî! ||| That's what makes women lose their heads; you'd better learn that, in case you find yourself in the same situation, it might stand you in good stead: let 'em feel you're burning inside and yet you don't touch 'em!

Ka, nîvê şevê hat û çû. ||| Well, midnight came and went.
Ronahî dest pê kir vedimirîn, qehwexane digirt. ||| The lights began going out, the café was closing.
Min lûleyek ji notên hezar-draxmayî derxist, hesab da û ji garson re baxşîşeke comerd hişt. ||| I took out a roll of thousand-drachma notes, paid the bill and left a generous tip for the waiter.
Keçik bi min ve zeliqî. «Navê te çi ye?» bi dengekî evîn-nexweş ji min pirsî. ||| The girl clung to me. "What's your name?" she asked me in a love-sick tone.
«Bapîr!» min bi acizî bersiv da. ||| "Grandad!" I replied, vexed.
Dêlika biçûk a bêrû min bi hêz quçand, û pist-pist kir: «Were bi min re... were bi min re!» ||| The brazen little bitch pinched me hard, and whispered: "Come with me... come with me!"
Min destê wê yê biçûk girt, bi rewşeke zana ew pelçiqand û bersiv da: ||| I took her little hand, squeezed it with a knowing air and answered:
##PG 96
«Vêca were, biçûko....» Dengê min xerexerî bû. ||| "Come, then, little one...." My voice was hoarse.
Tu dikarî mayî texmîn bikî, axa. Me karê xwe kir. Paşê em razan. ||| You can imagine the rest, boss. We did our stuff. Then we went to sleep.
Çaxê ez hişyar bûm, divê bi kêmî nîvro bûbe. ||| When I woke up it must have been at least midday.
Min li dora xwe nihêrî, û ez çi dibînim? Odeyeke biçûk a delal, paqij û pîs-paqij, kursiyên rehet, destşok, sabûn, şûşeyên bîhnê, neynikên ji her mezinahiyê, kirasên bi rengên şa li dîwêr daleqandî, gelek wêne: behrvan, efser, kaptan, polîs, jinên dansê, jinên ku tenê tiştek li xwe — cotek sol. ||| I looked round, and what do I see? A charming little room, spick and span, easychairs, a washbasin, soaps, scent bottles, mirrors of all sizes, gaily-colored dresses hanging on the wall, a crowd of photographs: sailors, officers, captains, policemen, dancing-women, women with only one thing on -- a pair of sandals.
Û li tenişta min di nivînê de — germ, bîhnxweş, û bi porê tevlihev, mêya cinsê! ||| And next to me in the bed -- warm, scented, and with ruffled hair, the female of the species!

«Ax, Zorba,» min ji xwe re got, çavên xwe digirt, «tu ketî Bihiştê dema ku tu hê sax î! Ev cihekî baş e ku mirov lê be; ji cî nelive!» ||| "Ah, Zorba," I said to myself, closing my eyes, "you've entered Paradise while you're still alive! This is a good place to be; don't budge!"
Min carekê berê ji te re got, axa, ku her mirovî bihişta xwe ya taybet heye. ||| I told you once before, boss, that each man has his own particular paradise.
Ji bo te, Bihişt dê tije pirtûk û fîçiyên mezin ên hibirê be. ||| For you, Paradise will be stocked full of books and big demijohns of ink.
Ji bo yekî din ew ê tije fîçiyên şerab, rom û brandiyê be, ji bo yekî din lodên pere. ||| For someone else it'll be full of casks of wine, of rum and brandy, for another piles of money.
Ji bo min Bihişt ev e: odeyeke biçûk a bîhnxweş bi kirasên bi rengên şa li dîwêr, sabûnên bîhnxweş, nivîneke mezin a bi sprîngên baş, û li kêleka min mêya cinsê. ||| For me Paradise is this: a little perfumed room with gay-colored dresses on the wall, scented soaps, a big bed with good springs, and at my side the female of the species.

Sûcê ku tê îtirafkirin nîvî tê serastkirin. ||| A fault confessed is half redressed.
Wê rojê min pozê xwe nexist derveyî derî. Ez ê biçûma kuderê? Min çi bikira? Tu tirs! Ez li cihê ku lê bûm baş bûm. ||| I didn't stick my nose outside the door that day. Where would I have gone? What should I have done? No fear! I was fine where I was.
Min sîparişek ji xaneya herî baş a bajêr şand û ji me re sîniyeke xwarinê anîn — tiştek pê ve nîne ji bilî xwarina baş û hêz-dayî: xevyara reş, parzeq, masî, ava lîmonê, kadayif (şîrîniyeke tirkî). ||| I sent an order to the best inn of the town and they brought us a tray of food -- nothing but good, strength-giving food: black caviar, chops, fish, lemon-juice, cadaif (a sweet Turkish pastry).
Me dîsa li karên xwe yên biçûk nihêrî û carek din pêkê razan. ||| We looked after our little affairs again and had another nap.
Em êvarê hişyar bûn, cilên xwe li xwe kirin û dîsa mil-di-mil çûn qehwexaneyê. ||| We woke up in the evening, dressed and went off arm-in-arm to the café once more.

Ku çîrokeke dirêj kurt bikim û te di peyvan de nexeniqînim, ew bername hê di meşê de ye. ||| To cut a long story short and not drown you in words, that program is still in operation.
Lê tu xwe netewizîne, axa, ez li karên te yên biçûk jî dinêrim. ||| But don't you worry yourself, boss, I'm looking after your little affairs, too.
Carna ez diçim û li dikanan digerim. Ez ê têl û her tiştê ku hewceyî me ye bikirim, tu xem neke. ||| Now and then I go and look round the shops. I'll buy the cable and all we need, don't you worry.
Rojek zûtir, an rojek an hefteyek derengtir, heta mehek derengtir, çi ferq dike? ||| A day sooner, or a day or a week later, even a month later, what does it matter?
Wek ku em dibêjin, eger pisîk pir bilez be, çêjikên wê ecêb dibin. ||| As we say, if the cat's in too much of a hurry, she has peculiar kittens.
Di berjewendiya te de, ez li bendê me ku guhên min her tiştî bigirin û hişê min zelal bibe, da ku ez neyêm xapandin. ||| In your interest, I'm waiting for my ears to pick up everything and my mind to clear, so I'm not swindled.
Têl divê pola yekem be, an na em ê têk biçin. ||| The cable must be first-class, or we shall be dished.
Loma sebir bike, axa, û baweriya xwe bi min bîne. ||| So be patient, boss, and trust in me.

Berî her tiştî, ji bo tenduristiya min xem neke. Macera ji bo min baş in. ||| Above all, don't worry about my health. Adventures are good for me.
Di çend rojan de ez dîsa bûme zilamekî ciwan ê bîst salî. ||| In the matter of a few days I've become a young man of twenty again.
Ez ewqas bihêz im, ez ji te re dibêjim, dê komeke nû ya diranan li min şîn bibe. ||| I'm so strong, I tell you, I shall be growing a new set o' teeth.
Pişta min dema ez hatim hineke min diêşand, niha ez gelek sax û silamet im. ||| My back was hurting me a bit when I arrived, now I'm as fit as a fiddle.
Her sibe ez di neynikê de li xwe dinêrim û ez heyirî dimînim ku porê min bi şev reş wek boyaxa solan nebûye. ||| Every morning I look at myself in the mirror and I'm amazed my hair hasn't turned as black as boot polish overnight.

Lê tu dê bipirsî çima ez wisa ji te re dinivîsim? Ka... tu ji bo min cûreyekî dêrkê îtirafê yî, axa, û ez şerm nakim ku hemû gunehên xwe ji te re îtiraf bikim. ||| But you'll be asking why I'm writing to you like this? Well... you're a sort of confessor to me, boss, and I'm not ashamed to admit all my sins to you.
Tu dizanî çima? Bi qasî ku ez dibînim, ka ez rast dikim an çewt, tu qet ne li ser î. ||| Do you know why? So far as I can see, whether I do right or wrong, you don't care a rap.
Tu sterkeke şil digirî, wek Xwedê, û flap! şlap! tu tenê wê hemûyê paqij dikî. ||| You hold a damp sponge, like God, and flap! slap! you just wipe it all out.
Ev e ya ku min teşwîq dike ku ez her tiştî wisa ji te re bibêjim. ||| That's what prompts me to tell you everything like this.

Vêca guhdarî bike! Ez hemû ser-û-bin im û li ber wê me ku ez bi temamî ji serê xwe biçim. ||| So listen! I'm all topsy-turvy and on the point of going completely off my head.
Ji kerema xwe, axa, qelema xwe hilde û hema ku tu vê nameyê bistînî ji min re binivîse. ||| Please, boss, take your pen and write to me as soon as you get this letter.
##PG 97
Heta ku bersiva te bi min re nebe, ez ê di hewleke mezin de bim. ||| Until I have your answer, I'll be on tenterhooks.
Ez difikirim ku bi salan e navê min ji deftera Xwedê hatiye xêzkirin. Û ji ya şeytan jî. ||| I think that for years now my name's been scratched off God's register. And off the devil's, too.
Defterê te ew defter a tenê ye ku ez difikirim ez hê tê de me, loma ji bilî xwe te yê birûmet kesê min tune ku ez berê xwe bidimê; loma guhdariya ya ku ez dixwazim bibêjim bike. ||| Yours is the only register I think I'm still on, so I've got nobody but your worshipful self to turn to; so listen to what I've got to say.

Mesele ev e: Duho li gundekî nêzî Kandiyayê cejnek hebû — bila şeytan min bibe eger ez bizanim ji bo kîjan pîrozî bû! ||| This is what it's about: Yesterday there was a fête on in a village near Candia -- devil take me if I know what saint it was in aid of!
Lola — ax! rast e, min ji bîr kiribû ku wê bidim nasîn ji te re; navê wê Lola ye — ji min re dibêje: «Bapîr!» ||| Lola -- ah! true enough, I'd forgotten to introduce her to you; her name's Lola -- she says to me: "Grandad!"
Carek din ji min re dibêje bapîr, lê niha ev navekî hezkirinê ye, axa. ||| She calls me grandad once more, but now it's a pet name, boss.
«Bapîr,» dibêje, «ez dixwazim biçim cejnê!» ||| "Grandad," she says, "I'd like to go to the fête!"
«Vêca here, dapîrê,» ez ji wê re dibêjim. ||| "Go on, then, Granma," I say to her.
«Lê ez dixwazim bi te re biçim.» ||| "But I want to go with you."
«Ez naçim. Ez ji pîrozan hez nakim. Tu bi tena serê xwe here.» ||| "I'm not going. I don't like saints. You go by yourself."
«Baş e, ez jî naçim.» ||| "All right, I shan't go either."
Min lê zîq mam. «Tu naçî? Çima na? Ma tu naxwazî?» ||| I stared at her. "You won't? Why not? Don't you want to?"
«Eger tu bi min re werî, ez dixwazim. Eger na, ez naxwazim.» ||| "If you come with me, I do. If not, I don't."
«Çima na? Tu kesekî azad î, ne wisa?» ||| "Why not? You're a free person, aren't you?"
«Na, ez ne azad im.» ||| "No, I'm not."
«Tu naxwazî azad bî?» ||| "You don't want to be free?"
«Na, ez naxwazim.» ||| "No, I don't."
Min fikirî ku divê ez dengan dibihîzim. Bi rastî min wisa fikirî. ||| I thought I must be hearing voices. I really did.
«Tu naxwazî azad bî?» min qîriya. ||| "You don't want to be free?" I cried.
«Na, ez naxwazim! Naxwazim! Naxwazim!» ||| "No, I don't! I don't! I don't!"

Axa, ez vê di odeya Lolayê de, li ser kaxezê Lolayê dinivîsim; ji bo Xwedê, bi baldarî guhdarî bike. ||| Boss, I'm writing this in Lola's room, on Lola's paper; for God's sake, listen carefully.
Ez difikirim tenê mirovên ku dixwazin azad bin mirov in. ||| I think only people who want to be free are human beings.
Jin naxwazin azad bin. Ka, ma jin mirov e? ||| Women don't want to be free. Well, is woman a human being?
Ji bo Xwedê, bi qasî ku ji destê te tê zû bersiv bide. ||| For heaven's sake, answer as soon as possible.
Hemû xêr ji axayê herî baş re. Ez, Alexîs Zorba. ||| All the best to the best of bosses. Me, Alexis Zorba.

Çaxê min xwendina nameya Zorba qedand, ez demekê di navbera du fikran de mam — na, sê. ||| When I had finished reading Zorba's letter I was for a while in two minds -- no, three.
Min nizanî ka ez hêrs bibim, an bikenim, an tenê heyranê vî mirovê seretayî bibim ê ku bi sadetî qalikê jiyanê — mantiq, exlaq, durustî — dişikand û rast diçû ber bi madeya wê ya bingehîn. ||| I did not know whether to be angry, or laugh, or just admire this primitive man who simply cracked life's shell -- logic, morality, honesty -- and went straight to its very substance.
Hemû fezîletên biçûk ên ku ewqas bi kêr in di wî de kêm in. ||| All the little virtues which are so useful are lacking in him.
Tişta ku bi wî re heye fezîleteke nerehet û metirsîdar e ku zehmet e bê têrkirin û ku wî bê navber û bê berxwedan ber bi sînorên herî dawî, ber bi kortê ve dehf dide. ||| All he has is an uncomfortable, dangerous virtue which is hard to satisfy and which urges him continually and irresistibly towards the utmost limits, towards the abyss.

Dema ku dinivîse, vî karkerê nezan di lezgîniya xwe de qelemên xwe dişkîne. ||| When he writes, this ignorant workman breaks his pens in his impetuosity.
Wek mirovên yekem ên ku çermên xwe yên meymûnan ji xwe avêtin, an wek fîlozofên mezin, ew di bin bandora pirsgirêkên bingehîn ên mirovahiyê de ye. ||| Like the first men to cast off their monkey skins, or like the great philosophers, he is dominated by the basic problems of mankind.
Ew wan dijî mîna ku ew hewcedariyên tavilê û lezgîn bin. ||| He lives them as if they were immediate and urgent necessities.
Wek zarokê, ew her tiştî cara yekem dibîne. ||| Like the child, he sees everything for the first time.
Ew her dem heyirî ye û meraq dike çima û bo çi. ||| He is forever astonished and wonders why and wherefore.
Her tişt ji wî re mîna keramatê xuya dibe, û her sibe çaxê çavên xwe vedike daran, behrê, keviran û çûçikan dibîne, û heyirî dimîne. ||| Everything seems miraculous to him, and each morning when he opens his eyes he sees trees, sea, stones and birds, and is amazed.
«Ev çi keramet e?» diqîre. «Ev sirên ku jê re tê gotin: dar, behr, kevir, çûçik, çi ne?» ||| "What is this miracle?" he cries. "What are these mysteries called: trees, sea, stones, birds?"

##PG 98
Rojekê, tê bîra min, dema ku em ber bi gund ve diçûn, em rastî pîrekî biçûk hatin ku li ser hêstirekê siwar bû. ||| One day, I remember, when we were making our way to the village, we met a little old man astride a mule.
Zorba çavên xwe vekirin dema li heywên dinihêrî. ||| Zorba opened his eyes wide as he looked at the beast.
Û nêrîna wî ewqas tûj bû ku gundî ji tirsan qîriya: «Ji bo Xwedê, birawo, çavê wî mexe!» Û xaç li xwe kir. ||| And his look was so intense that the peasant cried out in terror: "For God's sake, brother, don't give him the evil eye!" And he crossed himself.
Ez berê xwe da Zorba. «Te çi bi kalo kir ku wisa biqîre?» min jê pirsî. ||| I turned to Zorba. "What did you do to the old chap to make him cry out like that?" I asked him.
«Ez? Tu difikirî min çi kir? Ez li hêstira wî dinihêrîm, ew bes! Ma ew li te neket, axa?» ||| "Me? What d'you think I did? I was looking at his mule, that's all! Didn't it strike you, boss?"
«Çi?» ||| "What?"
«Ka... ku di vê dinyayê de tiştên wek hêstir hene!» ||| "Well... that there are such things as mules in this world!"

Rojeke din, ez dixwendim, li ser peravê dirêjbûyî, û Zorba hat û li hemberî min rûnişt, santûriya xwe danî ser çokên xwe û dest bi lêxistinê kir. ||| Another day, I was reading, stretched out on the shore, and Zorba came and sat down opposite me, placed his santuri on his knees and began to play.
Min çavên xwe rakirin da ku li wî binêrim. ||| I raised my eyes to look at him.
Hêdî hêdî sîmaya wî guherî û şahiyeke hov ew girt. ||| Gradually his expression changed and a wild joy took possession of him.
Situyê xwe yê dirêj û qermiçî hejand û dest bi stranê kir. ||| He shook his long, creased neck and began to sing.
Stranên Makedonî, stranên Kleftan, qîrînên hov; qirika mirovî bû wek ku di demên berî dîrokê de bû, çaxê qîrîn senteseke mezin bû ku di xwe de hemû ya ku em îro bi navên helbest, muzîk û fikrê dibêjin dihewand. ||| Macedonian songs, Klepht songs, savage cries; the human throat became as it was in prehistoric times, when the cry was a great synthesis which bore within it all we call today by the names of poetry, music and thought.
«Ax! Ax!» Qîrîn ji kûrahiya hebûna Zorba dihat û qalikê tenik ê tevahî yê ya ku em jê re dibêjin şaristanî şikest û heywanê nemir, xwedayê pirçî, gorîla tirsnak berdaye derve. ||| "Akh! Akh!" The cry came from the depth of Zorba's being and the whole thin crust of what we call civilization cracked and let out the immortal beast, the hairy god, the terrifying gorilla.
Komir, qezenc û ziyan, Madam Hortans û planên ji bo pêşerojê, hemû winda bûn. ||| Lignite, profits and losses, Dame Hortense and plans for the future, all vanished.
Ew qîrîn her tiştî li ber xwe dibir; em ne hewceyî tu tiştî din bûn. ||| That cry carried everything before it; we had no need of anything else.

Bêliv, li ser wê peravê tenê ya Krêtayê, me herduyan jî hemû tehlî û şîrîniya jiyanê di sîngên xwe de digirt. ||| Immobile, on that solitary coast of Crete, we both held in our breasts all the bitterness and sweetness of life.
Tehlî û şîrînî êdî tunebûn. ||| Bitterness and sweetness no longer existed.
Tav çû ava, şev hat, Hirça Mezin li dora teqla nelivok a ezman dans kir, heyv hilat û bi tirs li du heywanên biçûk nihêrî ku li ser qûman distiran û ji tu kesî netirsiyan. ||| The sun went down, night came, the Great Bear danced round the immovable axis of the sky, the moon rose and gazed in horror at two tiny beasts who were singing on the sands and fearing no one.

«Ha! Mirov heywanekî hov e,» Zorba ji nişkê ve got, ji stranbêjiya xwe zêde coşbûyî. ||| "Ha! Man is a wild beast," Zorba said suddenly, overexcited with his singing.
«Pirtûkên xwe bi tena bihêle. Ma tu şerm nakî? Mirov heywanekî hov e, û heywanên hov naxwînin.» ||| "Leave your books alone. Aren't you ashamed? Man is a wild beast, and wild beasts don't read."
Kêliyekê bêdeng bû, paşê dest bi kenê kir. ||| He was silent a moment, then started to laugh.
«Ma tu dizanî,» got, «Xwedê çawa mirov çêkir? Ma tu peyvên yekem ên ku vî heywanî, mirov, ji Xwedê re gotin dizanî?» ||| "D'you know," he said, "how God made man? Do you know the first words this animal, man, addressed to God?"
«Na. Ez çawa bizanim? Ez li wir nebûm.» ||| "No. How should I know? I wasn't there."
«Ez bûm!» qîriya Zorba, çavên wî dibiriqîn. ||| "I was!" cried Zorba, his eyes sparkling.
«Ka, ji min re bibêje.» ||| "Well, tell me."
Nîvî di kêfxweşiyê de, nîvî di tinazê de, dest bi afirandina çîroka efsanewî ya afirandina mirov kir. ||| Half in ecstasy, half in mockery, he began inventing the fabulous story of the creation of man.

«Ka, guhdarî bike, axa! Sibehekê Xwedê bi dilteng hişyar bû. ‹Ez çi Xwedayekî şeytan im! Heta tu mirovên min jî tunene ku bixûrê ji min re bişewitînin û bi navê min sond bixwin da ku alîkariya derbaskirina wextê bikin! Ez ji jiyana bi tena serê xwe wek kundekî pîr têr bûm. Ftt!› ||| "Well, listen, boss! One morning God woke up feeling down in the dumps. 'What a devil of a God I am! I haven't even any men to burn incense to me and swear by my name to help pass the time away! I've had enough of living all alone like an old screech-owl. Ftt!'
Tif kir destên xwe, mêlên xwe hilda, berçavkên xwe danîn, parçeyek ax girt, tif kir ser, jê herî çêkir, baş hêç kir û jê mirovekî biçûk çêkir ku danî ber tavê. ||| He spat on his hands, pulled up his sleeves, put on his glasses, took a piece of earth, spat on it, made mud of it, kneaded it well and made it into a little man which he stuck in the sun.
Heft roj şûnde wî ew ji tavê derxist. Pijiyabû. Xwedê lê nihêrî û dest pê kir bi ken hewdê xwe biteqîne. ||| Seven days later he pulled it out of the sun. It was baked. God looked at it and began to split his sides with laughter.
‹Bila şeytan min bibe,› dibêje, ‹ev berazek e ku li ser lingên xwe yên paşîn rawestiyaye! ||| 'Devil take me,' he says, 'it's a pig standing up on its hind legs!
##PG 99
Ev qet ne ya ku min dixwest bû! Tu şaşî tune, min karûbar tev li hev kirine!› ||| That's not what I wanted at all! There's no mistake, I've made a mess of things!'
Loma wî ew ji paşila situyê hildigire û lêpekê li qûna wî dixe. ||| So he picks him up by the scruff of his neck and kicks his backside.
‹Here, winda be! Tişta ku divê tu niha bikî ev e ku berazên din ên biçûk çêkî; erd ya te ye! Niha, lê bazde. Çep, rast, çep, rast.... Bi lez bimeşe!...› ||| 'Go on, clear off! All you've got to do now is to make other little pigs; the earth's yours! Now, jump to it. Left, right, left, right.... Quick march!...'
Lê, tu dibînî, ew qet ne beraz bû! Kumekî qedîfeyî li serî bû, çakêtekî bê bal li ser milan avêtî, şalekî baş pîlîkirî, û terlîkên tirkî yên bi rîşiyên sor. ||| But, you see, it wasn't a pig at all! It was wearing a felt hat, a jacket thrown carelessly across its shoulders, well-creased trousers, and Turkish slippers with red tassels.
Û di pista wî de — divê şeytan bûbe ê ku ew dabe wî — xençerekî tûj hebû ku peyvên: ‹Ezê te bigirim!› li ser neqişandî bûn. ||| And in its belt -- it must have been the devil who'd given it that -- was a pointed dagger with the words: 'I'll get you!' engraved on it.
Ew mirov bû! ||| It was man!
Xwedê destê xwe dirêj kir da ku yê din maç bike, lê mirov simbêlên xwe bada û got: ‹Were, kalo, ji rê derkeve! Bila ez derbas bibim!›» ||| God held out his hand for the other to kiss, but man twirled up his moustache and said: 'Come on, old 'un, out of the way! Let me pass!'"

Li vir Zorba sekinî dema dît ku ez ji kenê diteqim. Eniya xwe gurç kir. ||| Here Zorba stopped as he saw me bursting with laughter. He frowned.
«Nekene!» got. «Tam wisa qewimî!» ||| "Don't laugh!" he said. "That's exactly what happened!"
«Tu çawa dizanî?» ||| "How do you know?"
«Wisa ez hîs dikim ku qewimî, û ev e ya ku min ê bikira eger ez li şûna Adem bûma. ||| "That's how I feel it happened, and that's what I'd have done if I'd been in Adam's place.
Ez ê serê xwe deynim ser ku bê jêkirin eger Adem bi awayekî din tevgeriyabe. ||| I'd wager my head being chopped off if Adam acted any different.
Û tu hemû ya ku pirtûk ji te re dibêjin bawer neke; ez ew kes im ku divê tu pê bawer bî!» ||| And don't you believe all the books tell you; I'm the one you should trust!"
Destê xwe yê mezin dirêj kir bê ku li benda bersivê bimîne û dîsa dest bi lêxistina santûriyê kir. ||| He stretched out his big hand without waiting for an answer and started playing the santuri once more.

Ez hê nameya Zorba ya bîhnxweş bi dilê wê yê bi tîrekê qulkirî digirt, û ez wan rojan ji nû ve dijiyam, ên tije bi hebûna wî ya mirovî, ku min li kêleka wî derbas kiribûn. ||| I was still holding Zorba's scented letter with its heart pierced by an arrow, and was living through those days, filled with his human presence, which I had spent at his side.
Dem di hevaltiya Zorba de tameke nû girtibû. ||| Time had taken on a new savour in Zorba's company.
Êdî ne rêzeke hejmarî ya bûyeran a li derve bû, ne jî pirsgirêkeke felsefî ya nayê çareserkirin a li hundir. ||| It was no longer an arithmetical succession of events without, nor an insoluble philosophical problem within.
Ew qûma germ bû, hûrik bêjingkirî, û min hîs dikir ku ew bi nermî di navbera tiliyên min de diherike. ||| It was warm sand, finely sieved, and I felt it running gently through my fingers.
«Pîroz be Zorba!» min pist-pist kir. ||| "Blessed be Zorba!" I murmured.
«Wî laşekî germ, hezkirî û zindî daye hemû fikrên razber ên ku di hundirê min de dilerizîn. ||| "He has given a warm, beloved, living body to all the abstract ideas which were shivering inside me.
Çaxê ew ne li wir e, ez dîsa dest bi lerizînê dikim.» ||| When he is not there, I start shivering again."
Min kaxezek girt, gazî karkerekî kir û telegrameke lezgîn şand: «Tavilê vegere.» ||| I took a sheet of paper, called a workman and sent an urgent telegram: "Come back immediately."
"""

CH14 = r"""
##PG 99
##FIRST
Êvara şemiyê, yekê adarê. ||| Saturday afternoon, the first of March.
Ez li hember behrê paldayî bûm li ser kevirekî, dinivîsî. ||| I was leaning against a rock facing the sea, writing.
Wê rojê min hechecîka yekem dîtibû û ez bextewar bûm. ||| That day I had seen the first swallow and I was happy.
Efsûna Bûda bê asteng li ser kaxezê diherikî, û têkoşîna min a bi wî re aramtir bûbû; ez êdî di lezeke bêhêvî de nebûm, û ez ji rizgariya xwe piştrast bûm. ||| The exorcism of Buddha was flowing without hindrance onto the paper, and my struggle with him had become calmer; I was no longer in a desperate hurry, and I was sure of my deliverance.
Ji nişkê ve min dengê gavan li ser keviran bihîst. ||| Suddenly I heard steps on the pebbles.
Min çavên xwe rakirin û sîrena me ya pîr dît ku li ber peravê digindirî, wek keştiyeke şer xemilandî. ||| I raised my eyes and saw our old siren rolling along the shore, decked out like a frigate.
Ew germ bû û bêhna wê teng bû. Wisa xuya dikir ku ji ber tiştekî xemgîn bû. ||| She was hot and short of breath. She seemed to be worried about something.
«Ma nameyek heye?» bi bêhntengî pirsî. ||| "Is there a letter?" she asked anxiously.
«Erê!» min bi kenekî bersiv da, û rabûm ku pêşwaziya wê bikim. ||| "Yes!" I answered with a laugh, and rose to welcome her.
«Ew gelek silavan ji te re dişîne; dibêje roj û şev li te difikire. Ew hema nikare bixwe an vexwe, dûrketinê ewqas nayê ragirtin dibîne.» ||| "He sends you lots of greetings; says he's thinking about you day and night. He can hardly eat or drink, he finds the separation so unbearable."
«Ma ew hemû ya ku dibêje ev e?» jina bêbext pirsî, bêhna xwe bi zor digirt. ||| "Is that all he says?" the unhappy woman asked, gasping for breath.

##PG 100
Dilê min bi wê şewitî. ||| I was sorry for her.
Min nameya wî ji berîka xwe derxist û xwe wisa nîşan da ku ez wê dixwînim. ||| I took his letter from my pocket and pretended that I was reading it.
Sîrena pîr devê xwe yê bêdiran vekir, çavên wê yên biçûk vir-vir kirin û bê bêhn guhdarî kir. ||| The old siren opened her toothless mouth, her little eyes blinked and she listened breathlessly.
Min xwe wisa nîşan da ku ez dixwînim, lê, ji ber ku ez hineke ketim nav, min xwe wisa nîşan da ku ez di xwendina nivîsê de zehmetiyê dikişînim: ||| I made believe I was reading, but, as I got rather involved, I pretended I had difficulty in making out the writing:
«Duho, axa, ez ji bo xwarinê ketim xwaringeheke erzan. Ez birçî bûm.... ||| "Yesterday, boss, I went into a cheap eating-house for a meal. I was hungry....
Çaxê min keçeke ciwan a bi temamî bedew dît ku ket hundir, xwedawendeke rast.... Xwedêyo! Ew tam wek Bûbûlîna min dixuya! ||| When I saw an absolutely beautiful young girl come in, a real goddess.... My God! She looked just like my Bouboulina!
Û yekser çavên min dest pê kirin av wek kaniyê biherikînin, gewriya min girnî girtibû.... Min nikaribû daqurtînim! ||| And straight away my eyes began spouting water like a fountain, I had a lump in my throat.... I couldn't swallow!
Ez rabûm, hesabê xwe da û çûm. ||| I got up, paid my bill and left.
Û ez ê ku tenê carekê her sed salî li pîrozan difikirim, ez ewqas kûr hatim hejandin, axa, ku ez bezîm dêra Aziz Mînas û findek jê re vêxist. ||| And I who only think of the saints once in a blue moon, I was so deeply moved, boss, I ran to Saint Minas's church and lit a candle to him.
‹Aziz Mînas,› min di duaya xwe de got, ‹bila mizgîna milyaketê ku ez jê hez dikim bi min re bê. Bila baskên me pir zû bigihîjin hev!›» ||| 'Saint Minas,' I said in my prayer, 'let me have good news of the angel I love. May our wings be united very soon!'"
«Ha! Ha! Ha!» kir Madam Hortans, rûyê wê ji şahiyê dibiriqî. ||| "Ha! Ha! Ha!" went Dame Hortense, her face beaming with joy.
«Tu bi çi dikenî, jina min a baş?» min pirsî, disekinîm da ku bêhna xwe bigirim û hin derewên din çêkim. ||| "What are you laughing at, my good woman?" I asked stopping to get my breath and concoct some more lies.
«Tu bi çi dikenî? Ev min bêtir ber bi giriyê ve dibe.» ||| "What are you laughing at? This makes me feel more like weeping."
«Xwezî te bizaniya... xwezî te bizaniya....» bi nizmî keniya û dest bi kenekî mezin kir. ||| "If only you knew... if only you knew...." she chuckled and burst into laughter.
«Çi?» ||| "What?"
«Bask.... Ev e ya ku ew ji lingan re dibêje, qeşmer. Ev navê ku ew dema em bi tena bin lê dike. Bila baskên me bigihîjin hev, dibêje.... Ha! Ha! Ha!» ||| "Wings.... That's what he calls feet, the rascal. That's the name he gives them when we're alone. May our wings be united, he says.... Ha! Ha! Ha!"

«Vêca guhdariya ya ku tê pêre bike. Tu yê bi rastî heyirî bimînî....» ||| "Listen to what comes next, then. You'll be really astounded...."
Min rûpel zivirand û xwe wisa nîşan da ku ez dîsa dixwînim: ||| I turned over the page and made believe I was reading again:
«Û îro, dema ez ji ber dikaneke berber derbas dibûm, berber tasa xwe ya ava sabûnî li derve vala kir. Tevahiya kuçeyê bi wê bînê tije bû. ||| "And today, as I was passing a barber's shop, the barber emptied outside his bowl of soapy water. The whole street was filled with the scent.
Û ez dîsa li Bûbûlîna fikirîm û dest bi giriyê kir. Ez êdî nikarim ji wê dûr bimînim, axa.... Ez ê ji serê xwe biçim.... ||| And I thought of Bouboulina again and began to cry. I can't stay away from her any longer, boss.... I shall go off my head. ...
Binêre, min heta helbest jî nivîsiye. Du şev berê min nikaribû razêm û min dest bi nivîsandina helbesteke biçûk ji wê re kir.... Ez hêvî dikim tu yê wê jê re bixwînî da ku bibîne ez çawa diêşim....» ||| Look, I've even written poetry. I couldn't sleep two nights ago and I began writing a little poem for her.... I hope you'll read it to her so that she'll see how I'm suffering....

##VERSE
Ax! xwezî li ser rêçikekê ez û tu hev bidîtana,<br>û ew bi qasî ku keser û kovana me herduyan hilgire fireh bûya!<br>Bila ez bibim hûrik an goştê kutayî,<br>hestiyên min ên perçiqî dê hê jî hêza bezîna bal te bidîtana! ||| Ah! if only on some foot-path you and I could meet, and it were wide enough to hold our rue! Let me be ground to crumbs or pie-meat, my shattered bones would still have strength to run to you!

Madam Hortans, çavên wê nazdar û nîv-girtî, bi kêfxweşî guhdarî dikir, hemû bal. ||| Dame Hortense, her eyes languid and half-closed, was listening happily, all attention.
Heta bendika biçûk ji situyê xwe, ku hema wê dixeniqand, derxist, û qermiçokên xwe bo kêliyekê azad kir. ||| She even took the little ribbon from her neck, where it was nearly strangling her, and set her wrinkles free for a moment.
Bêdeng û bişirî bû. Bextewar û razî, wisa xuya dikir ku hişê wê dûr diçû. ||| She was silent and smiling. Happy and contented, her mind seemed to be drifting far away.

Meha adarê, giyayê taze, kulîlkên biçûk ên sor, zer û mor, ava zelal ku tê de komên qûwên spî û reş dema distiran cot dibûn. ||| The month of March, fresh grass, little red, yellow and purple flowers, limpid water where groups of white and black swans were mating as they sang.
Mêyik spî, nêr reş û bi nikulên nîv-vekirî, sortûj. ||| The females white, the males black and with half-open, crimson beaks.
Marmasiyên şîn ên mezin biriqdar ji avê radibûn û xwe li dora maran zer ên mezin dialandin. ||| Great blue Moray eels rose gleaming from the water and twined themselves round big yellow serpents.
Madam Hortans dîsa çardeh salî bû, li ser xalîçeyên rojhilatî li Îskenderiye, Beyrût, Îzmîr, Konstantînopolîs dans dikir, paşê li ber Krêtayê li ser palûbeyên keştiyan ên pîçkirî.... ||| Dame Hortense was fourteen again, dancing on oriental carpets in Alexandria, Beirut, Smyrna, Constantinople, then off Crete on the polished decks of ships....
Ew niha nikaribû pir zelal bi bîr bîne. Tevlihev dibû, sînga wê bilind û nizm dibû, perav ji hev diçûn. ||| She could not remember very clearly now. It was becoming confused, her breast was heaving, the shores were splitting.
Û ji nişkê ve, dema ku ew dans dikir, behr bi keştiyên bi pêşiyên zêrîn nixumî. ||| And suddenly, while she was dancing, the sea was covered with vessels with golden prows.
##PG 101
Li ser palûbeyên wan, konên pir-reng û alên hevirmiş. ||| On their decks, multicolored tents and silken oriflames.
Geşteke tevahî ya paşayan ji konan dihat bi rîşiyên zêrîn ên rast li ser fesên xwe, begên pîr ên dewlemend di hecê de bi destên tije diyariyên giranbiha, û kurên wan ên xemgîn û bê rî. ||| A whole procession of pashas came from the tents with golden tassels upright on their fezes, wealthy old beys on pilgrimages with hands full of rich offerings, and their melancholy, beardless sons.
Admîral jî hatin, bi kumên xwe yên sê-goşeyî yên biriqdar, û behrvan bi gerdenên xwe yên spî yên çavqamçîker û şalên fireh ên perçifok. ||| Admirals came, too, with their shining three-cornered hats, and sailors with their dazzling white collars and broad, flapping trousers.
Krêtayiyên ciwan li pey hatin, bi şalên xwe yên berfireh ên qumaşê şîn ê vekirî, çizmeyên zer, û laçikên reş ên li ser porê wan girêdayî. ||| Young Cretans followed, in their billowing breeches of light-blue cloth, yellow boots, and black kerchiefs knotted over their hair.
Di dawiyê de bi rûmet Zorba hat, mezin, ji evînbaziyê zeyf bûyî, bi gustîlkeke nîşanê ya girs li tiliya xwe, tacek ji kulîlka pirteqalê li ser porê xwe yê gewrdibû.... ||| A good last came Zorba, huge, grown lean from love-making, with a massive engagement ring on his finger, a crown of orange-blossom on his greying hair....
Ji keştiyan hemû mêrên ku wê di jiyana xwe ya bi macera de nas kiribûn dihatin, yek jî kêm nebû, heta ne ew kelekvanê pîr ê bi diranên valahî û pişt-xûz jî ê ku êvarekê li Konstantînopolîsê ew biribû ser avê. ||| From the ships came all the men she had known in her adventurous lifetime, not one was missing, not even the old gap-toothed and hunchbacked boatman who had taken her out on the water one evening at Constantinople.
Şev daketibû û tu kesî ew nedidîtin. ||| Night had fallen and no one could see them.
Ew hemû derketin, hemûyên wan, û li paş, cot dibûn, oho! Marmasî, Mar, Qû! ||| They all came out, all of them, and in the background, mating away, oho! the Morays, the Serpents, the Swans!

Mêr hatin û tev li wê bûn; ew bûn gûşe-gûşe, wek marên evîndar ên biharê, ên ku fîz dikin û wek baqekî radibin. ||| The men came and joined her; they formed clusters, like amorous snakes in the spring, who rise hissing in a sheaf.
Û li navendê, hemû spî û tazî, û ji xwêdanê dibiriqî, lêvên wê vekirî da ku diranên xwe yên biçûk ên tûj nîşan bide, hişk, bê têr, memikên wê rast, Madam Hortanseke çardeh, bîst, sî, çil, şêst havînan fîz dikir. ||| And in the center, all white and naked, and glistening with sweat, lips parted to show her little pointed teeth, rigid, insatiable, her breasts erect, hissed a Dame Hortense of fourteen, twenty, thirty, forty, sixty summers.
Tu tişt winda nebûbû, tu evîndar nemiribû! ||| Nothing was lost, no lover had died!
Di sînga wê ya çilmisî de ew hemû ji nû ve zindî bûbûn, bi tev cilên rêzê. ||| In her wilted breast they were all resuscitated, in full parade dress.
Mîna ku Madam Hortans keştiyeke şer a bi sê dîreq a birûmet bûya û hemû evîndarên wê — wê çil û pênc salên xebatê dîtibûn — li wê siwar dibûn, dadiketin embaran, derdiketin ser kêlekê, diketin nav benan, dema ku ew diherikî, gelek lêdayî û gelek pînekirî, ber bi wê bendera mezin a dawî ya ku wê ewqas bi kel hesret kiribû: zewac. ||| As if Dame Hortense were a noble three-masted frigate and all her lovers -- she had seen forty-five working years -- were boarding her, climbing into the holds, onto the gunwale, into the rigging, while she sailed along, much-battered and much-caulked, towards the last great haven she had longed for so ardently: marriage.
Û Zorba hezar rû girtin: tirkî, ewrûpî, ermenî, erebî, yûnanî, û, dema ku wê ew hembêz kir, Madam Hortans tevahiya geşta pîroz û bêdawî hembêz kir.... ||| And Zorba assumed a thousand faces: Turkish, European, Armenian, Arab, Greek, and, as she hugged him, Dame Hortense hugged the entire, blessed and interminable procession....

Sîrena pîr, ji nişkê ve, fêm kir ku min xwendin rawestandiye; xeyala wê ji nişkê ve sekinî û wê çavpilkên xwe yên giran rakirin: ||| The old siren, all at once, realized that I had ceased reading; her vision suddenly stopped and she raised her heavy lids:
«Ma tiştekî din nabêje?» bi awazeke gilî pirsî, lêvên xwe bi çavbirçîtî dialişt. ||| "Doesn't he say anything else?" she asked in a tone of reproach, licking her lips greedily.
«Tu çi din dixwazî, Madam Hortans? Ma tu nabînî? Tevahiya nameyê li ser te diaxive û tu tiştî din. ||| "What more do you want, Madame Hortense? Don't you see? The whole letter talks about you and nothing else.
Binêre, çar rûpelên wê! Û li vir li quncikê dilek jî heye. ||| Look, four sheets of it! And there's a heart here in the corner, too.
Zorba dibêje wî ew bi xwe, bi destê xwe kişandiye. Binêre, evînê ew qul kiriye, û li jêr, binêre, du kewên ku hev hembêz dikin, û li ser baskên wan, bi tîpên biçûk ên mîkroskopî bi hibira sor, du nav bi hev ve girêdayî: Hortans — Zorba!» ||| Zorba says he drew it himself, with his own hand. Look, love has pierced it through, and underneath, look, two doves embracing, and on their wings, in small microscopic letters in red ink, two names intertwined: Hortense -- Zorba!"
Ne kew hebûn ne nav, lê çavên biçûk ên sîrena pîr bi hêsiran tije bûbûn û dikaribûn her tiştê ku bixwazin bibînin. ||| There were neither doves nor names, but the old siren's small eyes had filled with tears and could see anything they wished.
«Tiştekî din na? Tiştekî din na?» dîsa pirsî, hê ne razî. ||| "Nothing else? Nothing else?" she asked again, still not satisfied.

Bask, ava sabûnî ya berber, kewên biçûk — ew hemû pir baş bûn, gelek peyvên xweş ew hemû, tiştek ji bilî hewayê na. ||| Wings, the barber's soapy water, the little doves -- that was all very well, a lot of fine words all that, nothing but air.
Hişê wê yê jinê yê pratîkî tiştekî din dixwest, tiştekî bêtir desttêkar, hişk. ||| Her practical woman's mind wanted something else, something more tangible, solid.
Çend caran di jiyana xwe de wê ev cûreyê qisûran bihîstibû! Û çi feyde dabû wê? ||| How many times in her life had she heard this sort of nonsense! And what good had it done her?
Piştî salên xebata dijwar, ew bi tena serê xwe, vala û hişk hatibû hiştin. ||| After years of hard work, she had been left all alone, high and dry.
«Tiştekî din na?» dîsa bi gilî pist-pist kir. «Tiştekî din na?» ||| "Nothing else?" she murmured again reproachfully. "Nothing else?"
Bi çavên wek ên xezaleke li kelacê li min nihêrî. ||| She looked at me with eyes like those of a hind at bay.

Dilê min pê şewitî. ||| I took pity on her.
##PG 102
«Ew tiştekî din ê pir, pir girîng dibêje, Madam Hortans,» min got. «Loma min ew heta dawiyê hişt.» ||| "He says something else very, very important, Madame Hortense," I said. "That's why I kept it till the end."
«Ew çi ye....?» bi axînekê got. ||| "What is it....?" she said with a sigh.
«Ew dinivîse ku, hema ku vegere, ew ê here ser çokan da ku ji te lava bike, bi hêsir di çavan de, ku tu pê re bizewicî. ||| "He writes that, as soon as he gets back, he'll go on his knees to implore you, with tears in his eyes, to marry him.
Ew êdî nikare li bendê bimîne. Ew dixwaze, dibêje, te bike jina xwe ya biçûk, Madam Hortans Zorba, da ku hûn êdî tu caran ji hev neqetin.» ||| He can't wait any longer. He wants to make you, he says, his own little wife, Madame Hortense Zorba, so that you need never be separated again."
Vê carê hêsir bi rastî dest pê kirin biherikin. ||| This time the tears really began to flow.
Ev şahiya herî bilind bû, bendera bi kel hatî xwestin; ev ew tişt bû ku heta niha wê poşmaniya nebûna wê di jiyana xwe de dikişand! ||| This was the supreme joy, the ardently desired haven; this was what she had hitherto regretted not having in her life!
Aramî û razana di nivîneke namûsdar de, tiştekî din na! ||| Tranquillity and lying in an honest bed, nothing more!
Çavên xwe bi destên xwe nixumand. ||| She covered her eyes with her hands.

«Baş e,» got, bi mezinahiya xanimeke mezin, «ez qebûl dikim. ||| "All right," she said, with the condescension of a great lady, "I accept.
Lê ji kerema xwe jê re binivîse; bibêje ku li vir li gund tu tacên kulîlka pirteqalê tunene. Ew ê neçar bibe ku wan ji Kandiyayê bîne. ||| But please write to him; say that here in the village there are no orange-blossom wreaths. He'll have to bring them from Candia.
Divê du findên spî jî bîne, bi bendikên pembe û hineke behîvên şekirkirî yên baş. ||| He must bring two white candles as well, with pink ribbons and some good sugared almonds.
Paşê divê ji min re kincekî zewacê bikire, yekî spî, û goreyên hevirmiş û solên seten ên rêzê. ||| Then he must buy me a wedding dress, a white one, and silk stockings and satin court shoes.
Çarşev bi me re hene, jê re bibêje, loma ne hewce ye ku bîne. Nivîn jî bi me re heye.» ||| We've got sheets, tell him, so he needn't bring any. We've also got a bed."
Lîsteya emrên xwe rêz kir, jixwe mêrê xwe dikir kurê peyên. ||| She arranged her list of orders, already making an errand boy of her husband.
Rabû ser xwe. Ji nişkê ve dîmenê jineke zewicî ya birûmet girtibû. ||| She stood up. She had suddenly taken on the look of a dignified married woman.

«Tiştek heye ku ez ji te bixwazim,» got. «Tiştekî cidî.» ||| "I've something to ask you," she said. "Something serious."
Paşê li bendê ma, hatî hejandin. ||| Then she waited, moved.
«Berde, Madam Hortans, ez di xizmeta te de me.» ||| "Go on, Madame Hortense, I'm at your service."
«Zorba û ez pir ji te hez dikin. Tu pir dilovan î, û tu yê me rezîl nekî. Ma tu yê bibî şahidê me?» ||| "Zorba and I are very fond of you. You are very kind, and you'll not disgrace us. Would you care to be our witness?"
Ez lerizîm. ||| I shuddered.

Berê, li mala dêûbavên min, xizmetkareke pîr a bi navê Diamandoula bi me re hebû, ku ji şêst salî mezintir bû, pîreyeke kal a bi simbêl, ji keçîniyê nîv-dînbûyî, bêhntengî, çilmisî û sîng-pehn. ||| Formerly, at my parents' house, we had had an old serving-woman named Diamandoula, who was over sixty, an old maid with a moustache, half-crazed by virginity, nervous, shrivelled up and flat-chested.
Ew bi Mîço re ket evînê, kurê bekalê herêmê, lawekî gundî yê ciwan ê qirêj, têr û bê rî. ||| She fell in love with Mitso, the local grocer's boy, a dirty, well-fed and beardless young peasant lad.
«Tu kengê yê bi min re bizewicî?» her yekşemê jê dipirsî. «Niha bi min re bizewice! Tu çawa dikarî ewqas dirêj li bendê bimînî? Ez wê ranagirim!» ||| "When is it you be going to marry me?" she used to ask him every Sunday. "Marry me now! How can you wait so long? I can't bear it!"
«Ez jî nikarim!» digot kurê bekal ê fêlbaz, ê ku ji bo kirîna wê ew dixapand. ||| "I can't either!" said the cunning grocer's boy, who was getting round her for her custom.
«Ez êdî nikarim xwe ragirim, Diamandoula; lê dîsa jî, em nikarin bizewicin heta ku simbêl wek ên te li min jî hebin....» ||| "I can't hold out any longer, Diamandoula; but all the same, we can't get married till I've a moustache as well as you...."
Sal wisa derbas bûn, û Diamandoula ya pîr li bendê ma. ||| The years went past like that, and old Diamandoula waited.
Asêbên wê aramtir bûn, serêşa wê kêmtir bû, lêvên wê yên tehl ên ku tu caran nehatibûn maçkirin fêrî bişirînê bûn. ||| Her nerves became calmer, she had fewer headaches, her bitter lips that had never been kissed learned to smile.
Niha cilan bi baldartir dişuşt, kêmtir firaq dişikandin, û tu caran xwarin neşewitand. ||| She washed the clothes more carefully now, broke fewer dishes, and never burned the food.
«Ma tu yê werî û bibî şahidê me, mîrê ciwan?» êvarekê bi dizî ji min pirsî. ||| "Will you come and be our witness, young master?" she asked me one evening on the sly.
«Bê guman ez ê werim, Diamandoula,» min bersiv da, gewriya min girnî girtibû, ji ber dilovaniya wê. ||| "Certainly I will, Diamandoula," I answered, a lump forming in my throat, out of pity for her.
Hema ew pêşniyaz dilê min guvaştibû; loma ez lerizîm dema min bihîst Madam Hortans heman tiştî dipirse. ||| The very suggestion had wrung my heart; that is why I shuddered when I heard Dame Hortense ask the same thing.
«Bê guman ez ê bikim,» min bersiv da. «Ew ê şerefek be, Madam Hortans.» ||| "Certainly I would," I replied. "It will be an honor, Madame Hortense."

Rabû, li wan bûklên biçûk ên ku ji bin kumê wê yê biçûk daleqandî bûn xist û lêvên xwe alişt. ||| She rose, patted the little ringlets that hung from beneath her little hat and licked her lips.
«Şeva te xweş,» got. «Şeva te xweş, û bila ew zû vegere ba me!» ||| "Good night," she said. "Good night, and may he soon come back to us!"

##PG 103
Min temaşe kir ku ew bi paldan-paldan diçû, laşê xwe yê pîr dihejand bi hemû nazikbaziyên keçeke ciwan. ||| I watched her waddling away, swaying her old body with all the affected airs of a young girl.
Şahiyê bask dabûn wê, û solên wê yên pîr ên xwar şopên kûr di qûmê de çêdikirin. ||| Joy gave her wings, and her twisted old court shoes made deep impressions in the sand.
Hema ku ew li serê pêşbestê zivirî, qîrînên tûj û hawar ji ber peravê hatin. ||| She had hardly rounded the headland than shrill cries and wailing came from along the shore.
Ez rabûm û bezîm ber bi wî aliyê ku deng jê dihat. ||| I leaped up and ran in the direction from which the noise was coming.
Li ser pêşbesta hember jin diqîriyan mîna ku şîneke cenazeyê distirin. ||| On the opposite headland women were howling as though they were singing a funeral dirge.
Ez li ser kevirekî hilkişiyam û nihêrî. ||| I climbed a rock and looked.
Mêr û jin ji gund radibûn dibezîn; li pey wan kûçik diewtiyan. Du an sê li ser hespan bûn û diçûn pêş. ||| Men and women were running up from the village; behind them dogs were barking. Two or three were on horseback and going on ahead.
Ewrekî stûr ê toz ji erdê radibû. ||| A thick cloud of dust was rising from the ground.
«Qezayek çêbûye,» min fikirî, û li dora kendavê bezîm. ||| "There's been an accident," I thought, and ran round the bay.
Hêwirze her tûjtir dibû. ||| The hubbub was growing more intense.
Du an sê ewrên biharê di ronahiya tava diçûava de bêliv sekinîbûn. ||| Two or three spring clouds stood still in the light of the setting sun.
Dara Hêjîrê ya Xanima Me ya Ciwan bi pelên kesk ên taze nixumî bû. ||| The Fig Tree of Our Young Lady was covered with fresh green leaves.

Ji nişkê ve Madam Hortans bi lik-likî hat ba min. Ew dîsa paşde dibezî, perîşan, bê bêhn, û yek ji solên wê derketibû. ||| Suddenly Dame Hortense staggered up to me. She was running back again, dishevelled, out of breath, and one of her shoes had come off.
Ew di destê xwe de digirt û dema dibezî digiriya. ||| She was holding it in her hand and was crying as she ran.
«Xwedêyo... Xwedêyo....» bi girî got dema ez dîtim. Şelifî û hema ket. Min ew girt. ||| "My God... my God...." she sobbed as she saw me. She stumbled and nearly fell. I caught her.
«Tu ji bo çi digirî? Çi qewimî?» Û min alîkariya wê kir ku sola xwe ya qewimî li xwe bike. ||| "What are you crying for? What's happened?" And I helped her put on her worn shoe.
«Ez ditirsim.... Ez ditirsim....» ||| "I'm frightened.... I'm frightened...."
«Ji çi?» ||| "Of what?"
«Ji mirinê.» ||| "Of death."
Wê bi tirs bîna mirinê di hewayê de hîs kiribû. ||| She had scented with terror the smell of death in the air.

Min milê wê yê sist girt da ku wê bibim wir, lê laşê wê yê pîrdibû berxwe da û lerizî. ||| I took her limp arm to lead her to the place, but her ageing body resisted and trembled.
«Ez naxwazim.... Ez naxwazim....» qîriya. ||| "I don't want to.... I don't want to...." she cried.
Belengaza reben ditirsiya ku nêzîkî cihekî bibe ku mirin lê xuya bûbe. ||| The poor wretch was terrified of going close to a place where death had appeared.
Divê Xaron wê nebîne û wê neyne bîra xwe. ... ||| Charon must not see her and remember her. ...
Wek hemû mirovên pîr, sîrena me ya belengaz hewl dida ku xwe veşêre bi girtina rengê kesk ê giyê, an bi girtina rengekî erdî, da ku Xaron wê ji erd an giyê cuda neke. ||| Like all old people our poor siren tried to hide herself by taking on the green color of grass, or by taking on an earthly color, so that Charon could not distinguish her from earth or grass.
Serê xwe xistibû nav milên xwe yên qelew û girover, û dilerizî. ||| She had tucked her head into her fat, rounded shoulders, and was trembling.
Xwe kişand ber dareke zeytûnê, çakêtê xwe yê pînekirî raxist û li erdê niqumî. ||| She dragged herself to an olive tree, spread out her patched coat and sank to the ground.
«Vê li ser min deyne, dê? Vê li ser min deyne û tu here binêre.» ||| "Put this over me, will you? Put this over me and you go and have a look."
«Ma tu sermayê hîs dikî?» ||| "Are you feeling cold?"
«Erê. Min binixumîne.» ||| "I am. Cover me up."
Min ew bi qasî ku ji destê min dihat nixumand, da ku ew ji erdê neyê cudakirin, paşê ez çûm. ||| I covered her up as well as I could, so that she was indistinguishable from the earth, then I went off.

Ez gihîştim pêşbestê û niha bi zelalî stranên şînê bihîstin. ||| I came up to the headland and now clearly heard the songs of lamentation.
Mîmîko bi bez ji ber min derbas bû. «Çi ye, Mîmîko?» min pirsî. ||| Mimiko came running past me. "What is it, Mimiko?" I asked.
«Ew xwe xeniqand! Xwe xeniqand!» bê sekin qîriya. ||| "He's drowned himself! Drowned himself!" he shouted without stopping.
##PG 104
«Kî?» ||| "Who?"
«Pavlî, kurê Mavrandonî.» ||| "Pavli, Mavrandoni's son."
«Çima?» ||| "Why?"
«Jinebî....» ||| "The widow...."
Peyv di hewaya êvarê de daleqandî ma û laşê metirsîdar û nerm ê wê jinê anî ber çavan. ||| The word hung in the evening air and conjured up the dangerous, supple body of that woman.

Ez gihîştim keviran û li wir tevahiya gund kombûyî dît. ||| I reached the rocks and there found the whole village assembled.
Mêr bêdeng bûn, serê wan tazî; jin, bi laçikên xwe yên ku li ser milan paşde avêtî, porê xwe diçirandin û qîrînên dilqul dikirin. ||| The men were silent, bare-headed; the women, with their kerchiefs thrown back over their shoulders, were tearing their hair and uttering piercing cries.
Cendekekî werimî û morbûyî li ser peravê kevirî dirêj bûbû. ||| A swollen, livid corpse lay on the pebbled beach.
Mavrandonî yê pîr li ser wê bêliv sekinîbû, lê dinihêrî. ||| Old Mavrandoni was standing motionless over it, gazing at it.
Bi destê xwe yê rastê li gopalê xwe paldayî bû. Bi yê çepê rîya xwe ya gewr û xelek-xelek digirt. ||| With his right hand he was leaning on his staff. With his left he was holding his curly grey beard.

«Nifir li te be, jinebî!» dengekî tûj ji nişkê ve got. «Xwedê dê vê ji te bistîne!» ||| "A curse on you, widow!" a shrill voice said suddenly. "God shall make you pay for this!"
Jinek rabû û berê xwe da mêran. ||| A woman leaped up and turned to the men.
«Ma li gund tu mêrek nîne ku wê li ser çokên xwe biavêje û qirika wê wek mîhekê jêke? Bah! lo tirsonek!» ||| "Isn't there a single man in the village to throw her across his knees and cut her throat like a sheep? Bah! you cowards!"
Û tif kir mêran, ên ku bê tu peyvê li wê nihêrîn. ||| And she spat at the men, who looked at her without a word.
Kondomanolio, xwediyê qehwexaneyê, bersiva wê da: «Me şermezar neke, Katerîna dîn,» qîriya, «me şermezar neke, hê hin mêr, hin palîkarî, li gundê me hene, tê bibînî!» ||| Kondomanolio, the café proprietor, answered her: "Don't humiliate us, crazy Katerina," he shouted, "don't humiliate us, there are still some men, some Palikaria, in our village, you'll see!"

Min nikaribû xwe bigirim. «Şerm li we hemûyan be!» min qîriya. «Bi çi awayî ew jin berpirsiyar e? Ev qeder bû. Ma hûn ji Xwedê natirsin?» ||| I could not contain myself. "Shame on you all!" I cried. "In what way is that woman responsible? It was fated. Don't you fear God?"
Lê tu kesî bersiv neda. ||| But no one replied.
Manolakas, pismamê mirovê xeniqî, laşê xwe yê girs xwar kir, cendek hilda nav milên xwe û rêya yekem ber bi gund ve girt. ||| Manolakas, the drowned man's cousin, bent his huge body, lifted the corpse in his arms and took the first path back to the village.
Jin diqîriyan, rûyên xwe diqurçandin û porê xwe diçirandin. ||| The women were screaming, scratching their faces and tearing their hair.
Çaxê dîtin ku cendek tê birin, bezîn ku wê hembêz bikin. ||| When they saw the body was being carried away, they ran to clasp it.
Lê Mavrandonî yê pîr, gopalê xwe dihejand, ew qewirandin û serê geştê girt, jin bi stranên şînê li pey. ||| But old Mavrandoni, brandishing his staff, drove them off and took the head of the procession, followed by the women singing dirges.
Di dawiyê de, bêdeng, mêr hatin. ||| Lastly, in silence, came the men.
Ew di tarîtava êvarê de winda bûn. ||| They disappeared into the twilight.
Te dikaribû dîsa bêhna aram a behrê bibihîsta. ||| You could hear the peaceful breathing of the sea once more.

Min li dora xwe nihêrî. Ez bi tena serê xwe bûm. ||| I looked around me. I was alone.
«Ez ê vegerim malê,» min got. «Rojeke din, ya Xwedê, ku para xwe ya keserê girtiye!» ||| "I'll go back home," I said. "Another day, O God, which has had its measure of sorrow!"
Kûr di fikrê de, ez li dû rêçikê çûm. ||| Deep in thought, I followed the pathway.
Ez heyranê van mirovan mam, ên ku ewqas nêzîk û germ tev li êşên mirovî bûbûn: Madam Hortans, Zorba, jinebî, û Pavlîyê zer ê ku ewqas bi wêrekî xwe avêtibû behrê da ku kesera xwe bixeniqîne, û Delî-Katerîna ya ku diqîriya da ku ew qirika jinebiyê wek mîhekê jêkin, û Mavrandonî yê ku red dikir ku bigirî an heta li ber yên din bipeyive. ||| I admired these people, so closely and warmly involved in human sufferings: Dame Hortense, Zorba, the widow, and the pale Pavli who had so bravely thrown himself in the sea to drown his sorrow, and Deli-Katerina shouting for them to cut the widow's throat like a sheep, and Mavrandoni refusing to weep or even to speak in front of the others.
Tenê ez bêhêz û aqilane bûm, xwîna min nedikeliya, ne jî min bi dilxwazî hez dikir an nefret dikir. ||| I alone was impotent and rational, my blood did not boil, nor did I love or hate with passion.
Min hê dixwest tiştan rast bikim, bi awayekî tirsonek, bi danîna her tiştî li ber deriyê qederê. ||| I still wanted to put things right, in cowardly fashion, by laying everything at destiny's door.

Di tarîtava êvarê de min hema dikaribû mam Anagnostî bibînim ku hê li wir li ser kevirekî rûniştî bû. ||| In the twilight I could just see uncle Anagnosti still sitting there on a stone.
Çena xwe danîbû ser gopalê xwe yê dirêj û li behrê dinihêrî. ||| He had propped his chin on his long stick and was gazing at the sea.
Min gazî wî kir, lê wî nebihîst. ||| I called to him, but he did not hear.
Ez çûm ba wî; ew min dît û serê xwe hejand. ||| I went up to him; he saw me and shook his head.
##PG 105
«Mirovahiya belengaz!» pist-pist kir. «Çi heyfa jiyaneke ciwan! Lawê belengaz nikaribû kesera xwe ragire, loma xwe avêt behrê û xeniqî. Niha ew rizgar e.» ||| "Poor humanity!" he murmured. "The waste of a young life! The poor boy couldn't bear his sorrow, so he threw himself in the sea and was drowned. Now he's saved."
«Rizgar?» ||| "Saved?"
«Rizgar, lawê min, erê, rizgar. Wî bi jiyana xwe çi dikaribû bikira? ||| "Saved, my son, yes, saved. What could he have done with his life?
Eger wî bi jinebiyê re zewicîbûya, dê pir zû şer derketana, belkî heta bêrûmetî jî. ||| If he'd married the widow, there would very soon have been quarrels, perhaps even dishonor.
Ew tam wek mehîneke nijandinê ye, ew jina bêşerm! Hema ku mêrekî dibîne, dest bi xirîn dike. ||| She's just like a brood mare, that shameless woman! As soon as she sees a man, she starts to whinny.
Û eger wî pê re nezewicîbûya, dê ezaba jiyana wî bûya, çimkî ew fikir dê di serê wî de mîx bûbûya ku wî bextewariyeke mezin ji dest daye! ||| And if he hadn't married her, it would have been the torment of his life, because the idea would have been fixed in his head that he'd missed a great happiness!
Korteke vekirî li pêş, zinarekî asê li paş!» ||| A yawning abyss in front, a precipice behind!"

«Wisa nepeyive, mam Anagnostî; tu yê bêhêvîtiyê bînî ser her kesê ku te bibihîze!» ||| "Don't talk like that, uncle Anagnosti; you'd bring despair to anyone who heard you!"
«Were, ewqas netirse. Tu kes nikare min bibihîze, ji bilî te. Û heta eger bikaribûna jî, ma ew ê bi min bawer bikira? ||| "Come on, don't be so frightened. No one can hear me, except you. And even if they could, would they believe me?
Binêre, ma qet mirovekî ji min bextiyartir hebûye? ||| Look, has there ever been a luckier man than me?
Zevî, rez, baxçeyên zeytûnê, û xaniyekî du-qatî bi min re hebûn. Ez dewlemend û rispiyekî gund bûm. ||| I've had fields, vineyards, olive groves, and a two-storied house. I've been rich and a village elder.
Ez rastî jineke baş û aram hatim ku ji min re tenê kur anîn. ||| I lighted on a good, docile woman who gave me only sons.
Min tu caran nedît ku ew çavên xwe bi serhildanê li min rake, û hemû zarokên min bavên baş in. ||| I've never seen her raise her eyes to me in defiance, and all my children are good fathers.
Tiştek min nîne ku gilî bikim. Nevî jî bi min re hebûn. Ez çi din dikaribûm bixwesta? Rehên min kûr diçin. ||| I've nothing to complain about. I've had grandchildren, too. What more could I want? My roots go deep.
Û dîsa jî eger min neçar bûya ku jiyana xwe ji nû ve dest pê bikim, min ê kevirekî li situyê xwe bikira, wek Pavlî, û xwe biavêta behrê. ||| And yet if I had to start my life all over again I'd put a stone round my neck, like Pavli, and throw myself in the sea.
Jiyan dijwar e, Xwedêyo dijwar e; heta jiyana herî bextiyar jî dijwar e, nifir li wê be!» ||| Life is hard, my God it is; even the luckiest life is hard, a curse on it!"

«Lê çi heye ku te kêm e, mam Anagnostî? Tu ji çi gilî dikî?» ||| "But what is there you lack, uncle Anagnosti? What are you complaining of?"
«Tiştek min kêm nîne, ez ji te re dibêjim! Lê tu here û dilên mirovan bipirse!» ||| "I lack nothing, I tell you! But you go and question men's hearts!"
Kêliyekê bêdeng bû, û dîsa li behra ku tarî dibû nihêrî. ||| He was silent a moment, and looked again at the darkening sea.
«Ka, Pavlî, te tişta rast kir!» qîriya, gopalê xwe dihejand. «Bila jin biqîrin; ew jin in û aqil nînin. Tu niha rizgar î, Pavlî — bavê te wê dizane û loma deng nekir!» ||| "Well, Pavli, you did the right thing!" he cried, waving his stick. "Let the women scream; they're women and have no brains. You're saved now, Pavli -- your father knows it and that's why he didn't make a sound!"

Ezman û çiyayên ku jixwe nediyar dibûn vekolî. ||| He scanned the sky and the mountains which were already growing indistinct.
«Va ye şev,» got. «Çêtir e em vegerin.» ||| "Here's the night," he said. "Better get back."
Ji nişkê ve sekinî, wisa xuya dikir ku poşmana wan peyvên ku ji devê wî ketibûn bû, mîna ku sirek mezin eşkere kiribe û niha bixwaze wê paşde bistîne. ||| He stopped all of a sudden, seeming to regret the words he had let drop, as if he had betrayed a great secret and now wanted to recover it.
Destê xwe yê çilmisî danî ser milê min. ||| He placed his shrivelled hand on my shoulder.
«Tu ciwan î,» got, li min dibişirî; «guhdariya pîran neke. Eger dinya guh bida wan, ew ê bi serê xwe ber bi wêrankirina xwe ve bibeze. ||| "You're young," he said, smiling at me; "don't listen to the old. If the world did heed them, it would rush headlong to its destruction.
Eger jinebiyek bikeve rêya te, wê bigire! Bizewice, zarokan çêbike, dudilî nebe! Belê ji bo ciwanan hatine çêkirin!» ||| If a widow crosses your path, get hold of her! Get married, have children, don't hesitate! Troubles were made for young men!"

Ez gihîştim peravê xwe, agir pêxist û çaya xwe ya êvarê çêkir. ||| I reached my beach, lit the fire and made my evening tea.
Ez westiyayî û birçî bûm, û min bi birçîtî xwar, xwe bi temamî dabû kêfa heywanî. ||| I was tired and hungry, and I ate ravenously, giving myself up entirely to animal pleasure.
Ji nişkê ve Mîmîko serê xwe yê biçûk ê pehnkirî di pencereyê re xist hundir, li min nihêrî ku li ber agir çemiyayî û dixwarim. ||| Suddenly Mimiko pushed his little flattened head through the window, looked at me crouching by the fire and eating.
Bi fêlbazî bişirî. ||| He smiled cunningly.
«Tu ji bo çi hatî, Mîmîko?» ||| "What have you come for, Mimiko?"
«Min tiştek ji te re aniye, axa... ji jinebiyê.... Selikeke pirteqalan. Dibêje ew ên dawî yên ji baxçeyê wê ne....» ||| "I've brought you something, boss... from the widow.... A basket of oranges. She says they're the last from her garden...."
«Ji jinebiyê?» min bi heyret got. «Çima ew ji min re şandin?» ||| "From the widow?" I said with a start. "Why did she send me them?"
##PG 106
«Ji ber wê gotina baş a ku te îro piştî nîvro li ber gundiyan ji wê re kir, wisa dibêje.» ||| "Because of the good word you put in for her to the villagers this afternoon, so she says."
«Kîjan gotina baş?» ||| "What good word?"
«Ez çi zanim? Ez tenê ya ku wê got ji te re dibêjim, ew bes!» ||| "How do I know? I'm just telling you what she said, that's all!"
Pirteqal li ser nivînê vala kirin. Tevahiya koxikê bi bîna wan tije bû. ||| He emptied the oranges on the bed. The whole hut became redolent with their smell.
«Jê re bibêje ku ez gelek spasiya wê dikim ji bo diyariya wê, û ez şîretê li wê dikim ku hay ji xwe hebe. Divê ew hay ji gava xwe hebe û bi tu awayî xwe li gund nîşan nede, ma tu dibihîzî? ||| "Tell her I thank her very much for her present, and I advise her to be careful. She must watch her step and not show herself in the village on any account, do you hear?
Divê ew demekê li hundir bimîne, heta ku ev karê bêbext ji bîr bibe. Ma tu fêm dikî, Mîmîko?» ||| She must stay indoors for a time, until this unhappy business has been forgotten. Do you understand, Mimiko?"
«Ma ew hemû ye, axa?» ||| "Is that all, boss?"
«Ew hemû ye. Tu dikarî niha biçî.» ||| "That's all. You can go now."
Mîmîko çavê xwe li min qirpand. «Ma ew hemû ye?» ||| Mimiko winked at me. "Is that all?"
«Here de!» ||| "Get away!"
Ew çû. ||| He went.

Min yek ji pirteqalên av-pir qalî kir; ew wek hingiv şîrîn bû. ||| I peeled one of the juicy oranges; it was as sweet as honey.
Ez razam, ketim xewê, û tevahiya şevê ez di baxçeyên pirteqalan de geriyam. ||| I lay down, fell asleep, and the whole night through I wandered in orange groves.
Bayekî germ dihat; min sînga xwe li ber bayê tazî kiribû û çiqilek rîhanê li pişt guhê min hebû. ||| A warm wind was blowing; I had bared my chest to the wind and had a sprig of sweet basil behind my ear.
Ez gundiyekî ciwan ê bîst salî bûm, û ez li baxçeyê pirteqalan digeriyam, fîk lê dixist û li bendê bûm. ||| I was a young peasant of twenty, and I roamed about the orange grove whistling and waiting.
Ez li hêviya kê bûm? — ez nizanim. Lê dilê min amade bû ku ji şahiyê biteqe. ||| For whom was I waiting? -- I do not know. But my heart was ready to burst for joy.
Min simbêlên xwe badan û guhdarî kir, tevahiya şevê, behra ku wek jinekê li pişt daran pirteqalê dikişand. ||| I twirled up my moustache and listened, the whole night through, to the sea sighing like a woman behind the orange trees.
"""

CH15 = r"""
##PG 106
##FIRST
Wê rojê bayekî xurt ê başûr hebû, ku ji qûmên Afrîkayê dişewitî û li ser Behra Spî dihat. ||| THAT DAY there was a strong south wind, which came burning from the sands of Africa across the Mediterranean.
Ewrên qûmê hûrik di hewayê de dipêçan û vedigeriyan û diketin gewrî û pişikan. ||| Clouds of fine sand twisted and turned in the air and got into throat and lungs.

Diran diqîliqîn û çav dişewitîn; ger mirov bixwesta piştrast bibe ku perçeyek nan ê bê qûm bixwe, divê derî û pencere hişk bihatana girtin. ||| Teeth were gritty and eyes inflamed; doors and windows had to be locked tight if one wanted to make sure of eating a single piece of bread that was not sprinkled with sand.

Hewa giran bû. ||| It was close.
Di wan rojên zextdar de, dema ku şîreya nebatan radibû, ez bi xwe jî bûbûm nêçîra bêhntengiya biharê ya ku belav bûbû. ||| During those oppressive days when the sap was rising I was myself a prey to the prevailing springtime unrest.
Hesteke westanê, gizgizîneke hestyarî di sîngê de, livîneke di seranserê laşê min de, daxwazeke -- an gelo bîranîn bû -- ji bextewariyeke fireh û sade. ||| A feeling of lassitude, an emotional tension in the breast, a tingling sensation throughout my body, a desire -- or was it memory -- of a vast and simple happiness.

Min riya çiyê ya bi keviran girt. ||| I took the pebbly mountain track.
Ji nişkê ve dilê min xwest ku biçim seredana bajarokê Mînowî yê biçûk ku piştî sê-çar hezar salan ji erdê rabûbû û careke din li bin tava xwe ya hezkirî ya Kretayê xwe germ dikir. ||| I had a sudden impulse to visit the small Minoan city which had risen from the ground after three or four thousand years and was warming itself once more under its beloved Cretan sun.
Min difikirî ku belkî piştî sê-çar saetan meşê, westan dê bêhntengiya ku bihar anîbû aram bike. ||| I thought that perhaps after three or four hours' walk fatigue would calm the unrest that spring had brought.

Kevirên gewr ên tazî, tazîtiyeke ronak, çiyayê hişk û çol ê ku ez jê hez dikim. ||| Bare grey stones, a luminous nakedness, the harsh and deserted mountain that I love.
Kundekî, çavên xwe yên gilover ên zer zîq vekirî, ji ber ronahiya geş kor bûbû, li ser kevirekî rûniştibû. ||| An owl, its round yellow eyes staring, blinded by the bright light, had perched on a stone.
Ew giran bû, bedew bû, tijî sir bû. ||| It was grave, beautiful, full of mystery.
Ez sivik dimeşiyam, lê bihîstina wî tûj bû; ew tirsiya, bêdeng di nav keviran de firiya û winda bû. ||| I was walking lightly, but its hearing was keen; it took fright, flew up silently among the stones and disappeared.

Di hewayê de bêhna sîrtê hebû. ||| There was a scent of thyme in the air.
Kulîlkên ewil ên nazik ên gewza zer berê ji nav stiriyên wê xuya dibûn. ||| The first tender flowers of the yellow gorse were already showing amongst its thorns.

##PG 107
Dema ez gihîştim ber çavê bajarokê wêranbûyî, ez ji ber efsûnê sekinîm. ||| When I came in sight of the small ruined city I stood spellbound.
Divê nêzîkî nîvro bûya, tîrêjên tavê stûnî dadiketin û keviran bi ronahiyê dadigirtin. ||| It must have been about noon, the sun's rays were falling perpendicularly and drenching the stones with light.
Di bajarên kevn ên wêran de ev demeke rojê ya xeternak e, çimkî hewa tijî qîrîn û gewriya giyanan e. ||| In old ruined cities this is a dangerous time of day, for the air is filled with cries and the noise of spirits.
Eger çiqilek biqîje, eger marmaroşkek bibeze, eger ewrek dema ku ji jor derbas dibe sîberekê bavêje, tirseke kûr te digire. ||| If a branch cracks, if a lizard darts, if a cloud throws a shadow as it passes overhead, panic seizes you.

Her bihostek ji erdê ku tu lê dimeşî gorek e, û tu dengê nalîna miriyan dibihîzî. ||| Every inch of ground you tread is a grave, and you hear the dead groaning.

Hêdî hêdî çavên min li ronahiya geş hatin. ||| Gradually my eyes grew accustomed to the bright light.
Niha min dikaribû şopên destê mirov di wêranan de bibînim: du rêyên fireh ên bi kevirên biriqok ferş kirî. ||| I could now see traces of the hand of man in the ruins: two broad roads paved with shining stones.
Li çep û rastê wan, kolanên teng ên xwar. ||| To the left and right of them, narrow tortuous alleys.
Li navendê agora ya gilover, an cihê civîna giştî, û li tenişta wê, bi nizmbûneke bi temamî demokratîk, qesra padîşah bi stûnên xwe yên cot, derenceyên kevir ên mezin û gelek avahiyên alîkar hatibû danîn. ||| In the center the circular agora, or public meeting place, and next to it, with a totally democratic condescension, had been placed the king's palace with its double columns, large stone stairways and numerous outbuildings.

Di dilê bajêr de kevir herî zêde bi pêya mirov hatibûn pêpestkirin û li wir divê perestgeha hundir hebûya: Xwedawenda Mezin li wir bû, bi memikên xwe yên gewre, ji hev dûr danî, û milên wê bi maran pêçayî. ||| In the heart of the city the stones were most heavily trodden by the foot of man and that was where the inner shrine must have been: the Great Goddess was there, with her huge breasts, set wide apart, and her arms wreathed in snakes.

Li her derê dikanên biçûk, guhêrên rûn, kûreyên hesinkaran, û kargehên dartiraş û kûzesazan hebûn. ||| Everywhere were small shops, oil presses, forges, and the workshops of joiners and potters.
Hêlîneke mêrûyan a bi jêhatî sêwirandî, baş di cihekî parastî de avakirî, û ku mêrû jê berî bi hezaran salan winda bûbûn. ||| A cleverly designed anthill, well-built in a sheltered position, and whence the ants had disappeared thousands of years ago.
Li cihekî hunermendekî ji kevirê xetdar cerek dixiş kir lê wextê wî nebûbû ku wê biqedîne; kelem ji destê wî ketibû, da ku bi hezaran salan şûnde, li tenişta xebata hunerî ya neqediyayî, were dîtin. ||| In one place a craftsman had been carving a jar out of veined stone but had not had the time to finish it; the chisel had fallen from his hand, to be discovered thousands of years later, lying next to the unfinished work of art.

Pirsên herheyî, vala, ehmeq: çima? ji bo çi? tên ku dilê te jehrî bikin. ||| The eternal, vain, stupid questions: why? what for? come to poison your heart.
Cerê neqediyayî, yê ku tê de îlhama hunermend a bextewar û bibawer ji nişkê ve têk çûbû, te bi tehlî tije dike. ||| The unfinished jar, where the artist's happy and confident inspiration had suddenly been defeated, fills you with bitterness.

Ji nişkê ve şivanekî biçûk, ji tavê qehweyî bûyî û destmalek perçemdar li dora porê xwe yê kej girêdayî, li ser kevirekî li kêleka qesra dirûxiyayî rabû ser xwe û çokên xwe yên reş nîşan da. ||| All at once a little shepherd, tanned by the sun and wearing a fringed handkerchief round his curly hair, stood up on a stone beside the crumbling palace and showed his black knees.

«Hey tu, bira!» wî qîriya. ||| "You there, brother!" he shouted.

Min dixwest bi tenê bim, û xwe wisa nîşan da ku min nebihîstiye. ||| I wanted to be alone, and made believe I had not heard.
Lê şivanê biçûk bi tinazî dest bi kenê kir. ||| But the little shepherd began to laugh mockingly.

«Ha! Tu xwe li kerî datînî, ha? Cixare hene? Yekê bide min! Di vê qula vala de ez ewqas ji jiyanê bêzar dibim.» ||| "Ha! Playing deaf, eh? Any cigarettes? Give me one! In this empty hole I get so fed up with life."

Wî peyvên dawî dirêj kirin û di wan de ewqas bêbextî hebû ku dilê min pê şewitî. ||| He dragged out the last words and there was such misery in them that I felt sorry for him.

Cixareyên min tunebûn, loma min drav pêşkêşî wî kir. ||| I had no cigarettes, so I offered him money.
Lê şivanê biçûk hêrs bû: ||| But the little shepherd was annoyed:

«Drav here cehennemê!» wî qîriya. «Ez ê pê çi bikim? Ez ji te re dibêjim ez ji her tiştî bêzar im. Ez cixareyekê dixwazim!» ||| "To hell with money!" he shouted. "What would I do with it? I tell you I'm fed up with everything. I want a cigarette!"

«Tune ne,» min bi bêhêvîtî got. «Tune ne.» ||| "I haven't any," I said in despair. "I haven't any."

«Cixare tune?» Ew ji xwe çû û bi gopalê xwe li erdê xist. «Cixare tune! Baş e, di berîkên te de çi heye? Ew bi tiştekî werimî ne.» ||| "No cigarettes?" He was beside himself and struck the ground with his crook. "No cigarettes! Well, what have you got in your pockets? They're bulging with something."

«Pirtûkek, destmalek, kaxez, qelemek, kêrokek,» min bersiv da, û tiştên di berîka xwe de yek bi yek derxistin. «Tu vê kêrokê dixwazî?» ||| "A book, a handkerchief, paper, a pencil, a penknife," I answered, pulling out one by one the things in my pocket. "Would you like this penknife?"

«Ya min heye. Her tiştê ku ez dixwazim heye: nan, penîr, zeytûn, kêra min, çermê ji bo solên min û şûjinek, û av di şûşeya min de, her tişt... ji bilî cixareyekê! Û ev wek wê ye ku qet tiştekî min tunebe! Û tu li wêranan li pey çi yî?» ||| "I've got one. I've got everything I want: bread, cheese, olives, my knife, leather for my boots and an awl, and water in my bottle, everything... except a cigarette! And it's as though I'd got nothing at all! And what might you be after in the ruins?"

«Ez kevnariyê dixwînim.» ||| "I'm studying antiquity."

«Tu jê çi qezenc dikî?» ||| "What good do you get out of that?"

«Tiştek na.» ||| "None."

##PG 108
«Tiştek na. Ez jî na. Ev hemû mirî ye, û em sax in. Çêtir e ku tu biçî, zû. Xwedê bi te re be!» ||| "None. Nor do I. This is all dead, and we're alive. You'd do better to go, quick. God be with you!"

«Ez diçim,» min bi guhdarî got. ||| "I'm going," I said obediently.

Ez bi riya biçûk vegeriyam û di mêjiyê min de hinekî bêhntengî hebû. ||| I went back along the little track with some anxiety in my mind.

Ez bo kêliyekê zivirîm û min dikaribû şivanê biçûk bibînim ku ji tenêtiya xwe ewqas westiyayî hîn li ser kevirê xwe sekinî bû. ||| I turned for a moment and could see the little shepherd who was so tired of his solitude still standing on his stone.
Porê wî yê kej, ji bin destmala wî ya reş difiriya, di bayê başûr de dihejiya. ||| His curly hair, escaping from under his black handkerchief, was waving in the south wind.
Ronahî ji serî heta pê li ser wî diherikî. ||| The light streamed over him from head to foot.
Min hîs kir ku ez li peykerekî bronz ê ciwanekî dinêrim. ||| I felt I was looking at a bronze statue of a youth.
Wî gopalê xwe li ser milên xwe danîbû û fîk lê dixist. ||| He had placed his crook across his shoulders and was whistling.

Min riyeke din girt û ber bi peravê ve daketim. ||| I took another track and went down towards the coast.
Carna, bayên germ ên bi bêhnxweşiyê barkirî ji baxçeyên nêzîk digihîştin min. ||| Now and then, warm breezes laden with perfume reached me from nearby gardens.
Erd bêhneke dewlemend dida, behr bi kenê dilîst, esman şîn û wek pola dibiriqî. ||| The earth had a rich smell, the sea was rippling with laughter, the sky was blue and gleaming like steel.

Zivistan mêjî û laşê mirov diçemisîne, lê paşê germahî tê ku sîngê fireh dike. ||| Winter shrivels up the mind and body of man, but then there comes the warmth which swells the breast.
Dema ez dimeşiyam ji nişkê ve min dengên boriyên bilind ên di hewayê de bihîst. ||| As I walked I suddenly heard loud trumpetings in the air.
Min çavên xwe rakirin û dîmenekî ecêb dît ku ji zarokatiya min ve her tim ez kûr hejandibûm: qulîng di rêzeke şer de li ezman belav dibûn, ji zivistandeketina li welatekî germtir vedigeriyan, û, wek ku efsane dibêje, hechecîkan li ser baskên xwe û di kortikên kûr ên laşên xwe yên hestûyî de hildigirtin. ||| I raised my eyes and saw a marvellous spectacle which had always moved me deeply ever since my childhood: cranes deploying across the sky in battle order, returning from wintering in a warmer country, and, as legend has it, carrying swallows on their wings and in the deep hollows of their bony bodies.

Ahenga neşikest a werzan, çerxa herdem-zivirî ya jiyanê, çar rûyên erdê ku bi nobetê ji aliyê tavê ve têne ronîkirin, derbasbûna jiyanê -- van hemûyan careke din ez bi hesta zextê tije kirim. ||| The unfailing rhythm of the seasons, the ever-turning wheel of life, the four facets of the earth which are lit in turn by the sun, the passing of life -- all these filled me once more with a feeling of oppression.
Careke din di hundirê min de, tevî qîrîna qulîngan, hişyariya tirsnak deng veda ku ji bo hemû mirovan tenê jiyanek heye, ku yeke din tune, û her tiştê ku dikare bê tam kirin divê li vir bê tam kirin. ||| Once more there sounded within me, together with the cranes' cry, the terrible warning that there is only one life for all men, that there is no other, and that all that can be enjoyed must be enjoyed here.
Di ebediyetê de tu firseteke din dê neyê dayîn me. ||| In eternity no other chance will be given to us.

Mêjiyek ku vê hişyariya bêrehm dibihîze -- hişyariyek ku, di heman demê de, ewqas dilovan e -- dê biryar bide ku qelsî û rezîliya xwe, tembelî û hêviyên xwe yên vala bi ser bikeve û bi hemû hêza xwe xwe bi her saniyeyê ku heta-hetayê difire ve girê bide. ||| A mind hearing this pitiless warning -- a warning which, at the same time, is so compassionate -- would decide to conquer its weakness and meanness, its laziness and vain hopes and cling with all its power to every second which flies away forever.

Mînakên mezin tên bîra te û tu bi zelalî dibînî ku tu giyanekî windabûyî yî, jiyana te li ser kêf û êşên biçûk û axaftinên pûç tê belavkirin. ||| Great examples come to your mind and you see clearly that you are a lost soul, your life is being frittered away on petty pleasures and pains and trifling talk.
«Şerm! Şerm!» tu diqîrî, û lêvên xwe didî ber diranan. ||| "Shame! Shame!" you cry, and bite your lips.

Qulîngan ezman derbas kiribû û ber bi bakur ve winda bûbûn, lê di serê min de ew berdewam kirin ku ji perestgehekê bo ya din bifirin, qîrînên xwe yên vala derdixistin. ||| The cranes had crossed the sky and disappeared to the north, but in my head they continued to fly from one temple to another, uttering their hollow cries.

Ez gihîştim behrê. ||| I came to the sea.
Ez bi lez li ber lêva avê dimeşiyam. ||| I was walking rapidly along the edge of the water.
Çiqas bêhntengî ye ku mirov bi tenê li ber behrê bimeşe! ||| How disquieting it is to walk alone by the sea!
Her pêlek, her teyrê li ezman gazî te dike û peywira te tîne bîra te. ||| Each wave, each bird in the sky calls to you and reminds you of your duty.

Dema mirov bi hevalan re dimeşe, mirov dikene û diaxive, û nikare bibihîze ka pêl û teyr çi dibêjin. ||| When walking with company you laugh and talk, and cannot hear what the waves and birds are saying.
Bê guman dibe ku ew tiştekî nabêjin. ||| It may be, of course, that they are saying nothing.
Ew li te dinêrin ku di ewrekî galegalê de derbas dibî û ji gazîkirinê radiwestin. ||| They watch you passing in a cloud of chatter and they stop calling.

Ez li ser keviran dirêj bûm û çavên xwe girtin. ||| I stretched out on the pebbles and closed my eyes.
«Wê demê giyan çi ye?» min ji xwe pirsî. ||| "What is the soul, then?" I wondered.
«Û ev girêdana veşartî ya di navbera giyan, û behr, ewr û bêhnxweşiyan de çi ye? Giyan bi xwe wek behr, ewr û bêhnxweşî xuya dike....» ||| "And what is this secret connection between the soul, and sea, clouds and perfumes? The soul itself appears to be sea, cloud and perfume...."

Ez rabûm û dîsa dest bi meşê kirim, wek ku ez gihîştibûm biryarekê. ||| I rose and started walking again, as if I had come to a decision.

Çi biryar? Min nizanibû. ||| What decision? I did not know.

Ji nişkê ve min dengek li pişt xwe bihîst. ||| Suddenly I heard a voice behind me.

«Tu bi xêra Xwedê bo ku diçî, ezbenî? Bo manastîrê?» ||| "Where are you going, sir, by the grace of God? To the convent?"

##PG 109
Ez zivirîm. ||| I turned round.
Pîremêrekî kurteqamet û qewîn, bi destmalek li dora porê xwe yê spî pêçayî, destê xwe dihejand û li min dikeniya. ||| A stocky, robust old man, with a handkerchief twisted round his white hair, was waving his hand and smiling at me.
Pîrejinek li pey wî dimeşiya, û li pey wê keça wan, keçeke çermqehweyî bi çavên hov, destmalek spî li serê xwe. ||| An old woman walked behind him, and behind her their daughter, a dark-skinned girl with fierce eyes, wearing a white scarf over her head.

«Manastîr?» pîremêr cara duyemîn pirsî. ||| "The convent?" asked the old man a second time.

Û ji nişkê ve min fêm kir ku min biryar dabû ku ez bi wê riyê biçim. ||| And suddenly I realized that I had decided to go that way.
Bi mehan bû ku min dixwest biçim manastîra biçûk a ku ji bo keşîşeyan li nêzî behrê hatibû avakirin, lê min tu caran nikaribû biryara xwe bidim. ||| For months I had wanted to go to the little convent built for the nuns near the sea, but I had never managed to make up my mind.
Laşê min wê êvarê ji nişkê ve biryar ji bo min dabû. ||| My body had abruptly made the decision for me that afternoon.

«Erê,» min bersiv da. «Ez diçim manastîrê ku stranên ji bo Meryema Pîroz bibihîzim.» ||| "Yes," I answered. "I'm going to the convent to hear the chants to the Holy Virgin."

«Bila bereketa Wê li ser te be.» ||| "May Her blessing be upon you."

Wî lezê da gavên xwe û gihîşt min. ||| He quickened his pace and caught me up.

«Ma tu ew î yê ku jê re dibêjin Şîrketa Komirê?» ||| "Are you what they call the Coal Company?"

«Rast e.» ||| "That's right."

«Baş e, bila Meryema Pîroz qezencên baş ji te re bişîne! Tu ji bo gund gelek qencî dikî, ji gelek bavên belengaz ên bi malbatên xwe re rêyek debarê tînî. Bila tu pîroz bî!» ||| "Well, may the Blessed Virgin send you good profits! You are doing a lot of good for the village, bringing a means of livelihood to many a poor father with a family to keep. May you be blessed!"

Û kêliyek an du paşê, pîremêrê jîr, ku divê bizanibûya ku me ne pir baş dikir, van peyvên dilxweşiyê lê zêde kir: ||| And a moment or two later the cunning old fellow, who must have known that we were not doing very well, added these words of consolation:

«Û heke tu jê tu qezencê negirî jî, kurê min, xem neke. Tu yê ne ziyandar bî. Giyanê te dê rasterast biçe bihiştê...» ||| "And even if you get no profit out of it, my son, don't worry. You'll not be the loser. Your soul will go direct to paradise..."

«Ev e ya ku ez hêvî dikim, bapîr.» ||| "That's what I'm hoping, grandad."

«Min tu carî xwendin nedîtiye, lê rojekê li dêrê min tiştek bihîst ku Îsa gotibû. ||| "I never had any education, but one day at church I heard something Christ had said.
Ew di serê min de cî girt û ez tu carî ji bîr nakim: ||| It stuck in my head and I never forget it:
‹Bifroşe,› wî got, ‹her tiştê ku tu xwedî yî, da ku tu Gewhera Mezin bi dest bixî.› ||| 'Sell,' he said, 'everything you possess to obtain the Great Pearl.'
Û ew Gewhera Mezin çi ye? ||| And what is that Great Pearl?
Rizgariya giyanê te. ||| The salvation of your soul.
Tu baş li ser riya bidestxistina Gewhera Mezin î, ezbenî.» ||| You are well on the way to getting the Great Pearl, sir."

Gewhera Mezin! Çend caran ew di tariya mêjiyê min de wek hêstirekê mezin biriqîbû! ||| The Great Pearl! How many times it had gleamed in the darkness of my mind like a huge tear!

Em dest bi meşê kirin, du mêr li pêş, du jin li pişt bi destên girêdayî. ||| We began walking, the two men in front, the two women behind with clasped hands.
Carna me gotinek dikir. ||| From time to time we made a remark.
Ma kulîlka zeytûnê dê li ser daran bidome? ||| Would the olive blossom last on the trees?
Ma dê baran bibariya û ceh dadipijand? ||| Would it rain and swell the barley?
Divê em herdu jî birçî bûna, çimkî me her tim axaftin ber bi xwarinê ve dibir. ||| We must both have been hungry because we constantly led the conversation round to food.

«Xwarina te ya bijare çi ye, bapîr?» ||| "What is your favorite dish, grandad?"

«Hemû, kurê min. Gunehekî mezin e ku mirov bibêje ev baş e û ew xirab e.» ||| "All of them, my son. It's a great sin to say this is good and that is bad."

«Çima? Ma em nikarin hilbijêrin?» ||| "Why? Can't we make a choice?"

«Na, bê guman em nikarin.» ||| "No, of course we can't."

«Çima na?» ||| "Why not?"

«Çimkî mirovên birçî hene.» ||| "Because there are people who are hungry."

Ez bêdeng bûm, şermisar. ||| I was silent, ashamed.
Dilê min tu caran nikaribû bigihîje wê bilindahiya rûmet û dilovaniyê. ||| My heart had never been able to reach that height of nobility and compassion.

Zengilê biçûk ê manastîrê bi şahî û bi lîstik lê xist, wek kenê jinekê. ||| The little convent bell rang out merrily and playfully, like a woman's laugh.

Pîremêr xaç li xwe kir. ||| The old man made the sign of the cross.

«Bila Meryema Şehîd bigihîje hawara me!» wî bi nizmî got. «Birîneke kêrê li stûyê wê heye û xwîn jê tê. Di dema talankerên behrê de...» ||| "May the Martyred Virgin come to our help!" he murmured. "She has a knife wound in the neck and bleeds. In the time of the corsairs..."

##PG 110
Û pîremêr dest bi xemilandina êşên Meryemê kir, wek ku ew çîroka jineke rastîn bûya, penaberek ciwan a perçiqandî ku bi hêsiran bi zarokê xwe re ji Rojhilatê hatibû û ji aliyê nebaweran ve hatibû kêr lê xistin. ||| And the old man began embroidering on the sufferings of the Virgin, as though it were the story of a real woman, a young persecuted refugee who had come in tears with her child from the East and had been stabbed by the unfaithful.

«Salê carekê xwîna germ a rastîn ji birîna wê diherike,» pîremêr berdewam kir. «Tê bîra min berî gelek zemanan, di salvegera wê de -- hîn simbêlên min derneketibûn -- mirov ji hemû gundên çiyan dahatibûn ku Meryemê biperizin. ||| "Once a year real warm blood runs from her wound," the old man went on. "I remember a long time ago, on her anniversary -- I hadn't yet grown a moustache -- people had come down from all the villages in the hills to worship the Virgin.
Pazdehê tebaxê bû. ||| It was the fifteenth of August.
Em mêr li derve, li hewşê razabûn; jin li hundir bûn. ||| We men slept outside, in the yard; the women were inside.
Û di xewa xwe de min dengê qîrîna Meryemê bihîst. ||| And in my sleep I heard the Virgin cry out.
Ez bi lez rabûm, bezîm îkona wê û destê xwe danî ser stûyê wê. ||| I got up in a hurry, ran to her icon and put my hand on her throat.
Û tu çi difikirî ku min dît? Tiliyên min bi xwînê sor bûbûn....» ||| And what do you think I saw? My fingers were red with blood...."

Pîremêr xaç li xwe kir û li jinan zivirî nêrî. ||| The old man crossed himself and looked round at the women.

«Werin, hûn jinno! Em hema gihîştin!» wî qîriya. ||| "Come on, you women! We're nearly there!" he cried.

Wî dengê xwe nizm kir. ||| He lowered his voice.

«Ez wê demê ne zewicî bûm. Min xwe li ber Pîroziya Wê deynand, û biryar da ku vê dinya derewan bihêlim û bibim keşîş....» ||| "I wasn't married then. I prostrated myself to Her Holiness, and decided to leave this world of lies and be a monk...."

Ew keniya. ||| He laughed.

«Çima tu dikenî, bapîr?» ||| "Why are you laughing, grandad?"

«Ma ne bes e ku te bide kenandin, kurê min? Heman roj, di dema cejnê de, şeytan, wek jinekê li xwe kirî, li pêşberî min sekinî. Ew bû!» ||| "Isn't it enough to make you laugh, my son? The very same day, during the festival, the devil, dressed up as a woman, stood before me. It was she!"

Bê ku serê xwe bizivirîne, wî tiliya xwe ya beranî ber bi paş ve hejand û pîrejina li pişt xwe, ku bêdeng li pey me dihat, nîşan da. ||| Without turning his head, he jerked his thumb backwards and indicated the old woman behind him, who was following us in silence.

«Niha lê nayê nêrîn,» wî got; «fikra dest lê dayînê te dilbijî dike. ||| "She doesn't bear looking at now," he said; "the thought of touching her disgusts you.
Lê wan rojan ew delaleke rast bû; ew wek masiyekî bi jiyanê dilerizî. ||| But in those days she was a regular flirt; she quivered with life like a fish.
‹Delala bijang-dirêj,› jê re digotin, û ew bi rastî hêjayî navî bû, ya bêbav! Lê niha... Xwedê giyanê min bihêle, bijangên wê niha li kû ne? Çûne ber bê! Yek jî nemaye!» ||| 'The long-lashed beauty,' they used to call her, and she well deserved the name, the little minx! But now... God rest my soul, where are her lashes now? Gone to blazes! Not a single one left!"

Wê gavê, tam li pişt me, pîrejinê fîzeke nixumandî kir wek kûçikekî hêrs ê li ser zincîrê. ||| At that moment, just behind us, the old woman made a muffled growl like a churlish dog on a chain.
Lê tu peyvek negot. ||| But she did not say a word.

«Va ye, ew e manastîr,» pîremêr got. ||| "There, that's the convent," said the old man.

Li ber lêva behrê, di navbera du zinarên mezin de çikandî, manastîra spî ya biriqok hebû. ||| At the edge of the sea, wedged between two great rocks, was the white, sparkling convent.
Li navê, qubeya kenîsê, nû spîkirî, biçûk û gilover wek memikê jinekê. ||| In the middle the chapel dome, freshly whitewashed, small and round like a woman's breast.
Li dora kenîsê şeş hucreyên bi deriyên şîn, sê darên selwiyê yên mezin di hewşê de, û li dora dîwêr çend hêjîrên frengî yên stirîdar ên qewîn ên di kulîlkê de hebûn. ||| About the chapel were half a dozen cells with blue doors, three large cypress trees in the courtyard, and along the wall some sturdy prickly pears in flower.

Em zûtir çûn. ||| We went faster.
Stranên awazdar ji deriyê vekirî yê perestgehê dadiketin, hewa şor bi bêhna lubanê bêhnxweş bûbû. ||| Melodious chanting floated down from the open door of the sanctuary, the salt air was perfumed with benjamin.
Deriyê ketinê yê li navê kemerê pan vekirî bû û li hewşa pak û bêhnxweş a bi keviran ên reş û spî reşandî vedibû. ||| The entrance door in the middle of the arch stood wide open and gave on to the clean, scented courtyard strewn with black and white pebbles.
Li dirêjahiya dîwaran, ber bi rast û çepê, rêzên kûzan hebûn, bi rosmarî, mardeqoş û rîhanê. ||| Along the walls, to the right and to the left, were rows of pots, with rosemary, marjoram and basil.

Çi aramî! Çi şîrînî! ||| What serenity! What sweetness!
Niha tav diçû ava û dîwarên spîkirî sor-pembe dibûn. ||| The sun was going down now and the whitewashed walls were turning pink.

Kenîseya biçûk, germ û hinekî tarî di hundir de, bêhna mûmê dida. ||| The little chapel, warm and rather dark inside, smelled of wax.

Mêr û jin di ewrên buxûr de dilivîn, û pênc-şeş keşîşe, di kincên xwe yên dirêj ên reş de hişk pêçayî, distiran: ||| Men and women were moving in clouds of incense, and five or six nuns, tightly wrapped in their long black dresses, were singing:

«Ya Xwedayê Karîndar...» bi dengên xwe yên şîrîn û tîz. ||| "O, Almighty God..." in their sweet, high-pitched voices.
Ew bi domdarî dema distiran li ser çokan diketin û xişîna kincên wan wek teyrên ku difirin dihat. ||| They were constantly kneeling as they sang and the rustling of their dresses sounded like birds on the wing.

Bi salên dirêj bû ku min stranên ji bo Meryema Pîroz nebihîstibû. ||| I had not heard hymns sung to the Virgin Mary for many years past.
Di serhildana xortaniya min a destpêkê de min bi hêrs û nefret di dilê xwe de derbasî her dêrê bûbûm. ||| During the revolt of my early youth I had passed by every church with anger and contempt in my heart.

##PG 111
Her ku dem derbas dibû ez kêmtir tundûtûj bûm. ||| As time went on I grew less violent.
Bi rastî, carna, ez diçûm cejnên olî -- Sersal, Şevên Pîroz, Vejîn -- û ez kêfxweş dibûm ku zarokê di hundirê min de dîsa zindî dibe. ||| Now and again, in fact, I went to religious festivals -- Christmas, the Vigils, the Resurrection -- and I was happy to see the child in me come to life again.
Coşa mîstîk a salên min ên destpêkê veguheribû xweşiyeke estetîk. ||| The mystic fervor of my early years had degenerated into an aesthetic pleasure.
Hovan bawer dikin ku dema amûrek muzîkê êdî ji bo merasîmên olî nayê bikaranîn, ew hêza xwe ya xwedayî winda dike û dest bi derxistina dengên ahengdar dike. ||| Savages believe that when a musical instrument is no longer used for religious rites it loses its divine power and begins to give out harmonious sounds.
Ol jî, bi heman awayî, di min de nizm bûbû: ew bûbû huner. ||| Religion, in the same way, had become degraded in me: it had become art.

Ez çûm quncikekî, paldam ser textika stranê ya biriqok a ku destên dîndaran wek diranê fîl nerm û saf kiribû, û bi efsûnê guhdarî kir dema ku îlahiyên Bîzansî ji rabirdûya dûr dihatin: ||| I went into a corner, leaned on the gleaming stall that the hands of the faithful had polished as smooth as ivory, and listened in enchantment as the Byzantine hymns came from the distant past:

##VERSE
Silav! Bilindahiyên ku ji mêjiyê mirov re negihiştî ne!<br>Silav! Kûrahiyên ku tewra ji çavên milyaketan re jî venegirtî ne!<br>Silav! Bûka pak, ya Gula ku tu caran naçilmise... ||| "Hail! heights inaccessible to the human mind! Hail! depths impenetrable even to the eyes of angels! Hail! immaculate bride, O never-fading Rose..."

Keşîşeyan careke din bi serê daxistî li ser çokan ketin û kincên wan wek baskan xişîn. ||| The nuns once more dropped on their knees with head bowed and their dresses rustled like wings.

Deqîqe derbas bûn -- milyaketên bi baskên bêhnxweş ên lubanê, ku sosinên girtî di destên xwe de digirtin û bedewiyên Meryemê distiran. ||| Minutes went by -- angels with benjamin-scented wings, bearing closed lilies in their hands and singing the beauties of Mary.
Tav çû ava, me di tariyeke şîn a nerm de hişt. ||| The sun went down, leaving us in a downy blue twilight.
Nayê bîra min ku em çawa gihîştin hewşê, lê ez li wir bi tenê bûm digel Dêya Manastîrê ya pîr û du keşîşeyên ciwan, li bin mezintirîn ji darên selwiyê. ||| I do not remember how we came to be in the courtyard, but I was alone there with the old Mother Superior and two young nuns, beneath the largest of the cypress trees.
Keşîşeyeke ciwan a nûhatî derket ku kefçiyek mireba, ava sar û qehweyê pêşkêşî min bike, û axaftineke aram dest pê kir. ||| A young novice came out to offer me a spoonful of jam, fresh water and coffee, and a peaceful conversation began.

Me li ser keramaetên ku Meryema Pîroz pêk anîbûn, li ser komirê, li ser mirîşkên ku niha ku bihar bû dest bi hêkkirinê dikirin, û li ser keşîşe Evdoksiya ya ku nexweşiya sarayê hebû û her dem li ser erdê kenîsê dadiket û wek masiyekî dilerizî, kef ji devê wê dihat û cilên xwe diçirand, axivîn. ||| We talked of the miracles wrought by the Virgin Mary, of lignite, of the hens beginning to lay now that it was spring, of sister Eudoxia who was epileptic and continually falling down on the floor of the chapel and quivering like a fish, foaming at the mouth and tearing her clothes.

«Ew sî û pênc salî ye,» Dêya Manastîrê bi axînekê lê zêde kir. «Temenekî bêbext -- pir zehmet! Bila Meryema Şehîd a Pîroz bigihîje hawara wê û wê sax bike! Di deh-pazdeh salan de ew ê sax bibe.» ||| "She is thirty-five," added the Mother Superior with a sigh. "An unhappy age -- very difficult! May the Holy Martyred Virgin come to her aid and cure her! In ten or fifteen years she will be cured."

«Deh an pazdeh sal,» min bi matmayî bi nizmî got. ||| "Ten or fifteen years," I murmured, aghast.

«Deh an pazdeh sal çi ne?» Dêya Manastîrê bi tundî pirsî. «Li ebediyetê bifikire!» ||| "What are ten or fifteen years?" asked the Mother Superior severely. "Think of eternity!"

Min tu bersiv neda. ||| I made no answer.
Min dizanî ku ebediyet her deqîqeya ku derbas dibe ye. ||| I knew that eternity is each minute that passes.
Min destê Dêya Manastîrê maç kir -- destekî qelew, spî, ku bêhna buxûr jê dihat -- û derketim. ||| I kissed the Mother Superior's hand -- a plump, white hand, smelling of incense -- and departed.

Şev daketibû. ||| Night had fallen.
Du-sê qijik bi lez vedigeriyan hêlînên xwe; kund ji darên kortikî derdiketin ku nêçîrê bikin. ||| Two or three crows were hurrying back to their nests; owls were coming out of the hollow trees to hunt.
Hiseynok, kurmikên pelan, kurm, mişkên zeviyê ji erdê derdiketin da ku ji aliyê kundan ve werin xwarin. ||| Snails, caterpillars, worms, field-mice were coming out of the earth to be eaten by the owls.

Marê nepenî yê ku dûvê xwe dixwe min di xelekê xwe de girt: erd zarokên xwe tîne jiyanê û dixwe, paşê hîn zêde tîne û dor bi dor wan dixwe. ||| The mysterious snake that devours its own tail enclosed me in its circle: the earth brings to life and devours her own children, then bears more and devours them in their turn.

Min li dora xwe nêrî. ||| I looked about me.
Pir tarî bû. ||| It was quite dark.
Yên dawî yên gundiyan çûbûn, kesî nikaribû min bibîne, ez bi temamî bi tenê bûm. ||| The last of the villagers had gone, no one could see me, I was absolutely alone.
Min pêyên xwe tazî kirin û di behrê de avêtin. ||| I bared my feet and dipped them in the sea.
Ez li ser qûmê gindirîm. ||| I rolled on the sand.
Min daxwazek hîs kir ku bi laşê xwe yê tazî dest li keviran, avê û hewayê bidim. ||| I felt an urge to touch the stones, the water, and the air with my bare body.
Dêya Manastîrê bi «ebediyeta» xwe ez aciz kiribûm, û min hîs kir ku peyv li dora min dikeve, wek kemendekê ku hespê hov digire. ||| The Mother Superior had exasperated me with her "eternity," and I felt the word fall about me, like a lasso catching a wild horse.
Min bazek da ku hewl bidim birevim. ||| I made a leap to try to escape.
Min daxwazek hîs kir ku laşê xwe yê tazî li hember erd û behrê bişidînim, da ku bi piştrastî hîs bikim ku ev tiştên hezkirî yên demborî bi rastî hebûn. ||| I felt a desire to press my naked body against the earth and the sea, to feel with certainty that these beloved ephemeral things really existed.

##PG 112
«Tu hî heyî, û tu bi tenê!» min di hundirê xwe yê herî kûr de qîriya. «Ya Erd! Ez zarokê te yê dawî me, ez memikê te dimijim û bernadim. Tu nahêlî ku ez ji deqîqeyekê bêtir bijîm, lê ew deqîqe dibe memik û ez dimijim.» ||| "You exist, and you alone!" I cried in my innermost self. "O Earth! I am your last-born, I am sucking at your breast and will not let go. You do not let me live for more than one minute, but that minute turns into a breast and I suck."

Ez ricifîm wek ku min hîs kir ku ez di xetera avêtina nav wê peyva mirovxwer «ebediyet» de me. ||| I shuddered as if I felt I was running the risk of being hurled into that anthropophagous word "eternity."
Hat bîra min ka berê -- kengî? tenê salek berê -- min çawa bi çavên girtî û milên vekirî bi dilxwazî li ser wê fikirîbû, dixwest xwe bavêjim nav wê. ||| I remembered how formerly -- when? only a year ago -- I had eagerly pondered it with closed eyes and arms apart, wanting to throw myself into it.

Dema ez di pola yekem a dibistana dewletê de bûm, di pirtûka xwendinê ya ku me ji bo nîvê duyemîn ê alfabeyê bi kar dianî de çîrokek hebû: ||| When I was in the first form at the state school there was a story in the reading book we used for the second half of the alphabet:

Zarokek ketibû bîrekê, çîrok digot. ||| A little child had fallen into a well, said the story.
Li wir wî bajarekî ecêb dît, baxçeyên kulîlkan, golek ji hingivê safî, çiyayek ji şîrbirinc û pîstikên pirreng. ||| There it found a marvellous city, flower gardens, a lake of pure honey, a mountain of rice pudding and multi-colored toys.
Her ku min ew tîp bi tîp dixwend, her kîte wek ku min hîn bêtir dibir nav wî bajarê sêhrbaz. ||| As I spelled it out, each syllable seemed to take me further into that magic city.
Carekê, nîvro, dema ku ez ji dibistanê hatibûm malê, ez bezîm baxçe, çûm ber lêva bîrê ya di bin kemera mêwê de û matmayî sekinîm, li rûyê reş ê hilû yê avê dinêrî. ||| Once, at midday, when I had come home from school, I ran into the garden, rushed to the rim of the well beneath the vine arbor and stood fascinated, staring at the smooth black surface of the water.
Zû min digot qey ez dikarim bajarê ecêb bibînim, xanî û kolanan, zarokan û kemera mêwê ya bi tirî barkirî. ||| I soon thought I could see the marvellous city, houses and streets, the children and the vine arbor loaded with grapes.
Min nikaribû bêtir li ber xwe bidim; min serê xwe ber bi jêr ve daliqand, milên xwe dirêj kirin û li erdê pêlatî kir da ku xwe ji ber kêlekê bidim xwarê. ||| I could hold out no longer; I hung my head down, held out my arms and kicked against the ground to push myself over the edge.
Lê wê gavê dayika min ez ferq kirim. ||| But at that moment my mother noticed me.
Ew qîriya, bezî der û ez ji kemberê girtim, tam di wextê de.... ||| She screamed, rushed out and caught me by my waistband, just in time....

Wek zarok, wê demê, ez hema hema ketibûm bîrê. ||| As a child, then, I had almost fallen into the well.
Dema mezin bûm, ez hema hema ketim nav peyva «ebediyet», û nav hejmareke baş a peyvên din jî -- «evîn», «hêvî», «welat», «Xwedê». ||| When grown up, I nearly fell into the word "eternity," and into quite a number of other words too -- "love," "hope," "country," "God."
Her ku peyvek dihat bi ser ketin û li paş dihat hiştin, min hîs dikir ku ez ji xetereyekê filitîbûm û hinekî pêş ketibûm. ||| As each word was conquered and left behind, I had the feeling that I had escaped a danger and made some progress.
Lê na, ez tenê peyvan diguherandim û jê re digot rizgarî. ||| But no, I was only changing words and calling it deliverance.
Û li wir bûm, ji bo du salên dawî, li ser kêleka peyva «Bûda» daliqandî. ||| And there I had been, for the last two years, hanging over the edge of the word "Buddha."

Lê niha ez piştrast im -- bila Zorba bê pesinandin -- ku Bûda dê bîra dawî ya hemûyan be, kendalê dawî yê peyvan, û paşê ez ê heta-hetayê rizgar bibim. ||| But I now feel sure -- Zorba be praised -- that Buddha will be the last well of all, the last word precipice, and then I shall be delivered forever.
Heta-hetayê? Ev e ya ku em her carê dibêjin. ||| Forever? That is what we say each time.

Ez bazdam ser xwe. ||| I jumped up.
Ez ji serî heta pê bextewar bûm. ||| I was happy from head to foot.
Min cilên xwe derxistin û xwe avêtim nav behrê; pêlên şahîdar dilîstin û ez bi wan re lîstim. ||| I undressed and plunged into the sea; the joyful waves were frolicking and I frolicked with them.
Di dawiyê de westiyayî, ez ji avê derketim, hiştim ku bayê şevê min ziwa bike, û dîsa bi gavên dirêj ên hêsan dest bi rê kirim, hîs dikir ku ez ji xetereyeke mezin filitîbûm û ku min hîn bi hêztir memikê Dayika Mezin girtibû. ||| Tired at last, I came out of the water, let the night wind dry me, and set out again with long easy strides, feeling I had escaped a great danger and that I had a still tighter grip on the Great Mother's breast.
"""

CH16 = r"""
##PG 112
##FIRST
Hema ku peravê komirê ket ber çavê min, ez ji nişkê ve sekinîm: ronahiyek di koxikê de hebû. ||| AS SOON as I came within sight of the lignite beach I stopped abruptly: there was a light in the hut.

«Divê Zorba vegeriyabe!» min bi kêfxweşî fikirî. ||| "Zorba must be back!" I thought happily.

Dilê min xwest ez bibezim, lê min xwe girt. ||| I felt like running, but restrained myself.
Divê ez şahiya xwe veşêrim, min fikirî. ||| I must hide my joy, I thought.
Divê ez xwe aciz nîşan bidim û pêşî jê re hinekî gotinên tund bibêjim. ||| I must look annoyed and first give him a good talking-to.

Min ew ji bo karekî lezgîn şandibû wir, û wî nû dirav ê min xerc kiribû, bi hin jineke kabareyê re jiyabû, û niha donzdeh roj dereng vedigere. ||| I sent him there on urgent business, and he'd just gone through my money, lived with some cabaret tart, and now comes back twelve days late.
Divê ez xwe wisa nîşan bidim ku ez di hêrseke kerb de me... divê! ||| I must look as if I'm in a furious temper... I must!

Min hêdîtir meşiya da ku wext bidim xwe ku hêrsê bînim ser xwe. ||| I walked slower to give me time to work up a temper.
Min gelek hewl da ku hêrs bibim -- birûyên xwe qermiçandin û mistên xwe girtin, her tiştê ku mirovekî hêrs bi gelemperî dike kir -- lê min nikaribû. ||| I tried hard to be angry -- frowned and clenched my fists, did everything an angry man usually does -- but could not manage it.
Berevajî, ez çiqas nêzîktir dibûm ewqas bextewartir dibûm. ||| On the contrary, the nearer I came the happier I grew.

##PG 113
Ez bi dizî nêzîkî koxikê bûm û ji pencereya biçûk a ronîkirî nêrî. ||| I crept up to the hut and looked through the small lighted window.
Zorba li ber sobeya biçûk a ku wî pêxistibû li ser çokan bû û kahwe çêdikir. ||| Zorba was on his knees by the tiny stove which he had lit and was making coffee.

Dilê min heliya û min qîriya: «Zorba!» ||| My heart melted and I shouted: "Zorba!"

Di kêliyekê de derî vebû û Zorba, pêxwas, bezî der. ||| In a trice the door swung open and Zorba, barefoot, rushed out.
Wî situyê xwe dirêj kir, di tariyê de çavê xwe pê girt, ez dîtim, milên xwe vekirin ku min hembêz bike, paşê sekinî û hişt ku ew dakevin kêlekên wî. ||| He craned his neck, peering in the dark, discovered me, opened his arms to embrace me, then stopped and let them fall to his sides.

«Kêfxweş im ku ez dîsa te dibînim, axa,» wî bi dudilî got, li pêşberî min bi rûyekî dirêj û bêliv sekinî. ||| "Glad to see you again, boss," he said hesitantly, standing longfaced and motionless before me.

Min hewl da ku dengê xwe bi hêrs bilind bikim: ||| I tried to raise my voice angrily:

«Kêfxweş im ku te zehmet kişandiye ku vegerî,» min bi tinazî got. «Newêrî nêzîktir bibî -- bêhna sabûna tuwaletê ji te tê.» ||| "Glad to see you've taken the trouble to come back," I mocked. "Don't come any nearer -- you reek of toilet soap."

«Ax, xwezî te bizaniya ku min çawa xwe şûştiye, axa,» wî got. «Min xwe çiqas paqij kir! Berî ku te bibînim min çermê xwe yê nifirî perçe perçe xurand, axa! Bi saetekê min xwe bi kevirê qûmê sûd. Lê ev bêhna cehennemî... Çi dibe bila bibe? Ew ê zû an dereng here. ||| "Ah, if only you knew what a scrubbing I've given myself, boss," he said. "Have I cleaned myself up! I scraped my blasted skin to bits before seeing you, boss! I've sandstoned myself for an hour. But this hellish smell... Anyway, what of it? It'll pass off sooner or later.
Ne cara yekem e -- ew ê here.» ||| It isn't the first time -- it's bound to go."

«Em herin hundir,» min got, hema bi ken biteqim. ||| "Let's get inside," I said, nearly bursting with laughter.

Em ketin hundir. ||| We went in.
Koxikê bêhna bêhnxweşî, pûdre, sabûn û jinan dida. ||| The hut smelled of perfume, powder, soap and women.

«Bi navê Xwedê ev hemû çi ne, ez dikarim bipirsim?» min got, û îşaret bi sindoqekê kir ku tijî çenteyên dest, perçeyên sabûna tuwaletê, gore, sîwanek sor a biçûk û du şûşeyên biçûk ên bêhnxweşiyê bû. ||| "What in God's name is all that, may I ask?" I said, pointing to a case filled with handbags, bars of toilet soap, stockings, a small red parasol and two minute bottles of scent.

«Diyarî...» Zorba bi serê daxistî di bin lêv de got. ||| "Presents..." muttered Zorba, hanging his head.

«Diyarî?» min got, hewl dida ku hêrs xuya bibim. «Diyarî?» ||| "Presents?" I said, trying to sound furious. "Presents?"

«Diyarî, axa... ji bo Bûbûlîna biçûk. Hêrs nebe, axa. Paskalya nêzîk dibe, û ew jî mirovek e, tu dizanî.» ||| "Presents, boss... for little Bouboulina. Don't be angry, boss. Easter's coming soon, and she's a human being too, you know."

Min careke din karîbû kenê xwe bigirim. ||| I managed to restrain my laughter once again.

«Te ya herî girîng jê re neaniye,» min got. ||| "You haven't brought her the most important thing," I said.

«Çi?» ||| "What?"

«Tacên zewacê, helbet.» ||| "The marriage wreaths, of course."

«Çi? Mebesta te çi ye? Ez fêm nakim.» ||| "What? What d'you mean? I don't understand."

Wê demê min jê re got ka min çawa bi sîrena evîndar re henek kiribû. ||| I then told him the way I had pulled the lovesick siren's leg.

Zorba bo saniyeyekê serê xwe xurand, fikirî û paşê got: ||| Zorba scratched his head a second, reflected and then said:

«Divê tu tiştên wisa neke, axa, eger tu li min nesekinî. Wî cure henekî, tu dizanî, ew... jin afirîdên qels û nazik in -- min çend caran ji te re gotiye? Ew wek qedehên porselenê ne, û divê tu wan pir bi baldarî bigirî, axa.» ||| "You shouldn't do things like that, boss, if you don't mind my saying so. That sort of joke, you know, is... women are weak, delicate creatures -- how many times have I got to tell you that? Like porcelain vases, they are, and you have to handle them very carefully, boss."

Ez şerm kirim. ||| I felt ashamed.
Min jî poşman bûbû, lê pir dereng bû. ||| I had regretted it, too, but it was too late.
Min mijar guhert. ||| I changed the subject.

«Û têl?» min pirsî. «Û amûr?» ||| "And the cable?" I asked. "And the tools?"

«Min her tişt aniye; xwe nelivîne! ‹Mirov nikare hem keka xwe bihêle hem jî bixwe!› wek ku dibêjin! Hesinrêya têlê, Lola, Bûbûlîna -- her tişt baş di destê min de ye.» ||| "I've brought everything; don't get worked up! 'You can't have your cake and eat it!' as they say! The cable railway, Lola, Bouboulina -- everything's well in hand."

Wî briki (qûşxaneya biçûk a kahweyê) ji ser êgir rakir, fîncana min tije kir, hin kuloçeyên bi sêmsem ên ku anîbûn da min û helawa hingiv a ku dizanibû şîrîniya min a bijare bû. ||| He took the briki off the flame, filled my cup, gave me some jumbals with sesame which he had brought and honey halva which he knew was my favorite sweet.

##PG 114
«Min ji te re diyariya sindoqeke mezin a helawê aniye!» wî bi dilovanî got. «Ez ji bîr nekirim, tu dibînî.» ||| "I've brought you a present of a large box of halva!" he said fondly. "I didn't forget you, you see."

«Binêre, min ji bo papaganê tûrikek fistiqan aniye. Min kes ji bîr nekiriye. Tu dizanî, mêjiyê min zêde giran e.» ||| "Look, I've brought a little bag of peanuts for the parrot. I've forgotten no one. You know, my brain's overweight."
Zorba kahweya xwe vedixwar, cixare dikişand û li min dinêrî. ||| Zorba was sipping his coffee, smoking and watching me.
Çavên wî wek yên marekî ez efsûnî kirim. ||| His eyes fascinated me like those of a serpent.

«Te ew pirsgirêka ku te diêşand çareser kir, fêlbazê pîr?» min jê pirsî, dengê min niha nermtir. ||| "Have you solved the problem which was tormenting you, you old rogue?" I asked him, my voice gentler now.

«Çi pirsgirêk, axa?» ||| "What problem, boss?"

«Ka jin mirov in an na?» ||| "If women are human beings or not?"

«Ox! Ew hat çareserkirin!» Zorba bersiv da, destê xwe dihejand. «Jin jî mirov e, mirovek wek me -- tenê xirabtir! Hema ku çavê wê bi kîsê te dikeve serê xwe winda dike. Ew xwe bi te ve digire, azadiya xwe berdide û kêfxweş e ku wê berde çimkî, li paş mêjiyê xwe, kîs dibiriqe. Lê ew zû... Ax, bila ev hemû here cehennemê, axa!» ||| "Oh! That's settled!" answered Zorba, waving his hand. "A woman's human, too, a human like us -- only worse! The minute she sees your purse she loses her head. She clings to you, gives up her freedom and is glad to give it up because, at the back of her mind, the purse is glittering. But she soon... Ah, to hell with all that, boss!"

Ew rabû ser xwe û cixareya xwe ji pencerê avêt der. ||| He stood up and threw his cigarette out of the window.

«Niha, wek mêr bi mêr,» wî berdewam kir. «Hefteya Pîroz tê, têl bi me re heye, êdî wext e ku em derkevin manastîrê û wan berazên qelew biguvêşin ku belgeyên wê erdê daristanê îmze bikin... berî ku ew xetê bibînin û bi heyecan bikevin -- tu fêm dikî ez çi dibêjim? Wext derbas dibe, axa, û em ê tu carî bi vî rengî tembel negihîjin tu deverê; divê em dest bi kar bikin; divê em dest bi berhevkirinê bikin... divê em dest bi barkirina keştiyan bikin da ku tiştê ku me xerc kiriye telafî bikin.... Ew sefera Kandiyayê pir bi me ket. Tu dibînî, şeytan...» ||| "Now, man to man," he went on. "Holy Week's coming, we've got the cable, it's high time we went up to the monastery and got those fat pigs to sign the documents for that forest land... before they see the line and become excited -- see what I mean? Time's going by, boss, and we'll never get anywhere being so lackadaisical; we must get down to it; we've got to start raking in... we must start loading the ships to make up for what we've spent.... That trip to Candia cost a packet. You see, the devil..."

Ew sekinî. ||| He stopped.
Dilê min pê şewitî. ||| I was sorry for him.
Ew tam wek zarokek bû ku tiştekî ehmeqane kiriye û, nizane ka çawa dikare tiştan dîsa rast bike, tenê hemû dilerize. ||| He was just like a child who has done something silly and, not knowing how he can put things right again, just trembles all over.

«Şerm li te be!» min ji xwe re got. «Tu çawa dihêlî ku giyanekî wisa bi tirs bilerize? Tu yê li ku derê Zorbayekî din bibînî? Were de, hemûyî jê bişo!» ||| "Shame on you!" I said to myself. "How can you let a soul like that tremble with fright? Where will you ever find another Zorba? Come on, sponge it all out!"

«Zorba!» min qîriya. «Şeytan bi tena xwe bihêle; em jê re tu kêrî nayên! Tiştê ku qewimî qewimî... û ji bîr bû! Santûriya xwe daxe!» ||| "Zorba!" I cried. "Leave the devil alone; we have no use for him! What's done is done... and forgotten! Take down your santuri!"

Wî dîsa milên xwe vekirin wek ku dixwest min hembêz bike. ||| He opened his arms again as if he wanted to embrace me.
Lê wî bi hêdî ew girtin, hîn dudil. ||| But he closed them slowly, still hesitant.

Bi bazdanekê ew li ber dîwêr bû. ||| In one bound he was at the wall.
Ew li ser pencên xwe rabû û santûrî daxist. ||| He stood up on his toes and took down the santuri.
Dema ew vegeriya ronahiya lempeyê min porê wî dît: ew wek qîr reş bû. ||| As he came back into the light of the lamp I saw his hair: it was as black as pitch.

«Kûçikê pîr,» min qîriya, «te bi serê Xwedê çi bi porê xwe kir? Te ew ji ku derê anî?» ||| "You old dog," I shouted, "what on earth have you done to your hair? Where did you get that?"

Zorba dest bi kenê kir. ||| Zorba began to laugh.

«Min ew boyax kir, axa. Aciz nebe... min ew boyax kir çimkî pê bextê min nedihat....» ||| "I've dyed it, boss. Don't get upset... I dyed it because I had no luck with it...."

«Ji bo çi?» ||| "What for?"

«Pozbilindî, bi Xwedê! Rojekê ez bi Lolayê re derketibûm meşê, ji destê wê girtî. Ne girtî jî... binêre, wisa, tenê bi serê tiliyên xwe! Û hin pîçê biçûk ê nifirî, ne ji vê destê mezintir, dest bi qîrîna li pey me kir: ‹Hey, pîrê!› pîçê qehpik qîriya. ‹Hey tu! Tu wê bo ku dibî, zarokrevîno?› ||| "Vanity, by God! One day I was out walking with Lola, holding her arm. Not even holding... look, like that, just the end of my fingers! And some bloody little urchin, no bigger than this hand, started shouting after us: 'I say, old 'un!' the whoreson kid shouted. 'You there! Where are you taking her, baby-snatcher?'

«Lola şerm kir, tu dikarî bifikirî, û ez jî. Loma ez heman şevê çûm ber sertaş û min perûka xwe reş boyax kir.» ||| "Lola was ashamed, you can imagine, and so was I. So I went the same night to the barber's and had my wig dyed black."

Ez dest bi kenê kirim. ||| I began to laugh.
Zorba bi giranî li min dinêrî. ||| Zorba watched me gravely.

##PG 115
«Ma ev ji te re tinaz xuya dike, axa? Baş e, tenê bisekine û bibîne ku mirov çi heywanekî ecêb e! Ji roja ku min ew kir, ez bûme mirovekî bi temamî din. Tu yê bifikirî ku porê min ji destpêkê reş bûye; min bi xwe jî dest bi baweriyê kir -- mirov bi hêsanî tiştê ku lê nayê ji bîr dike, tu dizanî -- û ez sond dixwim ku ez hêztir bûme. Lola jî ferq kiriye. Tê bîra te ew êşa ku min li vir li pişta xwe hebû? Baş e, ew çûye! Ji wê demê ve nemaye! Helbet tu bawer nakî, pirtûkên te tiştên wisa ji te re nabêjin.» ||| "Does that sound comic to you, boss? Well, just wait and see what a strange animal man is, though! From the day I had it done, I've been another man altogether. You'd think I had black hair for good; I've begun to believe it myself -- a man easily forgets what doesn't suit him, you know -- and I swear I've got stronger. Lola's noticed it, too. D'you remember that pain I used to have in my back here? Well, it's gone! Haven't had it since! You don't believe me, of course, your books don't tell you things like that."

Ew bi tinazî keniya, paşê poşman bû. ||| He laughed ironically, then repented.

«Eger ez bibêjim, axa... tenê pirtûka ku min di jiyana xwe de xwendiye Sindibadê Deryavan e, û ji bo wê hemû qenciya ku ew bi min kir...» ||| "If I may say so, boss... the only book I've ever read in my life is Sinbad the Sailor, and for all the good that did me..."

Wî santûrî bi hêdî û bi dilovanî vekir. ||| He undid the santuri slowly and affectionately.

«Were derve,» wî got. «Santûrî di nav çar dîwaran de li mal nîne. Ew hov e û cihên vekirî divê.» ||| "Come outside," he said. "The santuri isn't at home between four walls. It's wild and needs the open spaces."

Em derketin der. ||| We went out.
Stêr dibiriqîn. ||| The stars sparkled.
Riya Kadîzê ji aliyekî ezman bo aliyê din diherikî. ||| The Milky Way flowed from one side of the sky to the other.
Behr kef dikir. ||| The sea was frothing.
Em li ser keviran rûniştin û pêl pêyên me dialastin. ||| We sat down on the pebbles and the waves licked our feet.

«Çaxê tu bê pere yî, divê tu kêfa xwe bînî,» Zorba got. «Çi, em dev jê berdin? Were vir, santûrî!» ||| "When you're broke, you have to have a good time," said Zorba. "What, us give up? Come here, santuri!"

«Stranek Makedonî ji welatê xwe, Zorba,» min got. ||| "A Macedonian song of your own country, Zorba," I said.

«Stranek Kretî ji welatê te!» Zorba got. «Ez ê ji te re tiştek bibêjim ku li Kandiyayê hat hîn kirin; jiyana min guhert.» ||| "A Cretan song of your country!" said Zorba. "I'll sing you something I was taught at Candia; it changed my life."

Ew bo kêliyekê fikirî. ||| He reflected for a moment.

«Na, bi rastî nehat guhertin,» wî got, «tenê niha ez dizanim ku ez rast bûm.» ||| "No, it hasn't changed really," he said, "only now I know I was right."

Wî tiliyên xwe yên gewre danî ser santûrî û situyê xwe dirêj kir. ||| He placed his big fingers on the santuri and craned his neck.
Wî bi dengekî hov, hişk, bi keder stra: ||| He sang in a wild, harsh, dolorous voice:

##VERSE
Çaxê te biryara xwe da, fêde tune di paşvemanê de,<br>here pêş û tu nerm nebe;<br>bila xortaniya te serbest be, ew careke din nayê,<br>loma wêrek be û tu poşman nebe. ||| When you've made up your mind, no use lagging behind, go ahead and no relenting. Let your youth have free reign, it won't come again, so be bold and no repenting.

Xemên me belav bûn, derdên biçûk winda bûn, giyan gihîşt lûtkeya xwe. ||| Our cares were scattered, petty troubles vanished, the soul reached its peak.
Lola, komir, xet, «ebediyet», xemên mezin û biçûk, hemû bûn dûmaneke şîn ku di hewayê de winda bû, û tenê teyrekî ji pola ma, giyanê mirov ê ku distra. ||| Lola, lignite, the line, "eternity," big and small worries, all became blue smoke that faded into the air, and there remained only a bird of steel, the human soul which sang.

«Ez her tiştî diyarî te dikim, Zorba!» min qîriya, dema strana serbilind qediya. «Her tiştê ku te kiriye -- jin, porê te yê boyaxkirî, dravê ku te xerc kir -- hemû ya te ne! Tenê berdewam bike bi stranê!» ||| "I make you a present of everything, Zorba!" I cried, when the proud song was done. "All you've done -- the woman, your dyed hair, the money you spent -- all of it's yours! Just go on singing!"

Wî careke din situyê xwe yê jar dirêj kir: ||| He craned out his scraggy neck once more:

##VERSE
Cesaret! Bi navê Xwedê! Biwêre, çi bibe bila bibe!<br>Eger tu winda nekî, helbet tu yê serkevî! ||| Courage! In God's name! Venture, come what may! If you don't lose, you're bound to win the day!

Çend karkerên ku li nêzî kanê radizan dengê stranan bihîst; ew rabûn, bi dizî hatin xwarê ba me û li dora me çûçik rûniştin. ||| A number of workmen sleeping near the mine heard the songs; they got up, crept down to us and squatted round.
Wan li stranên xwe yên bijare guhdarî kir û hîs kirin ku lingên wan dilerizin. ||| They listened to their favorite songs and felt their legs tingling.
Di dawiyê de, êdî nikaribûn xwe bigirin, ew ji tariyê derketin, nîvtazî, porê wan tevlihev û şalên wan firefireh. ||| At last, unable to restrain themselves longer, they loomed out of the darkness, halfnaked, their hair ruffled and their breeches baggy.
Wan li dora Zorba û santûrî xelek girtin û li ser peravê ya bi keviran dest bi reqsê kirin. ||| They made a circle round Zorba and the santuri and began dancing on the pebbled shore.

Bi heyecan, min bê deng li wan temaşe kir. ||| Thrilled, I watched them in silence.

Ev e, min fikirî, damariya rast a ku ez li pey bûm! Ez tu ya din naxwazim. ||| This is, I thought, the real vein I have been looking for! I want no other.

Roja din, berî berbangê, dehlîzên kanê bi qîrînên Zorba û dengên kulinçan deng vedidan. ||| The next day, before dawn, the galleries of the mine were echoing with Zorba's cries and the sounds of the picks.
Mêr bi dîn dixebitîn. ||| The men were working frenziedly.
Zorba bi tena serê xwe dikaribû wan wisa bi pêş bixe. ||| Zorba alone could lead them on like that.
Pê re kar bû şerab, jin û stran, û mêr serxweş bûbûn. ||| With him work became wine, women and song, and the men were intoxicated.

##PG 116
Erd di destên wî de zindî bû, kevir, komir, dar û karker awazê wî qebûl kirin, cureyekî şer di dehlîzan de di ronahiya spî ya lempeyên asetîlênê de hat ragihandin û Zorba li pêş bû; dest bi dest şer dikir. ||| The earth came to life in his hands, the stones, coal, wood and workers adopted his rhythm, a sort of war was declared in the galleries in the white light of the acetylene lamps and Zorba was in the forefront; fighting hand to hand.
Wî navek da her dehlîz û damarê, û rûyek da hemû hêzên nedîtî, û piştî wê ji bo wan dijwar bû ku jê birevin. ||| He gave a name to each gallery and seam, and a face to all invisible forces, and after that it became difficult for them to escape him.

«Çaxê ez dizanim ku ew dehlîza ‹Kanavaro› ye,» wî digot derbarê dehlîza yekem a ku navê lê kiribû, «ew ê bi şeytanî li ku derê veşêre? Ez navê wê dizanim, ew ê newêre ku fêlê li min bike. Ne zêdetir ji ‹Dêya Manastîrê›, an ‹Çongkut›, an ‹Mîztînok›. Ez hemûyan dizanim, ez ji te re dibêjim, her yek bi navê xwe.» ||| "When I know that that is the 'Canavaro' gallery," he used to say about the first gallery he had christened, "where the hell do you think it can hide? I know its name, it wouldn't have the cheek to do the dirty on me. No more than 'Mother Superior,' or 'Knockknees,' or 'The Piddler.' I know them all, I tell you, each one by its own name."

Wê rojê ez bê ku ferq bike ketim dehlîzê. ||| That day I slipped into the gallery without his noticing me.

«Were de! Hinekî can têxê!» wî li karkeran diqîriya, wek ku her tim dikir dema di forma baş de bû. «Were de! Em ê hemû çiyê bixwin, hê! Em mêr in, ne wisa? Afirîdên ku divê mirov hesabê wan bike! Divê Xwedê bi xwe jî dema ku me dibîne bilerize! Hûn Kretî û ez, Makedonyayek, em ê vî çiyayî bigirin; ji çiyê bêtir divê ku me bişkîne! Me Tirk şikandin, ne wisa? Vêca çima divê çiyayekî wiha biçûk me bide sekinandin? Were de, hingê!» ||| "Come on! Put some life into it!" he was shouting to the workmen, as he always did when he was in good form. "Come on! We'll eat up the whole mountain, yet! We're men, aren't we? Creatures to be reckoned with! God himself must tremble when he sees us! You Cretans and me, a Macedonian, we'll have this mountain; it takes more than a mountain to beat us! We beat the Turks, didn't we? So why should a little mountain like this put us off? Come on, then!"

Yek bezî ber Zorba. ||| Someone ran up to Zorba.
Di ronahiya asetîlênê de min tenê dikaribû rûyê zirav ê Mîmîko fêm bikim. ||| In the acetylene light I could just make out Mimiko's thin face.

«Zorba,» wî bi dengê xwe yê mromromî got, «Zorba...» ||| "Zorba," he said in his mumbling voice, "Zorba..."

Zorba zivirî, û bi carekê dît ka mijar çi ye. ||| Zorba turned round, and saw at a glance what it was about.
Wî destê xwe yê mezin rakir: ||| He lifted his big hand:

«Bireve!» wî qîriya. «Wenda be!» ||| "Beat it!" he shouted. "Clear out!"

«Ez ji bo wê hatime...» ehmeq bi lerizî got. ||| "I've come for her..." faltered the simpleton.

«Wenda be, ez ji te re dibêjim! Karê me heye!» ||| "Clear out, I tell you! We've got work to do!"

Mîmîko bi lez wek ku lingên wî dikaribûn wî hilgirin reviya. ||| Mimiko made off as fast as his legs would carry him.
Zorba bi hêrs tif kir. ||| Zorba spat in exasperation.

«Roj ji bo kar e,» wî got. «Roj mêr e. Şev ji bo kêfê ye. Şev jin e. Divê tu wan tevlihev nekî!» ||| "The day's for working," he said. "Daytime is a man. The nighttime's for enjoying yourself. Night is a woman. You mustn't mix them up!"

Ez wê gavê hatim. ||| I came up at that moment.
«Saet donzdeh e,» min got. «Wext e ku tu dev ji kar berdî û tiştek bixwî.» ||| "It's twelve o'clock," I said. "Time you stopped work and had a meal."

Zorba zivirî, ez dîtim û birûyên xwe qermiçandin. ||| Zorba turned round, saw me and scowled.

«Li benda me nemîne, axa, eger tu li min nesekinî. Tu here û firavîna xwe bixwe. Me donzdeh roj winda kirine, bîne bîra xwe, û divê em xwe bigihînin. Ez hêvî dikim tu baş bixwî.» ||| "Don't wait for us, boss, d'you mind. You go and have your lunch. We've lost twelve days, remember, and we've got to catch up. I hope you eat well."

Ez ji dehlîzê derketim û ber bi behrê ve daketim. ||| I left the gallery and walked down towards the sea.
Min pirtûka ku pê re bû vekir. ||| I opened the book I was carrying.
Ez birçî bûm, lê min birçîbûna xwe ji bîr kir. ||| I was hungry, but I forgot my hunger.
Ramîn jî kanek e, min fikirî, vêca here pêş! ||| Meditation is also a mine, I thought, so go ahead!
Û ez ketim dehlîzên mezin ên hişê xwe. ||| And I plunged into the great galleries of the mind.

Pirtûkeke aloz: çiyayên Tîbetê yên bi berf nixumandî, manastîrên nepenî, keşîşên bêdeng ên di kincên xwe yên zafranî de ku vîna xwe berhev dikin û esîrê mecbûr dikin ku şiklê ku ew dixwazin bigire, dida nasîn. ||| A disturbing book: it described the snow-covered mountains of Tibet, the mysterious monasteries, the silent monks in their saffron robes who concentrate their will and oblige the ether to take what shape they desire.

Lûtkeyên çiyayên bilind, hewa tijî giyan. ||| High mountain tops, the air full of spirits.
Pistepista vala ya jiyana mirovan tu carî ewqas bilind nagihîje. ||| The vain murmur of human life never reaches so high.
Zahidê mezin şagirtên xwe digire, kurên şanzdeh heta hîjdeh salî, û nîvê şevê wan dibe ber gola cemidî ya li çiyê. ||| The great ascetic takes his pupils, boys of sixteen to eighteen, and leads them at midnight up to an icy lake in the mountain.
Ew cilên xwe derdixin, qeşayê dişkînin, cilên xwe dixin nav ava qerisî, dîsa li xwe dikin û dihêlin ku li ser pişta wan ziwa bibin. ||| They undress, break the ice, plunge their clothes into the freezing water, put them on again and leave them to dry on their backs.
Paşê wan ji nû ve dadixin nav avê, û dîsa dihêlin ku li ser laşên wan ziwa bibin. ||| Then they plunge them in afresh, and leave them to dry once more on their bodies.
Ew vê heft caran li pey hev dikin. ||| They do this seven times in succession.
Paşê ew vedigerin manastîrê ji bo ayîna sibehê. ||| Then they return to the monastery for morning service.

##PG 117
Ew hildikişin lûtkeyeke çiyê, pazdeh heta hîjdeh hezar ling bilind. ||| They climb a mountain peak, fifteen to eighteen thousand feet high.
Ew bi aramî rûdinin, kûr û birêkûpêk bêhna xwe distînin. ||| They sit down quietly, breathe deeply and regularly.
Ew heta navê tazî ne lê sermayê hîs nakin. ||| They are naked to the waist but feel no cold.
Ew kasek ava qeşayî di destên xwe de digirin, lê dinêrin, bi hemû hêza xwe li ser wê berhev dibin, û av dikele. ||| They hold a goblet of icy water in their hands, look at it, concentrate with all their power on it, and the water boils.
Paşê ew çaya xwe çêdikin. ||| Then they make their tea.

Zahidê mezin şagirtên xwe li dora xwe berhev dike û dibêje: ||| The great ascetic collects his students round him and says:

«Wey li wî yê ku di hundirê xwe de çavkaniya bextewariyê tune! ||| "Woe to him who has not within himself the source of happiness!
Wey li wî yê ku dixwaze kêfa hinên din bîne! ||| "Woe to him who wants to please others!
Wey li wî yê ku hîs nake ku ev jiyan û ya pêş tenê yek in!» ||| "Woe to him who does not feel that this life and the next are but one!"

Şev daketibû û min nikaribû bixwînim. ||| Night had fallen and I could not see to read.
Min pirtûk girt û li behrê nêrî. ||| I closed the book and looked at the sea.
Divê ez xwe ji van hemû xeyalan azad bikim, min fikirî, Bûda, Xwedê, Welat, Raman.... ||| I must free myself of all these phantoms, I thought, Buddhas, Gods, Motherlands, Ideas....
Wey li wî yê ku nikare xwe ji Bûda, Xwedê, Welat û Ramanan azad bike. ||| Woe to him who cannot free himself from Buddhas, Gods, Motherlands and Ideas.

Behr ji nişkê ve reş bûbû. ||| The sea had suddenly turned black.
Heyva nû bi lez diçû ava. ||| The young moon was rapidly setting.
Li baxçeyên dûr, kûçik bi xemgînî diqêriyan, û tevahiya geliyê bersiv dida. ||| In the gardens in the distance, dogs were howling sadly, and the whole ravine howled back.

Zorba xuya bû, bi qir nixumandî; kirasê wî perçe perçe daliqandî bû. ||| Zorba appeared, covered with dirt; his shirt was hanging in shreds.
Ew li ba min çûçik rûnişt. ||| He crouched by me.

«Îro pir baş çû,» wî bi kêfxweşî got; «gelek karê baş hat kirin.» ||| "It went very well today," he said happily; "plenty of good work done."

Min peyvên Zorba bê ku wateya wan bigirim bihîst. ||| I heard Zorba's words without grasping their meaning.
Hişê min hîn dûr li ser hêlanên dûr û xeternak bû. ||| My mind was still far away on distant and dangerous slopes.

«Tu li çi difikirî, axa?» wî ji min pirsî. «Ma hişê te li behrê ye?» ||| "What are you thinking of, boss?" he asked me. "Is your mind out at sea?"

Min hişê xwe vegerand, li Zorba zivirî nêrî û serê xwe hejand. ||| I brought my mind back, looked round at Zorba and shook my head.

«Zorba,» min got, «tu difikirî ku tu Sindibadê Deryavan ê ecêb î, û tu mezin diaxivî çimkî tu hinekî li dinyayê geriyayî. Lê te tiştek nedîtiye, qet tiştek. Tu tişt, ehmeqo belengaz! Ne ez jî, bala xwe bide. Dinya ji ya ku em difikirin pir firehtir e. Em rê diçin, welat û behran derbas dikin û lê me tu carî pozê xwe ji ber derê mala xwe derbasî der nekiriye.» ||| "Zorba," I said, "you think you're a wonderful Sinbad the Sailor, and you talk big because you've knocked about the world a bit. But you've seen nothing, nothing at all. Not a thing, you poor fool! Nor have I, mind you. The world's much vaster than we think. We travel, crossing whole countries and seas and yet we've never pushed our noses past the doorstep of our own home."

Zorba lêvên xwe çikand û tiştek negot. ||| Zorba pursed his lips and said nothing.
Wî tenê wek kûçikekî dilsoz dema lê tê xistin kûnirand. ||| He just grunted like a faithful dog when he is hit.

«Li dinyayê çiya hene,» min got, «ku gewre ne, mezin in û li seranserê wan manastîr belav bûne. Û di wan manastîran de keşîşên di kincên zafranî de dijîn. Ew rûdinin, bi lingên xaçkirî, ji bo mehekê, du, şeş mehan bi carê, li ser tiştekî û tenê tiştekî difikirin. Tiştek, tu dibihîzî? Ne du -- yek! Ew li jin û komirê an pirtûk û komirê nafikirin, wek ku em dikin; ew hişê xwe li ser yek û heman tiştî berhev dikin, û ew keramatan pêk tînin. Te dîtiye çi diqewime dema ku tu qedehekê li ber tavê digirî û hemû tîrêjan li ser yek xalê berhev dikî, Zorba? Ew xal zû dişewite, ne wisa? Çima? Çimkî hêza tavê belav nebûye lê li ser wê yek xalê berhev bûye. Bi hişê mirovan re jî heman tişt e. Tu keramatan dikî, eger tu hişê xwe li ser tiştekî û tenê yekî berhev bikî. Tu fêm dikî, Zorba?» ||| "There are mountains in the world," I said, "which are huge, immense and dotted all over with monasteries. And in those monasteries live monks in saffron robes. They stay seated, with crossed legs, for one, two, six months at a time, thinking of one thing and one thing only. One thing, do you hear? Not two -- one! They don't think of women and lignite or books and lignite, as we do; they concentrate their minds on one and the same thing, and they achieve miracles. You have seen what happens when you hold a glass out to the sun and concentrate all the rays onto one spot, Zorba? That spot soon catches fire, doesn't it? Why? Because the sun's power has not been dispersed but concentrated on that one spot. It is the same with men's minds. You do miracles, if you concentrate your mind on one thing and only one. Do you understand, Zorba?"

Zorba bi giranî bêhna xwe distand. ||| Zorba was breathing heavily.
Bo kêliyekê ew xwe hejand wek ku dixwest bireve, lê xwe kontrol kir. ||| For a moment he shook himself as though he wanted to run away, but he controlled himself.

«Berdewam bike,» wî bi dengekî xeniqandî kûnirand. ||| "Go on," he grunted, in a strangled voice.

Paşê ew yekser hilpekiya. ||| Then he straightway leaped up.

«Devê xwe bigir! Devê xwe bigir!» wî qîriya. «Çima tu vê ji min re dibêjî, axa? Çima tu hişê min jehrî dikî? Ez li vir baş bûm, çima tu min aciz dikî? Ez birçî bûm, û Xwedê û şeytan (ez nifirî bim eger ez cudahiyê bibînim) hestiyek avêtin min û min ew dialast. Ez dûvê xwe dihejand û diqîriyam: ‹Spas! Spas!› Û niha...» ||| "Shut up! Shut up!" he shouted. "Why are you saying this to me, boss? Why are you poisoning my mind? I was all right here, why are you upsetting me? I was hungry, and God and the devil (I'm damned if I can see the difference) threw me a bone and I was licking it. I was wagging my tail and shouting: 'Thank you! Thank you!' And now..."

##PG 118
Wî lingê xwe li erdê xist, pişta xwe zivirand, tevgerek kir wek ku ber bi koxikê ve diçe, lê hîn di hundir de dikeland. ||| He stamped his foot, turned his back, made a move as if he were going over to the hut, but he was still boiling inside.
Ew sekinî. ||| He stopped.

«Pff! Hestiyekî xweş bû ku wî avêt min, ew xwedê-şeytan!» wî borand. «Qehpeke pîr a kabareyê! Qeyikeke kevn ku êdî nikare biçe behrê jî!» ||| "Pff! A fine bone it was he threw me, that god-devil!" he roared. "A dirty old cabaret tart! An old tub that isn't even seaworthy!"

Wî mistek kevir girt û avêtin behrê. ||| He seized a handful of pebbles and threw them into the sea.

«Lê ew kî ye? Kî ye yê ku van hestiyan diavêje me? Hê?» ||| "But who is he? Who is it who throws these bones to us? Eh?"

Ew hinekî sekinî, paşê dema hîs kir ku tu bersiv nayê ew bi heyecan ket. ||| He waited a little, then when he felt no reply was coming he became excited.

«Ma tu nikarî tiştekî bibêjî, axa?» wî qîriya. «Eger tu dizanî, ji min re bibêje, da ku ez navê wî bizanim. Hingê, xem neke, ez ê lê binêrim! Lê eger ew tenê bi şens be, wisa, ez ê kîjan alî biçim? Ez ê bikevim belayê.» ||| "Can't you say anything, boss?" he cried. "If you know, tell me, so that I know his name. Then, don't you worry, I'll look after him! But if it's just on the off-chance, like that, which way must I go? I'll come to grief."

«Ez birçî me,» min got. «Here û hin xwarin bîne. Em pêşî bixwin!» ||| "I'm hungry," I said. "Go and get some food. Let's eat first!"

«Ma em nikarin êvarekê bê xwarin derbas bikin, axa? Yek ji apên min keşîş bû, û rojên hefteyê tenê xwê û av distand. Roja yekşemê û rojên cejnê hinekî kepek lê zêde dikir. Ew jiya heta sed û bîst salî.» ||| "Can't we last an evening without eating, boss? One of my uncles was a monk, and weekdays he took nothing but salt and water. On Sundays and feast days he added a bit of bran. He lived to be a hundred and twenty."

«Ew jiya heta sed û bîst salî, Zorba, çimkî baweriya wî hebû. Wî Xwedayê xwe dîtibû û xema wî tunebû. Lê me Xwedayê ku me xwedî bike tune, Zorba, loma êgir vêxe, kerem ke, û em ê wan masiyan bipijînin. Şorbeyeke stûr û germ bi gelek pîvaz û îsotê çêke, ji cûreya ku em jê hez dikin. Paşê em ê bibînin.» ||| "He lived to be a hundred and twenty, Zorba, because he had faith. He had found his God and he had no worries. But we have no God to nourish us, Zorba, so light the fire, will you, and we'll cook those chads. Make a thick, hot soup with plenty of onions and pepper, the sort we like. Then we'll see."

«Çi bibînin?» Zorba bi hêrs pirsî. «Hema ku zikê me tije bibe em ê wan hemûyan ji bîr bikin!» ||| "See what?" asked Zorba in a rage. "As soon as our bellies are full we shall forget all that!"

«Tam wisa! Ev e ya ku xwarin bi rastî jê re ye, Zorba. Êdî, here û şorbeyeke masî ya baş çêke da ku serê me neteqe!» ||| "Exactly! That's what food's really for, Zorba. Now then, off you go and make a good fish soup so that our heads don't burst!"

Lê Zorba neliviya. ||| But Zorba didn't budge.
Ew li cihê xwe ma, bêliv, li min dinêrî. ||| He stayed where he was, motionless, looking at me.

«Guhdarî bike, axa, ez dixwazim tiştek ji te re bibêjim. Ez dizanim tu li pey çi yî. Hema niha dema ku tu bi min re diaxivî ji nişkê ve tiştek hat hişê min; min hemû di çirkekê de dît.» ||| "Listen, boss, I want to tell you something. I know what you're up to. Just now when you were talking to me I suddenly had an inkling; I saw it all in a flash."

«Ez li pey çi me, Zorba?» min bi meraq pirsî. ||| "What am I up to, Zorba?" I asked, intrigued.

«Tu dixwazî manastîrekê ava bikî. Ev e! Li şûna keşîşan tu yê çend qelemajoyên wek cenabê xwe bixî hundir û ew ê wextê xwe bi nivîsandina roj û şev derbas bikin. Paşê, wek pîrozên di wêneyên kevn de, şeritên çapkirî yên dirêj ê ji devê we bigindirin der. Min rast texmîn kir, ne wisa?» ||| "You want to build a monastery. That's it! Instead of monks you'd stick a few quill drivers like your honored self inside and they'd pass the time scribbling day and night. Then, like the saints in the old pictures, printed ribbons would come rolling out of your mouths. I've guessed right, haven't I?"

Min serê xwe bi xemgînî daxist. ||| I hung my head, saddened.
Xewnên kevn ên xortaniya min, baskên gewre yên ku perên xwe winda kirine, hestên sade, esîl, comerd.... ||| Old dreams of my youth, huge wings that have lost their feathers, naive, noble, generous impulses....

Civakeke rewşenbîrî ava bike û xwe li wir veşêre; deh-donzdeh heval -- mûzîkjen, helbestvan, neqaş.... ||| Build an intellectual community and bury ourselves there; a dozen friends -- musicians, poets, painters....
Tevahiya rojê kar bike, tenê bi şev hev bibîne, bixwe, bistirê, bi hev re bixwîne, pirsgirêkên mezin ên mirovahiyê gengeşe bike, bersivên kevneşopî hilweşîne. ||| Work all day, meet only at night, eat, sing, read together, discuss the great problems of humanity, demolish the traditional answers.
Min jixwe rêzikên civakê amade kiribûn. ||| I had worked out the rules of the community already.
Min tewra avahî jî di yek ji dergehên Çiyayê Hîmetosê de, li ba Yûhennayê Nêçîrvan, dîtibû. ||| I had even found the building in one of the passes of Mount Hymettus, at St. John the Hunter.

«Min ew baş texmîn kir,» Zorba bi kêfxweşî got, dema dît ku ez bêdeng mam. «Baş e, ez ê ji te lavayekê bixwazim, abûnê pîroz: ez dixwazim tu min bikî dergehvanê manastîra xwe da ku ez hinekî qaçaxçîtiyê bikim û, carna, hin tiştên pir ecêb derbasî hundirê hewşa pîroz bikim: jin, mandolîn, kûpên mezin ên araqê, berazên şîrmij ên biraştî.... Hemû ji bo ku tu jiyana xwe bi gelek qerfan winda nekî!» ||| "I've guessed it right enough," said Zorba happily, when he saw I remained silent. "Well, I'm going to ask you a favor, holy abbot: I want you to appoint me doorkeeper to your monastery so that I can do some smuggling and, now and then, let some very strange things through into the holy precincts: women, mandolins, demijohns of raki, roast sucking pigs.... All so that you don't fritter away your life with a lot of nonsense!"

Ew keniya û bi lez ber bi koxikê ve çû. ||| He laughed and went quickly towards the hut.
Ez bezîm li pey wî. ||| I ran after him.

##PG 119
Wî masî paqij kirin, bê ku devê xwe veke, dema ku min dar anî û êgir vêxist. ||| He cleaned the fish, without opening his mouth, while I fetched wood and lit the fire.
Hema ku şorbe amade bû, me kefçiyên xwe girtin û rasterast ji tencerê dest bi xwarinê kir. ||| As soon as the soup was ready, we took our spoons and began eating straight out of the pot.

Tu ji me neaxivî. ||| Neither of us spoke.
Tevahiya rojê me tu loqme nexwaribû û me herduyan bi çavbirçîtî xwar. ||| We had not had a bite all day and we both ate ravenously.
Me hinek şerab vexwar û ruhê me baştir bû. ||| We drank some wine and our spirits improved.

Zorba di dawiyê de devê xwe vekir. ||| Zorba opened his mouth at last.

«Dê xweş bûya ku Madam Bûbûlîna niha xuya bibe, axa. Wext dê ji bo hatina wê baş bûya, lê Xwedê me biparêze! Ew ê bibûya derba dawî. Û dîsa jî tu dizanî, axa, ez bêriya wê kiriye, şeytan wê bibe!» ||| "It would be fun to see Dame Bouboulina turn up now, boss. It would be a good moment for her to come, but God preserve us! She'd be the last straw. And yet you know, boss, I've missed her, devil take her!"

«Ma tu ji min napirsî kî ew hestiyê biçûk ê taybetî avêt te, ne wisa?» ||| "You aren't asking me who threw you that particular little bone, are you?"

«Ji te re çi, axa? Ew wek kêçekê di komeke kayê de ye.... Hestî bigire û xema wî neke ka kî ew avêtiye xwarê ji te re. Ma bi tam e? Ma goşt lê heye? Ev in pirsên ku divê mirov bipirse. Ya mayî hemû...» ||| "What do you care, boss? It's like a flea in a haystack.... Take the bone and don't worry about who threw it down to you. Is it tasty? Is there any flesh on it? Those are the questions to ask. All the rest is...."

«Xwarinê keramata xwe ya ecêb kir!» min got, lê pişta wî dixist. «Laşê birçî aram bû... û ji ber vê yekê giyanê ku pirsan dikir jî aram bû. Santûriya xwe bîne!» ||| "Food has worked its wondrous miracle!" I said, slapping him on the back. "The famished body is calmed... and so the soul that was asking questions has calmed down, too. Get your santuri!"

Lê hema ku Zorba rabû ser xwe me dengên gavên lez û giran li ser keviran bihîst. ||| But just as Zorba stood up we heard quick, heavy steps on the pebbles.
Difnên Zorba yên pirçdar lerizîn. ||| Zorba's hairy nostrils quivered.

«Behsa şeytan...» wî bi dengekî nizm got, li ranên xwe dixist. «Va ye ew tê! Delê bêhna Zorbayekê di hewayê de girtiye, û va ye ew tê.» ||| "Speak of the devil...." he said in a low voice, slapping his thighs. "Here she is! The bitch has scented a Zorba smell in the air, and here she comes."

«Ez diçim,» min got, radibûm. «Ez naxwazim tu têkiliya min bi vê re hebe. Ez ê hinekî derkevim der. Ev ya te.» ||| "I'm off," I said, rising. "I don't want anything to do with this. I'll go out for a bit. I leave this to you."

«Şev baş, axa.» ||| "Good night, boss."

«Û ji bîr neke, Zorba. Te soz da ku tu yê wê bizewicî.... Min derewîn dernexe.» ||| "And don't forget, Zorba. You promised to marry her.... Don't make me a liar."

Zorba axîn kişand. ||| Zorba sighed.

«Dîsa bizewicim, axa? Min zikê xwe pê tije kiriye!» ||| "Marry again, boss? I've had my bellyful!"

Bêhna sabûna tuwaletê nêzîktir dibû. ||| The scent of toilet soap was coming nearer.

«Wêrekî, Zorba!» ||| "Courage, Zorba!"

Ez bi lez derketim. ||| I left quickly.
Li derve, min jixwe dikaribû bêhnvedana hilkişandî ya sîrena pîr bibihîzim. ||| Outside, I could already hear the panting breath of the old siren.
"""

CH17 = r"""
##PG 119
##FIRST
ROJA PIŞTÎ wê, di berbangê de, dengê Zorba ez ji xewê hişyar kirim. ||| THE NEXT DAY at dawn Zorba's voice woke me from sleep.

«Çi bi te hatiye ku tu ewqas zû radibî? Ev hemû qêrîn ji bo çi ye?» ||| "What's got into you so early in the morning? Why all this shouting?"

«Divê em tiştan bi ciddî bigirin, axa,» wî bersiv da, dema ku tûrikê xwe bi xwarinê tije dikir. ||| "We have to take things seriously, boss," he answered, filling his haversack with food.
«Min du hêstir anîne; rabe, em ê herin keşîşxaneyê û kaxezên rêya têlê bidin îmze kirin.» ||| "I've brought two mules; get up and we'll go to the monastery and have the papers signed for the cable railway."
«Tenê tiştek heye ku şêrekî ditirsîne, ew jî sipîk e.» ||| "There's only one thing makes a lion afraid and that's a louse."
«Sipî dê me hemûyan bixwin, axa.» ||| "The lice will eat us all up, boss."

«Çima tu ji wê Bûbûlîna belengaz re dibêjî sipî?» min bi kenê jê pirsî. ||| "Why call that poor Bouboulina a louse?" I asked him with a laugh.

Lê Zorba xwe wisa nîşan da ku nebihîstiye. ||| But Zorba pretended he had not heard.

«Were,» wî got, «berî ku roj pir bilind bibe.» ||| "Come on," he said, "before the sun is too high."

Bi rastî ez pir kêfxweş bûm ku ez ê hilkişim çiyan û ji bêhna darên kajê kêfê bigirim. ||| I was really very glad to go up into the mountains and enjoy the smell of the pine trees.
Em li ser sewalan siwar bûn û dest bi hilkişînê kirin, bo kêliyekê li ber kanê sekinîn, li wir Zorba çend talîmat dan karkeran. ||| We mounted our beasts and began the ascent, halting for a moment at the mine where Zorba gave some instructions to the workmen.

##PG 120
Wî ji wan re got ku li «Dayika Mezin» bixebitin, kortala «Mîzok» bikolin û «Kanavaro» paqij bikin. ||| He told them to work at the "Mother Superior," to dig out the trench in "The Piddler" and clean out the "Canavaro."

Roj wek almasekî ji zelaltirîn cûr dibiriqî. ||| The day shone like a diamond of the first water.
Em çiqas bilindtir diçûn, ruhê me ewqas zêdetir paqij û bilind dibû. ||| The higher we went, the more our spirits seemed to become purged and exalted.

Careke din min bandora hewaya paqij, bêhnstandina hêsan û asoyeke fireh li ser ruh hîs kir. ||| Once again I felt the influence on the soul of pure air, easy breathing and a vast horizon.
Mirov dê bifikiriya ku ruh jî heywanek e bi cger û bêvilan, û ku pêdiviya wê bi oksîjenê heye, di tozê de an di nav pir bêhna genî de difetise. ||| Anyone would think the soul, too, was an animal with lungs and nostrils, and that it needed oxygen, was stifled in the dust or in the midst of too much stale breath.

Roj jixwe bilind bû dema ku em ketin nav daristana kajan. ||| The sun was already high when we entered the pine forest.
Hewa li wir bêhna hingiv dida, ba li jor me dixist û wek deryayê dixuşiya. ||| The air there smelled of honey, the wind was blowing above us and soughed like the sea.

Di rê de Zorba li bejna çiyê dinerî. ||| During the trek Zorba studied the slope of the mountainside.
Di xeyala xwe de ew her çend metroyan stûnan dikutan erdê, û dema çavên xwe bilind dikir, ew jixwe dikaribû têlê bibîne ku di tavê de dibiriqî û rast diçû xwarê heta peravê. ||| In his imagination he was driving in piles every so many yards, and when he raised his eyes he could already see the cable shining in the sun and running right down to the shore.
Bi têlê ve girêdayî, qurmên daran ên birîn dadiketin, wek tîrên ji kevanê fîk dikişandin. ||| Attached to the cable the felled tree trunks descended, whistling along like arrows from a bow.

Wî destên xwe li hev midland: ||| He rubbed his hands together:

«Çi xweş!» wî got. ||| "Capital!" he said.
«Ev ê bibe kaneke zêrî! Em ê di demek nêz de di nav pereyan de bigevizin, û em ê her tiştê ku me got bikin.» ||| "This'll be a gold mine! We'll soon be rolling in money, and we can do all we said."

Min bi heyranî lê nêrî. ||| I looked at him in astonishment.

«Hê! Nebêje ku te jixwe ji bîr kiriye! Berî ku em keşîşxaneya te ava bikin, em ê hilkişiyana çiyayê mezin. Navê wî çi ye?» ||| "Hm! Don't tell me you've forgotten already! Before we built your monastery, we were going up the great mountain. What's its name?"

«Tîbet, Zorba, Tîbet. Lê tenê em herdu. Tu nikarî jinan bibî wir.» ||| "Tibet, Zorba, Tibet. But only the two of us. You can't take women there."

«Kê behsa birina jinan kir? Mexlûqên belengaz bi her hal pir bikêrhatî ne, loma tu tiştî li dijî wan nebêje; pir bikêrhatî ne, dema ku zilamek tu karê mêran nebe ku bike, wek birîna komirê, girtina bajaran bi êrîşê an axaftina bi Xwedê re.» ||| "Who mentioned taking women? The poor creatures are very useful, anyway, so don't say anything against them; very useful, when a man hasn't got any man's work to do, such as cutting coal, taking towns by assault or talking to God."
«Wê demê ji wî re çi maye ku bike, eger ew ê neteqe? Ew şerab vedixwe, zar dilîze, an destên xwe li dora jinekê dixe... û li benda xwe disekine... li benda hatina seetê ye -- eger were.» ||| "What else is there for him to do, then, if he isn't going to burst? He drinks wine, plays dice, or puts his arms round a woman... and he waits... waits for his hour to come -- if it is coming."

Ew bo kêliyekê bêdeng ma. ||| He was silent for a moment.

«Eger were,» wî bi awayekî aciz dubare kir, «ji ber ku dibe ku qet neyê.» ||| "If it is coming," he repeated, in an irritated tone, "because it might never come at all."

Û piştî kêliyekê: ||| And a moment later:

«Wisa nikare bidome, axa; an dinya dê biçûktir bibe an ez ê mecbûr bim mezintir bibim. Wekî din ez xilas im!» ||| "It can't just go on like this, boss; either the world will have to get smaller or I shall have to get bigger. Otherwise I'm done for!"

Keşîşek di nav kajan de xuya bû, por sor û rû zer, mil hildayî, kumekî gilover ê ji hirî yê malê li serî. ||| A monk appeared between the pines, redhaired and yellow complexioned, his sleeves rolled up, a round homespun cap on his head.
Wî gopalekî hesinî hilgirtibû ku pê li erdê dixist dema ku gav diavêt. ||| He was carrying an iron rod with which he struck the ground as he strode along.
Dema ku ew em dîtin, ew sekinî û gopalê xwe hildan hewayê. ||| When he saw us he stopped and raised his stick in the air.

«Hûn diçin ku derê?» wî pirsî. ||| "Where are you going?" he asked.

«Bo keşîşxaneyê,» Zorba bersiv da; «em ê herin dua bikin.» ||| "To the monastery," Zorba replied; "we're going to say our prayers."

«Vegerin, filehno!» keşîş qîriya, çavên wî yên şîn ên zelal dema diaxivî gur dibûn. ||| "Turn back, Christians!" cried the monk, his clear blue eyes growing inflamed as he spoke.
«Vegerin, eger hûn şîreta min bigirin! Ne rezê Meryemê ye ku hûn ê li wir bibînin, lê baxçeyê Şeytên!» ||| "Turn back, if you'll take my advice! It is not the Virgin's orchard you'll find there, but the garden of Satan!"
«Hejarî, dilnizmî, paqijî... tac a keşîşan, wek ku dibêjin! Pir gengaz e.» ||| "Poverty, humility, chastity... the monk's crown, as they say! Very likely."
«Vegerin, ez ji we re dibêjim. Pere, pozbilindî û kurên ciwan! Ev e Sêyemeniya wan a Pîroz!» ||| "Go back, I tell you. Money, pride, and young boys! That's their Holy Trinity!"

«Ev zilam henekçî ye,» Zorba bi kêf pistepist kir. Ew ber bi wî ve xwar bû. ||| "He's a comic, this chap," whispered Zorba, enchanted. He leaned towards him.

«Navê te çi ye, bira?» wî ji keşîş pirsî. «Û tu ji ku derê tê?» ||| "What's your name, brother?" he asked the monk. "And where do you come from?"

«Navê min Zaharya ye. Min tiştên xwe berhev kirine û ez ê herim!» ||| "My name is Zaharia. I've packed up my things and I'm off!"

##PG 121
«Niha, vê gavê. Ez êdî nikarim li ber bidim! Ji kerema xwe navê xwe ji min re bêje, hevwelatî.» ||| "Right away. I can't bear it any longer! Kindly tell me your name, countryman."

«Kanavaro.» ||| "Canavaro."

«Ez êdî nikarim li ber bidim, birayê Kanavaro. Tevahiya şevê Îsa dinale û nahêle ez razêm. Û ez jî pê re dinalim.» ||| "I can't endure it any longer, brother Canavaro. All night long Christ moans and prevents me sleeping. And I moan with him."
«Paşê serkeşîş -- bila heta hetayê di agirê dojehê de bişewite -- vê sibê zû şand pey min.» ||| "Then the abbot -- may he roast in hell-fire forever -- sent for me early this morning."

«‹Baş e, Zaharya,› wî got. ‹Ji ber vê, tu nahêlî birayên te yên keşîş razên. Ez ê te bavêjim der.›» ||| "'Well, Zaharia,' he said. 'So, you won't let your brother monks sleep. I'm going to throw you out.'"

«‹Ez nahêlim ew razên?› min got. ‹Ez? An Îsa? Ew e yê ku timî dinale.›» ||| "'I won't let them sleep?' I said. 'I won't? Or Christ won't? He's the one who keeps moaning.'"

«Paşê wî xaça xwe hilda, ew dijî-Îsa, û, baş e... binêre!» ||| "Then he raised his cross, that anti-Christ, and, well... look!"

Wî kumê xwe yê keşîşî hilanî û perçeyek xwîna meyaxisî di porê xwe de nîşan da. ||| He took off his monk's cap and revealed a patch of congealed blood in his hair.

«Loma min toza wî cihî ji solên xwe vêda û çûm.» ||| "So I shook the dust of the place from my shoes and left."

«Bi me re vegere keşîşxaneyê,» Zorba got. «Ez ê serkeşîş razî bikim. Were, tu dikarî bibî hevalê me û rê nîşanî me bidî. Tu ji ezmên bi xwe hatî şandin.» ||| "Come back to the monastery with us," said Zorba. "I'll get round the abbot. Come on, you can keep us company and show us the way. You've been sent by heaven itself."

Keşîş bo kêliyekê fikirî. Çavên wî biriqîn. ||| The monk thought for a moment. His eyes shone.

«Tu yê çi bidî min?» wî pirsî. ||| "What will you give me?" he asked.

«Tu çi dixwazî?» ||| "What do you want?"

«Du lîbre masiyê şor û şûşeyek brendî.» ||| "Two pounds of salt cod and a bottle of brandy."

Zorba ber bi wî ve xwar bû û lê nêrî. ||| Zorba leaned forward and looked at him.

«Dibe ku bi tesadufî cûreyek şeytan di hundirê te de hebe, ne wisa, Zaharya?» ||| "You wouldn't by any chance have a sort of devil inside you, would you, Zaharia?"

Keşîş ji nişkê ve hejiya. ||| The monk started.

«Te çawa texmîn kir?» wî bi heyranî pirsî. ||| "How did you guess?" he asked in amazement.

«Ez bi xwe ji Çiyayê Atosê têm,» Zorba bersiv da. «Ez tiştekî li ser dizanim.» ||| "I come from Mount Athos myself," answered Zorba. "I know something about it."

Keşîş serê xwe berjêr kir. Em bi zorê dikaribûn bersiva wî bibihîzin. ||| The monk hung his head. We could scarcely hear his reply.

«Erê, di hundirê min de şeytanek heye.» ||| "Yes, I have a devil inside me."

«Û ew ê masiyê şor û brendiyê bixwaze, ne wisa?» ||| "And he'd like some salt cod and brandy, would he?"

«Erê, sê caran lanetkirî ku ew e!» ||| "Yes, thrice damned as he is!"

«Baş e! Çêbû! Ma ew cixareyê jî dikişîne?» ||| "All right! Done! Does he smoke as well?"

Zorba cixareyek avêt wî û keşîş bi çavbirçîtî ew girt. ||| Zorba threw him a cigarette and the monk seized it eagerly.

«Ew dikişîne, erê, ew dikişîne, bela lê bê!» wî got. ||| "He smokes, yes, he smokes, plague on him!" he said.

Û wî kevirekî biçûk ê agir û perçeyek fitîlê ji berîka xwe derxist, cixare pêxist û bi kûrahî kişand. ||| And he took a small flint and a piece of wick from his pocket, lit the cigarette and inhaled deeply.

«Bi navê Îsa!» wî got. ||| "In Christ's name!" he said.

Wî gopalê xwe yê hesinî hilda, zivirî û bi rê ket. ||| He raised his iron rod, turned about face and started off.

«Navê şeytanê te çi ye?» Zorba pirsî, çavê xwe li min girt. ||| "What's your devil's name?" asked Zorba, winking at me.

«Yûsiv!» Zaharya bersiv da, bê ku serê xwe bizivirîne. ||| "Joseph!" answered Zaharia, without turning his head.

Hevaltiya vî keşîşê nîv-dîn qet li dilê min nebû. ||| This half-crazed monk's company was not at all to my taste.
Aqlê nexweş, wek laşê nexweş, di min de hem dilovanî û hem jî di heman demê de nefret çêdike. ||| A sick mind, like a sick body, makes me feel compassion, and at the same time disgust.
Lê min tiştek negot; min hişt ku Zorba tiştê ku dixwaze bike. ||| But I said nothing; I left it to Zorba to do what he liked.

Hewaya zelal û paqij em birçî kirin û em li bin dareke kajê ya dêw rûniştin û tûrik vekir. ||| The clear pure air made us hungry and we sat down beneath a giant pine tree and opened the haversack.
Keşîş ber bi pêş ve xwar bû û bi birçîtî tê de nêrî da ku bibîne çi tê de heye. ||| The monk leaned forward and hungrily peered into it to see what it contained.

##PG 122
«Ne ewqas zû!» Zorba qîriya. «Lêvên xwe ewqas zû nelês, Zaharya! Îro Duşemiya Pîroz e.» ||| "Not so fast!" cried Zorba. "Don't lick your chops too soon, Zaharia! It's Holy Monday today."
«Em farmason in, loma em ê hin goşt û mirîşk bixwin, Xwedê me biborîne! Lê binêre, hin helva û çend zeytûn ji bo zikê te yê pîroz heye!» ||| "We are freemasons, so we shall eat some meat and chicken, God forgive us! But look, there's some halva and a few olives for your own saintly stomach!"

Keşîş riha xwe ya qirêj mizda. ||| The monk stroked his filthy beard.

«Ez ê zeytûn û nan û ava sar bixwim,» wî bi poşmanî got. ||| "I will have olives and bread and fresh water," he said with contrition.
«Lê Yûsiv şeytanek e, ew ê bi we re goşt bixwe, birano; ew ji mirîşkê hez dike -- ax, ew ruhekî windabûyî ye -- û ew ê ji kûzika we şerabê vexwe!» ||| "But Joseph's a devil, he will eat meat with you, brothers; he likes chicken -- oh, he's a lost soul -- and he'll drink wine from your gourd!"

Wî xaç çêkir, nan, zeytûn û helva daqurtand, devê xwe bi pişta destê xwe paqij kir, av vexwar, û paşê dîsa xaç li xwe kir, mîna ku xwarina xwe qedandibe. ||| He made the sign of the cross, swallowed the bread, olives and halva, wiped his mouth with the back of his hand, drank the water, and then crossed himself again as if he had finished his meal.

«Niha,» wî got, «dora Yûsiv e, ew ruhê belengaz ê sê caran lanetkirî.» ||| "Now," he said, "it's Joseph's turn, the poor thrice-damned soul."

Û wî xwe avêt ser mirîşkê. ||| And he threw himself on the chicken.

«Bixwe, ey ruhê windabûyî!» wî bi hêrs di bin lêv de got, dema ku perçeyên mezin ên mirîşkê dixiste devê xwe. «Bixwe!» ||| "Eat, you lost soul!" he mumbled furiously as he rammed great lumps of chicken into his mouth. "Eat!"

«Hûra! Aferîn, keşîş!» Zorba bi coş qîriya. «Du têl li kevanê te hene, ez dibînim.» ||| "Hoorah! Good for you, monk!" shouted Zorba enthusiastically. "You've got two strings to your bow, I can see."

Ew zivirî ber bi min. ||| He turned to me.

«Tu li ser wî çi difikirî, axa?» ||| "What do you think of him, boss?"

«Ew pir dişibe te,» min bi kenê got. ||| "He's very like you," I said with a laugh.

Zorba kûzika şerabê da keşîş. ||| Zorba gave the monk the wine gourd.

«Yûsiv! Vexwe!» ||| "Joseph! Have a drink!"

«Vexwe! Ey ruhê windabûyî!» keşîş got, şûşê girt û li devê xwe da. ||| "Drink! You lost soul!" said the monk, seizing the bottle and clapping it to his mouth.

Roj pir germ bû û em hê zêdetir çûn nav siyê. ||| The sun was very hot and we moved further into the shade.
Keşîş bêhna xwêdana tirş û bixûrê dida. ||| The monk reeked of sour sweat and incense.
Ew hema hema di tavê de dihelya û Zorba ew kişand cihê herî bisî da ku bêhnê kêm bike. ||| He almost ran liquid in the sun and Zorba dragged him to the shadiest spot to reduce the stench.

«Tu çawa bûyî keşîş?» Zorba pirsî, yê ku baş xwaribû û dixwest qise bike. ||| "How did you become a monk?" asked Zorba, who had eaten well and wanted to gossip.

Keşîş bişirî. ||| The monk grinned.

«Ez texmîn dikim tu difikirî ji ber ku ez ewqas pîroz im? Na, qet! Bi rêya hejariyê bû, bira, hejariyê!» ||| "I suppose you think it was because I'm so saintly? You bet! It was through poverty, brother, poverty!"
«Tu tiştê min nedima ku bixwim, loma min ji xwe re got: eger ez biçim keşîşxaneyê, ez nikarim ji birçîna bimirim!» ||| "I had nothing left to eat, so I said to myself: if I go into a monastery, I can't starve!"

«Û tu razî yî?» ||| "And are you satisfied?"

«Şikir ji Xwedê re! Ez gelek caran dinalim û gilî dikim lê tu guh nede wê.» ||| "God be praised! I sigh and complain often enough but don't you pay any attention to that."
«Ez ji bo tiştên dinyayî nanalim; bi ya min ew dikarin herin û bibin... min biborîne... û ez her roj ji wan re dibêjim herin û bibin.... Lê ez bêriya ezmên dikim!» ||| "I don't sigh for earthly things; as far as I'm concerned they can go and be... forgive me... and I tell them every day to go and be.... But I long for heaven!"
«Ez henekan dikim û li dora derê dans dikim û keşîşan didim kenandin.» ||| "I tell jokes and cut capers about the place and make the monks laugh."
«Ew hemû dibêjin şeytan di min de ye û min biçûk dixin. Lê ez ji xwe re dibêjim: ‹Ev nikare rast be; divê Xwedê ji henek û kenê hez bike.›» ||| "They all say I'm possessed by the devil and insult me. But I say to myself: 'It can't be true; God must like fun and laughter.'"
«‹Were hundir, ey henekçiyê min ê biçûk, were hundir,› ew ê rojekê ji min re bibêje, ez dizanim. ‹Were û min bide kenandin!›» ||| "'Come inside, my little buffoon, come inside,' he'll say to me one day, I know. 'Come and make me laugh!'"
«Bi vî awayî ez ê bikevim Bihiştê, wek henekçiyek!» ||| "That's the way I'll get into Paradise, as a buffoon!"

«Serê te li cihê rast e, ey kalo!» Zorba got, dema rabû ser xwe. «Were, divê em rabin rê, da ku tarî me negire.» ||| "You've got your head screwed on the right way, old fellow!" said Zorba, standing up. "Come on, we must make a move, so that we don't get caught by the dark."

Keşîş dîsa pêş ket. ||| The monk went ahead again.
Dema em hilkişiyan çiyê, min hîs kir ku em li ser zincîreyên hişê di hundirê min de difirikîn, ji xemên nizm û biçûk ber bi yên hêja, ji rastiyên rehet ên deştan ber bi têgînên asê. ||| As we climbed the mountain I felt we were clambering over ranges of the mind within me, passing from base and petty cares to nobler ones, from the comfortable truths of the plains to precipitous conceptions.

##PG 123
Ji nişkê ve keşîş sekinî. ||| Suddenly the monk stopped.

«Meryema Tolhildanê!» wî qîriya, îşaret bi dêrokeke biçûk a bi qubeyeke spehî kir. ||| "Our Lady of Revenge!" he cried, pointing to a small chapel with a graceful dome.
Ew ket ser çokan û xaç çêkir. ||| He sank to his knees and made the sign of the cross.
Ez ji sewalê peya bûm û ketim hundirê wê perestgeha sar. ||| I dismounted and entered the cool oratory.
Li quncikekî îkoneke kevn hebû, ji dûyê reş bûyî û bi diyariyên nezirî nixumandî: pelên zirav ên zîvîn ku li ser wan bi awayekî hişk şeklên ling, dest, çav û dilan hatibûn neqişandin.... ||| In one corner was an old icon, black with smoke and covered with votive offerings: thin sheets of silver on which had been crudely engraved figures of feet, hands, eyes, hearts....
Şamdaneke zîvîn li ber îkonê bû ku ronahiyeke her dem vêketî digirt. ||| A silver candlestick stood before the icon holding an ever-burning light.

Ez bê deng nêzîk bûm: madoneyeke hov û şerker, bi stûyekî bihêz û nihêrîna hişk û bêhêvî ya keçeke keç, di destê xwe de ne pitika pîroz, lê rimekeke dirêj û rast digirt. ||| I approached in silence: a fierce, warlike madonna with a strong neck and the austere, uneasy look of a virgin, held in her hand, not the holy babe, but a long straight spear.

«Wey li wî yê ku êrîşî keşîşxaneyê dike!» keşîş bi tirs got. ||| "Woe to him who attacks the monastery!" said the monk in terror.
«Ew xwe diavêje ser wî û bi rima xwe wî dadiqulipîne.» ||| "She hurls herself at him and sticks him through with her spear."
«Di demên kevn de Cezayîrî hatin vir û keşîşxane şewitandin.» ||| "In ancient times the Algerians came here and burnt the monastery."
«Lê binêre ev ji van gawiran çi rakir: dema ku ew di ber vê dêrokê re derbas dibûn, Meryema Pîroz ji nişkê ve xwe ji îkonê avêt, bezî derve û dest pê kir bi rima xwe lê dixist, vir û wir, ber bi her aliyî.... Û wê ew hemû heta yekî dawî kuştin.» ||| "But see what it cost these heathens: as they passed this chapel the Holy Virgin, all of a sudden, threw herself from the icon, rushed outside and started thrusting with her spear, this way and that, in all directions.... And she killed them all to a man."
«Bapîrê min tê bîr ku hestiyên wan dîtibûn; ew li seranserê daristanê belav bûbûn. Ji wê demê ve, em jê re dibêjin Meryema Tolhildanê.» ||| "My grandfather remembered seeing their bones; they littered the whole of the forest. Since then, we call her Our Lady of Revenge."
«Berî wê jê re digotin Meryema Dilovaniyê.» ||| "Before that she was called Our Lady of Mercy."

«Çima wê berî ku ew keşîşxaneyê bişewitînin keramet nedikir, Bavê Zaharya?» Zorba pirsî. ||| "Why didn't she perform her miracle before they burnt the monastery, Father Zaharia?" asked Zorba.

«Ew daxwaza Yê Herî Bilind bû!» keşîş bersiv da, sê caran xaç li xwe kir. ||| "That was the will of the All-High!" answered the monk, crossing himself three times.

«Aferîn ji Yê Herî Bilind re!» Zorba di bin lêv de got, dema dîsa li ser zînê siwar bû. «Em biçin pêş!» ||| "Good for the All-High!" muttered Zorba, climbing back into the saddle. "On we go!"

Di demek nêz de zozanek xuya bû ku li ser me dikaribû xêza keşîşxaneya Meryema Pîroz bibîne, ku bi keviran û darên kajê dorpêçkirî bû. ||| Soon a plateau appeared on which we could see the outline of the Holy Virgin's monastery surrounded by rocks and pine trees.

Aram, bi ken, ji dinyaya mayî qutkirî di kortala vê geliyê bilind ê kesk de, di ahengeke kûr de hêjayiya lûtkeyê û nermiya deştê digihand hev, ev keşîşxane li ber çavê min wek perçeyeke bi awayekî ecêb hilbijartî ya bo medîtasyona mirovan xuya bû. ||| Serene, smiling, cut off from the rest of the world in the hollow of this high green gorge, uniting in deep harmony the nobility of the peak and the gentleness of the plain, this monastery appeared to me a marvellously chosen retreat for human meditation.

«Li vir,» min fikirî, «ruhekî nerm û aqilmend dikaribû coşeke olî biçandiya ku dê li gorî pîvana mirovan bûya.» ||| "Here," I thought, "a gentle, sober spirit could cultivate a religious exaltation that would match the stature of men."
«Ne lûtkeyeke asê û mirov-derbas, ne jî deşteke tembel û xweşîperest, lê tenê tiştê pêwîst, ne zêdetir, da ku ruh bê bilind kirin bê ku nermiya xwe ya mirovî winda bike.» ||| "Neither a precipitous, superhuman peak, nor a lazy, voluptuous plain, but what is needed, and no more, for the soul to be elevated without losing its human tenderness."
«Cihekî wek vî dê ne lehengan ne jî berazan çêbike. Ew ê mirovan çêbike.» ||| "A site like this will fashion neither heroes nor swine. It will fashion men."

Li vir perestgeheke spehî ya Yewnaniya kevn an mizgeftek a Misilmanan a şad dê li cih bûya. ||| Here a graceful ancient Greek temple or a gay Mohammedan mosque would be in keeping.
Divê Xwedê li vir bi şeklekî sade yê mirovî dakeve, bi pêxwasî li ser giyaya biharê bimeşe, û bi aramî bi mirovan re biaxive. ||| God must come down here in simple human form, walk barefoot across the spring grass, and converse quietly with men.

«Çi mucîze! Çi tenêtî! Çi bextewarî!» min di bin lêv de got. ||| "What a marvel! What solitude! What felicity!" I murmured.

Em peya bûn, di deriyê navendî re derbas bûn, hilkişiyan ode ya mêvanan, li wir tepsiya kevneşopî ya raki, mereba û qehweyê ji me re hat pêşkêş kirin. ||| We dismounted, went through the central door, climbed to the visiting room, where we were offered the traditional tray of raki, jam and coffee.
Serokê mêvanan, an mêvandar, hat me bibîne, û di kêliyekê de em ji aliyê keşîşan ve dorpêç bûn ku dest bi axaftinê kirin. ||| The guest master, or hospitaller, came to see us, and in a moment we were surrounded by monks who began to talk.
Çavên fêlbaz, lêvên têr-nebûyî, rih, simbêl, û bêhna ewqas nêriyan. ||| Cunning eyes, insatiable lips, beards, moustaches, and the odor of so many he-goats.

«We rojnameyek neaniye?» keşîşekî bi xem pirsî. ||| "Haven't you brought a newspaper?" one monk asked anxiously.

«Rojnameyek?» min bi heyranî got. «Hûn ê li vir bi rojnameyekê çi bikin?» ||| "A newspaper?" I said in astonishment. "What would you do with a newspaper here?"

##PG 124
«Rojnameyek, bira, dê ji me re bigota li dinyaya jêr çi diqewime!» du an sê dengên hêrsbûyî qîriyan. ||| "A newspaper, brother, would tell us what is happening in the world below!" cried two or three indignant voices.

Li ser tîrkên balkonê palda bûn, ew wek gelek qijikan diqîriyan. ||| Leaning on the rails of the balcony, they croaked like a lot of ravens.
Ew bi coş li ser Îngilîstanê, Rûsyayê, Venîzelos û qral diaxivîn. ||| They were talking excitedly of England, Russia, Venizelos, the king.
Dinyayê ew sirgûn kiribûn, lê wan dinya sirgûn nekiribû. ||| The world had banished them, but they had not banished the world.
Çavên wan tije bûn bi bajarên mezin, dikan, jin, rojname.... ||| Their eyes were full of the great cities, shops, women, newspapers....

Keşîşekî mezin, qelew û pirçdar rabû ser xwe û bêhn kişand. ||| A big, fat hairy monk stood up and sniffed.

«Tiştek min heye ku nîşanî we bidim,» wî ji min re got. «Tu dikarî ji min re bibêjî tu li ser çi difikirî. Ez ê herim wê bînim.» ||| "I have something to show you," he said to me. "You can tell me what you think of it. I'll go and fetch it."

Ew çû, destên xwe yên kurt û pirçdar li ser zikê xwe girêdayî, sîlikên wî yên qumaşî li erdê dikişiyan. Ew di derî re winda bû. ||| He went off, his short hairy hands clasped together over his stomach, his cloth slippers dragging along the floor. He disappeared through the door.

Hemû keşîş bi xêzanî bişirîn. ||| The monks all grinned nastily.

«Bavê Demetriyos dîsa diçe ku keçika xwe ya keşîşa ji herî bîne,» mêvandar got. ||| "Father Demetrios is going to fetch his clay nun again," said the hospitaller.
«Şeytên ew bi taybetî ji bo wî di erdê de veşartibû û rojekê Demetriyos ew dît dema ku di baxçe de dikola.» ||| "The devil buried it in the ground especially for him and one day Demetrios found it when he was digging in the garden."
«Wî ew bir hucreya xwe û ji wê demê ve xewa xwe winda kiriye. Ew hema hema aqlê xwe jî winda kiriye.» ||| "He took it to his cell and has lost his sleep ever since. He's nearly lost his senses, too."

Zorba rabû ser xwe. Ew dixeniqî. ||| Zorba stood up. He was suffocating.

«Em hatin ku Serkeşîş bibînin û hin kaxezan îmze bikin,» wî got. ||| "We came to see the Abbot and to sign some papers," he said.

«Serkeşîşê pîroz li vir nine,» mêvandar got. «Ew vê sibê çû gund. Sebir bike.» ||| "The holy abbot isn't here," said the hospitaller. "He went to the village this morning. Have patience."

Bavê Demetriyos dîsa xuya bû, herdu destên xwe yên girêdayî dirêjkirî mîna ku kasa pîroz hildigirt. ||| Father Demetrios reappeared, his two clasped hands outstretched as though he were carrying the holy chalice.

«Va ye!» wî got, destên xwe bi baldarî vekirin. ||| "There!" he said, opening his hands cautiously.

Ez nêzîkî wî bûm. ||| I went up to him.
Peykerekî biçûk ê Tanagrayê, nîv-tazî û şermok, ji tiliyên qelew ên keşîş ber bi min ve bişirî. ||| A tiny Tanagra figurine, half-naked and coy, smiled up at me from the monk's fat fingers.
Wê serê xwe bi wî destê yek ê ku jê re mabû digirt. ||| She was holding her head with the one hand that still remained to her.

«Ji ber ku ew serê xwe wisa nîşan dide,» Demetriyos got, «tê wateya ku kevirekî hêja di hundirê wê de heye, dibe ku almasek an mircanek be. Tu çi difikirî?» ||| "For her to show her head like that," said Demetrios, "means that she has a precious stone inside it, maybe a diamond or a pearl. What do you think?"

«Ez difikirim,» şîroveyeke tirş a keşîşekî hat, «ku serê wê diêşe.» ||| "I think," came one monk's acid comment, "that she's got a headache."

Lê Demetriyosê mezin, lêvên wî mîna yên bizinekê berjêr daleqandî, li min dinêrî û bi bêsebirî li bendê bû. ||| But big Demetrios, his lips hanging down like a goat's, watched me and waited impatiently.

«Ez difikirim divê ez wê bişkînim û bibînim,» wî got. «Ez bi şev qet xew nakim ji ber wê.... Eger almasek di hundir de hebûya....» ||| "I think I ought to break her and see," he said. "I can't get any sleep at night for it.... If there were a diamond inside...."

Min li keçika ciwan a spehî nêrî bi memikên xwe yên biçûk û hişk, li vir di nav bêhna bixûrê û di nav xwedayên xaçkirî de sirgûnkirî, ku nifirên xwe didan goşt, kenê û ramûsanan. ||| I looked at the graceful young girl with her tiny, firm breasts, exiled here in the smell of incense and among crucified gods that lay their curse on the flesh, on laughter and kisses.

Ax! xwezî min bikaribûya wê xilas bikira! ||| Ah! if only I could save her!

Zorba peykerê ji herî girt, laşê jinane yê zirav hîs kir, û tiliyên wî, dilerizî, li ser memikên hişk û tûjkirî man. ||| Zorba took the terra-cotta figurine, felt the thin womanly body, and his fingers stayed, trembling on the firm, pointed breasts.

«Lê ma tu nabînî, keşîşê min ê baş,» wî got, «ku ev şeytan e? Ev şeytan bi xwe ye, û çewtî tê de tune.» ||| "But can't you see, my good monk," he said, "that this is the devil? It's the devil himself, and no mistake."
«Tu xem neke, ez wî baş nas dikim, lanetkirî ku ew e. Li van memikan binêre, Bavê Demetriyos -- sar, gilover û hişk. Memikê şeytan tam wek vî ye, û ez gelek li ser wê dizanim!» ||| "Don't you worry, I know him well enough, accursed as he is. Look at her breasts here, Father Demetrios -- cool, round and firm. That's just what the devil's breast is like, and I know plenty about that!"

##PG 125
Keşîşekî ciwan li ber derî xuya bû. ||| A young monk appeared in the doorway.
Roj li ser porê wî yê zêrîn û rûyê wî yê gilover û hûrpirç dibiriqî. ||| The sun shone on his golden hair and round, downy face.

Keşîşê jehrziman ê ku berê axivîbû çavê xwe li mêvandar girt. Herduyan bi fêlbazî bişirîn. ||| The venomous-tongued monk who had spoken before winked to the hospitaller. They both smiled cunningly.

«Bavê Demetriyos,» wan got. «Va ye şagirtê te, Gavrîlî.» ||| "Father Demetrios," they said. "Here is your novice, Gavrili."

Keşîş tavilê keçika xwe ya biçûk a ji herî girt û mîna fiçiyekê gindirî ber bi derî ve çû. ||| The monk seized his tiny clay woman immediately and went rolling like a barrel towards the door.
Şagirtê bedew bê deng li pêşiya wî bi gaveke hejok dimeşiya. ||| The handsome novice walked silently in front of him with a swinging step.
Ew di dehlîza dirêj û kavilbûyî de winda bûn. ||| They disappeared down the long, dilapidated corridor.

Min îşaret bi Zorba kir û em derketin hewşê. ||| I signed to Zorba and we went out into the courtyard.
Li derve bi awayekî xweş germ bû. ||| It was agreeably hot outside.
Li navenda hewşê dareke porteqalê ya bi kulîlk bêhn dida hewayê. ||| In the middle of the courtyard an orange tree in blossom scented the air.
Nêzîk, av bi xulxul ji serê beranekî kevn ê ji mermer diherikî. ||| Close by, water ran murmuring from an ancient ram's head in marble.
Min serê xwe danî bin wê û xwe teze hîs kir. ||| I put my head underneath and felt refreshed.

«Bi navê Xwedê ev kî ne?» Zorba bi hinek nefret pirsî. ||| "What in God's name are these people?" Zorba asked with some disgust.
«Ew ne mêr in ne jin; ew hêstir in. Pûf! bila herin xwe daliqînin!» ||| "They're neither men nor women; they're mules. Pooh! let them go hang!"

Wî jî serê xwe danî bin ava sar û dest bi kenê kir. ||| He too plunged his head beneath the fresh water and began to laugh.

«Pûf! bila herin xwe daliqînin!» wî dîsa got. «Hemûyan cûreyek şeytan di hundirê xwe de heye.» ||| "Pooh! let them go hang!" he said again. "They've all got a devil of some sort in them."
«Yek jinekê dixwaze, yekî din masiyê şor, yekî din pere, yekî din rojname... komeke ehmeqan!» ||| "One wants a woman, another salt cod, another money, another newspapers... bunch of noodles!"
«Çima ew nayên xwarê nav dinyayê, xwe ji wan hemûyan tije nakin û mejiyê xwe paqij nakin?» ||| "Why don't they come down into the world, stuff themselves full of all that and purge their brains?"

Wî cixareyek pêxist û li ser textê bin dara porteqalê ya bi kulîlk rûnişt. ||| He lit a cigarette and sat on the bench beneath the blossoming orange tree.

«Dema ku ez bi xwe daxwaza tiştekî dikim,» wî got, «tu dizanî ez çi dikim?» ||| "When I have a longing for something myself," he said, "do you know what I do?"
«Ez xwe pê tije dikim heta ber, û wisa ez jê xilas dibim û êdî li ser nafikirim. An, eger bifikirim, ew min dide vereşandin.» ||| "I cram myself chockful of it, and so I get rid of it and don't think about it any longer. Or, if I do, it makes me retch."
«Carekê dema ez zarok bûm -- ev ê nîşanî te bide -- ez li ser gîlasan dîn bûbûm.» ||| "Once when I was a kid -- this'll show you -- I was mad on cherries."
«Pereyê min tune bû, loma min nikaribû yekcar pir bikirim, û dema min hemû yên ku min dikirîn dixwarin, min hê zêdetir dixwest.» ||| "I had no money, so I couldn't buy many at a time, and when I'd eaten all I could buy I still wanted more."
«Roj û şev min ji bilî gîlasan li tu tiştî nedifikirî. Kefê ji devê min dihat; ew ezab bû!» ||| "Day and night I thought of nothing but cherries. I foamed at the mouth; it was torture!"
«Lê rojekê ez hêrs bûm, an şerm kirim, ez nizanim kîjan. Bi her hal, min tenê hîs kir ku gîlas tiştê dixwestin bi min dikin û ev tişt kêmaqilî bû.» ||| "But one day I got mad, or ashamed, I don't know which. Anyway, I just felt cherries were doing what they liked with me and it was ludicrous."
«Loma min çi kir? Şevekê ez rabûm, min berîkên bavê xwe gerand û mecîdiyeyek zîvîn dît û ew dizî.» ||| "So what did I do? I got up one night, searched my father's pockets and found a silver mejidie and pinched it."
«Sibê zû ez rabûm, çûm cem baxçevanekî û selikek gîlas kirî.» ||| "I was up early the next morning, went to a market gardener and bought a basket o' cherries."
«Ez di çalekê de rûniştim û dest bi xwarinê kir. Min xwar û xwar heta ez bi tevahî werimîm.» ||| "I settled down in a ditch and began eating. I stuffed and stuffed till I was all swollen out."
«Zikê min dest bi êşê kir û min vereşand. Erê, axa, min bi temamî vereşand, û ji wê rojê heta îro min qet gîlasek nexwest.» ||| "My stomach began to ache and I was sick. Yes, boss, I was thoroughly sick, and from that day to this I've never wanted a cherry."
«Min nikaribû dîtina wan ragirta. Ez xilas bûm. Min dikaribû ji her gîlasekî re bigota: êdî pêdiviya min bi te tune.» ||| "I couldn't bear the sight of them. I was saved. I could say to any cherry: I don't need you any more."
«Û min paşê eynî tişt bi şerab û titûnê kir. Ez hê jî vedixwim û dikişînim, lê di her saniyeyê de, eger bixwazim, hop! ez dikarim wê biqetînim.» ||| "And I did the same thing later with wine and tobacco. I still drink and smoke, but at any second, if I want to, whoop! I can cut it out."
«Ez ne di bin destê dilxwaziyê de me. Bi welatê min re jî wisa ye.» ||| "I'm not ruled by passion. It's the same with my country."
«Min pir li ser fikirî, loma min xwe heta gewriyê pê tije kir, ew vereşand, û ji wê demê ve qet ew min aciz nekiriye.» ||| "I thought too much about it, so I stuffed myself up to the neck with it, spewed it up, and it's never troubled me since."

«Û jin?» min pirsî. ||| "What about women?" I asked.

«Dora wan jî dê were, bila bibin! Ew ê were! Dema ku ez bibim hema heftê salî!» ||| "Their turn will come, damn them! It'll come! When I'm about seventy!"

Ew bo kêliyekê fikirî, û ev jî pir nêzîk xuya bû. ||| He thought for a moment, and it seemed too imminent.

«Heştê,» wî got, xwe rast kir. «Ev te dide kenandin, axa, ez dibînim, lê ne hewce ye.» ||| "Eighty," he said, correcting himself. "That makes you laugh, boss, I can see, but you needn't."
«Bi vî awayî mirov xwe azad dikin! Guh bide min; ji bilî ku mirov xwe tije bikin heta biteqin rêyeke din tune.» ||| "That's how men free themselves! Listen to me; there's no other way except by stuffing themselves till they burst."
«Ne bi bûyîna keşîşekî pak. Tu çawa hêvî dikî ku tu li ser şeytanekî serkeftî bibî, axa, eger tu bi xwe nebî şeytanekî-û-nîv?» ||| "Not by turning ascetic. How do you expect to get the better of a devil, boss, if you don't turn into a devil-and-a-half yourself?"

Demetriyos bi behnvedan ket hewşê, keşîşê ciwan ê bedew li pey wî. ||| Demetrios came panting into the courtyard, followed by the fair young monk.

##PG 126
«Mirov dê bifikiriya ku ew milyaketek e di hêrsê de,» Zorba di bin lêv de got, heyranî şermokî û nazikiya wî ya ciwan dikir. ||| "Anybody'd think he was an angel in a temper," muttered Zorba, admiring his shyness and youthful grace.

Ew ber bi derenceya kevirî ya ku diçû hucreyên jorîn ve çûn. ||| They went towards the stone staircase leading to the upper cells.

Demetriyos zivirî, li keşîşê ciwan nêrî, û çend gotin gotin. ||| Demetrios turned round, looked at the young monk, and said a few words.
Keşîş serê xwe hejand mîna redkirinê. Lê tavilê piştre wî bi razîbûnê serê xwe hejand, milê xwe li dora keşîşê pîr xist û ew bi hev re hilkişiyan pêpelûkan. ||| The monk shook his head as in refusal. But immediately afterwards he nodded in submission, put his arm round the old monk and they mounted the steps together.

«Tê digihî? Tu dibînî? Sodom û Gomora!» Zorba pirsî. ||| "Get it?" asked Zorba. "D'you see? Sodom and Gomorrah!"

Du keşîş ji der ve nêrîn, çavê xwe li hev girtin û dest bi kenê kirin. ||| Two monks peeped out, winked at one another and began to laugh.

«Komeke dexesî!» Zorba di bin lêv de got. «Gur hev neçirandinin, lê li van keşîşan binêre!» ||| "Spiteful bunch!" grunted Zorba. "Wolves don't tear one another to pieces, but look at these monks!"
«Te qet dîtiye ku jin wisa êrîşî hev dikin?» ||| "Have you ever seen women go for one another like this?"

«Ew hemû mêr in,» min bi kenê got. ||| "They're all men," I said, laughing.

«Li vir cudahî ne pir e, axa, ji min bawer bike! Hemû hêstir in.» ||| "There's not much difference here, boss, you take it from me! Mules, all of them."
«Tu dikarî ji wan re bibêjî Gavrîlî, an Gavrîla, Demetriyos, an Demetriya, li gorî ku tu çawa hîs dikî.» ||| "You can call them Gavrilis, or Gavrila, Demetrios, or Demetria, according to how you feel."
«Were, axa, em rabin herin. Bila kaxez bi lez îmze bibin û em biçin.» ||| "Come on, boss, let's be off. Get the papers signed as quick as we can and let's go."
«Eger em li vir bimînin, em ê di demek nêz de ji mêr û jinan bi tevahî bizar bibin.» ||| "We'll soon get disgusted with men and women altogether if we stay here."

Wî dengê xwe nizm kir. ||| He lowered his voice.

«Ji xeynî vê, plansaziyek min heye....» ||| "Besides, I've got a scheme...."

«Fikreke din a dîn, ez dizanim. Ma tu nafikirî ku te di dema xwe de bes tiştên ehmeq kirine, ey nêriyê pîr? Ji min re bibêje plansaziya te çi ye.» ||| "Another mad idea, I know. Don't you think you've done enough foolish things in your time, you old goat? Tell me what your scheme is."

Zorba milên xwe hejand. ||| Zorba shrugged his shoulders.

«Ez çawa dikarim tiştekî wisa ji te re bibêjim, axa? Tu mirovekî baş î, eger destûrê bidî min ku ez bibêjim! Tu ji bo herkesî, çi dibe bila bibe, herî zêde hewl didî.» ||| "How can I tell you a thing like that, boss? You're a nice chap, if you'll allow me to say so! You do your utmost for everybody, whoever they are."
«Eger te di zivistanê de kêçeke li ser lihêfa xwe bidîta, te dê ew danîba bin da ku ew sermayê nexwe.» ||| "If you found a flea on your eiderdown in the winter you'd put it underneath so that it wouldn't catch cold."
«Tu çawa dikarî nîqaşkarekî pîr ê wek min fam bikî? Eger ez kêçekê bibînim, çirt! ez wê dipelçiqînim.» ||| "How should you understand an old scoundrel like me? If I find a flea, crack! I crush him."
«Eger ez mîhekê bibînim, fîş! ez gewriya wê dibirim, wê li ser şîşê dixim û hevalên xwe vedixwînim ziyafetê!» ||| "If I find a sheep, swish! I cut its throat, slap it onto the spit and invite my friends to a feast!"
«Lê tu dê bigotaya: mîh ne ya te ye! Na, ez wê qebûl dikim. Lê, axa, bila em pêşî wê biqedînin, paşê em ê bi aramî li ser biaxivin û li ser ‹ya te› û ‹ya min› çiqas ku tu bixwazî nîqaş bikin.» ||| "But you'd say: the sheep isn't yours! No, I admit that. But, boss, let's finish eating it first, afterwards we'll talk it over quietly and discuss what's 'yours' and 'mine' as much as you like."
«Tu dikarî heta dilê te bixwaze li ser biaxivî, dema ku ez diranên xwe bi şixçeyekê paqij dikim.» ||| "You could talk to your heart's content about it, while I cleaned my teeth with a matchstick."

Hewş bi qêrqêra kenê wî tije bû. ||| The courtyard resounded with his peals of laughter.
Zaharya xuya bû, tirsiyayî. ||| Zaharia appeared, terrified.
Wî tiliyek danî ser lêvên xwe û li ser pencan ber bi me ve hat. ||| He placed a finger on his lips and crept up to us on tiptoe.

«Şşş!» wî got. «Divê hûn nekenin! Li wir jor binêrin, wê pencereya biçûk... li wir metran dixebite; ew pirtûkxane ye.» ||| "Sh!" he said. "You mustn't laugh! Look up there, that little window... that's where the bishop is working; it's the library."
«Ew dinivîse, ew mirovê pîroz. Ew tevahiya rojê dinivîse, loma deng nekin.» ||| "He's writing, the holy man is. He writes all day long, so don't make a noise."

«Ha, tu tam ew kes î ku min dixwest bibînim, Bavê Yûsiv!» Zorba got, milê keşîş girt. «Were, min bibe hucreya xwe, ez dixwazim bi te re biaxivim.» ||| "Ha, you're just the person I wanted to see, Father Joseph!" said Zorba, taking the monk's arm. "Come, take me to your cell, I want a chat with you."

Paşê ew zivirî ber bi min: ||| Then he turned to me:

«Heta ku em ne li vir in, tu here û li dêrokê û hemû îkonên kevn binêre,» wî got. ||| "While we're away, you go and have a look round the chapel and all the old icons," he said.
«Ez ê li benda serkeşîş bisekinim, ew ê dereng nemîne. Lê tu bi xwe tiştekî dest pê neke, tu yê tenê wê xera bikî. Bila ji min re bimîne, plansaziyek min heye.» ||| "I'll wait for the abbot, he won't be long. But don't start anything yourself, you'll only make a mess of it. Leave it to me, I've got a scheme."

Ew xwar bû û di guhê min de axivî. ||| He bent down and spoke in my ear.

«Em ê wê daristanê bi nîvê bihayê bistînin.... Tu peyvekê nebêje.» ||| "We'll have that forest at half price.... Don't say a word."

Û ew bi lez çû, milê keşîşê dîn girt. ||| And he went off quickly, holding the mad monk's arm.
"""

CH18 = r"""
##PG 127
##FIRST
Ez ji ber derê dêrokê derbas bûm û xwe avêtim hundirê siyê, ku sar û bêhnxweş bû. ||| I CROSSED the threshold of the chapel and plunged into the shadowy interior, which was cool and fragrant.

Avahî vala bû. ||| The building was deserted.
Şamdanên bronz ronahiyeke qels belav dikirin. ||| The bronze chandeliers shed a faint light.
Îkonostasekî bi hostatî çêkirî dawiya dûr a dêrokê dagirtibû. ||| A finely worked iconostasis filled the far end of the chapel.
Ew rezeke zêrîn a tijî tirî nîşan dida. ||| It represented a golden vine arbor laden with grapes.
Dîwar ji jor heta jêr bi freskoyên nîv-jêbirî nixumandî bûn: wêneyên bitirs ên zahidên wek hestî, Bavên Dêrê, Êşa dirêj a Îsa, milyaketên mezin ên hov bi porên xwe yên bi şirîtên fireh ên şîn û pembe girêdayî yên ku ji şilbûnê beloq bûbûn. ||| The walls were covered from top to bottom with half-obliterated frescoes: terrifying pictures of skeleton-like ascetics, the Fathers of the Church, Christ's prolonged Passion, huge fierce-looking angels with their hair tied in broad blue and pink ribbons which had faded with the damp.

Li jor di qubê de Meryem hebû, bi destên xwe yên bi lavayî dirêjkirî. ||| High up in the vault was the Virgin, with arms imploringly outstretched.
Lempeyeke giran a zîvîn li ber wê bû û ronahiya nerm li dora wê dilerizî, rûyê wê yê dirêj û qermiçî dimist. ||| A heavy silver lamp stood before her and the soft light flickered round her, caressing her long, contorted face.
Ez ê tu carî çavên wê yên jankêş, devê wê yê biçûk û gilover û çena wê ya bihêz û serhişk ji bîr nekim. ||| I shall never forget her dolorous eyes, her puckered, rounded mouth and strong wilful chin.
Li vir, min fikirî, Dayikeke bi tevahî bextewar û têrbûyî ye, tewra di êşa herî dijwar de jî, ji ber ku ew hîs dike ku ji malzaroka wê ya mirî tiştek derketiye ku dê nemire. ||| Here, I thought, is the completely happy and satisfied Mother, even in the most agonizing pain, because she feels that from her mortal loins has issued something that will not die.

Dema ku ez dîsa ji ber derî derbas bûm roj diçû ava. ||| When I recrossed the threshold the sun was sinking.
Ez di rewşeke bextewariyê de li bin dara porteqalê rûniştim. ||| I sat down under the orange tree in a state of happiness.
Qubeya dêrokê pembe dibû mîna ku berbang bûya. ||| The dome of the chapel was turning pink as though it were dawn.
Keşîş çûbûn hucreyên xwe û bêhna xwe vedidan. ||| The monks had gone to their cells and were resting.
Ew ê qet nerazên; divê wan hemû hêza xwe berhev bikira. ||| They would not sleep at all; they had to muster all their strength.
Îsa wê şevê dest pê dikir hilkişiya Golgotayê, û divê ew pê re biçûna. ||| Christ would begin to climb Golgotha that night, and they had to go with him.
Du berazên reş bi memikên pembe li bin dareke harûbê di xeweke kûr de razayî bûn. ||| Two black sows with pink teats were lying fast asleep beneath a carob tree.
Kevok li ser banan digeriyan û dikutkutîn. ||| Pigeons were strutting on the roofs and cooing.

Çiqas, min fikirî, ez ê bijîm ku ji şîrîniya erdê, hewayê, bêdengiyê û bêhna dara porteqalê ya bi kulîlk kêfê bigirim? ||| How long, I thought, shall I live to enjoy the sweetness of the earth, the air, the silence and the scent of the orange tree in blossom?
Îkoneke Bachosê Pîroz, ya ku min di dêrokê de lê nêrîbû, dilê min bi bextewariyê dagirtibû. ||| An icon of Saint Bacchus, which I had looked at in the chapel, had made my heart overflow with happiness.
Tiştên ku min herî kûr dihejînin -- yekîtî, hişkbûna armancê û domdariya daxwazê -- careke din ji min re hatin eşkere kirin. ||| The things that move me most deeply -- unity, firmness of purpose and constancy of desire -- were once again revealed to me.
Pîroz be ew îkoneya biçûk a delal a ciwanekî Filehî bi porê xwe yê xelek-xelek ê ku mîna gûşiyên tirî li ser eniya wî dadiket. ||| Blessed be that charming little icon of a Christian youth with curly hair falling over his forehead like bunches of grapes.
Diyonîsos, xwedayê bedew ê şerab û coşê, û Bachosê Pîroz di hişê min de bûn yek û eynî dîmen girtin. ||| Dionysus, the handsome god of wine and ecstasy, and Saint Bacchus fused in my mind and took on the same appearance.
Di bin pelên rez û cilê keşîş de eynî laş bi jiyanê dilerizî, ji tavê şewitî -- Yewnanistan. ||| Under the vine leaves and the monk's habit there quivered with life the same body, burnt by the sun -- Greece.

Zorba vegeriya û bi lez nûçe da: ||| Zorba returned and hurriedly gave the news:

«Serkeşîş hat. Me hinekî axivî; pêdiviya wî bi pir lavakirinê heye; ew dibêje ku ew ê daristanê belaş nede; ew ji ya ku me got pir zêdetir dixwaze, ew fêlbazê pîr, lê min hê pê re neqedandiye.» ||| "The abbot did come. We had a little talk; he needs a lot of coaxing; he says he's not going to give the forest away for a song; he's asking a lot more than we said, the old rogue, but I haven't finished with him yet."

«Çima pêdiviya wî bi lavakirinê heye? Min digot qey em li hev kiribûn?» ||| "Why does he need coaxing? I thought we were agreed?"

«Ji bo xatirê Xwedê, axa, tu xwe têxe nav vê yekê,» Zorba lava kir. «Tu yê tenê tiştan xera bikî.» ||| "Don't you meddle in this, for heaven's sake, boss," Zorba pleaded. "You'd only spoil things."
«Va ye, piştî vê hemûyê, tu behsa li-hev-kirina kevn dikî; ew demek dirêj e ku hatiye veşartin.» ||| "There you are, after all this, talking about the old agreement; that's buried long ago."
«Birûyên xwe neqermiçîne; ew veşartî ye, ez ji te re dibêjim. Em ê wê daristanê bi nîvê bihayê bistînin!» ||| "Don't frown; it's buried, I tell you. We'll have that forest at half price!"

«Tu niha çi xerabî dikî, Zorba?» ||| "What mischief are you up to now, Zorba?"

«Tu xem neke. Ev karê min e. Ez ê çerxan rûn bikim û wan bizivirînim, tê digihî?» ||| "Never you mind. That's my business. I'm going to oil the works and make them turn, do you get it?"

«Lê çima? Ez qet tê nagihim.» ||| "But why? I don't get it at all."

«Ji ber ku min li Kandiyayê ji ya ku divabû zêdetir xerc kir, lema! Ji ber ku Lola komeke baş a -- ango, pereyê te daqurtand.» ||| "Because I spent more than I should have done at Candia, that's why! Because Lola swallowed quite a heap of my -- that is to say, your money."
«Tu nafikirî ku min ji bîr kiriye, ne wisa? Tiştek wek rûmeta xwe heye. Tu leke li ser deftera min tune!» ||| "You don't think I've forgotten, do you? There is such a thing as self-respect. No blots on my copybook!"

##PG 128
«Min ewqas xerc kir, loma ez ewqas didim. Min hesab kir; Lola heft hezar drahmî li min rûnişt.» ||| "I've spent so much, so I pay so much. I've reckoned it up; Lola cost me seven thousand drachmas."
«Ez ê wan ji bihayê daristanê kêm bikim. Serkeşîş, keşîşxane û Meryema Pîroz in ên ku dê bihayê Lolayê bidin.» ||| "I'll knock them off the price of the forest. It's the abbot, the monastery and the Holy Virgin who'll pay for Lola."
«Ev plana min e. Çawa dibe?» ||| "That's my scheme. How d'you like it?"

«Qet. Çima divê Meryema Pîroz ji bo zêdegaviyên te berpirsiyar be?» ||| "Not at all. Why should the Holy Virgin be responsible for your excesses?"

«Ew berpirsiyar e û ji berpirsiyar jî zêdetir! Binêre, kurê wê hebû: Xwedê.» ||| "She is responsible and more than responsible! Look, she had her son: God."
«Xwedê ez, Zorba, çêkirim, û wî hin amûr dan min -- tu dizanî ez çi dibêjim. Û van amûrên lanetkirî, li ku derê ku ez rastî mê ya cinsê têm, min ji serê min dikin û berîka min vedikin.» ||| "God made me, Zorba, and he gave me some instruments -- you know what I mean. And these damned instruments, no matter where I meet the female of the species, make me lose my head and open my purse."
«Dibînî? Loma, Pîroziya Wê berpirsiyar e û ji berpirsiyar jî zêdetir e. Bila ew bide.» ||| "See? Therefore, Her Holiness is responsible and more than responsible. Let her pay."

«Ez jê hez nakim, Zorba.» ||| "I don't like it, Zorba."

«Ew bi tevahî pirseke din e. Bila em pêşî heft kaxezên piçûk ên pereyan xilas bikin; em ê paşê li ser nîqaş bikin!» ||| "That's another question altogether. Let's save the seven little banknotes first; we'll discuss it later!"
«‹Pêşî bi min re evînê bike, delalê, ez ê paşê dîsa bibim meta te....› Tu dizanî stran çawa diçe....» ||| "'Make love to me first, darling, I'll be your aunt again afterwards....' You know how the song goes...."

Mêvandarê qelew xuya bû: «Werin hundir,» wî bi awayekî nerm ê dêrî got; «şîv amade ye.» ||| The fat hospitaller appeared: "Come inside," he said, in a suave ecclesiastical tone; "dinner is served."

Em daketin xwaringehê, salonek mezin bi textik û maseyên dirêj û teng. ||| We went down to the refectory, a large hall with benches and long narrow tables.
Bêhna rûnê tirş û genî hewa dagirtibû. ||| The smell of sour, rancid oil filled the air.
Li dawiya dûr freskoyeke kevn a Şîva Dawî hebû. ||| At the far end was an old fresco of the Last Supper.
Yanzdeh şagirtên dilsoz mîna keriyek pez li dora Îsa kom bûbûn, û li aliyê din, bi tena serê xwe sekinî, Cihûda yê por-sor bû, berxê reş. ||| The eleven faithful disciples crowded around Christ like a flock of sheep, and on the other side, standing quite alone, was the redhaired Judas, the black sheep.
Eniya wî girz bû û pozê wî yê wek nikulê teyr xwar bû. ||| He had a bulging forehead and aquiline nose.
Û Îsa nikaribû çavên xwe jê veqetîne. ||| And Christ could not take his eyes off him.

Mêvandar rûnişt, ez li milê xwe yê rastê û Zorba li milê xwe yê çepê danîm. ||| The hospitaller sat down, placing me on his right and Zorba on his left.

«Em rojî ne,» wî got, «loma ez hêvî dikim hûn me biborînin -- ne rûn ne şerab, tewra ji bo mêvanan jî. Lê hûn bi xêr hatin!» ||| "We are fasting," he said, "so I hope you will excuse us -- no oil or wine, even for visitors. But you are welcome!"

Me xaç çêkir; paşê me bê deng zeytûn, pîvazên hêşîn, fasûlyeyên taze û helva ji xwe re danî. ||| We made the sign of the cross; then we served ourselves in silence to olives, spring onions, fresh beans and halva.
Me her sêyan hêdî hêdî, mîna kêvroşkan, cût. ||| We all three munched slowly, like rabbits.

«Jiyan li vir jêr wisa ye,» mêvandar got. «Xaçkirinek û rojiyek.» ||| "Such is life here below," said the hospitaller. "A crucifixion and a fast."
«Lê sebir, birano, sebir, Vejîn û Berx tên, û Padîşahiya Ezmên.» ||| "But patience, brothers, patience, the Resurrection and the Lamb are coming, and the Kingdom of Heaven."

Min kuxiya. Zorba li lingê min xist mîna ku bibêje: «Devê xwe bigire!» ||| I coughed. Zorba trod on my foot as though to say: "Shut up!"

«Min Bavê Zaharya dîtiye...» Zorba got, da ku mijarê biguherîne. ||| "I've seen Father Zaharia..." said Zorba, to change the subject.

Mêvandar hejiya: ||| The hospitaller started:

«Wî dînî çi ji we re got?» wî bi xem pirsî. «Hemû heft cinên wî di hundirê wî de ne, guh nedin tu peyvên wî. Ruhê wî gemar e û ew gemarê li dora xwe hemûyî dibîne.» ||| "What did that madman say to you?" he asked anxiously. "He has all seven demons in him, don't listen to a word he says. His soul is impure and he sees impurity all around him."

Zengilê ji bo keşîşan bi awayekî xemgîn lê xist. ||| The bell for the monks rang lugubriously.
Mêvandar xaç li xwe kir û rabû ser xwe. ||| The hospitaller crossed himself and stood up.

«Divê ez herim,» wî got. «Êşa Îsa dest pê dike; divê em xaçê pê re hilgirin.» ||| "I shall have to go," he said. "Christ's Passion is beginning; we must carry the cross with him."
«Hûn dikarin îşev bêhna xwe vedin, divê hûn piştî rêwîtiya xwe westiyabin. Lê di nimêja sibê de....» ||| "You can rest tonight, you must be tired after your journey. But at matins tomorrow...."

«Ew beraz!» Zorba di nav diranên xwe de pistand hema ku keşîş çû. «Beraz! Derewîn! Hêstir!» ||| "Those swine!" Zorba muttered between his teeth as soon as the monk had gone. "Swine! Liars! Mules!"

«Çi çewt e, Zorba? Ma Zaharya tiştek ji te re gotiye?» ||| "What's wrong, Zorba? Has Zaharia told you something?"

«Tu xem neke, axa, bila here dojehê! Eger ew naxwazin îmze bikin, ez ê nîşanî wan bidim ez ji çi hatime çêkirin!» ||| "Never mind, boss, to hell with it! If they don't want to sign, I'll show them what I'm made of!"

##PG 129
Em çûn hucreya ku ji me re hatibû diyarkirin. ||| We went to the cell which had been assigned to us.
Li quncikê îkoneyek hebû ku Meryemê nîşan dida dema ku rûyê xwe li rûyê kurê xwe dida, çavên wê yên mezin tijî hêsir. ||| In the corner was an icon representing the Virgin pressing her cheek against her son's, her big eyes full of tears.

Zorba serê xwe yê mezin hejand. ||| Zorba shook his big head.

«Tu dizanî çima ew digirî, axa?» ||| "Do you know why she's crying, boss?"

«Na.» ||| "No."

«Ji ber ku ew dibîne çi diqewime. Eger ez wênesazê îkonan bûma, min ê Meryem bê çav, guh an poz xêz bikira. Ji ber ku ez ê li wê bisozim.» ||| "Because she can see what's going on. If I was a painter of icons, I'd draw the Virgin without eyes, ears or nose. Because I'd be sorry for her."

Em li ser nivînên hişk dirêj bûn. ||| We stretched out on the hard beds.
Karîteyên darîn bêhna selbûsê didan; ji pencereya vekirî bêhna nerm a biharê dihat, bi bêhna kulîlkan barkirî. ||| The wooden beams smelled of cypress; through the open window was wafted the gentle breath of spring, laden with the perfume of flowers.
Carna awazên xemgîn ji hewşê mîna bahozên bê radibûn. ||| Occasionally the mournful tunes surged from the courtyard like gusts of wind.
Bilbilek nêzîkî pencereyê dest bi stranê kir, paşê yekî din hinekî dûrtir, û hê yekî din. ||| A nightingale began to sing close to the window, then another a short distance away, and still another.
Şev bi evînê dagirtî bû. ||| The night was overflowing with love.

Ez nikaribûm razêm. ||| I could not sleep.
Stranê bilbil bi nalînên Îsa re tevlihev dibû, û min hewl da ku ez bi xwe di nav darên porteqalê yên gulvedayî re hilkişim Golgotayê, xwe bi lekeyên mezin ên xwînê rêber dikim. ||| The nightingale's song mingled with the lamentations of Christ, and I tried to climb Golgotha myself through the flowering orange trees, guiding myself by the huge spots of blood.
Di şeva şîn a biharê de min dikaribû xwêdana sar bibînim ku li ser laşê Îsa yê zer û lerizok dibiriqî. ||| In the blue spring night I could see the cold sweat glistening all over Christ's pale, faltering body.
Min dikaribû destên wî yên dirêjkirî û lerizok bibînim, mîna ku ew parsekek bûya ku ji yên li dora xwe lava dikir ku guhdarî bikin. ||| I could see his hands outstretched and trembling, as though he were a beggar imploring the bystanders to listen.
Gelê belengaz ê Celîlê li pey wî bilez diçûn, diqîriyan: «Hosanna! Hosanna!» ||| The poor people of Galilee hurried after him, crying: "Hosannah! Hosannah!"
Pelên xurmê di destên wan de bûn û wan kincên xwe li ber lingên wî radixistin. ||| They had palm leaves in their hands and spread their mantles before his feet.
Wî li yên ku jê hez dikirin nêrî, her çend tu kes nikaribû kûrahiya bêhêvîtiya wî texmîn bike. ||| He looked at the ones he loved, though none could divine the depths of his despair.
Tenê wî dizanibû ku ew diçû mirina xwe. ||| He alone knew he was going to his death.
Di bin stêrkan de, digirî û bêdeng, wî dilê xwe yê belengaz ê mirovî yê ku tijî tirs bû dilnerm dikir: ||| Beneath the stars, weeping and silent, he consoled his poor human heart that was full of fear:

«Mîna libekî genim, dilê min, divê tu jî bikevî erdê û bimirî. Netirse.» ||| "Like unto a grain of wheat, my heart, you, too, must fall into the ground and die. Be not afraid."
«Eger tu nemirî, tu çawa dikarî fêkî bidî? Tu çawa dikarî mirovên ku ji birçîna dimirin têr bikî?» ||| "If you do not, how can you bring forth fruit? How can you nourish men who die of hunger?"

Lê, di hundirê wî de, dilê wî yê mirovî diqehirî û dilerizî, û nedixwest bimire.... ||| But, within him, his man's heart was fainting and trembling, and did not want to die....

Daristana li dora keşîşxaneyê tijî stranê bilbilan bû. ||| The wood round the monastery was full of the song of nightingales.
Stranê wan di nav pelên şil de bilind dibû û bi tevahî behsa evîn û coşê dikir. ||| Their song rose amidst the damp foliage and spoke entirely of love and passion.
Û pê re dilê belengaz ê mirovahiyê dilerizî, werimî û digirî. ||| And with it trembled, swelled and wept the poor heart of mankind.

Hêdî hêdî, bê ku hîs bikim, ligel Êşa Îsa û stranê bilbil, ez ketim qada xewê, tam mîna ku divê ruh bikeve Bihiştê. ||| Gradually, imperceptibly, together with Christ's Passion and the nightingale's song, I entered the realm of sleep, just as the soul must enter Paradise.

Ez ji saetekê kêmtir razabûm dema ku ez bi sawekê ji xew rabûm, ji tirsê hejandî. ||| I had been sleeping less than an hour when I awoke with a start, terror-stricken.

«Zorba!» min qîriya. «Te bihîst? Gulleyek revolverê!» ||| "Zorba!" I cried. "Did you hear? A revolver shot!"

Lê Zorba li ser nivînê xwe rûniştibû û cixareyek dikişand. ||| But Zorba was sitting on his bed smoking a cigarette.

«Netirse, axa,» wî got, hê jî hewl dida ku hêrsa xwe kontrol bike, «bila ew hesabên xwe bi xwe çareser bikin, ew beraz!» ||| "Don't be alarmed, boss," he said, still trying to control his anger, "let them settle their own accounts, the swine!"

Qîrîn ji dehlîzê dihatin; me dikaribû sîlikên giran bibihîza ku li erdê dikişiyan, derî vedibûn û digirtin, û nalînek ji dûr ve mîna ku yek birîndar bûya. ||| Cries came from the corridor; we could hear heavy slippers dragging along, doors opening and closing, and a moaning in the distance as though someone were wounded.

Ez ji nivînê xwe firiyam û derî vekir. ||| I leaped from my bed and opened the door.
Pîrekî qermiçî li ber min xuya bû û destên xwe vekirin, rê li min girt. ||| A wizened old man appeared before me and spread out his arms, barring my passage.
Wî kumekî sipî yê tûj û kirasekî sipî heta çokan li xwe kiribû. ||| He was wearing a white pointed bonnet and a white shirt down to his knees.

«Tu kî yî?» ||| "Who are you?"

«Metran...» wî bersiv da, dengê wî dilerizî. ||| "The bishop..." he replied, his voice trembling.

Ez hema bi ken biteqiyama. ||| I almost burst out laughing.
Metranek? Xemilên wî, qebaya zêrîn, tac û xaç, kevirên xapînok ên pirreng li ku bûn... ||| A bishop? Where were his ornaments, the gold chasuble, mitre and cross, the many-colored false stones...
Cara yekem bû ku min metranek di cilên xewê de didît. ||| It was the first time I had seen a bishop in his night attire.

##PG 130
«Ew gulleya revolverê çi bû, Mîrê min?» ||| "What was that revolver shot, Your Lordship?"

«Ez nizanim, ez nizanim...» wî qiriqî, min bi nermî paşde dehland hundirê odeyê. ||| "I don't know, I don't know..." he stammered, pushing me gently back into the room.

Zorba ji ser nivînê xwe bi ken teqiya. ||| Zorba burst out laughing from his bed.

«Tu ditirsî, bavê piçûk?» wî got. «Were hundir, kalo, û bi me re bimîne. Em ne keşîş in, loma ne hewce ye tu xem bikî.» ||| "Are you scared, little Father?" he said. "Come in, then, old fellow, and stay with us. We are no monks, so you needn't worry."

«Zorba,» min bi dengekî nizm got, «hinekî hurmetê nîşan bide, nikarî? Ev metran e.» ||| "Zorba," I said in an undertone, "show more respect, can't you? It's the bishop."

«Hê! di kirasekî de tu kes ne metran e! Were hundir, kalo!» ||| "H'm! in a shirt nobody's a bishop! Come in, old chap!"

Ew rabû ser xwe, metran ji milê wî girt û ew bir hundirê hucreyê, derî li pişt wî girt. ||| He stood up, took the bishop by the arm and led him into the cell, closing the door behind him.
Wî şûşeyek rûmê ji tûrikê xwe derxist û qedehek piçûk tije kir. ||| He took a bottle of rum out of his haversack and filled a small glass.

«Vexwe, hevalê min,» wî got. «Ev ê te xurt bike.» ||| "Drink, my friend," he said. "That'll buck you up."

Pîrê piçûk qedeh vala kir û zû hat ser hişê xwe. ||| The little old man drained the glass and soon came round.
Ew li ser nivînê min rûnişt û xwe da dîwêr. ||| He sat down on my bed and leaned against the wall.

«Bavê pir Birûmet,» min got, «ew gulleya revolverê çi bû?» ||| "Very Reverend Father," I said, "what was that revolver shot?"

«Ez nizanim, kurê min.... Min heta nîvê şevê xebitî û çûm raketinê, dema ku li hucreya Bavê Demetriyos a tenişta min min bihîst....» ||| "I don't know, my son.... I had worked till midnight and gone to bed, when next door in Father Demetrios's cell I heard...."

«Ax! ax!» Zorba bi ken got. «Wê demê tu rast bûyî, Zaharya! Ew berazên qirêj!» ||| "Ah! ah!" said Zorba with a laugh. "You were right, then, Zaharia! Those dirty swine!"

Metran serê xwe danî. ||| The bishop bowed his head.

«Divê diz ji cûreyekê bûbe,» wî di bin lêv de got. ||| "It must have been a thief of some sort," he murmured.

Di dehlîzê de hengame sekinîbû û keşîşxane dîsa ket bêdengiyê. ||| In the corridor the uproar had ceased and the monastery sank into silence once more.
Metran bi çavên xwe yên dilovan û tirsiyayî li min nêrî, mîna ku lava dikira. ||| The bishop looked at me with his kind, frightened eyes, as if in supplication.

«Tu di xew de yî, kurê min?» wî pirsî. ||| "Are you sleepy, my son?" he asked.

Min bi zelalî hîs kir ku ew nedixwest derkeve û vegere ku bi tena serê xwe di hucreya xwe de be. Ew ditirsiya. ||| I felt clearly that he did not want to leave and go back to be alone in his cell. He was afraid.

«Na,» min bersiv da, «ez qet di xew de nînim; demekê li vir bimîne.» ||| "No," I answered, "I'm not at all sleepy; stay here a while."

Em dest bi axaftinê kirin. Zorba xwe da ser balgeha xwe û cixareyek dipêça. ||| We began to talk. Zorba was leaning on his pillow and rolling a cigarette.

«Tu xuya dikî ku ciwanekî xwende yî,» metran ji min re got. «Li vir ez nikarim kesî bibînim ku pê re biaxivim.» ||| "You appear to be a cultured young man," the bishop said to me. "Here I can't find anyone to talk to."
«Sê teoriyên min hene ku alîkariya min dikin ku jiyana min xweş bibe; ez dixwazim li ser wan ji te re bibêjim, zarokê min.» ||| "I have three theories that help to make my life agreeable; I would like to tell you about them, my child."

Wî li benda bersiva min nesekinî lê tavilê dest pê kir: ||| He didn't wait for my reply but began straight away:

«Teoriya min a yekem ev e: şeklê kulîlkan bandorê li rengê wan dike; rengê wan bandorê li taybetiyên wan dike.» ||| "My first theory is this: the shape of flowers influences their color; their color influences their properties."
«Bi vî awayî her kulîlk bandoreke cuda li ser laşê mirovekî dike, û loma li ser ruhê wî.» ||| "Thus it is that each flower has a different effect on a man's body, and therefore on his soul."
«Loma divê em pir baldar bin dema ku em di nav zeviyekê re derbas dibin ku kulîlk lê gulvedayî ne.» ||| "That is why we must be extremely careful in passing through a field when the flowers are in bloom."

Ew sekinî mîna ku li benda raya min bûya. ||| He stopped as though waiting for my opinion.
Min dikaribû pîrê piçûk bibînim ku di nav zeviyekê re digeriya, li erdê dinêrî, bi coşeke veşartî, li pey şekl û rengên kulîlkan. ||| I could see the little old man wandering through a field, searching the ground, with secret excitement, for the shapes and colors of the flowers.

Divê pîrê belengaz bi tirseke mîstîkî bilerize; di biharê de divê zevî ji bo wî bi şeytan û milyaketên pirreng tije bibin. ||| The poor old man must tremble with mystic awe; in the spring the fields must be peopled for him with many-colored devils and angels.

«Ev teoriya min a duyem e: her ramana ku bandoreke rastîn heye, hebûneke rastîn jî heye.» ||| "This is my second theory: every idea that has a real influence has also a real existence."
«Ew bi rastî li wir e, ew bi nedîtî di hewayê de naçe -- laşekî rastîn heye -- çav, dev, ling, zik.» ||| "It is really there, it does not float invisibly in the atmosphere -- it has a real body -- eyes, a mouth, feet, a stomach."
«Ew nêr an mê ye û loma li pey mêran an jinan dibeze, li gorî rewşê. Loma Încîl dibêje: ‹Peyv bû goşt...›» ||| "It is male or female and therefore runs after men or women, as the case may be. That is why the Gospel says: 'The word became flesh...'"

##PG 131
Wî dîsa bi xem li min nêrî. ||| He looked anxiously at me again.

«Teoriya min a sêyem,» wî bi lez berdewam kir, ji ber ku nikaribû li ber bêdengiya min bisekine, «ev e: hin Ebedîyet di jiyana me ya demkî de jî heye, lê ji bo me pir zehmet e ku em wê bi tenê kifş bikin.» ||| "My third theory," he went on hurriedly, as he could not bear my silence, "is this: there is some Eternity even in our ephemeral lives, only it is very difficult for us to discover it alone."
«Xemên me yên rojane me ji rê derdixin. Tenê çend kes, kulîlka mirovahiyê, dikarin di jiyana xwe ya derbasdar a li ser vê erdê de jî ebedîyetekê bijîn.» ||| "Our daily cares lead us astray. A few people only, the flower of humanity, manage to live an eternity even in their transitory lives on this earth."
«Ji ber ku hemû yên din wê bi vî awayî winda bibûna, Xwedê rehmê li wan kir û ji wan re ol şand -- bi vî awayî girseyî jî dikare di ebedîyetê de bijî.» ||| "Since all the others would therefore be lost, God had mercy on them and sent them religion -- thus the crowd is able to live in eternity, too."

Wî qedandibû û bi eşkereyî rihet bûbû ku axivîbû. ||| He had finished and was visibly relieved for having spoken.
Wî çavên xwe yên piçûk, ên ku bijang lê tunebûn, bilind kirin û li min bişirî. ||| He raised his small eyes, which had no lashes, and smiled at me.
Mîna ku ew digot: «Va ye, ez her tiştê ku min heye didim te, bigire!» ||| It was as though he were saying: "There, I am giving you all I have, take it!"
Ez pir bandar bûm dema min ev pîrê piçûk dît ku wisa, dema ku ew hema min nas nedikir, berhemên xebata jiyanekê rasterast pêşkêşî min dikir. ||| I was very moved at the sight of this little old man thus offering me outright, when he hardly knew me, the fruits of a lifetime's work.

Hêsir di çavên wî de bûn. ||| He had tears in his eyes.

«Tu li ser teoriyên min çi difikirî?» wî pirsî, destê min di nav destên xwe de girt û li çavên min nêrî. ||| "What do you think of my theories?" he asked, taking my hand between his own and looking into my eyes.
Min hîs kir ku ew bi bersiva min ve girêdayî bû da ku jê re bibêje ka jiyana wî bi kêr hatibû an na. ||| I felt that he depended on my reply to tell him whether his life had been of any use or not.

Min dizanibû ku, ji rastiyê wêdetir, peywirek din heye ku pir girîngtir û pir mirovîtir e. ||| I knew that, over and above the truth, there exists another duty which is much more important and much more human.

«Ew teorî dibe ku gelek ruhan xilas bikin,» min bersiv da. ||| "Those theories may save many souls," I answered.

Rûyê metran ronî bû. Ev rastdarkirina tevahiya jiyana wî bû. ||| The bishop's face lit up. That was the justification of his entire life.

«Spas, kurê min,» wî pistand, destê min bi dilovanî guvaşt. ||| "Thank you, my son," he whispered, squeezing my hand affectionately.

Zorba ji quncikê xwe firiya. ||| Zorba leaped from his corner.

«Teoriyeke min a çaremîn heye!» wî qîriya. ||| "I've got a fourth theory!" he cried.

Min bi xem li wî nêrî. Metran zivirî ber bi wî. ||| I looked anxiously at him. The bishop turned to him.

«Bibêje, kurê min, û bila teoriya te pîroz be! Ew çi ye?» ||| "Speak, my son, and may your theory be blessed! What is it?"

«Ku du û du dibin çar!» Zorba bi giranî got. ||| "That two and two make four!" said Zorba gravely.

Metran ecêbmayî lê nêrî. ||| The bishop looked at him, flabbergasted.

«Û teoriyeke pêncemîn, kalo,» Zorba berdewam kir. «Ku du û du nabin çar.» ||| "And a fifth theory, old man," Zorba went on. "That two and two don't make four."
«Berdewam bike, hevalê min, şansê xwe biceribîne! Hilbijartina xwe bike!» ||| "Go on, my friend, take a chance! Make your choice!"

«Ez tê nagihim,» pîr qiriqî, bi pirsyarî li min nêrî. ||| "I don't understand," stammered the old man, casting a questioning glance at me.

«Ez jî na!» Zorba got, bi ken teqiya. ||| "Neither do I!" said Zorba, bursting into laughter.

Ez zivirîm ber bi pîrê belengaz, yê ku şerm kiribû, û mijar guhert. ||| I turned to the poor old man, who was abashed, and changed the subject.

«Lêkolînên te yên taybetî li vir di keşîşxaneyê de çi ne, Bavê Birûmet?» min pirsî. ||| "What are your special studies here in the monastery, Reverend Father?" I asked.

«Ez kopiyên destnivîsên kevn ên keşîşxaneyê çêdikim, kurê min, û vê dawiyê min hemû navên pîroz ên ku Dêrê di derbarê Dayika Meryem de bi kar tîne berhev dikin.» ||| "I am making copies of the ancient manuscripts of the monastery, my son, and recently I have been collecting all the sacred epithets used by the Church in connection with the Virgin Mother."

Wî axîn kişand. ||| He sighed.

«Ez pîr im,» wî got, «û ez nikarim tiştekî din bikim. Ez di rêzkirina hemû xemilên peyvî yên Meryemê de rihetiyê dibînim, û bi vî awayî ez bêbextiyên vê dinyayê ji bîr dikim.» ||| "I am old," he said, "and I can't do anything else. I find relief in listing all the verbal adornments of the Virgin, and thus I forget the miseries of this world."

Wî enîşka xwe da ser balgehê, çavên xwe girt û dest bi pistepistê kir mîna ku di hîlmê de bû: ||| He leaned his elbow on the pillow, closed his eyes and began murmuring as though in delirium:

«Gula Bêpûç, Erda Berhemdar, Rez, Kanî, Çavkaniya Keramatan, Pêlikana Ezmên, Pir, Keştiya Rizgarker a Keştîşkestiyan, Bendera Bêhnvedanê, Mifteya Bihiştê, Berbang, Ronahiya Ebedî, Birûsk, Stûna Agir, Generalê Nezetbar, Bircê Nelivok, Kelehê Negirtî, Dilxweşî, Şahî, Gopalê Koran, Dayika Sêwiyan, Mase, Xwarin, Aştî, Aramî, Bêhnxweşî, Ziyafet, Şîr û Hingiv...» ||| "Imperishable Rose, Fruitful Earth, Vine, Fountain, Source of Miracles, Ladder to Heaven, Bridge, Rescuing Frigate for the Shipwrecked, Haven of Rest, Key to Paradise, Dawn, Eternal Light, Lightning, Pillar of Fire, Invincible General, Immovable Tower, Impregnable Fortress, Consolation, Joy, Staff for the Blind, Mother for the Orphan, Table, Food, Peace, Serenity, Perfume, Banquet, Milk and Honey..."

##PG 132
«Pîr di hîlmê de ye...» Zorba bi dengekî nizm got. «Ez ê wî bipêçim da ku ew sermayê nexwe.» ||| "The old boy's delirious..." said Zorba in an undertone. "I'll cover him over so that he doesn't catch cold."

Ew rabû ser xwe, betaniyek avêt ser metran û balgeha wî rast kir. ||| He stood up, threw a blanket over the bishop and put his pillow straight.

«Heftê û heft cûre dînîtî hene, wisa min bihîstiye,» wî got. «Divê ev heftê û heştem be.» ||| "There are seventy-seven kinds of madness, so I've heard," he said. "This one must be the seventy-eighth."

Roj diçirisî. Me dikaribû lêdana semantronê bibihîza. ||| Day was dawning. We could hear the ringing of the semantron.

Min serê xwe ji pencereyê derxist. ||| I leaned my head out of the window.
Di tîrêjên yekem ên berbangê de min keşîşekî zirav dît, kumekî reş ê dirêj li serê wî, ku hêdî hêdî li dora hewşê digeriya û bi çakûçek piçûk li perçeyek dirêj a darê dixist ku taybetiyên muzîkî yên ecêb hebûn. ||| In the first rays of dawn I saw a gaunt monk, a long black hood over his head, walk slowly round the courtyard striking with a small hammer on a long piece of wood which had marvellously musical properties.
Dengê semantronê di hewaya sibehê de deng veda, tijî şîrînî, aheng û bandan. ||| The sound of the semantron echoed through the morning air, full of sweetness, harmony and appeal.
Bilbilan dev ji stranê berdabû û çûkên din di nav daran de dest bi cûcikandinê dikirin. ||| The nightingales had stopped singing and other birds were beginning to chirp in the trees.

Min guhdarî kir, ji notayên şîrîn û vejîner ên semantronê kêfxweş. ||| I listened, charmed with the sweet evocative notes of the semantron.
Min fikirî ka çawa, tewra di hilweşînê de jî, awazeke bilind di jiyanê de hemû şeklê xwe yê derve diparêze, bandar e û tijî esalet e. ||| I thought how, even in decay, an elevated rhythm in life preserves all its outward form, is impressive and full of nobility.

Ruh diçe, lê ew warê xwe yê fireh dihêle ku wî hêdî hêdî pêşxistiye û ku mîna qalikekî deryayê tevlihev e. ||| The spirit departs, but it leaves its vast dwelling which it has slowly evolved and which is as intricate as a sea shell.

Katedralên ecêb ên ku tu di bajarên qerebalix û bêxwedê de dibînî tam wisa qalikên vala ne, min fikirî. ||| The wonderful cathedrals you see in noisy, godless cities are just such empty shells, I thought.
Cinawirên berdîrokî yên ku ji wan tenê îskeletek, ji tav û baranê westiyayî, maye. ||| Prehistoric monsters of which only a skeleton, worn by sun and rain, is left.

Li derê hucreya me lêdan hat. Dengê rûnî yê mêvandar gihîşt guhên me. ||| There was a knock at the door of our cell. The unctuous voice of the hospitaller came to our ears.

«Werin, rabin niha, birano, wexta nimêja sibê ye.» ||| "Come, rise now, brothers, it's time for matins."

Zorba firiya: ||| Zorba leaped up:

«Gulleya revolverê ya şevê çi bû?» wî qîriya, ji xwe çûyî. ||| "What was the revolver shot in the night?" he shouted, beside himself.

Wî kêliyekê li bendê ma. Bêdengî. Divê keşîş wî di derî re bihîstibe, ji ber ku me dikaribû bêhnvedana wî ya dengdar bibihîza. ||| He waited a moment. Silence. The monk must have heard him through the door, because we could hear his noisy breathing.

Zorba ji hêrsê lingê xwe li erdê kuta. ||| Zorba stamped with rage.

«Ew gulleya revolverê çi bû?» wî dîsa pirsî, di hêrsekê de. ||| "What was that revolver shot?" he asked again, in a fury.

Me bihîst ku gav bi lez dûr diçûn. Bi lehzekê Zorba li ber derî bû. Wî ew vekir: ||| We heard steps going rapidly away. With one bound Zorba was at the door. He opened it:

«Qereçiyên qirêj! Bênamûs!» wî qîriya, di aliyê keşîşê ku vedigeriya de tif kir. ||| "Filthy scoundrels! Blackguards!" he shouted, spitting in the direction of the retreating monk.
«Keşîş, rahîbe, rahib, mizgînvan, dêrvan, hûn hemû, ev e tişta ku hûn jê re hêja ne!» ||| "Priests, nuns, monks, churchwardens, sacristans, the whole lot of you, that's all you're worth!"

Û wî dîsa tif kir. ||| And he spat again.

«Em herin!» min got. «Bêhna xwînê di hewayê de heye.» ||| "Let's go!" I said. "There's a smell of blood in the air."

«Xwezî tenê xwîn bûya!» Zorba pistand. «Tu here nimêja sibê, axa, eger tu bixwazî. Ez ê li dora xwe binêrim ka ez çi dikarim kifş bikim.» ||| "If it were only blood!" grunted Zorba. "You go to matins, boss, if you want to. I'll have a look round to see what I can find out."

«Em herin!» min dîsa got, bizarbûyî. «Û tu yê ewqas baş bî ku tu pozê xwe nexî cihê ku ne karê te ye?» ||| "Let's go!" I said again, nauseated. "And will you be good enough not to go poking your nose where it's none of your business?"

«Tam li wir e ku ez timî dixwazim wî bixim!» Zorba got. ||| "That's just where I always want to poke it!" said Zorba.

Ew kêliyekê fikirî, paşê bi fêlbazî bişirî: ||| He thought for a moment, then smiled cunningly:

«Şeytan ji me re qenciyekê dike,» wî got. «Ez difikirim ew tiştan tîne serî.» ||| "The devil is doing us a favor," he said. "I think he's bringing things to a head."
«Tu fêm dikî ev ê çi li keşîşxaneyê rûnê, axa, gulleyek revolverê ya wisa? Tam heft hezar!» ||| "Do you realize what that might cost the monastery, boss, a revolver shot like that? A cool seven thousand!"

Ew daket hewşê. ||| He went down into the courtyard.
Bêhna kulîlkan, şîrîniya sibehê, bextewariya ezmanî. ||| The scent of blossom, morning sweetness, heavenly felicity.
Zaharya li benda me bû. Ew bi lez hat û milê Zorba girt. ||| Zaharia was waiting for us. He ran up and seized Zorba's arm.

##PG 133
«Birayê Kanavaro,» wî bi dengekî lerizok pistand. ||| "Brother Canavaro," he whispered with a trembling voice.

«Were, divê em herin!» ||| "Come, we must go!"

«Ew gulleya revolverê çi bû? Wan kesek kuşt, ne wisa? De bibêje yan ez ê situyê te bişkênim!» ||| "What was that revolver shot? They killed somebody, didn't they? Come on, talk or I'll wring your neck!"

Çena keşîş lerizî. Wî li dora xwe nêrî. ||| The monk's chin quivered. He looked round him.
Hewş vala bû, hucre girtî; ji deriyê vekirî yê dêrokê pêlên muzîkê dihatin. ||| The courtyard was deserted, the cells closed; through the open chapel door came waves of music.

«Li pey min werin, hûn herdu,» wî di bin lêv de got. «Sodom û Gomora!» ||| "Follow me, both of you," he muttered. "Sodom and Gomorrah!"

Em li kêleka dîwêr çûn, em gihîştin aliyê din ê hewşê û ji baxçe derketin. ||| We slipped along the side of the wall, gained the other side of the courtyard and went out of the garden.
Nêzîkî sed metro ji keşîşxaneyê goristanek hebû. Em çûn hundir. ||| A hundred yards or so from the monastery was a cemetery. We went inside.

Em li ser goran derbas bûn, Zaharya deriyê piçûk ê dêrokê pal da û em li pey wî ketin hundir. ||| We stepped over the graves, Zaharia pushed the little door of the chapel and we entered behind him.
Li navendê, li ser hesîrekê, cesedek razayî bû ku bi cilê keşîşekî nixumandî. ||| In the center, on a rush mat, lay a body covered over with a monk's habit.
Mûmek li serî û li lingê cesed her du jî dişewitî. ||| There was a candle burning at both head and foot of the corpse.

Ez xwar bûm ku li cesed binêrim. ||| I stooped to look at the body.

«Keşîşê ciwan!» min bi lerizînê di bin lêv de got. «Şagirtê ciwan ê por-zer ê Bavê Demetriyos!» ||| "The young monk!" I murmured with a shudder. "Father Demetrios's fair-haired young novice!"

Li ser deriyê perestgehê, bi baskên xwe yên belavkirî û şûrê xwe yê ji kalan derxistî, û sandalên sor li xwe, şeklê serfîreştê Mîkaîl dibiriqî. ||| On the door of the sanctuary, with widespread wings and unsheathed sword, and wearing red sandals, glittered the figure of the archangel Michael.

«Serfîreştê Mîkaîl!» keşîş qîriya, «agir û kibrît bişîne û wan hemûyan bişewitîne! Serfîreştê Mîkaîl, tiştekî bike. Îkoneya xwe bihêle! Şûrê xwe rake û li wan bide! Te ew gulleya revolverê nebihîst?» ||| "Archangel Michael!" cried the monk, "send fire and brimstone and burn them all! Archangel Michael, do something. Leave your icon! Raise your sword and smite them! Did you not hear that revolver shot?"

«Kê ew kuşt? Kî bû? Demetriyos? Bibêje, ey rihê bizinê pîr!» ||| "Who killed him? Who was it? Demetrios? Speak, old goatbeard!"

Keşîş ji destê Zorba xelas bû û xwe rast avêt erdê li ber serfîreşt. ||| The monk slipped out of Zorba's grasp and threw himself flat on the floor before the archangel.
Ew çend kêliyan bê liv ma, rû berjor, çav ji serê wî derketî, dev fireh vekirî, bi baldarî li îkonê dinêrî. ||| He remained motionless for a few moments, face upraised, eyes starting from his head, mouth wide open, watching the icon intently.

Ji nişkê ve ew ji şahiyê firiya. ||| Suddenly he jumped for joy.

«Ez ê wan bişewitînim!» wî bi dengekî biryardar got. «Serfîreşt livî, min ew dît, wî îşaret bi min kir!» ||| "I will burn them!" he declared in a resolute voice. "The archangel moved, I saw him, he made a sign to me!"

Ew nêzîkî îkonê bû û lêvên xwe yên qalind li şûrê serfîreşt zeliqand. ||| He went close to the icon and glued his thick lips to the archangel's sword.

«Şikir ji Xwedê re!» wî got. «Ez rihet bûm!» ||| "God be praised!" he said. "I am relieved!"

Zorba dîsa keşîş girt. ||| Zorba seized the monk again.

«Were vir, Zaharya,» wî got. «Niha, tu yê tiştê ku ez ji te re dibêjim bikî.» ||| "Come here, Zaharia," he said. "Now, you'll do what I tell you."

Paşê ew zivirî ber bi min. ||| Then he turned to me.

«Pereyê bide min, axa, ez ê bi xwe kaxezan îmze bikim. Ew hemû gur in li wir, û tu berxek î, ew ê te bixwin.» ||| "Give me the money, boss, I'll sign the papers myself. They're all wolves in there, and you're a lamb, they'll eat you."
«Bila ji min re bimîne. Tu xem neke, min berazên qelew li cihê ku ez dixwazim girtine.» ||| "Leave it to me. Don't you worry, I've got the fat hogs where I want them."
«Em ê nîvro ji vir derkevin bi daristanê di berîkên xwe de. Were, Zaharya.» ||| "We'll leave here at midday with the forest in our pockets. Come on, Zaharia."

Ew bi dizî ber bi keşîşxaneyê ve çûn. Ez çûm gerê li bin darên kajê. ||| They slipped away furtively towards the monastery. I went for a stroll under the pine trees.

Roj jixwe bilind bû û jale li ser pelan dibiriqî. ||| The sun was high already and the dew was sparkling on the leaves.
Reşêleyekê li pêşberî min firî ser şaxê dareke hermê ya kovî, dûvika xwe hejand, nikulê xwe vekir, li min nêrî û du an sê notayên tinazî fîk kirin. ||| A blackbird in front of me flew on to the branch of a wild pear tree, flicked his tail, opened his beak, looked at me and whistled two or three mocking notes.

Di nav kajan re min dikaribû hewş bibîne û keşîş ku di refeke dirêj de derdiketin, serên wan xwarkirî û kumên reş li ser milên wan daleqandî. ||| Through the pines I could see the courtyard and the monks coming out in a long file, their heads bowed and black cowls hanging over their shoulders.
Ayîn qediyabû; ew ber bi xwaringehê ve diçûn. ||| The service was over; they were on their way to the refectory.

##PG 134
«Çi heyf,» min fikirî, «ku divê hişkî û esaleteke wisa bê ruh be.» ||| "What a pity," I thought, "that such austerity and nobility should be without a soul."

Ez westiyabûm, min baş nexewtibû, û ez li ser giyê dirêj bûm. ||| I was tired, I had not slept well, and I stretched out on the grass.

Binefşên kovî, gez, rosmarî û sêwîng hewa bîhndar dikirin. ||| The wild violets, broom, rosemary and sage made the air redolent.

Kêzik bê navber vizevizî dikirin dema ku ew di birçîtiya xwe de mîna keleşan xwe diavêtin nav kulîlkan û hingiv dimijîn. ||| Insects buzzed continually as in their hunger they plunged into the flowers like pirates and sucked the honey.
Li dûr çiya dibiriqîn, şefaf, aram, mîna mija livok di ronahiya şewatî ya tavê de. ||| In the distance the mountains sparkled, transparent, serene, like a moving haze in the burning light of the sun.

Min çavên xwe girtin, hênikbûyî. ||| I closed my eyes, soothed.
Kêfeke aram û sirî min girt -- mîna ku ew hemû keramata kesk a li dora min bi xwe bihişt bûya, mîna ku ew hemû teze bûn, hewabûn û şahiya aram a ku min hîs dikir Xwedê bûya. ||| A quiet, mysterious pleasure took possession of me -- as if all that green miracle around me were paradise itself, as if all the freshness, airiness and sober rapture which I was feeling were God.
Xwedê her saniyeyê dîmenê xwe diguherîne. ||| God changes his appearance every second.
Pîroz e ew mirovê ku dikare wî di hemû kinckirinên wî de nas bike. ||| Blessed is the man who can recognize him in all his disguises.
Di kêliyekê de ew qedehek ava taze ye, ya din kurê te yê ku li ser çokên te dilîze an jineke efsûnkar, an dibe ku tenê gereke sibehê be. ||| At one moment he is a glass of fresh water, the next your son bouncing on your knees or an enchanting woman, or perhaps merely a morning walk.

Hêdî hêdî, her tişt li dora min, bê ku şeklê xwe biguherîne, bû xewn. ||| Little by little, everything around me, without changing shape, became a dream.
Ez bextewar bûm. Erd û bihişt bûn yek. ||| I was happy. Earth and paradise were one.
Kulîlkek di zeviyan de bi dilopeke mezin a hingiv di navenda xwe de: jiyan ji min re wisa xuya dikir. ||| A flower in the fields with a large drop of honey in its center: that was how life appeared to me.
Û ruhê min, mêşeke hingiv a kovî ku talan dikir. ||| And my soul, a wild bee plundering.

Ez bi hovîtî ji vê rewşa xweşiyê hatim hişyar kirin. ||| I was brutally awakened from this state of beatitude.
Min gavên li pişt xwe û pistepist bihîst. ||| I heard steps behind me and whispers.
Di heman kêliyê de dengekî bextewar qîriya: ||| At the same instant a happy voice cried:

«Axa, em diçin!» ||| "Boss, we're off!"

Zorba li pêşberî min sekinî û çavên wî yên piçûk bi biriqîneke şeytanî dibiriqîn. ||| Zorba stood in front of me and his small eyes shone with a diabolical gleam.

«Diçin?» min bi rihetî got. «Ma her tişt çareser bû?» ||| "Off?" I said with relief. "Is it all settled?"

«Her tişt!» Zorba got, li beşê jorîn ê çakêtê xwe lê xist. ||| "Everything!" said Zorba, tapping the upper part of his jacket.

«Va ye daristan. Ez hêvî dikim ku ew ji me re bextê baş bîne! Û va ne ew heft hezarên ku Lola li me rûnişt!» ||| "Here's the forest. I hope it brings us luck! And here are the seven thousand Lola cost us!"

Wî gulokeke kaxezên pereyan ji berîka xwe ya hundir derxist. ||| He took a roll of banknotes from his inside pocket.

«Wan bigire!» wî got. «Ez deynên xwe didim; ez êdî şerm nakim ku li rûyê te binêrim.» ||| "Take 'em!" he said. "I pay my debts; I'm not ashamed to look you in the face any more."
«Goreyên, û destçente, û bêhnxweşî û sîwana Bûbûlîna hemû di wê de hene. Tewra findiqên papaxanê jî! Û helva ku min ji te re anî, jî!» ||| "The stockings, and handbags, and perfume and Dame Bouboulina's parasol are all included in that. Even the parrot's nuts! And the halva I brought you, as well!"

«Ji xwe re bihêle, Zorba; ew diyariyek e ji min,» min got. «Here û mûmek bişewitîne ji bo Meryema ku te li dijî wê guneh kiriye.» ||| "Keep it yourself, Zorba; it's a present from me," I said. "Go and burn a candle to the Virgin you've sinned against."

Zorba zivirî. Bavê Zaharya ber bi me ve dihat di qebaya xwe ya qirêj de, ya ku kesk dibû, û solên xwe yên topik-şikestî. ||| Zorba turned round. Father Zaharia was coming towards us in his filthy gown, which was turning green, and his down-at-heel shoes.
Wî herdu hêstirên me dianîn. ||| He was leading our two mules.

Zorba guloka kaxezan nîşanî wî da. ||| Zorba showed him the roll of notes.

«Em ê parve bikin, Bavê Yûsiv,» wî got. «Tu dikarî du sed lîbre masiyê şor bikirî û xwe pê tije bikî heta zikê te biteqe.» ||| "We'll split, Father Joseph," he said. "You can buy two hundred pounds of salt cod and stuff yourself with it till you burst your belly."
«Heta tu wê vereşînî û xwe ji masiyê şor ji bo her û her azad bikî! Were, destê xwe dirêj bike!» ||| "Till you spew it up and deliver yourself from cod for ever and ever! Come on, hold out your paw!"

Keşîş kaxezên qirêj girt û ew veşartin. ||| The monk took the dirty notes and hid them.

«Ez ê hin neft bikirim!» wî got. ||| "I shall buy some paraffin!" he said.

Zorba dengê xwe nizm kir û di guhê keşîşê pîr de pistand. ||| Zorba lowered his voice and whispered in the old monk's ear.

«Di tariyê de dema ku ew hemû razayî ne, ew bizinên pîr ên rihdar; û divê bayekî baş hebe,» wî pêşniyar kir. ||| "In the dark when they're all asleep, the bearded old goats; and there must be a good wind," he recommended.
«Dîwaran ji her aliyî bişilîne. Tenê hewce ye tu çend perçe paçik an pembû bişilînî, her tişt, paşê agirekî lê bide. Fikir girt?» ||| "Sprinkle the walls on all sides. You only need soak some rags or cotton waste, anything, then put a light to it. Got the idea?"

Keşîş dilerizî. ||| The monk was trembling.

«Wisa nelerize! Serfîreşt fermana te da ku tu wê bikî, ne wisa? Baweriya xwe bi neftê û keremê Xwedê bîne! Bextê baş ji te re!» ||| "Don't tremble like that! The archangel ordered you to do it, didn't he? Put your trust in paraffin and the grace of God! Good luck to you!"

##PG 135
Em siwar bûn, û min nihêrîneke dawî li keşîşxaneyê kir. ||| We mounted, and I took a last look at the monastery.

«Te tiştek fêr bû, Zorba?» min pirsî. ||| "Have you learned anything, Zorba?" I asked.

«Di derbarê gulleya revolverê de? Serê xwe pê neêşîne, axa; Zaharyayê pîr rast e: Sodom û Gomora! Demetriyos keşîşê piçûk ê delal kuşt. Va ye ji te re.» ||| "About the revolver shot? Don't worry your head about that, boss; old Zaharia's right: Sodom and Gomorrah! Demetrios killed the nice little monk. There you have it."

«Demetriyos? Çima?» ||| "Demetrios? Why?"

«Hewl nede ku tu wê derxî, axa, ew hemû qirêj û gemarî ye.» ||| "Don't try to ferret it out, boss, it's all filth and foulness."

Ew zivirî ber bi keşîşxaneyê. Keşîş ji xwaringehê derdiketin, serên xwe xwarkirî, destên xwe girêdayî, di rê de ku xwe di hucreyên xwe de kilît bikin. ||| He turned towards the monastery. The monks were filing out of the refectory, heads bent, hands clasped, on their way to lock themselves in their cells.

«Nifirên xwe bidin min, Bavên pîroz!» wî qîriya. ||| "Give me your curses, holy Fathers!" he cried.
"""

CH19 = r"""
##PG 135
##FIRST
KESA YEKEM ku em wê şevê li peravê xwe peya bûn pê re rastî hev hatin Bûbûlîna bû, ya ku li ber koxikê kombûyî rûniştibû. ||| THE FIRST PERSON we met as we dismounted on our beach that night was Bouboulina, who was sitting huddled up in front of the hut.
Dema ku lempe hat pêxistin û min rûyê wê dît ez tirsiyam. ||| When the lamp was lit and I saw her face I was alarmed.

«Çi çewt e, Madam Hortens? Tu nexweş î?» ||| "What's wrong, Madame Hortense? Are you ill?"

Ji kêliya ku hêviya mezin -- zewac -- di hişê wê de biriqîbû, sîrena me ya pîr hemû efsûnên xwe yên nediyar û gumanbar winda kiribûn. ||| From the moment the great hope -- marriage -- had gleamed in her mind, our old siren had lost all her indefinable and dubious charms.
Wê hewl dida ku rabirdûyê pak bike û perên geş ên ku wê xwe pê xemilandibû ji talanê paşa, beg û amîralên xwe bavêje. ||| She tried to wipe out the past and cast off the gaudy feathers with which she had adorned herself out of the spoils from her pashas, beys and admirals.
Ji bilî bûyîna welatiyeke ciddî û birûmet, jineke baş û qenc, tu armanca wê tunebû. ||| She had no aspiration beyond that of becoming a serious and respectable commoner, a good, virtuous woman.
Wê êdî ne sifet dixist ne xwe dixemiland; wê xwe tam wek ku bû nîşan dida: mexlûqeke belengaz ku dixwest bizewice. ||| She no longer made up, nor decked herself out; she showed herself just as she was: a poor creature who wanted to get married.

Zorba devê xwe venekir. ||| Zorba did not open his mouth.
Ew bi awayekî bêhntengî simbêlê xwe yê nû-boyaxkirî dikişand. ||| He kept nervously pulling at his newly dyed moustache.
Ew xwar bû, soba pêxist û hinek av danî ser ji bo çêkirina qehweyê. ||| He bent down, lit the stove and put on some water for making coffee.

«Tu bêrehm î!» stranbêja kabareyê ya pîr ji nişkê ve bi dengekî qirçî got. ||| "You're cruel!" the old cabaret singer said all of a sudden in a hoarse voice.

Zorba serê xwe rakir û lê nêrî. Çavên wî nerm bûn. ||| Zorba raised his head and looked at her. His eyes softened.
Ew tu carî nikaribû bibihîze ku jinek bi awayekî dilşewat tiştekî jê re bibêje bê ku bi tevahî bibişkive. ||| He could never hear a woman say anything to him in a harrowing tone without being completely overwhelmed.
Hêsireke tenê ji jinekê dikaribû wî bifetisîne. ||| One tear from a woman could drown him.

Wî tiştek negot, qehwe û şekir kir nav cizweyê, û tevda. ||| He said nothing, put the coffee and sugar in the pot, and stirred.

«Çima tu min ewqas dirêj dihêlî di bêhêvîtiyê de berî ku bi min re bizewicî?» sîrena pîr got. «Ez êdî newêrim xwe li gund nîşan bidim.» ||| "Why do you keep me pining so long before marrying me?" said the old siren. "I daren't show myself in the village any more."
«Ez riswa bûm! Riswa! Ez ê xwe bikujim.» ||| "I'm disgraced! Disgraced! I shall kill myself."

Ez li ser nivînê bêhna xwe vedidam. Bi enîşka xwe li ser balgehê palda bûyî, min ji vê dîmena bi awayekî komîk dilşewat kêf digirt. ||| I was resting on the bed. Leaning with my elbow on the pillow, I enjoyed this comically moving scene.

«Çima te tacên zewacê neanîn?» ||| "Why didn't you bring the marriage wreaths?"

Zorba hîs kir ku destê piçûk û qelew ê Bûbûlîna li ser çoka wî dilerizî. ||| Zorba felt Bouboulina's plump little hand trembling on his knee.
Ew çok perçeyê dawî yê erdê hişk bû ku ev mexlûqa belengaz a hezar û yek keştîşkestinan dikaribû xwe pê bigirta. ||| That knee was the last inch of solid ground to which this poor creature of a thousand and one shipwrecks could cling.

Zorba xuya bû ku vê fêm dike û dilê wî nerm bû. Lê dîsa wî tiştek negot. ||| Zorba seemed to understand this and his heart relented. But once more he said nothing.
Wî qehwe kir nav sê fincanan. ||| He poured the coffee into three cups.

«Çima te tacên zewacê neanîn, delalê?» wê bi dengekî lerizok dubare kir. ||| "Why didn't you bring the marriage wreaths, darling?" she repeated in a quavering voice.

«Li Kandiyayê yên baş tunebûn,» Zorba bi kurtî bersiv da. ||| "They haven't got any good ones in Candia," Zorba replied curtly.

Wî fincan belav kirin û li quncikekî çemiya. ||| He handed the cups round and squatted in a corner.

##PG 136
«Min nameyek ji Atînayê re nivîsiye ku ew hin bişînin,» wî berdewam kir. «Min hin mûmên sipî jî sipariş kirine, û behîvên şekirî bi tama çîkolatayê.» ||| "I've written to Athens for them to send some," he went on. "I've ordered some white candles, too, and sugared almonds with chocolate flavor."

Dema ku diaxivî xeyala wî geş dibû. ||| As he spoke his imagination kindled.
Çavên wî dibiriqîn, û mîna helbestvanekî di saniyeya şewatî ya afirandinê de, Zorba bilind dibû ber bi bilindahiyên ku derew û rastî tê de tevlihev dibin û mîna xwişkan dişibin hev. ||| His eyes sparkled, and like a poet in the burning second of creation, Zorba soared to heights where fiction and truth mingle and resemble each other, like sisters.

Ew çemiyayî bû, û, wisa bêhna xwe vedida, bi dengê bilind qehweya xwe vedixwar. ||| He was squatting, and, resting thus, noisily drank his coffee.
Wî cixareyeke duyem pêxist; rojeke baş bûbû -- li-hev-kirina daristanê di berîka wî de bû, wî deynên xwe dabûn, ew bextewar bû. Wî xwe berda. ||| He lit a second cigarette; it had been a good day -- he had the forest settlement in his pocket, he had paid off his debts, he was happy. He let himself go.

«Zewaca me, Bûbûlîna ya min a şîrîn,» wî got, «divê dengvedanê çêbike. Tu sekine heta ku tu kincê bûkaniyê yê ku min ji te re sipariş kiriye bibînî.» ||| "Our marriage, my sweet Bouboulina," he said, "must make a stir. You wait till you see the bridal gown I've ordered for you."
«Loma ez ewqas dirêj li Kandiyayê mam, evîna min. Min şand pey du sêwirmendên mezin ên modayê ji Atînayê û min ji wan re got: ‹Binêrin! Jina ku ez ê bi wê re bizewicim ne li Rojhilat ne li Rojava hempa heye!›» ||| "That's why I stayed so long in Candia, my love. I sent for two big fashion designers from Athens and I told them: 'Look! The woman I'm going to marry has no equal in the East or West!'"
«‹Ew qraliçeya naskirî ya çar Hêzên Mezin bû; niha ew jinebî ye, Hêzên Mezin mirine û wê razî bûye ku min wek mêrê xwe bigire.›» ||| "'She was the acknowledged queen of four great Powers; now she's a widow, the great Powers are dead and she's consented to take me as her husband.'"
«‹Loma ez dixwazim kincê wê yê bûkaniyê jî hempa nebe: divê ew hemû ji hevirmiş, mircan û stêrkên zêrîn be!› Herdu sêwirmendan îtiraz kirin:» ||| "'So I want her bridal gown to have no equal either: it must be all in silk, pearls and gold stars!' The two designers protested:"
«‹Lê ew ê pir bedew be!› wan got. ‹Hemû mêvan dê ji bedewiyeke wisa kor bibin!›» ||| "'But that will be too beautiful!' they said. 'All the guests will be blinded by such magnificence!'"
«‹Pê xema xwe nexwin!› min got. ‹Çi girîng e? Heta ku evîndara min razî be!›» ||| "'Never mind about that!' I said. 'What does it matter? As long as my beloved is satisfied!'"

Madam Hortens guhdarî wî dikir, xwe dabû dîwêr. ||| Dame Hortense listened to him, leaning against the wall.
Bişirîneke fireh û goştî li ser rûyê wê yê qermiçî û şilbûyî belav bû, û şirîta sor a li dora situyê wê hema diqetiya. ||| A wide, fleshy smile spread across her creased and flabby face, and the red ribbon round her neck was well nigh splitting.

«Ez dixwazim di guhê te de bipistînim,» wê ji Zorba re got, çavên xwe yên mezin ên wek yên mihê lê dikir. ||| "I want to whisper in your ear," she said to Zorba, making great sheep's eyes at him.

Zorba çavê xwe li min girt û ber bi pêş ve xwar bû. ||| Zorba winked at me and leaned forward.

«Min îşev tiştek ji te re aniye,» jina wî ya pêşerojê pistand, hema zimanê xwe yê piçûk dixiste guhê wî yê mezin û pirçdar. ||| "I've brought you something tonight," whispered his future wife, almost poking her little tongue into his big hairy ear.

Wê ji bin berstûka xwe destmalek derxist ku quncikek wê girêdayî bû, û ew pêşkêşî Zorba kir. ||| She pulled out of her bodice a handkerchief with one corner knotted, and proffered it to Zorba.

Wî destmala piçûk di navbera du tiliyan de girt û danî ser çoka xwe ya rastê, paşê, zivirî ber bi derî, li deryayê nêrî. ||| He took the little handkerchief between two fingers and placed it on his right knee, then, turning to the door, looked out at the sea.

«Ma tu yê girêkê venekî, Zorba?» wê pirsî. «Tu xuya nakî ku tu di lez de yî!» ||| "Aren't you going to undo the knot, Zorba?" she asked. "You don't seem to be in a hurry!"

«Bila ez pêşî qehweya xwe vexwim û cixareya xwe bikişînim,» wî bersiv da. «Ne hewce ye ez wê vekim, ez dizanim çi tê de heye.» ||| "Let me drink my coffee and smoke my cigarette first," he answered. "I don't have to undo it, I know what there is inside."

«Veke, veke!» sîrena pîr lê lava kir. ||| "Undo it, undo it!" the old siren begged him.

«Ez ê pêşî cixareya xwe biqedînim, ez ji te re dibêjim!» ||| "I'm going to finish my smoke first, I tell you!"

Û wî nihêrîneke tometkar avêt min, mîna ku bibêje: «Ev sûcê te ye!» ||| And he cast a glance of accusation at me, as if to say: "This is your fault!"

Ew hêdî hêdî cixare dikişand, dûyê ji bêvilên xwe derdixist dema ku li deryayê dinêrî. ||| He was smoking slowly, expelling the smoke from his nostrils as he looked at the sea.

«Sibê em ê sîrokoyek bibînin,» wî got. «Hewa guheriye.» ||| "We'll have a sirocco tomorrow," he said. "The weather's changed."
«Dar dê biwerime, û memikên keçên ciwan jî -- ew ê ji berstûkên xwe biteqin! Ax! bihar dirûsek e! Îcadeke şeytan!» ||| "The tree'll swell, and so will young girls' breasts -- they'll be bursting out of their bodices! Ah! spring's a rogue! An invention of the devil!"

Wî dev ji axaftinê berda. Çend kêlî şûnde wî zêde kir: ||| He stopped speaking. A few moments later he added:

##PG 137
«Te bala xwe daye, axa, her tiştê baş di vê dinyayê de îcadeke şeytan e? Jinên bedew, bihar, berxê şilandî yê biraştî, şerab -- şeytan ew hemû çêkirin!» ||| "Have you noticed, boss, everything good in this world is an invention of the devil? Pretty women, spring, roast suckling, wine -- the devil made them all!"
«Xwedê keşîş, rojî, çaya beybûnê û jinên kirêt çêkirin... pûf!» ||| "God made monks, fasting, camomile-tea and ugly women... pooh!"

Dema wî ev got wî nihêrîneke hov avêt Madam Hortensa belengaz, ya ku li quncikekî kombûyî bû, guhdarî wî dikir. ||| As he said that he threw a fierce glance at poor Dame Hortense, who was curled up in a corner, listening to him.

«Zorba! Zorba!» wê her saniye lê lava dikir. ||| "Zorba! Zorba!" she implored him every second.

Lê wî cixareyeke din pêxist û ji nû ve dest bi temaşekirina deryayê kir. ||| But he lit another cigarette and started contemplating the sea afresh.

«Di biharê de,» wî got, «Şeytan bi tevahî serwer e. Kember şil dibin, kiras vedibin, pîrejin dinalin.... Dest bikşîne, Bûbûlîna!» ||| "In the spring," he said, "Satan reigns supreme. Belts are slackened, blouses unbuttoned, old ladies sigh.... Hands off, Bouboulina!"

«Zorba! Zorba!» mexlûqa pîr a belengaz lava kir. Wê xwe xwar kir ku destmalê hilîne û ew xiste destê wî. ||| "Zorba! Zorba!" the poor old creature implored. She stooped to pick up the handkerchief and thrust it into his hand.

Wî cixareya xwe avêt, girêk girt û vekir. ||| He threw away his cigarette, took hold of the knot and undid it.
Wî destê xwe vekirî girt û nêrî. ||| He held his hand open and looked.

«Ev çi ye, Madam Bûbûlîna?» wî bi nefret pirsî. ||| "Whatever's this, Dame Bouboulina?" he asked with disgust.

«Gustîl, gustîlên piçûk, gencîna min. Gustîlên zewacê,» sîrena pîr di bin lêv de got, hemû dilerizî. ||| "Rings, little rings, my treasure. Wedding rings," muttered the old siren, all of a tremble.
«Va ye şahidek, Xwedê wî pîroz bike, şev xweş e, hewaya sîrokoyê ye, Xwedê dinêre, em dest bi dergistiyê bikin, Zorba!» ||| "Here is a witness, God bless him, the night is beautiful, it's sirocco weather, God is watching, let's get engaged, Zorba!"

Zorba niha li min, niha li Madam Hortens, niha li gustîlan dinêrî. ||| Zorba looked now at me, now at Dame Hortense, now at the rings.
Komeke şeytanan di hundirê wî de şer dikirin û ji bo wê kêliyê tu yek li ser nebû. ||| A host of demons were fighting inside him and for the moment none was on top.
Jina belengaz bi tirs lê dinêrî. ||| The wretched woman looked at him in terror.

«Zorba!... Zorbayê min!» wê bi nazikî got. ||| "Zorba!... My Zorba!" she cooed.

Ez li ser nivînê xwe rûniştibûm û dinêrîm. Ji hemû rêyên li ber wî vekirî, Zorba dê kîjanê hilbijêre? ||| I had sat up on my bed and was watching. Of all courses open to him, which was Zorba going to choose?

Ji nişkê ve wî serê xwe hejand. Wî biryara xwe dabû. Rûyê wî vebû, wî destên xwe li hev xistin û firiya. ||| Suddenly he shook his head. He had made his decision. His face cleared, he clapped his hands and leaped up.

«Em herin derve!» wî qîriya. «Di bin stêrkan de, da ku Xwedê bi xwe me bibîne! Tu gustîlan hilgire, axa; tu dikarî bistirê?» ||| "Let's go outside!" he cried. "Beneath the stars, so that God himself can see us! You carry the rings, boss; can you chant?"

«Na,» min bersiv da, kêfxweş. «Lê ev ne girîng e!» Min jixwe ji nivînê xwe xwar firiyabû û alîkariya jinika baş dikir ku rabe. ||| "No," I replied, amused. "But that doesn't matter!" I had already jumped down from the bed and was helping the good lady to get up.

«Baş e, ez dikarim. Min ji bîr kir ku ji te re bibêjim ku ez carekê stranbêjê koroyê bûm; min li dû keşîş diçû di zewac, vaftîz, definkirin û hwd de; min hemû stranên dêrê ji ber hîn bûn.» ||| "Well, I can. I forgot to tell you I was once a choirboy; I used to follow the priest at weddings, baptisms, funerals and so on; I learned all the church songs by heart."
«Were, Bûbûlîna ya min, were, baskê keştiya xwe veke, fîrqata min a piçûk a Frensî, û were ser milê min ê rastê!» ||| "Come, my Bouboulina, come, hoist your sail, my little French frigate, and come on my right!"

Ji hemû şeytanên Zorba, ew lîstikvanê dilqenc bû yê ku bi ser ket. ||| Of all Zorba's demons it was the kind-hearted clown who had won.
Zorba -- dilê wî bi sîrena pîr şewitîbû, dilê wî qetiyabû dema wî dît ku çavên wê yên beloqbûyî ewqas bi xem li wî zoq bûbûn. ||| Zorba had been sorry for the old siren, his heart had been torn when he saw her faded eyes fixed on him so anxiously.

«Bila şeytan min bibe,» wî di bin lêv de got dema ku biryara xwe dida, «ez hê jî dikarim hinek şahiyê bidim mê ya cinsê! Were!» ||| "Devil take me," he muttered as he made his decision, "I can still give some joy to the female of the species! Come on!"

Ew bezî ser peravê, milê Madam Hortens girt, gustîl dan min, zivirî ber bi deryayê û dest bi stranê kir: ||| He rushed out onto the beach, took Dame Hortense's arm, gave me the rings, turned to the sea and began to chant:

«Pîroz be Xudanê me di dinyaya bêdawî de, amîn!» ||| "Blessed be our Lord in the world without end, amen!"

Ew zivirî ber bi min û got: ||| He turned to me and said:

«Karê xwe bike, axa!» ||| "Do your stuff, boss!"

«Îşev tiştek wek ‹axa› tune,» min got. «Ez şahidê te yê sereke me.» ||| "There is no such thing as 'boss' tonight," I said. "I'm your best man."

«Baş e, wê demê hişê xwe li ba xwe bigire. Dema ez biqîrim: ‹Bravo!› tu gustîlan dixî.» ||| "Well, keep your wits about you, then. When I cry out: 'Bravo!' you put the rings on."

Wî dîsa dest bi stranê kir bi zîqîna xwe ya kûr a wek ya kerê: ||| He started chanting again in his deep ass's bray:

##PG 138
«Ji bo bendeyê Xwedê, Aleksîs, û bendeya Xwedê, Hortens, ku niha bi hev re dergistî ne, em rizgariyê dixwazin, ya Xudan.» ||| "For the servant of God, Alexis, and the servant of God, Hortense, now affianced to each other, we beg salvation, O Lord."

«Kyrie eleison! Kyrie eleison!» min bi lerizîn got, bi zehmetî ken û hêsiran kontrol dikirim. ||| "Kyrie eleison! Kyrie eleison!" I quavered, with difficulty controlling laughter and tears.

«Hê gelek kar maye,» Zorba got, «bila ez bimirim eger ez bikaribim wê hemûyê bi bîr bînim! Bi her hal, bila em beşê zehmet derbas bikin!» ||| "There's a lot more business, yet," said Zorba, "damned if I can remember it all! Anyway, let's get the ticklish part over!"

Ew mîna masiyekî hilfiriya hewayê û qîriya: ||| He leaped in the air like a carp and cried:

«Bravo! Bravo!» destên xwe yên mezin ber bi min dirêj kir. ||| "Bravo! Bravo!" holding out his big hands towards me.

«Niha tu destê xwe yê piçûk dirêj bike,» wî ji dergistiya xwe re got. ||| "Now you hold out your little hand," he said to his fiancée.

Destê qelew, ku bi cilşûştin û karê malê xêz xêz bûbû, lerizok ber bi min hat dirêjkirin. ||| The fat hand, lined with washing and housework, was held out trembling towards me.

Min gustîlên wan kir dema ku Zorba, bi tevahî ji xwe çûyî, mîna Derwêşekî diqîriya: ||| I put their rings on while Zorba, quite beside himself, roared out like a Dervish:

«Bendeyê Xwedê, Aleksîs bi bendeya Xwedê, Hortens re dergistî ye, bi navê Xwedê Bav, Kur û Ruhê Pîroz, amîn! Bendeya Xwedê, Hortens bi bendeyê Xwedê, Aleksîs re dergistî ye!» ||| "The servant of God, Alexis is affianced to the servant of God, Hortense, in the name of God the Father, the Son and the Holy Ghost, amen! The servant of God, Hortense is affianced to the servant of God, Alexis!"

«Baş e. Niha, ev heta sala bê qediya! Were vir, şîrîna min, bila ez ramûsana yekem a birûmet û rewa ya ku te heta niha tu carî nedîtiye bidim te!» ||| "Good. Now, that's done till next year! Come here, my sweet, let me give you the first respectable and legitimate kiss you've ever had!"

Lê Madam Hortens ketibû erdê; wê lingên Zorba hembêz dikirin û digiriya. ||| But Dame Hortense had collapsed to the ground; she was clasping Zorba's legs and weeping.
Zorba bi dilovanî serê xwe hejand. ||| Zorba shook his head with compassion.

«Jinên belengaz! Çiqas ehmeq in!» wî di bin lêv de got. ||| "Poor women! What fools they are!" he murmured.

Madam Hortens rabû ser xwe, dawa xwe hejand û destên xwe vekirin. ||| Dame Hortense stood up, shook her skirt and opened her arms.

«Ê, niha!» Zorba qîriya. «Îro Sêşema Berî-Rojiyê ye, dest bikşîne! Rojî ye!» ||| "Eh, now!" shouted Zorba. "It's Shrove Tuesday today, keep your hands off! It's Lent!"

«Zorbayê min....» wê bi qelsî kekeland. ||| "My Zorba...." she faltered faintly.

«Sebir, delala min. Sekine heta Cejna Vejînê; em ê wê demê hinek goşt bixwin, û hêkên sor bi hev re bişkînin.» ||| "Patience, my dear. Wait till Easter; we'll eat some meat then, and crack red eggs together."
«Niha wext e ku tu vegerî malê. Xelk ê çi bibêjin eger te bibînin ku tu heta vê demê ya şevê li vir digerî?» ||| "Now it's time you were getting home. What will folks say if they see you hanging about here till this time of night?"

Nihêrîna Bûbûlîna lavakar bû. ||| Bouboulina's look was imploring.

«Na! Na! Rojî ye!» Zorba got. «Ne berî Cejna Vejînê! Were bi me re.» ||| "No! No! It's Lent!" said Zorba. "Not before Easter! Come along with us."

Ew xwar bû û di guhê min de got: ||| He leaned over and said in my ear:

«Ji bo xatirê Xwedê, me bi tena serê xwe nehêle! Ez ne di kêfê de me!» ||| "Don't leave us alone, for God's sake! I'm not in the mood!"

Em ketin rê ber bi gund. Ezman ron bû, bêhna deryayê me dorpêç kir, çûkên şevê li dora me diqîriyan. ||| We took the road to the village. The sky was bright, the tang of the sea enveloped us, the birds of night hooted about us.
Sîrena pîr, bi milê Zorba ve daliqandî, bextewar lê bêhêvî xwe dikişand. ||| The old siren, hanging on to Zorba's arm, dragged along happy but disappointed.

Wê di dawiyê de ketibû wê bendera ku ewqas bêriya wê kiribû. ||| She had at last entered the harbor she had yearned for so much.

Tevahiya jiyana xwe wê stran gotibû û dans kiribû, demên xweş borandibûn, henek bi jinên rûmetdar kiribû... lê dilê wê perçe perçe bûbû. ||| All her life she had sung and danced, had a high old time, made fun of decent women... but her heart had been torn to shreds.

Dema ku ew, bîhnxweş û bi giranî bi boyaxê reşkirî, bi cilên bilind û geş, di kolanên Îskenderiye, Beyrût, Konstantînopolê re derbas dibû, û jinên ku şîr didan zarokên xwe didît, memikên wê bi xwe dixulixîn û diwerimîn, serê memikên wê derdiketin, ji bo devekî piçûk ê wek yê zarokan dixwestin. ||| When she went by, perfumed and heavily plastered with paint, wearing loud and garish clothes, in the streets of Alexandria, Beirut, Constantinople, and saw women giving the breast to their babies, her own breasts tingled and swelled, her nipples stood out, asking for a tiny childlike mouth as well.
«Mêrekî bistîne, mêrekî bistîne, zarokek bîne....» ev di tevahiya jiyana wê ya dirêj de xewna wê bû. ||| "Get a husband, get a husband, have a child...." that had been her dream throughout her long life.
Lê wê tu carî ev hesretên bi êş ji tu ruhê zindî re eşkere nekirin. ||| But she never revealed these painful longings to a living soul.

Niha, şikir ji Xwedê re, hinekî dereng lê ji qet çêtir, ew dikete wê bendera bêrîkirî, her çend seqet û ji aliyê pêlan ve lêdayî. ||| Now, God be praised, a little late but better than never, she was entering the longed-for haven, though crippled and buffeted by the waves.

##PG 139
Carna wê çavên xwe radikirin û ji kêlekê li wî zilamê dirêj û qerase yê ku li tenişta wê gav diavêt dinêrî. ||| From time to time she raised her eyes and peeped sideways at the great gawk of a fellow who was striding beside her.
«Ew ne paşayekî dewlemend e bi fesekî bi rîşiyên zêrîn,» wê difikirî, «û ew ne kurê bedew ê begek e, lê, şikir ji Xwedê re, ew ji tunebûnê çêtir e! Ew ê bibe mêrê min! Mêrê min her û her, şikir ji Xwedê re!» ||| "He isn't a rich pasha with a gold-tasselled fez," she was thinking, "and he's not the handsome son of a bey, but, God be praised, he's better than nothing! He will be my husband! My husband forever, God be praised!"

Zorba hîs kir ku ew li ser milê wî giran dibû û ew kişand pêş, dilxwaz ku bigihîje gund û jê xilas bibe. ||| Zorba felt her weighing on his arm and dragged her on eager to reach the village and be rid of her.
Û jina belengaz timî li ser keviran di rê de dilikumî; neynûkên lingên wê hema diqetiyan, mêşikên wê diêşiyan, lê wê tu peyv negot. ||| And the poor woman kept tripping over the stones in the road; her toenails were almost torn out, her corns were hurting, but she said not a word.
Çima biaxive? Çima gilî bike? Her tişt spehî bû, şikir ji Xwedê re! ||| Why speak? Why complain? Everything was splendid, praise be to God!

Em di ber Dara Hêjîrê ya Xanima me ya Ciwan û baxçeyê jinebiyê re derbas bûn, û dema malên gund ên yekem xuya bûn em sekinîn. ||| We passed the Fig Tree of Our Young Lady and the widow's garden, and when the first village houses appeared we stopped.

«Şev xweş, gencîna min,» sîrena pîr bi dilovanî got, li ser pencan rabû ku bigihîje lêvên dergistiyê xwe. ||| "Good night, my treasure," said the old siren fondly, standing up on tiptoe to reach her fiancé's lips.

Lê Zorba xwe xwar nekir. ||| But Zorba did not bend.

«Bila ez lingên te ramûsim, evîna min!» Bûbûlîna got, xwe amade dikir ku bikeve erdê. ||| "Let me kiss your feet, my love!" said Bouboulina, making ready to drop to the ground.

«Na! Na!» Zorba îtiraz kir. Ew bandar bû û ew hembêz kir. «Divê ez lingên te ramûsim, evîna min! Divê ez... lê dilê min îşev naçe! Şev xweş!» ||| "No! No!" protested Zorba. He was moved and took her in his arms. "I ought to kiss your feet, my love! I ought to... but I don't feel up to it! Good night!"

Em jê veqetiyan û bê deng li rê çûn, bêhna bîhnxweş dikişandin. Zorba ji nişkê ve zivirî ber bi min. ||| We left her and went in silence along the road, breathing in the scented air. Zorba suddenly turned to me.

«Em ê çi bikin, axa? Bikenin? An bigirîn? Hinek şîretê bide min.» ||| "What ought we to do, boss? Laugh? Or cry? Give me some advice."

Min bersiv neda. Gewriya min jî teng bûbû, û min nikaribû bibêjim çima: ji kenê bû an ji giriyê? ||| I made no answer. I was tight about the throat, too, and could not say why: was it from laughing or crying?

«Axa,» Zorba ji nişkê ve got, «ew xwedayê dirûs kî bû yê ku tu carî nedihişt tu jinek cihê gilîkirinê hebe? Min tiştek li ser bihîstiye, ez dizanim.» ||| "Boss," said Zorba suddenly, "who was that rascally god who would never let a single woman have room for complaint? I've heard something about him, I know."
«Wisa xuya dike ku wî rîha xwe jî boyax dikir, û dil û tîr û sîren li ser milên xwe deq dikirin; ew xwe vedişart, dibêjin: dibû ga, qû, beran, û, bi destûra wî, ker; bi rastî, çi ku van qehpan dixwest.» ||| "It seems he used to dye his beard, too, and tattooed hearts and arrows and sirens on his arms; he used to disguise himself, they say: turned into a bull, a swan, a ram, and, saving his reverence, an ass; in fact, whatever the jades desired."
«Navê wî çi bû?» ||| "What was his name?"

«Divê tu behsa Zeûs bikî. Çi tu xistî bîra wî?» ||| "You must be talking about Zeus. What made you think of him?"

«Xwedê ruhê wî biparêze!» Zorba got, destên xwe bilind kir ber bi ezmên. ||| "God preserve his soul!" said Zorba, raising his arms to heaven.

«Wî demên dijwar dîtin, wî dît! Çi ku divê wî derbas kiribe! Şehîdekî mezin, ji min bawer bike, axa!» ||| "He had some rough times, he did! What he must have gone through! A great martyr, believe me, boss!"
«Tu her tiştê ku pirtûkên te dibêjin daqurtînî, lê tenê kêliyekê bifikire ka mirovên ku pirtûkan dinivîsin çawa ne! Pff! gelek mamosteyên dibistanê.» ||| "You swallow everything your books say, but just think a moment what the people who write books are like! Pff! a lot of schoolmasters."
«Ew li ser jinan, an mêrên ku li pey jinan dibezin, çi dizanin? Tu tişt!» ||| "What do they know about women, or men who run after women? Not the first thing!"

«Çima tu bi xwe pirtûkekê nanivîsî, Zorba? Û hemû nepeniyên dinyayê ji me re rave nakî?» min bi tinaz got. ||| "Why don't you write a book yourself, Zorba? And explain all the mysteries of the world to us?" I sneered.

«Çima na? Ji ber sedemeke sade ku ez van hemû nepeniyan, wek ku tu jê re dibêjî, dijîm, û wextê min tune ku binivîsim.» ||| "Why not? For the simple reason that I live all those mysteries, as you call them, and I haven't the time to write."
«Carna şer e, carna jin in, carna şerab e, carna santûrî ye: ez ê li ku wext bibînim ku qelemeke reben bajom? Loma ev kar dikeve destê qelem-ajoyan!» ||| "Sometimes it's war, sometimes women, sometimes wine, sometimes the santuri: where would I find time to drive a miserable pen? That's how the business falls into the hands of the pen-pushers!"
«Hemû yên ku bi rastî nepeniyên jiyanê dijîn wextê wan tune ku binivîsin, û hemû yên ku wext heye wan najîn! Tu dibînî?» ||| "All those who actually live the mysteries of life haven't the time to write, and all those who have the time don't live them! D'you see?"

«Em vegerin ser mijara xwe! Zeûs çawa bû?» ||| "Let's get back to our subject! What about Zeus?"

«Ax! zilamê belengaz!» Zorba axîn kişand. «Ez yê tenê me ku dizanim wî çi kişand. Wî ji jinan hez dikir, helbet, lê ne bi awayê ku hûn difikirin, hûn qelem-ajo! Qet na!» ||| "Ah! the poor chap!" sighed Zorba. "I'm the only one to know what he suffered. He loved women, of course, but not the way you think, you pen-pushers! Not at all!"
«Dilê wî bi wan dişewitî! Wî fêm dikir ku ew hemû çi dikişandin û wî xwe ji bo xatirê wan qurban dikir!» ||| "He was sorry for them! He understood what they all suffered and he sacrificed himself for their sakes!"
«Dema ku, li kelekek welatê ji-Xwedê-terikandî, wî keçeke pîr a ku bi daxwaz û poşmaniyê dihelya didît,» ||| "When, in some god-forsaken country hole, he saw an old maid wasting away with desire and regret,"

##PG 140
«an bûkeke ciwan a bedew -- an tewra eger ew qet ne bedew bûya, tewra eger ew cinawirek bûya -- û mêrê wê ne li malê û wê nikaribû razêya, ew xaç li xwe dikir, ev zilamê baş, cilên xwe diguhert, çi şeklê ku jinê di hişê xwe de hebû digirt û diçû odeya wê.» ||| "or a pretty young wife -- or even if she wasn't at all pretty, even if she was a monster -- and her husband away and she couldn't get to sleep, he used to cross himself, this good fellow, change his clothes, take on whatever shape the woman had in mind and go to her room."

«Wî tu carî xwe bi jinên ku tenê dixwestin werin nazkirin ne diêşand. Na!» ||| "He never bothered about women who just wanted petting. No!"
«Pir caran tewra ew bi xwe jî bê hal dima: tu dikarî vê fêm bikî.» ||| "Often enough even he was dead-beat: you can understand that."
«Kê dikaribû hemû wan bizinan têr bike? Ax! Zeûs! nêriyê pîr ê belengaz.» ||| "How could anybody satisfy all those she-goats? Ah! Zeus! the poor old goat."
«Zêdetir ji carekê wî nikaribû xwe biwestîne, ew xwe ne pir baş hîs dikir. Te tu carî nêriyek nedîtiye piştî ku wî çend bizin gan kirine?» ||| "More than once he couldn't be bothered, he didn't feel too good. Have you never seen a billy after he's covered several she-goats?"
«Devê wî dilop dike, çavên wî hemû tarî û rijî ne, ew hinekî dikuxe û hema nikare li ser lingên xwe bisekine. Belê, Zeûsê pîr ê belengaz divê pir caran di wê rewşa xemgîn de bûbe.» ||| "He slobbers at the mouth, his eyes are all misty and rheumy, he coughs a bit and can hardly stand on his feet. Well, poor old Zeus must have been in that sad state quite often."

«Di berbangê de ew dihat malê, digot: ‹Ax! Xwedayê min! ez ê kengî bikaribim şevek baş bêhna xwe vedim? Ez dikevim!› Û wî timî gilêz ji devê xwe paqij dikir.» ||| "At dawn he'd come home, saying: 'Ah! my God! whenever shall I be able to have a good night's rest? I'm dropping!' And he'd keep wiping the saliva from his mouth."

«Lê ji nişkê ve wî axînek dibihîst: li jêr li ser erdê jinekê nivîna xwe avêtibû, derketibû balkonê, hema rût, û ewqas axîn dikişand ku dikaribû baskên aşekî bizivirîne!» ||| "But suddenly he'd hear a sigh: down there on earth some woman had thrown off her bedclothes, gone out onto the balcony, almost stark naked, and was sighing enough to turn the sails of a mill!"
«Û Zeûsê min ê pîr bi tevahî dihelya. ‹Of, dojeh! Ez ê neçar bim dîsa daketim!› ew dinaliya. ‹Jinek heye ku li ser bextê xwe dinale! Ez ê neçar bim biçim û wê dilxweş bikim!›» ||| "And my old Zeus would be quite overcome. 'Oh, hell! I'll have to go down again!' he'd groan. 'There's a woman bemoaning her lot! I'll have to go and console her!'"

«Û wisa berdewam bû heta wê astê ku jinan ew bi tevahî vala kirin. Wî nikaribû pişta xwe bilivîne, wî dest bi vereşînê kir, felc bû û mir.» ||| "And it went on like that to such an extent that the women emptied him completely. He couldn't move his back, he started vomiting, became paralyzed and died."
«Wê demê mîratgirê wî, Îsa, hat. Wî rewşa belengaz a ku pîr tê de bû dît: ‹Ji jinan hay ji xwe hebe!› wî qîriya.» ||| "That's when his heir, Christ, arrived. He saw the wretched state the old man was in: 'Beware of women!' he cried."

Min ji taze-fikriya Zorba heyranî kir û ji kenê hejiyam. ||| I admired Zorba's freshness of mind and rocked with laughter.

«Tu dikarî bikenî, axa! Lê eger xweda-şeytan vê hewldana me ya piçûk a li vir biser bixe -- ji min re ne gengaz xuya dike, lê dîsa jî -- tu dizanî ez ê çi cûre dikan vekim?» ||| "You can laugh, boss! But if the god-devil makes our little venture here successful -- it seems impossible to me, but still -- do you know what sort of shop I'll open?"
«Buroyeke zewacê. Erê... rast e. ‹Ajansa Zewacê ya Zeûs›! Hingê jinên belengaz ên ku nekarîne mêrekî bidin der hemû dikarin şanseke din hebin: keçên pîr, jinên sade, çongişkestî, çavxwar, kûzepişt, şeht, û ez ê wan hemûyan di salonek piçûk de bipejirînim bi komeke wêneyan li ser dîwaran ên xortên xweşik,» ||| "A marriage bureau. Yes... that's right. The Zeus Marriage Agency'! Then the poor women who haven't managed to pick up a husband can all have another chance: old maids, plain women, the knock-kneed, the cross-eyed, the humpbacked, the lame, and I shall receive them all in a small lounge with a crowd of photographs on the walls of fine young fellows,"
«û ez ê ji wan re bibêjim: ‹Hilbijartina xwe bikin, xanimno, yê ku hûn dixwazin hilbijêrin, û ez ê dest bi kirina wî mêrê we bikim.›» ||| "and I'll say to them: 'Take your pick, ladies, choose the one you want, and I'll set about making him your husband.'"
«Hingê ez ê her zilamê ku hinekî dişibe wêneyê bibînim, wî bi heman awayî bi cil bikim, hinek pere bidim wî û jê re bibêjim: ‹Kolana filan, hejmara bêvan, here û Xanima filankes bibîne û bi hêz evînê lê bike.›» ||| "Then I'll find any fellow who looks a bit like the photo, dress him up the same, give him some money and tell him: 'So-and-so Street, such-and-such a number, go and see Miss What's-it and make violent love to her.'"
«‹Bizar nebe; ez ê bihayê wê bidim. Pê re raze. Hemû tiştên xweş ên ku mêrek tu carî ji jinekê re dibêje jê re bibêje; wê tu carî tu yek ji wan nebihîstine, mexlûqa belengaz. Sond bixwe ku tu yê bi wê re bizewicî.›» ||| "'Don't be disgusted; I'll pay for it. Sleep with her. Tell her all the nice things a man ever tells a woman; she's never heard any of them, poor creature. Swear you'll marry her.'"
«‹Hinek kêfê bide wê belengazê, ew cûre kêfa ku bizinan heye, û tewra kîsel û kêzikên sed-lingî jî heye.›» ||| "'Give the poor wretch a bit of pleasure, the sort of pleasure nanny-goats have, and even tortoises and centipedes.'"

«Û eger pîrejinek mîna Bûbûlîna me ya pîr derketa holê -- Xwedê wê pîroz bike! -- û tu kes razî nebûya ku wê dilxweş bike, çiqas ku min bidaya wî jî, baş e... ez ê xaç li xwe bikira, û ez, rêvebirê buroya zewacê, ez ê bi xwe wê bikira!» ||| "And if some old nanny turned up on the lines of our old Bouboulina -- God bless her! -- and nobody would agree to console her, no matter how much I paid him, well... I'd cross myself, and I, director of the marriage bureau, would do it in person!"
«Hingê tu yê bibihîstaya ku hemû ehmeqên pîr ên taxê digotin: ‹Lê binêre! Çi rindekê pîr! Ma çavên wî tune ku bibîne an pozê wî tune ku bîhn bike?›» ||| "Then you'd hear all the old fools of the neighborhood saying: 'Look at that! What an old rake! Hasn't he any eyes to see or nose to smell with?'"
«‹Erê, hûn komek kerin, çavên min hene! Erê, hûn destek galegalvanên dilkevir in, pozê min heye! Lê dilê min jî heye, û dilê min bi wê dişewite! Û eger we dilek hebe,›» ||| "'Yes, you bunch of donkeys, I have got eyes! Yes, you pack of flinthearted gossips, I have got a nose! But I've got a heart, too, and I'm sorry for her! And if you've"

##PG 141
«‹dilek hebe, bê kêr e ku hemû çav û pozên dinyayê hebin. Dema wext tê, ew qet nayên hesibandin!›» ||| "got a heart, it's no use having all the eyes and noses in the world. When the time comes, they don't count a jot!'"

«Hingê, dema ku ez bi xwe bi tevahî bêhêz bibim, ji ber çandina tovên kovî, û ez bimirim, Pêtrosê Pîroz ê Dergevan dê deriyê Bihiştê ji min re veke: ‹Were hundir, Zorba, zilamê belengaz,› ew ê bibêje; ‹were hundir, Zorbayê şehîd.›» ||| "Then, when I'm absolutely impotent myself, through sowing wild oats, and I peg out, Saint Peter the Porter will open the gate of Paradise to me: 'Come in, Zorba, poor fellow,' he'll say; 'come in, Zorba the martyr.'"
«‹Here û li tenişta hevalê xwe, Zeûs, dirêj bibe! Bêhna xwe vede, kalo, te para xwe li ser erdê kir! Bereketa min li ser te be!›» ||| "'Go and lie down beside your comrade, Zeus! Rest, old chap, you did your bit on earth! My blessing on you!'"

Zorba berdewam kir diaxivî. Xeyala wî jê re xefik datanîn û ew rast diket nav wan. Wî dest pê kir ku bi çîrokên xwe bawer bike. ||| Zorba went on talking. His imagination laid traps for him and he fell right into them. He began to believe in his own stories.
Dema em di ber Dara Hêjîrê ya Xanima me ya Ciwan re derbas dibûn, wî axîn kişand. Paşê destên xwe dirêj kir mîna ku sond dixwar, wî got: ||| As we were passing the Fig Tree of Our Young Lady, he sighed. Then holding out his arms as though swearing an oath, he said:

«Xem neke, Bûbûlîna, keştiya pîr a belengaz, xerakirî, rizyayî. Xem neke! Ez ê te bê tesellî nehêlim!» ||| "Don't fret, Bouboulina, poor ill-treated, rotting old hulk. Don't fret! I won't leave you without consolation!"
«Dibe ku tu ji aliyê çar Hêzên Mezin ve, ji aliyê ciwaniyê ve, û tewra ji aliyê Xwedê bi xwe ve hatibî terikandin, lê ez, Zorba, ez ê te terk nekim!» ||| "You may have been abandoned by the four great Powers, by youth, and even by God himself, but I, Zorba, will not abandon you!"

Piştî nîvê şevê bû dema ku em vegeriyan peravê, û ba radibû. ||| It was after midnight when we got back to the beach, and the wind was rising.
Ji wir, ji Afrîkayê, Notus dihat, bayê germ ê başûr ê ku daran, rezan û memikên Krîtê diwerimîne. ||| From yonder, from Africa, came the Notus, the warm south wind which swells out the trees, the vines, and the breasts of Crete.
Tevahiya giravê, çawa li ber avê razayî bû, di bin bêhna germ a vî bayî de ku xun dide rabûnê, hat jiyanê. ||| The whole island, as it lay by the water, came to life beneath the warm breath of this wind which makes the sap begin to rise.
Zeûs, Zorba û bayê başûr tevlihev bûn, û di şevê de min bi zelalî rûyekî mêr ê mezin dît, bi rîha reş û porê rûnî, ku xwe xwar dikir û lêvên xwe yên germ ên sor li ser Madam Hortens, Erdê, dipelçiqand. ||| Zeus, Zorba and the south wind mingled together, and in the night I distinctly saw a great male face, with black beard and oily hair, bending down and pressing hot red lips on Dame Hortense, the Earth.
"""

CH20 = r"""
##PG 141
##FIRST
HEMA KU em gihîştin, em ketin nav nivînan. Zorba bi razîbûnî destên xwe li hev dixişand. ||| AS SOON as we arrived, we went to bed. Zorba rubbed his hands together in satisfaction.

«Ev rojeke baş bû, patron. ||| "This has been a good day, boss.
Ez texmîn dikim tê ji min bipirsî ku mebesta min ji ‹baş› çi ye? ||| I suppose you'll ask me what I mean by 'good'?
Mebesta min: tijî. ||| I mean full.
Bifikire: vê sibehê em bi kîlometreyan dûr li keşîşxaneyê bûn, me kar bi serê abat anî -- divê wî nifirên xwe li me kiribin! ||| Just think: this morning we were miles away at the monastery, settling the abbot's hash -- he must have cursed us!
Paşê em hatin xwarê bo koxika xwe, me Madam Bûbûlîna dît û ez bi wê re nîşan bûm. ||| Afterwards we came down here to our hut, found Dame Bouboulina and I got engaged.
Bi awayî, li gustîlê binêre. ||| By the way, look at the ring.
Zêrê safî.... ||| Mint gold....
Wê got hê du sovereignên Îngilîzî hene ku amîralê Îngilîz di dawiya sedsala borî de dabûnê. ||| She said she still had two English sovereigns the English admiral gave her towards the end of last century.
Wê got, ew ji bo defina xwe diparastin; û niha -- bila saet li wê xêrê be -- ew diçe û wan dide zêrînger da ku jê gustîl çêbike. ||| She was keeping them, she said, for her funeral; and now -- may the hour be kind to her -- she goes and gives them to the goldsmith to have rings made of them.
Mirovahî çi sira lanetkirî ye!» ||| What a damned mystery mankind is!"

«Here razê, Zorba!» min got. «Hêdî bibe! ||| "Go to sleep, Zorba!" I said. "Calm down!
Ji bo rojekê ev bes e. ||| That's enough for one day.
Sibê merasîmeke bi rûmet li ber me ye ku em pêk bînin: danîna pîlona yekem a têla me. ||| Tomorrow we have a solemn ceremony to perform: the setting up of the first pylon for our cable.
Min ji Papas Stefanos xwestiye ku bê.» ||| I've asked Pappa Stephanos to come."

«Te baş kir, patron; ev ne fikreke xirab e. ||| "You did well, boss; that's not a bad idea.
Bila ew bê, ew keşîşê pîr ê bi rîha bizinî, û bila hemû giregirên gund jî bên; em ê heta mûmên piçûk jî belav bikin û ew dikarin wan pêxin. ||| Let him come, that old goat-bearded priest, and let all the village notables come as well; we'll even give out little candles and they can light them.
Ev tişt e ku bandorê çêdike; ew ê ji bo karê me baş be. ||| That's the sort of thing to make an impression; it'll be good for our business.

Guh nede tiştê ku ez dikim; Xwedayê min ê xwe û şeytanê min ê xwe heye. ||| Don't take any notice of what I do; I've got my own God and my own devil.
Lê mirovên din....» ||| But other people...."

Wî dest bi kenê kir. ||| He began to laugh.
Ew nikaribû razê; mejiyê wî di nav bahozê de bû. ||| He could not sleep; his brain was in a turmoil.

«Ax, Bapîr, bila Xwedê hestiyên te pîroz bike!» wî piştî demekê got. ||| "Ah, Grandad, may God sanctify your bones!" he said after a time.
«Ew jî serserîkî bû; tam mîna min. ||| "He was a rake, too; just like me.
Lê dîsa jî ew bedmestê pîr çû Gora Pîroz û bû hacî (yê ku çûye ziyareta cihên pîroz) -- Xwedê dizane çima! ||| And yet the old rascal went to the Holy Sepulcher and became a hadji God knows why!

##PG 142
Dema ew vegeriya gund, yek ji hevalên wî, dizekî bizinan, ê ku di tevahiya jiyana xwe de qet tiştekî rast nekiribû, got: ‹Erê, hevalê min, ma te ji Gora Pîroz perçeyek ji Xaça Pîroz ji min re neanî?› ||| When he got back to the village, one of his cronies, a goat thief, who had never done a decent thing in his life, said: 'Well, my friend, didn't you bring me back a piece of the Holy Cross from the Holy Sepulcher?'

‹Çi mebesta te ye, min ji te re neanî?› bapîrê min ê pîr ê jîr got, ‹Tu dibêjî ez ê te ji bîr bikim? ||| 'What do you mean, didn't I bring you any back?' said my cunning old grandad, 'Do you think I'd forget you?
Îşev were mala min û keşîş jî bi xwe re bîne ku bereketê bide, û ez ê wê radestî te bikim. ||| Come to my house tonight and bring the priest with you to give his blessing and I'll hand it over to you.
Berazekî şîrmij ê biraştî jî bîne, û hinek şerab, da ku bextê me vebe!› ||| Bring a roast sucking pig, too, and some wine, to bring us luck!'

Wê êvarê bapîr çû malê û ji çarçoveya derî, ya ku bi tevahî kurmî bûbû, perçeyekî piçûk ê dar birrî, ne mezintir ji libekî birinc; ew di nav pembûyekî de pêçand, du dilop rûn berdan ser û li bendê ma. ||| That evening grandad went home and cut out of the doorpost, which was all worm-eaten, a small piece of wood, no bigger than a grain of rice; he wrapped it in some wadding, poured a drop or two of oil over it and waited.
Piştî demekê, ew zilam bi keşîş, berazê şîrmij û şerabê re tê. ||| After a time, up comes the fellow in question with the priest, the sucking pig and the wine.
Keşîş şela xwe derdixe û bereketê dide. ||| The priest brings out his stole and gives the blessing.
Bapîr merasîma radestkirina wê perçeya dar a giranbiha pêk tîne, û paşê ew dest bi xwarina berazê şîrmij dikin. ||| Grandad performs the ceremony of handing over the precious piece of wood, and then they start devouring the sucking pig.
Erê, bawer bike, patron, zilam li ber wê perçeya dar a piçûk çemiya û xwe devariskand, ew li dora situyê xwe daleqand, û ji wê rojê û pê ve bû mirovekî bi tevahî din. ||| Well, believe me, boss, the fellow bowed and prostrated himself before that little piece of wood, hung it round his neck, and from that day forth was another man altogether.
Ew bi temamî guherî. ||| He changed completely.
Ew hilkişiya çiyan, beşdarî Armatol û Kleftan bû, û alîkariya şewitandina gundên Tirkan kir. ||| He went up into the mountains, joined the Armatoles and Klephts, and helped to burn Turkish villages.
Ew bê tirs di nav baranên gullan re direviya. ||| He'd run fearlessly through showers of bullets.
Çima divê ew bitirsiya? ||| Why should he be afraid?
Ew perçeyek ji Xaça Pîroz a ji Gora Pîroz hildigirt -- gulle nikaribûn lê bikevin.» ||| He was carrying a piece of the Holy Cross from the Holy Sepulcher -- the bullets couldn't hit him."

Zorba bi qehqehe keniya. ||| Zorba burst out laughing.

«Fikir her tişt e,» wî got. «Bawerî bi te heye? Hingê pizdarek ji deriyekî kevn dibe bermayiyeke pîroz. ||| "The idea's everything," he said. "Have you faith? Then a splinter from an old door becomes a sacred relic.
Bawerî bi te tune? Hingê tevahiya Xaça Pîroz bi xwe ji te re dibe çarçoveya deriyekî kevn.» ||| Have you no faith? Then the whole Holy Cross itself becomes an old doorpost to you."

Min ji vî mirovî heyranî girt, yê ku mejiyê wî bi ewqas pêbawerî û wêrekî dixebitî û yê ku giyanê wî, li ku derê ku te lê bida, agir jê dipekiya. ||| I admired this man whose brain functioned with so much confidence and daring and whose soul, wherever you touched it, struck out fire.

«Tu carî çûyî şer, Zorba?» ||| "Have you ever been to war, Zorba?"

«Ez çi dizanim?» wî bi eniya hev-tirîçkirî pirsî. «Nayê bîra min. Kîjan şer?» ||| "How do I know?" he asked with a frown. "I can't remember. What war?"

«Mebesta min, tu carî ji bo welatê xwe şer kiriye?» ||| "I mean, have you ever fought for your country?"

«Ma tu nikarî li ser tiştekî din biaxivî? Ew hemû bêmane qediya û çû, û çêtir e bê jibîrkirin.» ||| "Couldn't you talk about something else? All that nonsense is over and done with and best forgotten."

«Tu jê re dibêjî bêmane, Zorba? Ma şerm nakî? Ma tu wisa li ser welatê xwe diaxivî?» ||| "Do you call that nonsense, Zorba? Aren't you ashamed? Is that how you speak of your country?"

Zorba serê xwe rakir û li min nêrî. ||| Zorba raised his head and looked at me.
Ez jî li ser nivîna xwe dirêjkirî bûm, û lempeya rûn li ser serê min dişewitî. ||| I was lying on my bed, too, and the oil lamp was burning above my head.
Wî demekê bi tundî li min nêrî, paşê, simbêlê xwe bi cidî girt, got: ||| He looked at me severely for a time, then, taking a firm hold of his moustache, said:

«Ev gotineke nîvçe ye; ev tiştê ku ez ji mamosteyekî hêvî dikim. ||| "That's a half-baked thing to say; it's what I expect from a schoolmaster.
Bila bibore ku ez wisa dibêjim, patron, lê axaftina min bi te re ewqas bê kêr e ku çêtir bû ez stranê bibêjim.» ||| I might as well be singing, boss, for all the good it is my talking to you, if you'll pardon my saying so."

«Çi?» min îtiraz kir. «Ez tiştan fêm dikim, Zorba, ji bîr neke.» ||| "What?" I protested. "I understand things, Zorba, don't forget."

##PG 143
«Erê, tu bi mejiyê xwe fêm dikî. ||| "Yes, you understand with your brain.
Tu dibêjî: ‹Ev rast e, û ew şaş e; ev rast e, û ew na; ew rast e, yê din şaş e....› Lê ev me dibe ku derê? ||| You say: 'This is right, and that's wrong; this is true, and that isn't; he's right, the other one's wrong....' But where does that lead us?
Dema tu diaxivî ez li milên te û sîngê te dinêrim. ||| While you are talking I watch your arms and chest.
Erê, ew çi dikin? ||| Well, what are they doing?
Ew bêdeng in. ||| They're silent.
Ew peyvekê jî nabêjin. ||| They don't say a word.
Mîna ku di navbera wan de dilopek xwîn tunebe. ||| As though they hadn't a drop of blood between them.
Ê, te çi digot tu pê fêm dikî? Bi serê xwe? Pûf!» ||| Well, what do you think you understand with? With your head? Bah!"

«De, bersivekê bide min, Zorba; hewl nede ku ji pirsê birevî!» min got, da ku wî bikelijînim. ||| "Come, give me an answer, Zorba; don't try to dodge the question!" I said, to excite him.
«Ez baş bawer im ku tu xwe zêde bi welatê xwe ve mijûl nakî, ne wisa?» ||| "I'm pretty sure you don't bother yourself overmuch about your country, do you?"

Ew hêrs bû û kulma xwe li dîwarê bîdonên benzînê xist. ||| He was angry and banged his fist on the wall of petrol cans.

«Ev zilamê ku tu li pêşberî xwe dibînî,» wî qêriya, «carekê Dêra Aya Sofya bi mûyên serê xwe neqişand, û ew bi xwe re digerand, mîna nuskek li ser sîngê xwe daleqandî. ||| "The man you see here in front of you," he cried, "once embroidered the Church of Saint Sophia in hairs from his own head, and carried it round with him, hanging on his chest like a charm.
Erê, patron, min ev kir, û min ew bi van pencên xwe yên mezin neqişand, û bi van mûyan jî, yên ku wê demê wek qîrê reş bûn. ||| Yes, boss, that's what I did, and I embroidered it with these great paws of mine, and with these hairs, too, which were as black as jet at the time.
Min bi Pavlos Melas (efserekî Yûnanî) re li çiyayên Makedonyayê digeriya -- ez wê demê hêjakî zexm bûm, ji vê koxikê bilindtir, bi fistanê xwe, fesê sor, nuskên zîvîn, tilismat, yataxan, qutiyên fîşekan û tabancan. ||| I used to wander about the mountains of Macedonia with Pavlos Melas -- I was a strapping fellow then, taller than this hut, with my kilt, red fez, silver charms, amulets, yataghan, cartridge cases and pistols.
Ez bi pola, zîv û bişkokan dapoşandî bûm. ||| I was covered with steel, silver and studs.
Dema ez dimeşiyam, dengeke teqereq û şeqîn hebû mîna ku alayek di kuçeyê re derbas dibe! ||| When I marched, there was a clatter and clank as if a regiment were passing down the street!
Li vir binêre! Vir! Û li wir binêre!» ||| Look here! Here! And look there!"

Wî kirasê xwe vekir û şalê xwe daxist. ||| He opened his shirt and lowered his trousers.

«Ronahiyê bîne vir!» wî ferman da. ||| "Bring the light over!" he ordered.

Min lempe nêzîkî laşê wî yê zirav û qewirî kir. ||| I held the lamp close to the thin, tanned body.
Ji ber birînên kûr, şopên gulle û şûran, laşê wî mîna parzûnekê bû. ||| What with deep scars, bullet and sword marks, his body was like a colander.

«Niha li aliyê din binêre!» ||| "Now look at the other side!"

Ew zivirî û pişta xwe nîşanî min da. ||| He turned round and showed me his back.

«Li pişt qet xêzek jî tune, tu dibînî. Tu fêm dikî? Niha lempeyê vegerîne.» ||| "Not a scratch on the back, you see. Do you understand? Now take the lamp back."

«Bêmane!» wî bi hêrs qêriya. «Ev nefretbar e! ||| "Nonsense!" he cried in a rage. "It's disgusting!
Tu çi difikirî, kengî dê mirov bi rastî bibin mirov? ||| When will men really be men, d'you think?
Em şalan li xwe dikin, û kiras û berstû û kumelan, û dîsa jî em hîn jî komek hêstir, rovî, gur û beraz in. ||| We put trousers on, and shirts and collars and hats, and yet we're still a lot of mules, foxes, wolves and pigs.
Em dibêjin em li gorî sûreta Xwedê hatine afirandin! Kî, em? Ez tif dikim ser rûyên me yên ehmeq!» ||| We say we're made in the image of God! Who, us? I spit on our idiotic mugs!"

Xuya bû ku bîranînên tirsnak dihatin bîra wî û ew her diçû bêhntengtir dibû. ||| Terrifying memories seemed to be coming to his mind and he was getting more and more exasperated.
Peyvên nayên fêmkirin ji navbera diranên wî yên lerizok û vala derdiketin. ||| Incomprehensible words issued from between his shaking, hollow teeth.

Ew rabû, cer hilda, vexwarineke dirêj kir û xuya bû ku vehnewiyaye û aramtir bûye. ||| He rose, picked up the water jug, took a long drink and seemed refreshed and calmer.

«Ferq nake li ku derê tu dest li min bidî, ez diqîrim,» wî got. «Ez hemû birîn û şop û werimîn im. ||| "No matter where you touch me, I yell," he said. "I'm all wounds and scars and lumps.
Mebesta te ji wan hemû gotinên pûç ên li ser jinan çi ye? ||| What d'you mean by all that rot about women?
Dema min kifş kir ku ez bi rastî mêr im, min serê xwe jî nezivirand ku li wan binêrim. ||| When I discovered I was really a man, I didn't even turn round to look at them.
Min deqeyekê dest lê dida, wisa, di derbasbûnê de, mîna dîkekî, paşê dewam dikir. ||| I touched them for a minute, like that, in passing, like a cock, then went on.
‹Rasûyên qirêj,› min ji xwe re got. ‹Ew dixwazin hemû hêza min jê bimijin. Pûf! Bila jin biçin dojehê!› ||| 'The dirty ferrets,' I said to myself. 'They'd like to suck me dry of all my strength. Bah! To hell with women!'

«Paşê min tivinga xwe hilda û ez çûm! ||| "Then I picked up my rifle and off I went!
Ez wek komîtacîyekî çûm çiyan. ||| I went into the mountains as a comitadji.
Rojekê, di nav tariyê de, ez ketim gundekî Bulgar û xwe di axurekê de veşart. ||| One day, at dusk, I came into a Bulgarian village and hid in a stable.
##PG 144
Ew rast mala keşîşekî bû, komîtacîyekî Bulgar ê hov û bêrehm. ||| It was the very house of a priest, a ferocious, pitiless Bulgarian comitadji.
Bi şev wî cilûbergê keşîşiyê ji xwe dikir, kincê şivanan li xwe dikir, tivinga xwe hildida û derbas dibû gundên Yûnanî yên cîran. ||| At night he'd take off his cassock, put on shepherd's clothes, pick up his rifle and go over into the neighboring Greek villages.
Berî berbangê vedigeriya, ji herî û xwînê dilop dikir, û bi lez diçû dêrê ku ji bo bawermendan ayîna xwe bike. ||| He came back before dawn, trickling with mud and blood, and hurried to church to conduct mass for the faithful.
Çend roj berî vê, wî mamosteyekî Yûnanî yê ku di nav nivîna xwe de razayî bû kuştibû. ||| A few days before this, he had killed a Greek schoolmaster asleep in his bed.
Loma ez ketim vê axura keşîş û li bendê mam. ||| So I went into this priest's stable and waited.

Ber bi êvarê ve keşîş hat axurê ku ajalan xwedî bike. ||| Towards nightfall the priest came into the stable to feed the animals.
Min xwe avêt ser wî û qirika wî mîna mihê jêkir. ||| I threw myself on him and cut his throat like a sheep.
Min guhên wî jêkirin û xistin berîka xwe. ||| I lopped off his ears and stuck them in my pocket.
Min koleksiyonek ji guhên Bulgaran çêdikir, tu dibînî; loma min guhên keşîş hildan û çûm. ||| I was making a collection of Bulgar ears, you see; so I took the priest's ears and made off.

«Çend roj şûnde, va ez dîsa li gund bûm. ||| "A few days later, there I was in the village again.
Nîvro bû. ||| It was midday.
Ez firotvaniya kolanê dikir. ||| I was peddling.
Min çekên xwe li çiyan hiştibûn û hatibûm xwarê ku ji bo yên din nan, xwê û potîn bikirim. ||| I'd left my arms in the mountains and had come down to buy bread, salt and boots for the others.
Paşê li ber yekî ji malan ez rastî pênc zarokên piçûk hatim -- ew hemû bi reş li xwe kiribû, pêxwas, dest bi destê hev girtî û pars dikirin. ||| Then I met five little kids in front of one of the houses -- they were all dressed in black, barefoot, holding one another by the hand and begging.

Sê keç û du kur. ||| Three girls and two boys.
Ê mezin nedikaribû ji deh salî zêdetir bûya, ê biçûk hîn pitik bû. ||| The eldest couldn't have been more than ten, the youngest was still a baby.
Keça herî mezin a biçûk di hembêza xwe de hildigirt, ramûsan dikir û nazê wî dikir da ku negirî. ||| The eldest girl was carrying the youngster in her arms, kissing him and caressing him so that he shouldn't cry.
Nizanim çima, dibe ku îlhama îlahî, lê ez ber bi wan ve çûm. ||| I don't know why, divine inspiration I suppose, but I went up to them.

‹Hûn zarokên kê ne?› min bi Bulgarî ji wan pirsî. ||| "'Whose children are you?' I asked them in Bulgarian.

Kurê herî mezin serê xwe yê piçûk rakir. ||| The eldest boy raised his little head.

‹Yên keşîş. Qirika bavê me wê rojê di axurê de hat jêkirin,› wî bersiv da. ||| "'The priest's. Father's throat was cut the other day in the stable,' he answered.

Hêsir hatin çavên min û erd dest pê kir ku mîna kevirê aşê bizivire. ||| The tears came to my eyes and the earth began turning round like a millstone.
Min xwe da dîwêr, û ew rawestiya. ||| I leaned against the wall, and it stopped.

‹Werin vir, zarokno,› min got, ‹werin nêzîkî min.› ||| "'Come here, children,' I said, 'come near to me.'

Min berîka xwe ya pere derxist; ew tijî lîreyên Tirkî û mecîdî bû, ez çûm ser çokan û min hemû rijandin ser erdê. ||| I took out my purse; it was full of Turkish pounds and mejidies, I knelt down and poured them all out on the floor.

‹Vaye, hildin!› min qêriya. ‹Hildin! Hildin!› ||| "'There, take them!' I cried. 'Take them! Take them!'

Zarokan xwe avêtin erdê û peran berhev kirin. ||| The children threw themselves on the ground and gathered up the money.

‹Ji we re ye! Ji we re ye!› min qêriya. ‹Hemûyî hildin!› ||| "'It's for you! It's for you!' I cried. 'Take it all!'

Paşê min selika xwe bi hemû tiştên ku min kirîbûn ji wan re hişt. ||| Then I left them my basket with all I had bought.

‹Ew hemû jî ji we re ne; hemûyî hildin!› ||| "'All that's for you, too; take it all!'

Û ez rabûm çûm. ||| "And I cleared out.
Min gund terikand, kirasê xwe vekir, Aya Sofya ya ku min neqişandibû girt û perçe perçe kir, ew avêt û bi hemû hêza xwe reviyam. ||| I left the village, opened my shirt, seized the Saint Sophia I had embroidered and tore it to shreds, threw it away and ran for all I was worth.

Û ez hîn jî direvim....» ||| And I'm still running..."

Zorba xwe da dîwêr, û ber bi min ve zivirî. ||| Zorba leaned against the wall, and turned towards me.

«Wisa bû ku ez xilas bûm,» wî got. ||| "That was how I was rescued," he said.

«Ji welatê xwe xilas bûyî?» ||| "Rescued from your country?"

«Erê, ji welatê xwe,» wî bi dengekî bicidî û aram got. ||| "Yes, from my country," he said in a firm, calm voice.

Paşê piştî kêliyekê: ||| Then after a moment:

«Ji welatê xwe, ji keşîşan, û ji peran xilas bûm. ||| "Rescued from my country, from priests, and from money.
Min dest pê kir ku tiştan biparzinînim, her diçû tiştên zêdetir ji xwe diparzinandin. ||| I began sifting things, sifting more and more things out.
Bi vî awayî ez barê xwe sivik dikim. ||| I lighten my burden that way.
Ez -- çawa bibêjim? -- ez rizgariya xwe dibînim, ez dibim mirov.» ||| I -- how shall I put it? -- I find my own deliverance, I become a man."

Çavên Zorba dibiriqîn, devê wî yê mezin bi razîbûnî keniya. ||| Zorba's eyes glowed, his large mouth laughed contentedly.

Piştî ku kêlîkek-du bêdeng ma, dîsa dest pê kir. ||| After staying silent a moment or two he started off again.
Dilê wî dirijiya, nikaribû xwe ragire. ||| His heart was overflowing, he couldn't control it.

##PG 145
«Demek hebû ku min digot: ew zilam Tirk e, an Bulgar e, an Yûnanî ye. ||| "There was a time when I used to say: that man's a Turk, or a Bulgar, or a Greek.
Min ji bo welatê xwe tiştên ku porê serê te radike kirine, patron. ||| I've done things for my country that would make your hair stand on end, boss.
Min qirikên mirovan jêkirine, gund şewitandine, jin talan kirine û destdirêjî wan kirine, malbatên temam ji holê rakirine. ||| I've cut people's throats, burned villages, robbed and raped women, wiped out entire families.
Çima? ||| Why?
Ji ber ku ew Bulgar bûn, an Tirk. ||| Because they were Bulgars, or Turks.
‹Pûf! Here dojehê, te beraz!› carinan ez ji xwe re dibêjim. ‹Yekser here dojehê, te ker.› ||| 'Bah! To hell with you, you swine!' I say to myself sometimes. 'To hell with you right away, you ass.'
Van rojan ez dibêjim ev zilam camêrekî baş e, ew yek herambeze. ||| Nowadays I say this man is a good fellow, that one's a bastard.
Ew dikarin Yûnanî an Bulgar an Tirk bin, ferq nake. ||| They can be Greeks or Bulgars or Turks, it doesn't matter.
Ew baş e? An xirab e? Ev tenê tiştê ku ez van rojan dipirsim. ||| Is he good? Or is he bad? That's the only thing I ask nowadays.

«Û her ku ez kal dibim -- ez vê li ser parîkê dawî yê ku ez dixwim sond dixwim -- ez hîs dikim ku ez ê wê pirsê jî êdî nepirsim! ||| "And as I grow older -- I'd swear this on the last crust I eat -- I feel I shan't even go on asking that!
Mirov baş be an xirab be, ez bi halê wî dişewitim, bi halê wan hemûyan. ||| Whether a man's good or bad, I'm sorry for him, for all of 'em.
Dîtina mirovekî hema hundirê min diqelişîne, tevî ku ez xwe wisa nîşan didim ku qet xema min nake! ||| The sight of a man just rends my insides, even if I act as though I don't care a damn!
Va ye, belengazê reben, ez difikirim; ew jî dixwe û vedixwe û evînê dike û ditirse, kî dibe bila bibe: Xwedayê wî û şeytanê wî yê wek her kesî heye, û ew ê bimire û mîna texteyekî hişk di bin erdê de dirêj bibe û bibe xwarina kurman, wek her kesî. ||| There he is, poor devil, I think; he also eats and drinks and makes love and is frightened, whoever he is: he has his God and his devil just the same, and he'll peg out and lie as stiff as a board beneath the ground and be food for worms, just the same.
Belengazê reben! Em hemû bira ne! Hemû goştê kurman! ||| Poor devil! We're all brothers! All worm meat!"

«Û eger jin be.... Ax! hingê ez tenê dixwazim çavên xwe bigirîm! ||| "And if it's a woman.... Ah! then I just want to cry my eyes out!
Tu, patronê hêja, her tinazên xwe bi min dikî û dibêjî ez zêde ji jinan hez dikim. ||| Your honored self, boss, keeps teasing me and saying I'm too fond of the women.
Çima ez ji wan hez nekim, dema ew hemû mexlûqên qels in ku nizanin çi dikin û eger tu tenê memikên wan bigirî di cih de teslîm dibin... ||| Why shouldn't I be fond of 'em, when they're all weak creatures who don't know what they're doing and surrender on the spot if you just catch hold of their breasts...

«Carekê ez ketim gundekî din ê Bulgar. ||| "Once I went into another Bulgarian village.
Û hovekî pîr ê ku min dîtibû -- ew rûspîyê gund bû -- ji yên din re got û wan mala ku ez lê bûm dorpêç kir. ||| And one old brute who'd spotted me -- he was a village elder -- told the others and they surrounded the house I was lodging in.
Ez xilmaş bûm derketim eywanê û ji banê yekî gihîştim yê din; heyv hilatibû û ez mîna pisîkekê ji eywanekê dibazdam yê din. ||| I slipped out onto the balcony and crept from one roof to the next; the moon was up and I jumped from balcony to balcony like a cat.
Lê wan siya min dît, hilkişiyan ser banan û dest bi gulebaranê kirin. ||| But they saw my shadow, climbed up on to the roofs and started shooting.
Êdî ez çi bikim? ||| So what do I do?

Ez ketim hewşê, û li wir min jineke Bulgar a di nav nivînan de dît. ||| I dropped down into the yard, and there I found a Bulgarian woman in bed.
Ew bi kincê xwe yê şevê rabû ser xwe, ez dîtim û devê xwe vekir ku biqîre, lê min destên xwe dirêj kirin û pistandin: ‹Rehmê! Rehmê! Neqîre!› û memikên wê girtin. ||| She stood up in her nightdress, saw me and opened her mouth to shout, but I held out my arms and whispered: 'Mercy! Mercy! Don't shout!' and seized her breasts.
Ew zer bû û nîvco ji hiş çû. ||| She went pale and half swooned.

‹Were hundir,› wê bi dengekî nizm got. ‹Were hundir da ku em neyên dîtin....› ||| "'Come inside,' she said in a low voice. 'Come in so that we can't be seen....'

Ez ketim hundir, wê destê min girt: ‹Tu Yûnanî yî?› wê got. ||| I went inside, she gripped my hand: 'Are you a Greek?' she said.
‹Erê, Yûnanî. Min ne îxbar bike.› Min ew ji navtengê girt. ||| 'Yes, Greek. Don't betray me.' I took her by the waist.
Wê peyvek jî negot. ||| She said not a word.
Ez bi wê re ketim nav nivînan, û dilê min ji kêfê dilerizî. ||| I went to bed with her, and my heart trembled with pleasure.
‹Vaye, Zorba, te seg,› min ji xwe re got, ‹jinek li ber te ye; mirovahî ev e! ||| 'There, Zorba, you dog,' I said to myself, 'there's a woman for you; that's what humanity means!
Ew çi ye? Bulgar? Yûnanî? Papua? Ev tişta herî dawî ye ku girîng e! ||| What is she? Bulgar? Greek? Papuan? That's the last thing that matters!
Ew mirov e, û mirovekî bi dev, û bi memik, û dikare hez bike. ||| She's human, and a human being with a mouth, and breasts, and she can love.
Ma tu ji kuştinê şerm nakî? Pûf! Beraz!› ||| Aren't you ashamed of killing? Bah! Swine!'

«Wisa min difikirî dema ez bi wê re bûm, germahiya wê parve dikir. ||| "That's the way I thought while I was with her, sharing her warmth.
Lê tu difikirî ku wê delîya har, welatê min, min ji bo wê bi hêminî bihişt? ||| But did that mad bitch, my country, leave me in peace for that, do you think?
Sibê zû ez bi kincên ku jina Bulgar da min winda bûm. ||| I disappeared next morning in the clothes the Bulgar woman gave me.
Ew jinebî bû. ||| She was a widow.
Wê kincên mêrê xwe yê mirî ji sindoqekê derxistin, dan min, û çokên min hembêz kirin û ji min lava kir ku ez vegerim ba wê. ||| She took her late husband's clothes out of a chest, gave them to me, and she hugged my knees and begged me to come back to her.

Erê, erê, ez vegeriyam... şeva paşê. ||| "Yes, yes, I did go back... the following night.
Ez wê demê welatperwer bûm, helbet -- canewerekî hov; ez bi bîdonek nefta vegeriyam û agir berda gund. ||| I was a patriot then, of course -- a wild beast; I went back with a can of paraffin and set fire to the village.
Divê ew bi yên din re şewitî be, belengaza reben. ||| She must have been burnt along with the others, poor wretch.
Navê wê Ludmîlla bû.» ||| Her name was Ludmilla."

Zorba axîn kişand. ||| Zorba sighed.
Wî cixareyek pêxist, careke-du kişand û paşê ew avêt. ||| He lit a cigarette, took one or two puffs and then threw it away.

##PG 146
«Welatê min, tu dibêjî?... Tu bawerî bi hemû wan pûçên ku pirtûkên te ji te re dibêjin dikî...? ||| "My country, you say?... You believe all the rubbish your books tell you...?
De, ez ew im ku divê tu bawerî pê bînî. ||| Well, I'm the one you should believe.
Heta ku welat hebin, mirov dê mîna heywanekî bimîne, heywanekî hov.... ||| So long as there are countries, man will stay like an animal, a ferocious animal....
Lê ez ji wan hemûyan xilas bûme, şikir ji Xwedê re! ||| But I am delivered from all that, God be praised!
Ji bo min ew qediya! Tu çi?» ||| It's finished for me! What about you?"

Min bersiv neda. ||| I didn't answer.
Min çavnebariya vî mirovî dikir. ||| I was envious of the man.
Wî bi goşt û xwîna xwe jiyabû -- şer dikir, dikuşt, ramûsan dikir -- ew hemû ku min hewl dabû tenê bi pênûs û hibrê fêr bibim. ||| He had lived with his flesh and blood -- fighting, killing, kissing -- all that I had tried to learn through pen and ink alone.
Hemû kêşeyên ku min hewl dida xal bi xal di tenêtiya xwe de û bi kursiya xwe ve zeliqî çareser bikim, vî mirovî li jor di hewaya paqij a çiyan de bi şûrê xwe çareser kiribûn. ||| All the problems I was trying to solve point by point in my solitude and glued to my chair, this man had solved up in the pure air of the mountains with his sword.

Min çavên xwe girtin, bê tesellî. ||| I closed my eyes, inconsolable.

«Tu razayî, patron?» Zorba bi aciziyê got. «Va ye ez, mîna ehmeqekî, bi te re diaxivim!» ||| "Are you asleep, boss?" said Zorba, vexed. "Here I am, like a fool, talking to you!"

Ew bi gilîgilî dirêj bû, û pir zû min bihîst ku ew dixir. ||| He lay down grumbling, and very soon I heard him snoring.

Ez tevahiya şevê nikaribûm razêm. ||| I was not able to sleep all night.
Bilbilekî ku me wê şevê cara yekem bihîst tenêtiya me bi xemgîniyeke nayê ragirtin tijî kir û ji nişkê ve min hêsir li ser hinarokên xwe hîs kirin. ||| A nightingale we heard for the first time that night filled our solitude with an unbearable sadness and suddenly I felt the tears on my cheeks.

Ez difetisîm. ||| I was choking.
Ez bi berbangê rabûm û ji deriyê koxika xwe li erd û deryayê nêrî. ||| I rose at dawn and gazed at the earth and the sea from the doorway of our hut.
Wisa li min hat ku cîhan di şevekê de hatibû guhertin. ||| It seemed to me that the world had been transformed overnight.
Li hemberî min li ser qûmê, gulîçkek darên stirîdar, yên ku roja berê rengekî bêkêf û tarî hebû, niha bi kulîlkên piçûk ên spî daleqandî bûn. ||| Opposite me on the sand, a small clump of thorny bushes, which had been a miserable dull color the day before, was now covered with tiny white blossoms.
Di hewayê de bêhneke şîrîn û dilkêş a darên lîmon û porteqalan ên kulîlkvedayî dihat. ||| In the air hung a sweet, haunting perfume of lemon and orange trees in flower.
Ez çend gav derketim derve. ||| I walked out a few steps.
Ez tu carî nikaribûm têra xwe li vê mucîzeya her-dubarbûyî binêrim. ||| I could never see too much of this ever-recurring miracle.

Ji nişkê ve min li pişt xwe qêrîneke bextewar bihîst. ||| Suddenly I heard a happy cry behind me.
Zorba rabûbû û nîv-tazî ber bi derî ve bazdabû. ||| Zorba had risen and rushed to the door, half-naked.
Ew jî bi vê dîmena biharê hejiyabû. ||| He, too, was thrilled by this sight of spring.

«Ew çi ye?» wî matmayî pirsî. «Ew mucîzeya li wir, patron, ew şînahiya bi livîn, jê re çi dibêjin? ||| "What is that?" he asked stupefied. "That miracle over there, boss, that moving blue, what do they call it?
Derya? Derya? Û ew çi ye ku pêşmaleke kesk a kulîlkdar li xwe kiriye? ||| Sea? Sea? And what's that wearing a flowered green apron?
Erd? Kî ew hunermend bû ku ev çêkir? ||| Earth? Who was the artist who did it?
Cara yekem e ku ez wê dibînim, patron, sond dixwim!» ||| It's the first time I've seen that, boss, I swear!"

Çavên wî tijî hêsir bûbûn. ||| His eyes were brimming over.

«Zorba!» min qêriya. «Ma tu ji aqilê xwe çûyî?» ||| "Zorba!" I cried. "Have you gone off your head?"

«Tu bi çi dikenî? Ma tu nabînî? Li pişt wan hemûyan efsûn heye, patron.» ||| "What are you laughing at? Don't you see? There's magic behind all that, boss."

Ew bazda derve, dest bi reqsê kir û mîna canîkî di biharê de di nav giyayê de digevizî. ||| He rushed outside, began dancing and rolling in the grass like a foal in spring.

Roj derket û min lepên xwe ber bi germahiyê ve vekirin. ||| The sun appeared and I held out my palms to the warmth.
Xuna ku radibû... sîngê ku diwerimî... û giyan jî mîna darekê kulîlk vedida; mirov dikaribû hîs bike ku laş û giyan ji heman maddeyê hatibûn hevîrkirin. ||| Rising sap... the swelling breast... and the soul also blossoming like a tree; you could feel that body and soul were kneaded from the same material.

Zorba dîsa rabûbû ser xwe, porê wî tijî xunav û ax. ||| Zorba had stood up again, his hair full of dew and earth.

«Bilez, patron!» wî qêriya. «Em ê xwe li xwe bikin û xwe xweşik bikin! ||| "Quick, boss!" he shouted. "We'll dress and make ourselves smart!
Îro em ê bên pîrozkirin. ||| Today we are to be blessed.
Ne dûr e ku keşîş û giregirên gund li vir bin. ||| It won't be long before the priest and the village notables are here.
Eger ew me wisa di nav giyayê de gevizî bibînin, ev ê ji bo şîrketê riswayî be! ||| If they find us grovelling in the grass like this it will be a disgrace to the firm!
Loma berstû û qiravatan li xwe bike! Rûyên cidî deynin! ||| So on with the collars and ties! Out with the serious faces!
Qet ne girîng e eger serê te tunebe, divê tu cureyê rast ê kumî li xwe bikî...! Cîhaneke dîn e!» ||| It doesn't matter a damn if you have no head, you must wear the right sort of hat...! It's a crazy world!"

Me xwe li xwe kir, karker hatin, û demek kin piştî wan giregir. ||| We dressed, the workmen arrived, and soon after them the notables.

«Biryara xwe bide, patron, îro tu henek tune! Divê em xwe nexînin rewşeke biken.» ||| "Make your mind up, boss, no fooling today! We mustn't make ourselves look ridiculous."

Papas Stefanos li pêş dimeşiya bi cilûbergê xwe yê keşîşiyê yê qirêj ê bi berîkên kûr. ||| Pappa Stephanos walked in front in his dirty cassock with its deep pockets.
Di merasîmên pîrozkirinê, definan, zewacan, vaftîzan de, wî her tiştê ku jê re dihat pêşkêşkirin diavêt nav van berîkên bêbinî: tirî, nanê hûr, kuloçên penîr, xiyar, perçeyên goşt, şîrîniyên şekirî, her tişt... ||| At consecration ceremonies, funerals, marriages, baptisms, he would throw into these abysmal pockets anything he was offered: raisins, rolls, cheese pies, cucumbers, bits of meat, sugared sweets, everything...
û bi şev, jina wî, Papadiya ya pîr, berçavkên xwe li xwe dikir û her tiştî vediqetand, hemû dem hûrhûr dixwar. ||| and at night, his wife, old Pappadia, would put on her spectacles and sort it all out, nibbling all the time.

##PG 147
Li pişt Papas Stefanos rûspî dihatin: Kondomanolio, xwediyê qehwexaneyê, ê ku digot qey cîhanê nas dike ji ber ku heta Kaneayê çûbû û Prens George bi xwe dîtibû; ||| Behind Pappa Stephanos came the elders: Kondomanolio, the café proprietor, who fancied he knew the world because he had been as far as Canea and had seen Prince George himself;
apê Anagnosti, aram û bişirîn, kirasekî spî yê biriqok ê bi mil-fireh li xwe kiribû; mamoste, giran û bi rûmet bi gopalê xwe, û, ya herî dawî, Mavrandoni, bi gava xwe ya hêdî û giran. ||| uncle Anagnosti, calm and smiling, wearing a wide-sleeved, dazzling white shirt; the schoolmaster, grave and solemn with his stick, and, last of all, Mavrandoni, with his slow, heavy tread.
Wî destmaleke reş li serê xwe, kirasekî reş û pêlavên reş kiribûn; wî bi awayekî bizorê silav li me kir. ||| He wore a black kerchief on his head, a black shirt and black shoes; he acknowledged us with a forced air.
Ew tal û dûr bû. ||| He was bitter and aloof.
Ew piçekî dûrtir rawesta, pişta wî li deryayê. ||| He stood a little apart, his back to the sea.

«Bi navê Xudanê me Îsa Mesîh!» Zorba bi dengekî bi rûmet got. ||| "In the name of Our Lord Jesus Christ!" said Zorba in a solemn voice.
Ew çû serê rêzê û hemûyan bi xwe-civandineke dîndar li pey wî çûn. ||| He went to the head of the procession and all followed him in pious self-communion.

Bîranînên sed-salî yên merasîmên efsûnî di wan sîngên gundiyan de hişyar bûn. ||| Century-old memories of magic ceremonies were awakened in those peasant breasts.
Hemûyan çavên xwe li keşîş miçiqandibûn mîna ku ew hêvî dikirin ku ew li hember hêzên nedîtbar rawestê û wan biqewirîne. ||| They all had their eyes riveted on the priest as though they expected him to confront and exorcise invisible forces.
Hezarsalan berê sêhrbaz destên xwe radikirin, ava xwe ya pîroz li hewayê dipijiqand, peyvên nepenî û hemû-hêzdar dikirin pistepist, û cinên xerab direviyan dema ku ruhên baş ji av, ax û hewayê dihatin hawara mirovahiyê. ||| Thousands of years ago the sorcerer raised his arms, sprinkled the air with his holy water, muttered mysterious and all-powerful words, and the evil demons fled while the good spirits came from water, earth and air, to the aid of mankind.

Em gihîştin çalê ku me li ber deryayê kolabû ji bo pîlona yekem a xetê. ||| We arrived at the pit we had dug by the sea to take the first pylon of the line.
Zilaman qurmekî kajê yê pir mezin rakir û rast danî nav çalê. ||| The men raised a huge pine trunk and set it up erect in the hole.
Papas Stefanos şela xwe li xwe kir, bixûrdana xwe hilda û, hemû dem li qurmê dinêrî, dest bi xwendina efsûnê kir: ||| Pappa Stephanos put on his stole, took his censer and, gazing at the trunk all the time, began intoning the exorcism:

«Bila ew li ser kevirê hişk were avakirin, da ku ne ba ne av nikaribe wê bihejîne. Amîn.» ||| "May it be founded on solid rock, that neither wind nor water may shake it. Amen."

«Amîn!» Zorba bi gurmîn got, xaça xwe çêkir. ||| "Amen!" thundered Zorba, crossing himself.

«Amîn!» rûspiyan kir pistepist. ||| "Amen!" murmured the elders.

«Amîn!» karkeran got, ya dawî. ||| "Amen!" said the workmen, last.

«Bila Xwedê karê we pîroz bike û dewlemendiya Birahîm û Îshaq bide we!» keşîşê gund berdewam kir, û Zorba kaxezeke sed drahmî xiste destê wî. ||| "May God bless your work and give you the wealth of Abraham and Isaac!" the village priest continued, and Zorba pushed a hundred drachma note into his hand.

«Bereketa min li ser we be!» keşîş got, gelek razî. ||| "My blessing on you!" said the priest, well content.

Em vegeriyan koxikê, li wir Zorba ji wan hemûyan re şerab û mezeyên rojîgirtinê pêşkêş kirin -- ehtepotê biraştî, sûbiyeya qelandî, fasûlyeya avhilanî û zeytûn. ||| We returned to the hut, where Zorba offered them all wine and lenten hors d'oeuvres -- grilled octopus, fried squid, soaked beans and olives.
Dema ku wan her tişt xwar, rayedar çûn malê. ||| When they had devoured the lot, the officials went off home.

Merasîma efsûnî qediya. ||| The magic ceremony was over.

«Me ew bi rê ve birin baş!» Zorba got, destên xwe li hev dixişand. ||| "We managed to get through that all right!" said Zorba, rubbing his hands.

Wî cilên xwe ji xwe kirin, kincê xwe yê karî li xwe kir û kulingek hilda. ||| He undressed, put on his work clothes and took a pick.

«Werin!» wî ji zilaman re qêriya. «Xaça xwe çêkin û dest bi kar bikin!» ||| "Come on!" he shouted to the men. "Cross yourselves and get on with the work!"

Zorba ji bo tevahiya rojê dîsa serê xwe ranekir. ||| Zorba didn't raise his head again for the rest of the day.

Karkeran her pêncî gavî çalek dikolan, stûnek datanîn, û berdewam dikirin, rasterast ber bi lûtkeya gir ve. ||| Every fifty yards the workmen dug a hole, put in a post, and went on, making a beeline for the summit of the hill.
Zorba dipîva, hesab dikir û ferman dida; wî tevahiya rojê ne dixwar, ne cixare dikişand, ne jî bêhna xwe vedida. ||| Zorba measured, calculated and gave orders; he did not eat, smoke, or take a rest the whole day long.
Ew bi temamî di nav karî de winda bûbû. ||| He was completely absorbed in the job.

«Ev hemû ji ber kirina tiştan bi nîvî ye,» wî pir caran ji min re digot, «gotina tiştan bi nîvî, başbûna bi nîvî, ku cîhan îro di vê tevliheviyê de ye ku tê de ye. ||| "It's all because of doing things by halves," he would often say to me, and "saying things by halves, being good by halves, that the world is in the mess it's in today.
Bi navê Xwedê tiştan wek pêwîst bike! Ji bo her bizmarekî lêdanek baş û tê bi ser dikevî! ||| Do things properly by God! One good knock for each nail and you'll win through!
Xwedê ji nîv-şeytanekî deh caran zêdetir nefret dike ji serşeytanekî!» ||| God hates a half-devil ten times more than an archdevil!"

Wê êvarê, dema ji kar hat, ew westiyayî li ser qûmê dirêj bû. ||| That evening, when he came in from work, he lay down on the sand, exhausted.

«Ez ê li vir razêm,» wî got. «Ez ê li benda berbangê bimînim, paşê em ê dîsa dest bi kar bikin. Ez ê dest bi şîftên şevê bikim.» ||| "I'm going to sleep here," he said. "I'll wait for dawn, then we'll begin work again. I'm going to start night shifts."

##PG 148
«Çima ev hemû lez, Zorba?» ||| "Why all the hurry, Zorba?"

Ew kêliyekê dudil ma. ||| He hesitated a moment.

«Çima? De, ez dixwazim bibînim ka min nişîva rast dîtiye an na. ||| "Why? Well, I want to see whether I've found the right slope or not.
Eger min nedîtibe, em ji dest çûn. ||| If I haven't, we're done for.
Ma tu nabînî, patron? Çiqas zûtir ez bibînim ka em xera bûne, ewqas çêtir e ji bo me.» ||| Don't you see, boss? The sooner I see if we're dished, the better it'll be for us."

Wî bi lez, bi çikûsî xwar, û demek kin şûnde perav bi xurîniya wî dengvedan. ||| He ate quickly, gluttonously, and soon afterwards the beach echoed to his snores.
Ez, ji aliyê xwe ve, demeke dirêj hişyar mam, li stêrkan dinêrim ku di asîman re digeriyan. ||| I, for my part, stayed awake a long time, watching the stars travel across the sky.
Min dît ku tevahiya asîman cihê xwe diguherand -- û qalikê serê min, mîna qubeya çavdêrxaneyekê, jî cihê xwe diguherand, bi komstêrkan re. ||| I saw the whole sky change its position -- and the shell of my skull, like an observatory dome, changed position, too, together with the constellations.
«Liva stêrkan wisa temaşe bike mîna ku tu bi wan re dizivirî....» ||| "Watch the movement of the stars as if you were turning with them...."

Vê hevoka Marcus Aurelius dilê min bi ahengê tijî kir. ||| This sentence of Marcus Aurelius filled my heart with harmony.
"""

CH22 = r"""
##PG 155
##FIRST
BÊN DARÊN SIPÎNDARAN reqsa cejna Paskê di lûtkeya xwe de bû. ||| BENEATH THE POPLAR TREES the paschal dance was at its height.

Ew ji aliyê xortekî bilind, bedew û esmer ê nêzîkî bîst salî ve dihat birêvebirin, yê ku hinarokên wî bi pirçeke stûr a ku qet hetan nas nekiribû dapoşandî bûn. ||| It was led by a tall, handsome, dark youth of about twenty, whose cheeks were covered with a thick down which had never known a razor.
Di vebûna kirasê wî de sîngê wî leke yeke rengê tarî çêdikir -- ew bi mûyên xelekî dapoşandî bû. ||| In the opening of his shirt his chest made a splash of dark color -- it was covered with curly hair.
Serê wî ber bi paş ve avêtî bû, lingên wî mîna baskan li erdê dixistin; carcaran wî nihêrînek li keçekê dida, û spîtahiya çavên wî bi awayekî domdar û nerehetker ji rûyekî ku ji tavê reş bûbû dibiriqî. ||| His head was thrown back, his feet beating against the earth like wings; from time to time he cast a glance at some girl, and the whites of his eyes gleamed steadily, disturbingly from a visage blackened by the sun.

Ez efsûnî bûm û di heman demê de tirsiyam. ||| I was enchanted and at the same time frightened.
Ez ji mala Madam Hortens vedigeriyam; min jinek gazî kiribû ku miqatî wê be. ||| I was returning from Dame Hortense's house; I had called a woman in to look after her.
Vê ez rehet kirim, û ez hatibûm ku li Krêtiyan temaşe bikim dema reqsê dikirin. ||| This relieved me, and I had come to watch the Cretans dance.
Loma ez çûm cem apê Anagnosti û li ser textekî li kêleka wî rûniştim. ||| So I went up to uncle Anagnosti and sat down on a bench next to him.

«Ew xortê ku reqsê dibe pêş kî ye?» min pirsî. ||| "Who is that young man leading the dance?" I asked.

Apê Anagnosti keniya: ||| Uncle Anagnosti laughed:

«Ew mîna milyaketê serekî ye ku canê te dibe, ew bêbav,» wî bi heyranî got. «Ew Sifakas e, şivan. ||| "He's like the archangel who bears your soul away, the rascal," he said with admiration. "It's Sifakas, the shepherd.
Tevahiya salê ew keriyê xwe li çiyan dipeyitîne, paşê di Paskê de tê xwarê ku mirovan bibîne û reqsê bike.» ||| All the year round he keeps his flock on the mountains, then comes down at Easter to see people and to dance."

Wî axîn kişand. ||| He sighed.

«Ax, xwezî ciwaniya wî ya min hebûya!» wî kir pistepist. «Ger ciwaniya wî ya min hebûya, bi Xwedê! Min ê Stenbol bi êrîşê bigirta!» ||| "Ah, if only I had his youth!" he muttered. "If I had his youth, by God! I'd take Constantinople by storm!"

Xort serê xwe hejand û qêriyek kir, bi awayekî nemirovî dibehirî, mîna beranekî di demsala cotbûnê de. ||| The young man shook his head and gave a cry, bleating inhumanly, like a rutting ram.

«Lê bide, lê bide, Fanurio!» wî qêriya. «Lê bide heta ku Karon bi xwe bimire.» ||| "Play, play, Fanurio!" he shouted. "Play until Charon himself is dead."

Her kêlî mirin dimir û ji nû ve çêdibû, tam mîna jiyanê. ||| Every minute death was dying and being reborn, just like life.

Bi hezaran salan keç û xortên ciwan di biharê de bin pelên nazik ên daran reqs kirine -- bin sipîndar, kaj, mazî, çinar û xurmeyên zirav -- û ew ê bi hezaran salên din jî reqsê bikin, rûyên wan bi arezûyê dagirtî. ||| For thousands of years young girls and boys have danced beneath the tender foliage of the trees in spring -- beneath the poplars, firs, oaks, planes and slender palms -- and they will go on dancing for thousands more years, their faces consumed with desire.
Rû diguherin, dirizin, vedigerin axê; lê yên din radibin ku cihê wan bigirin. ||| Faces change, crumble, return to earth; but others rise to take their place.

Tenê yek reqaspar heye, lê hezar rûçik bi wî re hene. Ew her tim bîst salî ye. Ew nemir e. ||| There is only one dancer, but he has a thousand masks. He is always twenty. He is immortal.

##PG 156
Xort destê xwe rakir ku simbêlê xwe mişt bide, lê yê wî tunebû. ||| The young man raised his hand to stroke his moustache, but he had none.

«Lê bide!» wî dîsa qêriya. «Lê bide, Fanurio, an na ez ê biteqim!» ||| "Play!" he cried again. "Play, Fanurio, or I shall burst!"

Lîrejen destê xwe hejand, lîr bersiv da, zengil bi ritm dest bi tinglîngê kirin û xort yek firqas kir, lingên xwe sê caran li hewayê li hev xistin, bi qasî ku mirovek bilind e, û bi potînên xwe destmala spî ji dora serê cîranê xwe, Manolakas ê pasewan, girt. ||| The lyre player shook his hand, the lyre responded, the bells began to tinkle in rhythm and the young man took one leap, striking his feet together three times on the air, as high as a man stands, and with his boots caught the white kerchief from round the head of his neighbor, Manolakas, the constable.

«Aferîn, Sifakas!» wan qêriya, û keçên ciwan lerizîn û çavên xwe dadan. Lê xort bêdeng bû û li tu kesî qet nedinêrî. ||| "Bravo, Sifakas!" they cried, and the young girls trembled and lowered their eyes. But the young man was silent and not looking at anyone at all.

Hov û lê dîsa bi disîplîn, wî destê xwe yê çep, kefa wî ber bi derve, li ser ranên xwe yên zirav û bihêz danî, dema bi çavên xwe yên bi tirs li erdê miçiqandî reqs dikir. ||| Wild and yet self-disciplined, he rested his left hand, palm outwards on his slim and powerful thighs, as he danced with his eyes fixed timidly on the ground.
Reqs ji nişkê ve sekinî dema xizmetkarê dêrê yê pîr, Androulio, bazda nav meydanê, destên wî ber bi ezman ve rakirî. ||| The dance ceased abruptly as the old verger, Androulio, came rushing into the square, his arms raised to heaven.

«Jinebî! Jinebî!» wî bê nefes qêriya. ||| "The widow! The widow!" he shouted breathlessly.

Manolakas ê pasewan ê yekem bû ku ber bi wî ve bazda, reqs şikand. ||| Manolakas, the constable, was the first to run to him, breaking off the dance.
Ji meydanê tu dikaribû dêrê bibînî, ya ku hîn jî bi şaxên mort û rihanê xemilandî bû. ||| From the square you could see the church, which was still adorned with myrtle and laurel branches.
Reqaspar sekinîn, xwîn di serên wan re diçû, û pîremêr ji cihên xwe rabûn. ||| The dancers stopped, the blood coursing through their heads, and the old men rose from their seats.
Fanurio lîr danî ser çoka xwe, gula nîsanê ji pişt guhê xwe hilda û bêhn kir. ||| Fanurio put the lyre down on his lap, took the April rose from behind his ear and smelled it.

«Li ku, Androulio?» wan qêriya, ji hêrsan dikelîn. «Ew li ku ye?» ||| "Where, Androulio?" they cried, boiling with rage. "Where is she?"

«Di dêrê de; ya belengaz nû ket hundir; baskek kulîlkên lîmonê di hembêza xwe de dianî!» ||| "In the church; the wretch has just gone in; she was carrying an armful of lemon blossom!"

«Werin! Bidin pey wê!» pasewan qêriya, ber bi pêş ve bazda. ||| "Come on! At her!" cried the constable, rushing ahead.

Di wê kêliyê de jinebî li ber deriyê dêrê xuya bû, destmaleke reş li ser serê wê. Wê xaça xwe çêkir. ||| At that moment the widow appeared on the doorstep of the church, a black kerchief over her head. She crossed herself.

«Belengaz! Qehpik! Mêrkuj!» dengan qêriya. «Û rûyê wê heye ku xwe li vir nîşan bide! Bidin pey wê! Wê gund riswa kir!» ||| "Wretch! Slut! Murderess!" the voices cried. "And she's got the cheek to show herself here! After her! She's disgraced the village!"

Hin li pey pasewan çûn ê ku ber bi dêrê ve dibazda, hinên din, ji jor ve, kevir li wê barandin. ||| Some followed the constable who was running towards the church, others, from above, threw stones at her.
Kevirek li milê wê ket; wê qîriya, rûyê xwe bi destên xwe nixumand, û ber bi pêş ve bazda. ||| One stone hit her on the shoulder; she screamed, covered her face with her hands, and rushed forward.
Lê xortan jixwe gihîştibûn deriyê dêrê û Manolakas kêra xwe derxistibû. ||| But the young men had already reached the church door and Manolakas had pulled out his knife.

Jinebî paşde kişiya, qêrînên piçûk ên tirsê derdixistin, xwe ducar kir ku rûyê xwe biparêze û bi pekpekî paşde bazda ku di dêrê de bihewe. ||| The widow drew back uttering little cries of terror, bent herself double to protect her face and ran back stumbling to shelter in the church.
Lê li ser dergeh Mavrandoni yê pîr ros bûbû. Bi destekî li her aliyê derî riya wê girt. ||| But on the threshold was planted old Mavrandoni. With a hand on each side of the door he blocked the way.

Jinebî ber bi çepê ve firqas kir û xwe avêt dara serwa mezin a li hewşê. Kevirek di hewayê re fîqand, li serê wê ket û destmala wê qetand. Porê wê vebû û li ser milên wê belav bû. ||| The widow jumped to the left and clung to the big cypress tree in the courtyard. A stone whistled through the air, hit her head and tore off her kerchief. Her hair came undone and tumbled down over her shoulders.

«Bi navê Mesîh! Bi navê Mesîh!» jinebî qêriya, xwe bi hişkî bi dara serwê girtî. ||| "In Christ's name! In Christ's name!" the widow screamed, clinging tightly to the cypress tree.

Li ser meydanê di rêzekê de rawestayî, keçên ciwan ên gund destmalên xwe yên spî digestin, bi hesret temaşeyî dîmenê dikirin. Pîrejin, xwe dabûn dîwaran, dikirin zûzî: «Wê bikujin! Wê bikujin!» ||| Standing in a row on the square the young girls of the village were biting their white kerchiefs, eagerly watching the scene. The old women, leaning on the walls, were yelping: "Kill her! Kill her!"

Du xortan xwe avêtin ser wê, ew girtin. Kirasê wê yê reş çirand û memikên wê dibiriqîn, spî mîna mermerê. ||| Two young men threw themselves at her, caught her. Her black blouse was torn open and her breasts gleamed, white as marble.
Xwîn ji serê serê wê dadiket xwarê li ser eniya wê, hinarokan û situyê wê. ||| The blood was running from the top of her head down her forehead, cheeks and neck.

«Bi navê Mesîh! Bi navê Mesîh!» wê bê nefes got. ||| "In Christ's name! In Christ's name!" she panted.

##PG 157
Xwîna ku diherikî û memikên ku dibiriqîn xort gurr kiribûn. Kêr ji piştbendên wan xuya bûn. ||| The flowing blood and the gleaming breasts had excited the young men. Knives appeared from their belts.

«Sekinin!» Mavrandoni qêriya. «Ew ya min e!» ||| "Stop!" shouted Mavrandoni. "She's mine!"

Mavrandoni, hîn li ser dergehê dêrê rawestayî, destê xwe rakir. Hemû sekinîn. ||| Mavrandoni, still standing on the threshold of the church, raised his hand. They all stopped.

«Manolakas,» wî bi dengekî kûr got, «xwîna pismamê te gazî te dike. Aramiyê bidê.» ||| "Manolakas," he said in a deep voice, "your cousin's blood is crying out to you. Give him peace."

Ez ji dîwarê ku ez lê hilkişiyabûm firqas kirim û ber bi dêrê ve bazdam; lingê min li keviran ket û ez ketim erdê. ||| I leaped from the wall on which I had climbed and ran towards the church; my foot hit a stone and I fell to the ground.

Tam di wê kêliyê de Sifakas di ber re derbas dibû. Ew xwar bû, ez mîna pisîkekê ji eniya situyê hildam û ez li ser lingan rawestandim. ||| Just at that moment Sifakas was passing. He bent down, picked me up by the scruff of the neck like a cat and put me on my feet.

«Ev ne cihê wek te ye!» wî got. «Here ji vir!» ||| "This is no place for the likes of you!" he said. "Clear off!"

«Ma hîsek ji bo wê bi te re tune, Sifakas?» min pirsî. «Rehmê li wê bike!» ||| "Have you no feeling for her, Sifakas?" I asked. "Have pity on her!"

Çiyayiyê hov li rûyê min keniya. ||| The savage mountaineer laughed in my face.

«Tu min jinekê dihesibînî? Ji min dixwazî ku ez rehmê bikim! Ez mêr im!» ||| "D'you take me for a woman? Asking me to have pity! I'm a man!"

Û di saniyeyekê de ew di hewşa dêrê de bû. ||| And in a second he was in the churchyard.

Ez ji nêz ve li pey wî çûm lê bêhna min çikiyabû. Niha ew hemû li dora jinebî bûn. Bêdengiyeke giran hebû. Tu tenê dikaribû nefesa fetisî ya qurbaniyê bibihîze. ||| I followed him closely but was out of breath. They were all round the widow now. There was a heavy silence. You could hear only the victim's strangled breathing.

Manolakas xaça xwe çêkir, ber bi pêş ve gav avêt, kêr rakir; pîrejinan, jor li ser dîwaran, ji şahiyê zûzî kir. Keçên ciwan destmalên xwe daxistin û rûyên xwe veşartin. ||| Manolakas crossed himself, stepped forward, raised the knife; the old women, up on the walls, yelped with joy. The young girls pulled down their kerchiefs and hid their faces.

Jinebî çavên xwe rakir, kêra li ser xwe dît, û mîna nêçîrekê bizirî. Ew li bin dara serwê hilweşiya û serê wê di navbera milên wê de daket. Porê wê erd nixumand, situyê wê yê lerizok di nîvtariyê de dibiriqî. ||| The widow raised her eyes, saw the knife above her, and bellowed like a heifer. She collapsed at the foot of the cypress and her head sank between her shoulders. Her hair covered the ground, her throbbing neck glistened in the half-light.

«Ez gazî dadweriya Xwedê dikim!» Mavrandoni yê pîr qêriya, û wî jî xaça xwe çêkir. ||| "I call on God's justice!" cried old Mavrandoni, and he also crossed himself.

Lê tam di wê saniyeyê de dengekî bilind li pişt me hat bihîstin: ||| But just at that second a loud voice was heard behind us:

«Kêra xwe daxe, te mêrkuj!» ||| "Lower your knife, you murderer!"

Hemû bi şaşwazî zivirîn. Manolakas serê xwe rakir: Zorba li pêşberî wî rawestayî bû, milên xwe bi hêrs dihejand. Wî qêriya: ||| Everyone turned round in stupefaction. Manolakas raised his head: Zorba was standing before him, swinging his arms with rage. He shouted:

«Ma şerm nakin? Hûn çi mêrên hêja ne! Gundekî temam ku jinekê bikuje! Hay ji xwe bin an na hûn ê tevahiya Krêtê riswa bikin!» ||| "Aren't you ashamed? Fine lot of men you are! A whole village to kill a single woman! Take care or you'll disgrace the whole of Crete!"

«Tu karê xwe bike, Zorba! Û poza xwe ji ya me dûr bigire!» Mavrandoni biriqand. ||| "Mind your own business, Zorba! And keep your nose out of ours!" roared Mavrandoni.

Paşê ew zivirî ber bi biraziyê xwe. ||| Then he turned to his nephew.

«Manolakas,» wî got, «bi navê Mesîh û Meryema Pîroz, lêxe!» ||| "Manolakas," he said, "in the name of Christ and the Holy Virgin, strike!"

Manolakas firqas kir. Wî jinebî girt, avêt erdê, çoka xwe danî ser zikê wê û kêra xwe rakir. Lê di çavtepekekê de Zorba milê wî girtibû û, bi destmala xwe ya mezin a li dora destê wî pêçayî, hewl da ku kêrê ji destê pasewan bikişîne. ||| Manolakas leaped up. He seized the widow, threw her to the ground, placed his knee on her stomach and raised his knife. But in a flash Zorba had seized his arm and, with his big handkerchief wrapped round his hand, strained to pull the knife from the constable's hand.

Jinebî hat ser çokan û li dora xwe gerîya ji bo rêyeke revê, lê gundiyan rê girtibû. Ew di xelekekê de li dora hewşa dêrê bûn û li ser textan rawestayî; dema wan dît ku ew li valahiyekê digere ew ber bi pêş ve hatin û xelek girtin. ||| The widow got onto her knees and looked about her for a way of escape, but the villagers had barred the way. They were in a circle round the churchyard and standing on the benches; when they saw her looking for an opening they stepped forward and closed the circle.

Di vê navê de Zorba, çust, biryardar û aram, bê deng têdikoşiya. Ji cihê xwe yê nêzîkî deriyê dêrê, min bi nigeranî temaşe dikir. ||| Meanwhile Zorba, agile, resolute and calm, was struggling silently. From my place near the church door, I watched anxiously.

##PG 158
Rûyê Manolakas ji hêrsan mor bûbû. Sifakas û dêwekî din ê mêr hatin ku alîkariya wî bikin. Lê Manolakas bi hêrs çavên xwe gêr kirin: ||| Manolakas's face had gone purple with fury. Sifakas and another giant of a man came up to help him. But Manolakas indignantly rolled his eyes:

«Dûr bisekinin! Dûr bisekinin! Tu kes nêzîk nebe!» wî qêriya. ||| "Keep away! Keep away! Nobody's to come near!" he shouted.

Wî dîsa bi hovîtî êrîşî Zorba kir. Wî bi serê xwe mîna gayekî lê da. Zorba lêvên xwe gestin bê ku peyvekê bibêje. Wî milê rastê yê pasewan mîna mengeneyê girt, û ber bi rast û çepê ve xwe diçeland ku ji lêdanên serê pasewan birevê. Ji hêrsan dîn bûyî, Manolakas ber bi pêş ve avêt û guhê Zorba di navbera diranên xwe de girt, û bi hemû hêza xwe wê çirand. Xwîn pijiqî. ||| He attacked Zorba again fiercely. He charged him with his head like a bull. Zorba bit his lips without saying a word. He got a hold like a vise on the constable's right arm, and dodged to right and left to avoid the blows from the constable's head. Mad with rage, Manolakas lunged forward and seized Zorba's ear between his teeth, and tore at it with all his might. The blood spurted.

«Zorba!» min qêriya, tirsiyayî, ber bi pêş ve bazdam ku wî rizgar bikim. ||| "Zorba!" I cried, terrified, rushing forward to save him.

«Dûr keve, patron!» wî qêriya. «Xwe têkilî neke!» ||| "Get away, boss!" he cried. "Keep out of it!"

Wî kulma xwe gulî kir û lêdaneke tirsnak li beşa jêr a zikê Manolakas xist. Cinawirê hov yekser berda. ||| He clenched his fist and hit Manolakas a terrible blow in the lower part of the abdomen. The wild beast let go immediately.

Diranên wî ji hev veqetiyan û guhê nîv-çirandî berdan. Rûyê wî yê mor zer-spîçolkî bû. Zorba ew avêt erdê, kêra wî jê revand û ew avêt aliyê din ê dîwarê dêrê. ||| His teeth parted and set free the half-torn ear. His purple face turned ghastly white. Zorba thrust him to the ground, snatched away his knife and threw it over the church wall.

Wî herikîna xwînê ya ji guhê xwe bi destmala xwe rawestand. Paşê wî rûyê xwe paqij kir, ê ku bi xwêdanê diherikî û rûyê wî bi tevahî bi xwînê leke bû. Wî xwe rast kir, li dora xwe nêrî. Çavên wî werimî û sor bûbûn. Wî ji jinebî re qêriya: ||| He stemmed the flow of blood from his ear with his handkerchief. He then wiped his face, which was streaming with sweat and his face became all smeared with blood. He straightened up, glanced around him. His eyes were swollen and red. He shouted to the widow:

«Rabe! Were bi min re!» ||| "Get up! Come with me!"

Û ew ber bi deriyê hewşa dêrê ve meşiya. ||| And he walked towards the churchyard door.

Jinebî rabû ser xwe; wê hemû hêza xwe kom kir ku ber bi pêş ve bazde. Lê dem wê re tunebû. Mîna baz, Mavrandoni yê pîr xwe avêt ser wê, ew gêr kir, porê wê yê reş ê dirêj sê caran li dora milê xwe pêça û bi lêdaneke kêra xwe serê wê jê kir. ||| The widow stood up; she gathered all her strength together in order to rush forward. But she did not have the time. Like a falcon, old Mavrandoni threw himself on her, knocked her over, wound her long black hair three times round his arm and with a single blow of his knife cut off her head.

«Ez berpirsiyariya vî gunehî digirim ser xwe!» wî qêriya, û serê qurbaniyê avêt ser dergehê dêrê. Paşê wî xaça xwe çêkir. ||| "I take the responsibility for this sin!" he cried, and threw the victim's head on the doorstep of the church. Then he crossed himself.

Zorba li dora xwe nêrî û dîmenê tirsnak dît. Wî simbêlê xwe girt û ji tirsê çend mû jê kişandin. Ez çûm cem wî û milê wî girt. Ew ber bi pêş ve xwar bû û li min nêrî. Du hêsirên mezin li ser bijangên wî daleqandî bûn. ||| Zorba looked round and saw the terrible sight. He gripped his moustache and pulled out a number of hairs in horror. I went up to him and took his arm. He leaned forward and looked at me. Two big tears were hanging on his lashes.

«Em ji vir biçin, patron,» wî bi dengekî fetisî got. ||| "Let's get away, boss," he said in a choking voice.

Wê êvarê Zorba ne tiştek xwar ne jî vexwar. «Qirika min pir teng e,» wî got; «tu tişt naçe xwarê.» Wî guhê xwe bi ava sar şuşt, perçeyek pembû di hinek raqiyê de avêt û banzek çêkir. Li ser doşeka xwe rûniştî, serê xwe di navbera destên xwe de, ew di xeyalan de ma. ||| That evening Zorba would have nothing to eat or drink. "My throat's too tight," he said; "nothing will go down." He washed his ear in cold water, dipped a piece of cotton wool in some raki and made a bandage. Seated on his mattress, his head between his hands, he remained pensive.

Ez jî li ser enîşkên xwe palda bûm dema li erdê li ber dîwêr dirêjkirî bûm, û min hîs kir ku hêsirên germ hêdî hêdî li ser hinarokên min dadiketin. Mejiyê min qet naxebitî, ez li ser tu tiştî nedifikirîm. Ez giriyam, mîna zarokekî ku xemeke kûr ew dagirtibe. ||| I too was leaning on my elbows as I lay on the floor along by the wall, and I felt warm tears run slowly down my cheeks. My brain was not working at all, I was thinking of nothing. I wept, like a child overcome by deep sorrow.

Ji nişkê ve Zorba serê xwe rakir û dilê xwe vala kir. Li pey ramanên xwe yên hov diçû, wî dest bi qêrîna bi dengê bilind kir: ||| Suddenly Zorba raised his head and gave vent to his feelings. Pursuing his savage thoughts, he began to shout aloud:

«Ez ji te re dibêjim, patron, her tiştê ku di vê dinyayê de çêdibe neheq e, neheq e, neheq e! Ez ê nebim hevparê wê! Ez, Zorba, kurm, lîç! Çima divê ciwan bimirin û wêranên pîr berdewam bikin bijîn? ||| "I tell you, boss, everything that happens in this world is unjust, unjust, unjust! I won't be a party to it! I, Zorba, the worm, the slug! Why must the young die and the old wrecks go on living?
Çima zarokên piçûk dimirin? Carekê kurekî min hebû -- jê re Dimitri digotin -- û min ew di sê saliya xwe de winda kir. De... ez ê tu carî, tu carî vê ji Xwedê re nebexşînim, tu dibihîzî? Ez ji te re dibêjim, roja ku ez bimirim, ger wî rûyê wî hebe ku li pêşberî min xuya bibe, û ger ew bi rastî û rastî Xwedê be, ew ê şerm bike! ||| Why do little children die? I had a boy once -- Dimitri he was called -- and I lost him when he was three years old. Well... I shall never, never forgive God for that, do you hear? I tell you, the day I die, if He has the cheek to appear in front of me, and if He is really and truly a God, He'll be ashamed!
##PG 159
Erê, erê, ew ê şerm bike ku xwe nîşanî Zorba, lîç, bide!» ||| Yes, yes, He'll be ashamed to show himself to Zorba, the slug!"

Wî rûyê xwe tirş kir mîna ku di êşê de be. Xwîn dîsa ji birîna wî dest bi herikînê kir. Wî lêvên xwe gestin da ku neqîre. ||| He grimaced as though he was in pain. The blood started flowing again from his wound. He bit his lips so that he should not cry out.

«Sekine, Zorba!» min got. «Ez ê banza te biguherim!» ||| "Wait, Zorba!" I said. "I'll change your dressing!"

Min guhê wî careke din bi raqiyê şuşt, paşê min ava porteqalê ya ku jinebî ji min re şandibû û ku min li ser nivîna xwe dîtibû hilda, û min pembû tê de avêt. ||| I washed his ear once again in raki, then I took the orangewater which the widow had sent me and which I had found on my bed, and I dipped the cotton wool in it.

«Ava porteqalê?» Zorba got, bi dilxwazî wê bêhn dikir. «Ava porteqalê? Hinekî bavêje ser porê min, wisa, dê bikî? Ev e! Û li ser destên min, hemûyî birije, dewam bike!» ||| "Orange water?" said Zorba, eagerly sniffing at it. "Orange water? Put some on my hair, like that, will you? That's it! And on my hands, pour it all out, go on!"

Ew vegeriyabû jiyanê. Ez bi heyranî lê nêrîm. ||| He had come back to life. I looked at him astounded.

«Ez hîs dikim ku ez dikevim baxçeyê jinebî,» wî got. ||| "I feel as though I'm entering the widow's garden," he said.

Û wî dîsa dest bi giriyên xwe kir. ||| And he began his lamentations again.

«Çend salan girt,» wî kir pistepist, «çend salên dirêj ji bo ku erd serkeftî bibe di çêkirina laşekî wisa de! Te lê dinêrî û digot: Ax! xwezî ez bîst salî bûma û tevahiya nijada mirovan ji rûyê erdê winda bûya û tenê ew jin bimaya, û min jê re zarok çêkirana! Na, ne zarok, ew ê xwedayên rastîn bûna.... Lê niha...» ||| "How many years it's taken," he muttered, "how many long years for the earth to succeed in making a body like that! You looked at her and said: Ah! if only I were twenty and the whole race of men disappeared from the earth and only that woman remained, and I gave her children! No, not children, real gods they'd be.... Whereas now..."

Wî xwe avêt ser lingan. Çavên wî bi hêsiran tijî bûn. ||| He leaped to his feet. His eyes filled with tears.

«Ez nikarim li ber bisekinim, patron,» wî got. «Divê ez bimeşim, divê ez îşev du-sê caran li nişîva çiyê hilkişim û dakevim ku xwe biwestînim, xwe hinekî aram bikim.... Ax! ew jinebî! Ez hîs dikim ku divê ez ji bo te mîrologekê (stranek şînê) bibêjim.» ||| "I can't stand it, boss," he said. "I've got to walk, I shall have to go up and down the mountainside two or three times tonight to tire myself, calm myself a bit.... Ah! that widow! I feel I must chant a mirologue for you."

Ew bazda derve, ber bi çiyê ve çû û di tariyê de winda bû. ||| He rushed out, went towards the mountain and disappeared into the darkness.

Ez li ser nivîna xwe dirêj bûm, lempe vemirand û dîsa dest pê kir, bi awayê xwe yê belengaz û nemirovî, ku rastiyê biguherînim, xwîn, goşt û hestiyan jê derdixim û wê dadixim bo ya razber, wê bi qanûnên gerdûnî ve girê didim, heta ku ez gihîştim encama tirsnak ku tiştê qewimî pêwîst bû. Û, hê bêtir, ku ew tevkariya ahenga gerdûnî dikir. Ez gihîştim vê tesellîya dawî û nefretbar: rast bû ku her tiştê ku qewimî divê biqewimiya. ||| I lay down on my bed, turned out the lamp and once more began, in my wretched, inhuman way, to transpose reality, removing blood, flesh and bones and reduce it to the abstract, link it with universal laws, until I came to the awful conclusion that what had happened was necessary. And, what is more, that it contributed to the universal harmony. I arrived at this final and abominable consolation: it was right that all that had happened should have happened.

Kuştina jinebî ket mejiyê min -- kewara ku tê de bi salan hemû jehr veguherîbûn hingivê -- û ew tevlihev kir. Lê felsefeya min yekser hişyariya tirsnak girt, ew bi wêne û fenan dorpêç kir û zû ew bê ziyan kir. Bi heman awayî, mêş kêzika birçî ya ku tê dize hingivê wan dixe nav mûmê dema ku tê. ||| The widow's murder entered my brain -- the hive in which for years all poisons had been changed into honey -- and threw it into confusion. But my philosophy immediately seized upon the dreadful warning, surrounded it with images and artifice and quickly made it harmless. In the same way, bees encase the starving drone in wax when it comes to steal their honey.

Çend saetan şûnde jinebî di bîra min de aram bû, hêmin û aram, veguherî sembolekê. Ew di dilê min de di mûmê de hatibû dorpêçkirin; ew êdî nikaribû tirs di hundirê min de belav bike û mejiyê min felc bike. Bûyerên tirsnak ên wê rojê fireh bûn, di nav dem û cî de dirêj bûn, û bûn yek bi şaristaniyên mezin ên rabirdûyê; şaristanî bûn yek bi qedera erdê; erd bi qedera gerdûnê -- û bi vî awayî, vedigerim bo jinebî, min ew di bin qanûnên mezin ên hebûnê de dît, bi mêrkujên xwe re li hev hatî, bêliv û hêmin. ||| A few hours later the widow was at rest in my memory, calm and serene, changed into a symbol. She was encased in wax in my heart; she could no longer spread panic inside me and paralyze my brain. The terrible events of that one day broadened, extended into time and space, and became one with great past civilizations; the civilizations became one with the earth's destiny; the earth with the destiny of the universe -- and thus, returning to the widow, I found her subject to the great laws of existence, reconciled with her murderers, immobile and serene.
Ji bo min wext wateya xwe ya rastîn dîtibû: jinebî bi hezaran salan berê miribû, di serdema şaristaniya Egeyî de, û keçên ciwan ên Knossosê bi porên xwe yên xelekî tam wê sibehê li ber peravên vê deryaya xweş miribûn. ||| For me time had found its real meaning: the widow had died thousands of years before, in the epoch of the Aegean civilization, and the young girls of Cnossos with their curly hair had died that very morning on the shores of this pleasant sea.

##PG 160
Xew li min bû xwedan, tam wek ku rojekê -- tu tişt ji vê piştir nîne -- mirin dê bibe, û ez bi nermî di tariyê de şemitîm. Min nebihîst kengî Zorba vegeriya, an gelo qet vegeriya. Sibeha din min ew li nişîva çiyê dît, li ser karkeran diqêriya û nifir lê dikirin. ||| Sleep took possession of me, just as one day -- nothing is more certain -- death will do, and I slipped gently into darkness. I did not hear when Zorba returned, or even if he returned. The next morning I found him on the mountainside shouting and cursing at the workers.

Tu tiştê ku wan dikir li gorî dilê wî nebû. Wî sê karkerên ku serhişk bûn ji kar derxistin, kuling bi xwe hilda û dest pê kir ku di nav kevir û çolê re riya ku wî ji bo stûnan nîşan kiribû paqij bike. Ew hilkişiya çiyê, rastî hinek darbiran hat ku kajan dibirîn û dest bi nifirên bahozî kir. ||| Nothing they did was to his liking. He dismissed three workers who were obstinate, took the pick himself and began clearing through the rocks and brush the path which he had marked out for the posts. He climbed the mountain, met some woodcutters who were cutting down the pines and began to thunder abuse.

Yek ji wan keniya û kir pistepist; Zorba xwe avêt ser wî. ||| One of them laughed and muttered; Zorba hurled himself at him.

Wê êvarê ew westiyayî û perçe-perçe hat xwarê bo koxikê. ||| That evening he came down to the hut worn out and in rags.

Ew li kêleka min li ser peravê rûnişt. Wî bi zorê dikaribû devê xwe veke; dema axifî di dawiyê de, ew li ser dar, têl û lînyîtê bû; ew mîna nehêtkarekî çavbirçî bû, di lez de ku cî wêran bike, çiqas ku bikare jê qezenc bike û here. ||| He sat beside me on the beach. He could hardly open his mouth; when he did speak at last, it was about timber, cables and lignite; he was like a grasping contractor, in a hurry to devastate the place, make as much profit out of it as he could and leave.

Di qonaxa xwe-tesellîkirinê ya ku ez gihîştibûmê de, ez carekê li ber bûm ku li ser jinebî biaxivim; Zorba milê xwe yê dirêj dirêj kir û destê xwe yê mezin danî ser devê min. ||| In the stage of self-consolation which I had reached, I was once on the point of speaking about the widow; Zorba stretched out his long arm and put his big hand over my mouth.

«Devê xwe bigire!» wî bi dengekî girtî got. ||| "Shut up!" he said in a muffled voice.

Ez sekinîm, şermisar. Mêrekî rastîn wisa ye, min fikirî, çavnebariya xema Zorba dikir. Mêrekî bi xwîna germ û hestiyên hişk, ê ku dihêle hêsirên rastîn li ser hinarokên wî bazin dema dikişîne; û dema bextewar e ew tendurustiya kêfa xwe xera nake bi derbaskirina wê di parzûna zirav a metafizîkê re. ||| I stopped, ashamed. That is what a real man is like, I thought, envying Zorba's sorrow. A man with warm blood and solid bones, who lets real tears run down his cheeks when he is suffering; and when he is happy he does not spoil the freshness of his joy by running it through the fine sieve of metaphysics.

Sê-çar roj bi vî awayî derbas bûn. Zorba bi domdarî dixebitî, nedisekinî ku bixwe, an vexwe, an bêhna xwe vede. Ew bingehan datanî. ||| Three or four days went by in this way. Zorba worked steadily, not stopping to eat, or drink, or rest. He was laying the foundations.

Êvarekê min behs kir ku Madam Bûbûlîna hîn jî di nav nivînan de ye, ku bijîşk nehatibû û ku ew di hizyana xwe de bê navber gazî wî dikir. ||| One evening I mentioned that Dame Bouboulina was still in bed, that the doctor had not come and that she was continually calling for him in her delirium.

Wî kulmên xwe gulî kirin. ||| He clenched his fists.

«Baş e,» wî bersiv da. ||| "All right," he answered.

Sibeha din bi berbangê ew çû gund û hema yekser piştî wê vegeriya koxikê. ||| The next morning at dawn he went to the village and almost immediately afterwards returned to the hut.

«Te ew dît?» min pirsî. «Ew çawa ye?» ||| "Did you see her?" I asked. "How is she?"

«Tu tişt li wê nebûye,» wî bersiv da, «ew ê bimire.» ||| "Nothing wrong with her," he answered, "she's going to die."

Û ew bi gavên mezin çû ser karê xwe. ||| And he strode off to his work.

Wê êvarê, bê xwarin, wî darê xwe yê stûr hilda û derket. ||| That evening, without eating, he took his thick stick and went out.

«Tu diçî ku derê?» min pirsî. «Bo gund?» ||| "Where are you going?" I asked. "To the village?"

«Na. Ez diçim ji bo gerê. Ez ê zû vegerim.» ||| "No. I'm going for a walk. I'll soon be back."

Ew bi gavên bilez û biryardar ber bi gund ve meşiya. ||| He strode towards the village with fast determined steps.

Ez westiyabûm û çûm razam. Hişê min dîsa xwe da ser derbaskirina tevahiya dinyayê di nirxandinê re; bîranîn hatin, û xem; ramanên min li dora ramanên herî dûr difiriyan lê vedigeriyan û li ser Zorba rûdiniştin. ||| I was tired and went to bed. My mind again set itself to passing the whole world in review; memories came, and sorrows; my thoughts flitted around the most remote ideas but came back and settled on Zorba.

Ger ew tu carî rastî Manolakas were dema li derve ye, min fikirî, ew dêwê Krêtî dê bi hêrseke hov xwe biavêje ser wî. Dibêjin ku van çend rojên dawî ew di hundir de maye. Ew şerm dike ku xwe li gund nîşan bide û her dibêje ku ger Zorba bigire ew ê «wî bi diranên xwe perçe-perçe bike, mîna sardînekê.» Yek ji karkeran got ku wî ew di nîvê şevê de dîtibû ku bi tevahî çekdar li dora koxikê digeriya. Ger ew îşev hev bibînin dê kuştin hebe. ||| If he ever runs across Manolakas while he's out, I thought, that Cretan giant will hurl himself on him in a savage fury. They say that for these last few days he has been staying indoors. He is ashamed to show himself in the village and keeps saying that if he catches Zorba he will "tear him to bits with his teeth, like a sardine." One of the workmen said he had seen him in the middle of the night prowling about the hut fully armed. If they meet tonight there will be murder.

Ez firqas kirim, xwe li xwe kir û bi lez di rê re çûm xwarê bo gund. ||| I leaped up, dressed and hurried down the road to the village.

##PG 161
Hewaya şevê ya hêmin û şil bêhna binefşên çolê dida. Demek şûnde min Zorba dît ku hêdî hêdî, mîna ku pir westiyayî, ber bi gund ve dimeşiya. ||| The calm, humid night air smelled of wild violets. After a time I saw Zorba walking slowly, as if very tired, towards the village.

Carcaran ew disekinî, li stêrkan dinêrî, guhdarî dikir; paşê dîsa dest pê dikir, hinekî bileztir, û min dikaribû dengê darê wî yê li ser keviran bibihîze. ||| From time to time he stopped, stared at the stars, listened; then he started off again, a little faster, and I could hear his stick on the stones.

Ew nêzîkî baxçeyê jinebî dibû. Hewa bi bêhna kulîlkên lîmonê û hingivkulîlkê tijî bû. Di wê kêliyê de, ji darên porteqalê yên di baxçe de, bilbil dest pê kir ku strana xwe ya dilşewat bi notayên zelal mîna ava biharê birijîne. Ew distra û distra di tariyê de bi bedewiyeke bêhnbir. Zorba sekinî, ji şîrîniya stranê bêhna xwe digirt. ||| He was approaching the widow's garden. The air was full of the scent of lemon blossom and honeysuckle. At that moment, from the orange trees in the garden, the nightingale began to pour out its heart-rending song in notes as clear as spring water. It sang and sang in the darkness with breath-taking beauty. Zorba stopped, gasping at the sweetness of the song.

Ji nişkê ve qamîşên çeperê livîn; pelên wan ên tûj mîna tîxên pola li hev ketin. ||| Suddenly the reeds of the hedge moved; their sharp leaves clashed like blades of steel.

«Tu, li wir!» dengekî bilind û hêrsbûyî qêriya. «Te bilûlê pîr ê bêaqil! Va min tu di dawiyê de dîtî!» ||| "You, there!" shouted a loud and furious voice. "You doting old fool! So I've found you at last!"

Xwîna min sar bû. Min deng nas kir. ||| My blood ran cold. I recognized the voice.

Zorba ber bi pêş ve gav avêt, darê xwe rakir û sekinî. Min dikaribû her livîna wî bi ronahiya stêrkan bibîne. ||| Zorba stepped forward, raised his stick and stopped. I could see every one of his movements by the light of the stars.

Mêrekî pir mezin ji çepera qamîşan firqas kir. ||| A huge man leaped out from the reed hedge.

«Kî ye?» Zorba qêriya, situyê xwe dirêj kir. ||| "Who is it?" cried Zorba, craning his neck.

«Ez, Manolakas.» ||| "Me, Manolakas."

«Riya xwe bigire! Bilez ji vir!» ||| "Go your way! Beat it!"

«Çima te ez riswa kirim?» ||| "Why did you disgrace me?"

«Min tu riswa nekirî, Manolakas! Bilez ji vir, ez dibêjim. Tu mêrekî mezin û bihêz î, erê, lê şans li dijî te bû... û şans kor e, te ev nedizanî?» ||| "I didn't disgrace you, Manolakas! Beat it, I say. You're a big, strong fellow, yes, but luck was against you... and luck is blind, didn't you know that?"

«Şans an bêşans, kor an ne kor,» Manolakas got, û min bihîst ku diranên wî dixiriqîn, «ez ê riswayiyê paqij bikim. Û îşev jî. Kêr bi te re heye?» ||| "Luck or no luck, blind or not," said Manolakas, and I heard his teeth grinding, "I'm going to wipe out the disgrace. And tonight, too. Got a knife?"

«Na,» Zorba bersiv da. «Tenê dar.» ||| "No," answered Zorba. "Just a stick."

«Here û kêra xwe bîne. Ez ê li vir bisekinim. Bide!» ||| "Go and fetch your knife. I'll wait here. Go on!"

Zorba neliviya. ||| Zorba did not move.

«Ditirsî?» Manolakas bi tinazî pisand. «Bide, ez ji te re dibêjim!» ||| "Afraid?" hissed Manolakas, in a sneer. "Go on, I tell you!"

«Û ez ê bi kêrê çi bikim?» Zorba pirsî, ê ku dest pê dikir gurr bibe. «Ez ê pê çi bikim? Li dêrê çi qewimî? Wisa tê bîra min ku wê demê kêr bi te re hebû, û ne bi min... lê ez serketî derketim, ne wisa?» ||| "And what would I do with a knife?" asked Zorba, who was beginning to get excited. "What would I do with it? What happened at the church? I seem to remember you had a knife then, and I didn't... but I came out on top, didn't I?"

Manolakas ji hêrsan biriqand. ||| Manolakas roared in fury.

«Tu hewl didî ku min jî bikelijînî, ha? Te dema xelet hilbijart ku tinazan bikî; ji bîr neke ku ez çekdar im û tu ne! Kêra xwe bîne, te Makedonî yê genî, paşê em ê bibînin kî çêtir e.» ||| "Trying to get a rise out of me as well, eh? You've picked the wrong moment to sneer; don't forget I'm armed and you're not! Fetch your knife, you lousy Macedonian, then we'll see who's best."

Zorba milê xwe rakir, darê xwe avêt; min bihîst ku ew nav qamîşan ket. ||| Zorba raised his arm, threw away his stick; I heard it fall among the reeds.

«Kêra xwe biavêje!» wî qêriya. ||| "Throw your knife away!" he cried.

Ez li ser pencan çûbûm cem wan, û di ronahiya stêrkan de min tenê dikaribû biriqîna kêrê bibînim dema ew jî nav qamîşan ket. ||| I had gone up to them on tiptoe, and in the light of the stars I could just see the glitter of the knife as it too fell among the reeds.

Zorba tif kir ser destên xwe. ||| Zorba spat upon his hands.

«Were!» wî qêriya, firqaseke pêşîn di hewayê de kir. ||| "Come on!" he shouted, making a preliminary leap into the air.

Lê berî ku wext bibin ku bi hev bigirin ez ketim navbera wan. ||| But before they had time to come to grips I ran in between them.

«Sekinin!» min qêriya. «Were vir, Manolakas! Û tu, Zorba! Werin vir! Şerm li we be!» ||| "Stop!" I cried. "Here, Manolakas! And you, Zorba! Come here! Shame on you!"

Her du dijber hêdî hêdî ber bi min ve hatin. Min her yek ji destê rastê girt. ||| The two adversaries came slowly towards me. I took each by the right hand.

##PG 162
«Destê hev bigirin!» min got. «Hûn herdu mêrên baş û qewîn in, divê hûn vî nakokiyê çareser bikin.» ||| "Shake hands!" I said. "You are both good, stout fellows, you must patch up this quarrel."

«Wî ez bêrûmet kirim!» Manolakas got, hewl da ku destê xwe paşde bikişîne. ||| "He's dishonored me!" said Manolakas, trying to withdraw his hand.

«Tu kes nikare te ewqas bi hêsanî bêrûmet bike,» min got. «Tevahiya gund dizane ku tu mêrekî wêrek î. Tiştê ku wê rojê li dêrê qewimî ji bîr bike. Saeteke bêbext bû! Tiştê ku qewimî qediya û çû! Û ji bîr neke, Zorba biyaniyek e, Makedonîyek e, û ev riswayiya herî mezin e ku em Krêtî dikarin li ser xwe bînin ku destê xwe li dijî mêvanekî li welatê xwe rakin.... De were, destê xwe bidê, ev camêriya rastîn e -- û were koxikê, Manolakas. Em ê bi hev re vexwin û yard sosîsekê biraştin ku hevaltiya xwe mor bikin!» ||| "No one can dishonor you as easily as that," I said. "The whole village knows you're a brave man. Forget what happened at the church the other day. It was an unlucky hour! What's happened is over and done with! And don't forget, Zorba is a foreigner, a Macedonian, and it's the greatest disgrace we Cretans can bring on ourselves to raise a hand against a guest in our country.... Come now, give him your hand, that's real gallantry -- and come to the hut, Manolakas. We'll drink together and roast a yard of sausage to seal our friendship!"

Min Manolakas ji navtengê girt û ez ew hinekî dûr birim. ||| I took Manolakas by the waist and led him a little apart.

«Belengaz pîr e, ji bîr neke,» min pistand. «Camêrekî bihêz û ciwan ê wek te divê êrîşî mirovekî di temenê wî de neke.» ||| "The poor fellow's old, remember," I whispered. "A strong, young fellow like you shouldn't attack a man of his age."

Manolakas hinekî nerm bû. ||| Manolakas softened a little.

«Baş e,» wî got. «Tenê ji bo ku te kêfxweş bikim.» ||| "All right," he said. "Just to please you."

Ew ber bi Zorba ve gav avêt û destê xwe yê pir mezin dirêj kir. ||| He stepped towards Zorba and held out his huge hand.

«Were, hevalê Zorba,» wî got. «Her tişt qediya û hat jibîrkirin; destê xwe bide min.» ||| "Come, friend Zorba," he said. "It's all over and forgotten; give me your hand."

«Te guhê min cût,» Zorba got, «bila ji te re saxil be! Va destê min!» ||| "You chewed my ear," said Zorba, "much good may it do you! Here's my hand!"

Wan bi hêz destê hev girt, her diçû bi hêztir, li çavên hev dinêrîn. Ez tirsiyam ku ew ê dîsa dest bi şer bikin. ||| They shook hands forcefully, more and more vigorously, looking each other in the eyes. I was afraid they were going to start fighting again.

«Girtina te ya bihêz e, Manolakas,» Zorba got. «Tu mêrekî qewîn î û pir hişk!» ||| "You've got a strong grip, Manolakas," said Zorba. "You're a stout fellow and pretty tough!"

«Destê te jî bihêz e; binêre ka tu dikarî min hê hişktir bigirî.» ||| "You've a strong hand, too; see if you can grip me tighter still."

«Ev bes e!» min qêriya. «Em biçin û hevaltiya xwe bi vexwarinekê mor bikin!» ||| "That's enough!" I cried. "Let's go and seal our friendship with a drink!"

Di riya vegerê bo peravê de ez di navbera wan de meşiyam, Zorba li rastê min û Manolakas li çepê min. ||| On the way back to the beach I walked in between them, Zorba on my right and Manolakas on my left.

«Îsal dê dexlek pir baş hebe...» min got, ji bo ku mijarê biguherim. «Baran pir bariye.» ||| "There'll be a very good harvest this year..." I said, to change the subject. "There's been a lot of rain."

Ne yekî ji wan bersiv da. Ew hîn jî di sîngê xwe de teng bûn. ||| Neither of them answered. They were still tight about the chest.

Hêviya min di şerabê de bû. Em gihîştin koxikê. ||| My hope lay in the wine. We reached the hut.

«Hûn bi xêr hatin mala me ya hêsan,» min got. «Zorba, sosîsê biraşte û tiştek ji bo vexwarinê bibîne.» ||| "Welcome to our humble home," I said. "Zorba, roast the sausage and find something to drink."

Manolakas li ser kevirekî li ber koxikê rûnişt. Zorba kefek çiqil hilda, sosîs biraşt û sê qedeh tijî kirin. ||| Manolakas sat down on a stone in front of the hut. Zorba took a handful of twigs, roasted the sausage and filled three glasses.

«Saxî!» min got, qedeha xwe rakir. «Saxî, Manolakas! Saxî, Zorba! Qedehan li hev bidin!» ||| "Good health!" I said, raising my glass. "Good health, Manolakas! Good health, Zorba! Clink glasses!"

Wan qedehên xwe li hev xistin, û Manolakas çend dilop li ser erdê rijand. ||| They clinked glasses, and Manolakas spilled a few drops on the ground.

«Bila xwîna min mîna vê şerabê birije,» wî bi dengekî bi rûmet got, «ger ez tu carî destê xwe li dijî te rakim, Zorba.» ||| "May my blood run like this wine," he said in a solemn voice, "if ever I raise my hand against you, Zorba."

«Bila xwîna min jî mîna vê şerabê birije,» Zorba got, li wî şopand û çend dilop li ser erdê rijand, «ger min jixwe awayê ku te guhê min cût ji bîr nekiribe!» ||| "May my blood, too, run like this wine," said Zorba, following suit and pouring a few spots on the ground, "if I haven't already forgotten the way you chewed my ear!"
"""

def esc(s):
    return html.escape(s, quote=False)

def build_article(num, data):
    blocks = re.split(r"\n\s*\n", data.strip("\n"))
    out = []
    out.append('<article class="flow chapter">')
    out.append('<h2 class="chapter-num">%s</h2>' % num)
    out.append('<hr class="chapter-rule">')
    for blk in blocks:
        lines = [l for l in blk.split("\n") if l.strip() != ""]
        if not lines:
            continue
        cls = ""
        is_verse = False
        body = []
        for l in lines:
            ls = l.strip()
            if ls == "##FIRST":
                cls = "first"; continue
            if ls == "##VERSE":
                is_verse = True; continue
            m = re.match(r"^##PG\s+(\d+)$", ls)
            if m:
                pg = m.group(1)
                body.append(('pg', pg)); continue
            if "|||" in l:
                ku, en = l.split("|||", 1)
                body.append(('s', ku.strip(), en.strip()))
        if is_verse:
            # one clickable verse block
            ku, en = None, None
            for item in body:
                if item[0] == 's':
                    ku, en = item[1], item[2]
            out.append('<p class="verse"><span class="sent"><span class="ku">%s</span><span class="orig">%s</span></span></p>'
                       % (ku, esc(en)))
            continue
        # normal paragraph
        pcls = ' class="%s"' % cls if cls else ""
        chunk = ['<p%s>' % pcls]
        for item in body:
            if item[0] == 'pg':
                chunk.append('<span class="pagemark" data-page="%s">%s</span> ' % (item[1], item[1]))
            else:
                _, ku, en = item
                chunk.append('<span class="sent"><span class="ku">%s </span><span class="orig">%s</span></span>'
                             % (esc(ku), esc(en)))
        chunk.append('</p>')
        out.append("".join(chunk))
    out.append('</article>')
    return "\n".join(out)

ARTICLE = build_article(10, CH10) + "\n" + build_article(11, CH11) + "\n" + build_article(12, CH12) + "\n" + build_article(13, CH13) + "\n" + build_article(14, CH14) + "\n" + build_article(15, CH15) + "\n" + build_article(16, CH16) + "\n" + build_article(17, CH17) + "\n" + build_article(18, CH18) + "\n" + build_article(19, CH19) + "\n" + build_article(20, CH20) + "\n" + build_article(22, CH22)

HTML_DOC = r"""<!DOCTYPE html>
<html lang="ku">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zorbayê Yûnanî — Nîkos Kazancakîs</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2024%2024%22%3E%3Crect%20width=%2224%22%20height=%2224%22%20rx=%224%22%20fill=%22%23f4ecd2%22/%3E%3Cpath%20d=%22M7%203h10v18l-5-3.4L7%2021z%22%20fill=%22%237a5b1e%22/%3E%3C/svg%3E">
<style>
  @page { size: A4; margin: 30mm 22mm 22mm 22mm; }
  html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body {
    font-family: "Georgia","Times New Roman",serif;
    color:#2a241b; margin:0; text-align:justify;
    hyphens:auto; -webkit-hyphens:auto; line-height:1.62;
  }

  /* ---- Sernavka ku li ser her rûpelî dimîne ---- */
  .run-head{
    position:fixed; top:0; left:0; right:0; z-index:50;
    text-align:center; background:#f4ecd2; cursor:pointer;
    border-bottom:0.6px solid #2a241b; padding:6px 8px 7px;
  }
  .run-head .rh-title{ font-size:13pt; letter-spacing:1px; }
  .run-head .rh-en{ display:block; font-size:8.5pt; font-style:italic; letter-spacing:2px; color:#6b5d44; margin-top:1px; }

  .page{ page-break-after:always; break-after:page; }
  .page:last-child{ page-break-after:auto; }
  .flow{ page-break-after:auto; }

  /* ---- Berg ---- */
  .cover{
    display:flex; flex-direction:column; justify-content:center;
    text-align:center; border:1.5px solid #2a241b; box-sizing:border-box;
    position:relative; padding:18mm 16mm;
  }
  .cover .motif{ font-size:18pt; letter-spacing:8px; margin:0 0 14mm; }
  .cover .title{ font-size:44pt; letter-spacing:1px; line-height:1.08; margin:0; font-weight:normal; }
  .cover .title-en{ font-size:15pt; font-style:italic; letter-spacing:5px; text-transform:uppercase; margin-top:6mm; color:#4a4031; }
  .cover .rule{ width:56mm; border:none; border-top:1px solid #2a241b; margin:11mm auto; }
  .cover .author{ font-size:18pt; letter-spacing:1px; text-align:right; margin:0 2mm 0 0; }
  .cover .subtitle{ font-size:12pt; font-style:italic; letter-spacing:3px; margin-top:9mm; text-align:center; text-transform:uppercase; color:#4a4031; }
  .cover .footer{ position:absolute; bottom:18mm; left:0; right:0; text-align:center; font-size:10pt; letter-spacing:3px; text-transform:uppercase; color:#5a4f3e; }

  /* ---- Beş ---- */
  .chapter-num{ text-align:center; font-size:26pt; margin:2mm 0 2mm; font-weight:normal; }
  .chapter-rule{ width:28mm; border:none; border-top:1px solid #2a241b; margin:0 auto 9mm; }
  p{ margin:0 0 4mm; text-indent:6mm; }
  p.first{ text-indent:0; }
  p.first::first-letter{ font-size:230%; line-height:1; font-weight:bold; padding-right:2px; }
  .verse{ text-indent:0; font-style:italic; margin:5mm 0 5mm 8mm; text-align:left; }

  /* ---- Hevok bi tikandinê: orîjînala îngilîzî li jêr xuya dibe ---- */
  .sent{ cursor:pointer; position:relative; }
  .sent:hover .ku{ background:rgba(120,90,30,0.10); }
  .sent .orig{ display:none; }
  .sent.on .orig{
    display:block; position:relative; text-indent:0; text-align:left;
    margin:3mm 0 3.5mm 7mm; padding:1mm 0 1mm 5mm;
    border-left:2px solid #b9a77d; font-style:italic;
    color:#6b5d44; font-size:0.92em;
  }
  .sent.on .orig::before{ content:"\201C"; }
  .sent.on .orig::after{ content:"\201D"; }

  /* ---- Bilêvkirin (TTS): lîstika dengî ya her hevokê ---- */
  .tts{ display:none; }
  /* lîstik di valahiya çepê ya bloka îngilîzî de radiweste — ne di nav nivîsê de */
  .sent.on .tts{
    display:flex; flex-direction:column; align-items:flex-end; gap:5px;
    position:absolute; top:0; right:100%; margin-right:3.5mm;
    text-indent:0; user-select:none;
  }
  /* bişkojka HTML: çargoşeyek gilover a bi sînor (ne xelek) */
  .tts button{
    -webkit-appearance:none; appearance:none; cursor:pointer;
    display:inline-flex; align-items:center; justify-content:center;
    padding:5px 6px; border-radius:7px; line-height:0;
    background:#f7f0db; border:1px solid #b9a77d; color:#5a4a22;
    transition:background .15s, border-color .15s;
  }
  .tts button:hover{ background:#fff; border-color:#8a7a55; }
  .tts button:disabled{ cursor:default; opacity:.6; }
  .tts svg{ width:15px; height:15px; display:block; fill:none;
    stroke:currentColor; stroke-width:2; stroke-linecap:round; stroke-linejoin:round; }
  .tts-toggle{ padding:6px 8px !important; }
  .tts-speed{ padding:3px 7px !important; border-radius:7px !important;
    font:600 10px "Georgia",serif; line-height:1 !important; color:#5a4a22; }
  /* destek lîstikê yên zêde: tenê dema çalak xuya dibin (li jêr, di valahiyê de) */
  .tts-more{ display:none; flex-direction:column; align-items:flex-end; gap:5px; }
  .tts.active .tts-more{ display:flex; }
  /* spinner — tenê HTML/CSS, bê wêne */
  .tts-spin{ width:14px; height:14px; border-radius:50%;
    border:2px solid #c9bb98; border-top-color:#5a4a22; animation:tts-rot .7s linear infinite; }
  @keyframes tts-rot{ to{ transform:rotate(360deg); } }
  /* peyva ku niha tê xwendin — ronîkirin (heman ruhê reveal accent) */
  .ku .w-on{ background:rgba(150,110,30,.26); border-radius:3px;
    box-shadow:0 0 0 1px rgba(150,110,30,.22); }

  /* ---- Nîşana rûpela PDF-ê (referans) ---- */
  .pagemark{
    display:inline-block; font-size:8pt; color:#9a8a66; letter-spacing:1px;
    border:0.6px solid #cbbd98; border-radius:3px; padding:0 4px; margin:0 5px;
    vertical-align:1px; text-indent:0; cursor:default;
  }
  .pagemark::before{ content:"r."; opacity:.7; margin-right:2px; }

  /* ---- Bara xwendinê: çekmece ji jêr ber bi jor (drawer) ---- */
  .reader-drawer{
    position:fixed; left:0; right:0; bottom:0; z-index:60;
    display:flex; flex-direction:column; align-items:center;
    transform:translateY(calc(100% - 34px));   /* girtî: tenê destik xuya dibe */
    transition:transform .28s ease;
    pointer-events:none;                        /* deverên vala rê li tikandinê venekin */
  }
  .reader-drawer.open{ transform:translateY(0); }
  .reader-drawer > *{ pointer-events:auto; }

  /* destika ku her dem xuya ye (digel rûpela niha) */
  .drawer-handle{
    height:34px; box-sizing:border-box;
    display:flex; align-items:center; gap:9px;
    background:#efe5c8; border:0.6px solid #2a241b; border-bottom:none;
    border-radius:9px 9px 0 0; padding:0 16px; cursor:pointer;
    font-family:"Georgia",serif; font-size:11px; color:#3a3225;
    box-shadow:0 -1px 6px rgba(60,48,20,.15);
  }
  .drawer-handle b{ font-weight:bold; }
  .drawer-handle .dh-arrow{ font-size:10px; transition:transform .28s ease; }
  .reader-drawer.open .drawer-handle .dh-arrow{ transform:rotate(180deg); }

  .reader-bar{
    width:100%; box-sizing:border-box;
    display:flex; gap:7px 9px; align-items:center; justify-content:center; flex-wrap:wrap;
    background:#efe5c8; border-top:0.6px solid #2a241b; padding:6px 9px;
    font-family:"Georgia",serif; font-size:10.5px; color:#3a3225;
  }
  .reader-bar button{
    font:inherit; cursor:pointer; background:#f7f0db; border:0.6px solid #8a7a55;
    border-radius:5px; padding:3px 8px; color:#3a3225;
  }
  .reader-bar button:hover{ background:#fff; }
  .reader-bar select{
    font:inherit; background:#f7f0db; border:0.6px solid #8a7a55;
    border-radius:5px; padding:2px 4px; color:#3a3225; cursor:pointer;
  }
  .reader-bar label{ display:flex; align-items:center; gap:4px; }
  .reader-bar .rb-item b{ font-weight:bold; }
  .reader-bar .rb-flash{ opacity:0; transition:opacity .3s; font-style:italic; color:#6b5d44; min-width:1px; }
  .reader-bar .rb-sep{ width:1px; align-self:stretch; background:#c9bb98; margin:0 2px; }
  .reader-bar .rb-group{ display:flex; align-items:center; gap:5px; }
  .reader-bar input[type=range]{ width:96px; cursor:pointer; accent-color:#8a7a55; vertical-align:middle; }

  /* ---- Ekran: rûpel dagire, kêm valahî li kêlekan ---- */
  @media screen{
    body{ background:#d9ccac; padding:62px 0 44px; font-size:17px; }
    .flow, .cover-host{
      width:100%; max-width:72rem; margin:0 auto; box-sizing:border-box;
      background:#f4ecd2; box-shadow:0 1px 10px rgba(60,48,20,.25);
    }
    .cover-host{ margin-bottom:16px; padding:16px; }
    .flow{ padding:20px 16px 44px; font-size:var(--reader-fs,17px); }
    .cover{ min-height:74vh; }
  }

  /* ---- Moda tarî: heman ruhê kaxezê, lê tarî (tenê li ser ekranê) ---- */
  @media screen{
    body.dark{ background:#211c16; color:#e9ddc4; }
    body.dark .flow, body.dark .cover-host{ background:#322b22; box-shadow:0 1px 12px rgba(0,0,0,.45); }
    body.dark .run-head{ background:#2b251d; border-bottom-color:#b7a47e; }
    body.dark .run-head .rh-en{ color:#c9b48a; }
    body.dark .cover{ border-color:#b7a47e; }
    body.dark .cover .title-en, body.dark .cover .subtitle, body.dark .cover .footer{ color:#c9b48a; }
    body.dark .cover .rule, body.dark .chapter-rule{ border-top-color:#b7a47e; }
    body.dark .sent:hover .ku{ background:rgba(230,210,160,.13); }
    body.dark .sent.on .orig{ color:#cbb78c; border-left-color:#7a6a48; }
    body.dark .tts button{ background:#3a3228; border-color:#6b5d44; color:#e0cfa6; }
    body.dark .tts button:hover{ background:#473a2c; }
    body.dark .tts-spin{ border-color:#5a4f3e; border-top-color:#e0cfa6; }
    body.dark .ku .w-on{ background:rgba(230,200,130,.22); box-shadow:0 0 0 1px rgba(230,200,130,.18); }
    body.dark .pagemark{ color:#b7a47e; border-color:#5a4f3e; }
    body.dark .drawer-handle, body.dark .reader-bar{ background:#2b251d; border-color:#b7a47e; color:#e9ddc4; }
    body.dark .reader-bar{ border-top-color:#b7a47e; }
    body.dark .reader-bar button, body.dark .reader-bar select{ background:#3a3228; border-color:#6b5d44; color:#e9ddc4; }
    body.dark .reader-bar button:hover{ background:#473a2c; }
    body.dark .reader-bar .rb-sep{ background:#5a4f3e; }
    body.dark .reader-bar .rb-flash{ color:#cbb78c; }
    body.dark .reader-bar input[type=range]{ accent-color:#b7a47e; }
  }

  /* her beş li ser rûpeleke nû dest pê dike (di çapê de) */
  .flow + .flow{ page-break-before:always; break-before:page; }

  /* ---- Çap: kaxez spî, tenê Kurmancî, kêm hibir ---- */
  @media print{
    body{ background:#fff; color:#111; padding:0; font-size:12.5pt; }
    .run-head{ display:none !important; }
    .reader-bar, .reader-drawer, .drawer-handle{ display:none !important; }
    .pagemark{ display:none !important; }
    .sent .orig{ display:none !important; }
    .tts{ display:none !important; }
    .ku .w-on{ background:none !important; box-shadow:none !important; }
    .sent:hover .ku{ background:none; }
    .cover{ min-height:247mm; border-color:#111; }
    .cover .rule, .chapter-rule{ border-top-color:#111; }
    .flow, .cover-host{ width:auto; max-width:none; margin:0; padding:0; background:none; box-shadow:none; }
  }
</style>
</head>
<body>

<div class="run-head">
  <span class="rh-title">Zorbayê Yûnanî</span>
  <span class="rh-en">Zorba the Greek</span>
</div>

<section class="page cover-host">
  <div class="cover">
    <div class="motif">&#10086;</div>
    <h1 class="title">Zorbayê<br>Yûnanî</h1>
    <div class="title-en">Zorba the Greek</div>
    <hr class="rule">
    <div class="author">Nîkos Kazancakîs</div>
    <div class="subtitle">Roman</div>
    <div class="footer">Wergera Kurmancî</div>
  </div>
</section>

<!--ARTICLE-->

<div class="reader-drawer" id="reader-drawer">
  <div class="drawer-handle" id="drawer-handle" role="button" tabindex="0" aria-label="Bara xwendinê veke/bigire">
    <span class="dh-arrow">&#9650;</span>
    <span>Rûpel (PDF): <b id="curpage">&mdash;</b></span>
  </div>
  <div class="reader-bar">
    <span class="rb-group">
      <label>Rûpel <select id="page-select"></select></label>
      <label>Beş <select id="chap-select"></select></label>
    </span>
    <span class="rb-sep"></span>
    <button id="bm-set">Şopê deyne</button>
    <button id="bm-go">Here şopê <small id="bm-page"></small></button>
    <span class="rb-sep"></span>
    <span class="rb-group">
      <button id="fs-dn" title="Biçûktir">A&minus;</button>
      <input id="fs-range" type="range" min="12" max="34" step="1" value="17" aria-label="Mezinahiya nivîsê">
      <button id="fs-up" title="Mezintir">A+</button>
    </span>
    <span class="rb-sep"></span>
    <button id="ex-all">Hemûyan veke</button>
    <button id="col-all">Hemûyan bigire</button>
    <span class="rb-sep"></span>
    <button id="theme-toggle" title="Moda tarî / ronahî">Tarî</button>
    <span id="bm-flash" class="rb-flash"></span>
  </div>
</div>

<script>
(function(){
  var KEY='zorba-book:v4';
  var marks=[].slice.call(document.querySelectorAll('.pagemark'));
  var firstPage = marks.length ? marks[0].getAttribute('data-page') : '—';
  var curEl=document.getElementById('curpage');
  var flashEl=document.getElementById('bm-flash');

  // ---- Sernavk: tikandin -> here serî ----
  var rh=document.querySelector('.run-head');
  if(rh) rh.addEventListener('click', function(){ window.scrollTo({ top:0, behavior:'smooth' }); });

  // ---- Moda tarî / ronahî (tê tomarkirin) ----
  var themeKey=KEY+':theme';
  var themeBtn=document.getElementById('theme-toggle');
  function applyTheme(dark){
    document.body.classList.toggle('dark', dark);
    if(themeBtn) themeBtn.textContent = dark ? 'Ronahî' : 'Tarî';
    localStorage.setItem(themeKey, dark ? 'dark' : 'light');
  }
  if(themeBtn) themeBtn.addEventListener('click', function(){
    applyTheme(!document.body.classList.contains('dark'));
  });
  applyTheme(localStorage.getItem(themeKey)==='dark');

  // ---- Çekmece: veke/bigire (girtî di destpêkê de) ----
  var drawer=document.getElementById('reader-drawer');
  var handle=document.getElementById('drawer-handle');
  function toggleDrawer(){ if(drawer) drawer.classList.toggle('open'); }
  if(handle){
    handle.addEventListener('click', toggleDrawer);
    handle.addEventListener('keydown', function(e){
      if(e.key==='Enter'||e.key===' '){ e.preventDefault(); toggleDrawer(); }
    });
  }

  // ---- Birina cî: offset ji bo sernavka jorîn ----
  function jumpTo(el){
    if(!el) return;
    var top = el.getBoundingClientRect().top + window.scrollY - 80;
    window.scrollTo({ top: Math.max(0, top), behavior:'smooth' });
  }

  // ---- Hilbijêrê rûpelê (ji nîşanên ##PG) ----
  var pageSel=document.getElementById('page-select');
  if(pageSel){
    marks.forEach(function(m){
      var p=m.getAttribute('data-page');
      var o=document.createElement('option'); o.value=p; o.textContent=p; pageSel.appendChild(o);
    });
    pageSel.addEventListener('change', function(){
      var m=null;
      for(var i=0;i<marks.length;i++){ if(marks[i].getAttribute('data-page')===this.value){ m=marks[i]; break; } }
      jumpTo(m);
    });
  }

  // ---- Hilbijêrê beşê (ji sernavên beşan) ----
  var chapSel=document.getElementById('chap-select');
  var chapEls=[].slice.call(document.querySelectorAll('.chapter-num'));
  if(chapSel){
    chapEls.forEach(function(h,i){
      var o=document.createElement('option'); o.value=String(i); o.textContent=h.textContent.trim(); chapSel.appendChild(o);
    });
    chapSel.addEventListener('change', function(){ jumpTo(chapEls[parseInt(this.value,10)]); });
  }

  // tikandin -> orîjînala îngilîzî veke/bigire
  var allSents=document.querySelectorAll('.sent');
  allSents.forEach(function(s){
    s.addEventListener('click', function(e){ this.classList.toggle('on'); });
  });

  // veke / bigire HEMÛ wergeran
  var exAll=document.getElementById('ex-all'), colAll=document.getElementById('col-all');
  if(exAll) exAll.addEventListener('click', function(){ allSents.forEach(function(s){ s.classList.add('on'); }); });
  if(colAll) colAll.addEventListener('click', function(){ allSents.forEach(function(s){ s.classList.remove('on'); }); });

  // mezinahiya nivîsê: slider + A- / A+ (tê tomarkirin)
  var fsRange=document.getElementById('fs-range');
  var fsKey=KEY+':fs';
  function applyFs(v){
    v=Math.max(12, Math.min(34, parseInt(v,10)||17));
    document.documentElement.style.setProperty('--reader-fs', v+'px');
    if(fsRange) fsRange.value=v;
    localStorage.setItem(fsKey, String(v));
  }
  if(fsRange) fsRange.addEventListener('input', function(){ applyFs(this.value); });
  var fsDn=document.getElementById('fs-dn'), fsUp=document.getElementById('fs-up');
  if(fsDn) fsDn.addEventListener('click', function(){ applyFs((parseInt(fsRange?fsRange.value:17,10)||17)-1); });
  if(fsUp) fsUp.addEventListener('click', function(){ applyFs((parseInt(fsRange?fsRange.value:17,10)||17)+1); });
  var savedFs=localStorage.getItem(fsKey); applyFs(savedFs!==null?savedFs:17);

  function currentPage(){
    var cur = firstPage;
    for (var i=0;i<marks.length;i++){
      var top = marks[i].getBoundingClientRect().top;
      if (top <= 90) cur = marks[i].getAttribute('data-page');
      else break;
    }
    return cur;
  }
  function refresh(){
    var p=currentPage();
    if(curEl) curEl.textContent = p;
    if(pageSel && pageSel.value!==String(p)) pageSel.value = String(p);
  }

  var ticking=false;
  window.addEventListener('scroll', function(){
    if(!ticking){ window.requestAnimationFrame(function(){
      refresh();
      localStorage.setItem(KEY+':scroll', String(window.scrollY));
      ticking=false;
    }); ticking=true; }
  }, {passive:true});

  function flash(msg){
    if(!flashEl) return;
    flashEl.textContent=msg; flashEl.style.opacity=1;
    clearTimeout(flashEl._t); flashEl._t=setTimeout(function(){flashEl.style.opacity=0;},1900);
  }

  document.getElementById('bm-set').addEventListener('click', function(){
    var p=currentPage();
    localStorage.setItem(KEY+':bm', String(window.scrollY));
    localStorage.setItem(KEY+':bmpage', p);
    var bp=document.getElementById('bm-page'); if(bp) bp.textContent='('+p+')';
    flash('Şop hate danîn — r. '+p);
  });
  document.getElementById('bm-go').addEventListener('click', function(){
    var b=localStorage.getItem(KEY+':bm');
    if(b!==null){ window.scrollTo({top:parseInt(b,10), behavior:'smooth'}); }
    else flash('Tu şop nehatiye danîn');
  });

  window.addEventListener('load', function(){
    var bm=localStorage.getItem(KEY+':bm');
    var sc=localStorage.getItem(KEY+':scroll');
    var target = (bm!==null) ? bm : sc;   // veke -> here cihê şopê / cihê dawî
    if(target!==null){ window.scrollTo(0, parseInt(target,10)); }
    var bp=localStorage.getItem(KEY+':bmpage');
    if(bp){ var e=document.getElementById('bm-page'); if(e) e.textContent='('+bp+')'; }
    refresh();
  });
  refresh();
})();
</script>

<script>
/* ---- Bilêvkirin (TTS): play/pause her hevokê + ronîkirina peyvan ---- */
(function(){
  var API='/api/tts';
  /* îkonên xêzkirî (outline) — wek bişkojkên referansê */
  var ICON={
    play:'<svg viewBox="0 0 24 24"><polygon points="6 4 20 12 6 20 6 4"/></svg>',
    pause:'<svg viewBox="0 0 24 24"><rect x="6" y="4" width="4" height="16" rx="1"/><rect x="14" y="4" width="4" height="16" rx="1"/></svg>',
    restart:'<svg viewBox="0 0 24 24"><polyline points="3 4 3 9 8 9"/><path d="M3.5 9.5A9 9 0 1 1 3 13"/></svg>',
    rw:'<svg viewBox="0 0 24 24"><polygon points="11 5 4 12 11 19 11 5"/><polygon points="20 5 13 12 20 19 20 5"/></svg>',
    ff:'<svg viewBox="0 0 24 24"><polygon points="13 5 20 12 13 19 13 5"/><polygon points="4 5 11 12 4 19 4 5"/></svg>'
  };
  var SPEEDS=[1,1.25,1.5,0.75], speedIdx=0;
  function speedVal(){ return SPEEDS[speedIdx]; }
  function speedLabel(v){ return (v===1?'1':String(v))+'x'; }

  /* ---- Cache: IndexedDB (deng + timestamps tê tomarkirin, careke din bê req) ---- */
  var dbp=(function(){ return new Promise(function(res){
    try{
      var r=indexedDB.open('zorba-tts',1);
      r.onupgradeneeded=function(){ r.result.createObjectStore('audio'); };
      r.onsuccess=function(){ res(r.result); };
      r.onerror=function(){ res(null); };
    }catch(e){ res(null); }
  }); })();
  function cacheGet(key){ return dbp.then(function(db){ if(!db) return null; return new Promise(function(res){
    try{ var q=db.transaction('audio','readonly').objectStore('audio').get(key);
      q.onsuccess=function(){ res(q.result||null); }; q.onerror=function(){ res(null); };
    }catch(e){ res(null); } }); }); }
  function cachePut(key,val){ dbp.then(function(db){ if(!db) return;
    try{ db.transaction('audio','readwrite').objectStore('audio').put(val,key); }catch(e){} }); }

  function b64ToBlob(b64,type){
    var bin=atob(b64), len=bin.length, u8=new Uint8Array(len);
    for(var i=0;i<len;i++) u8[i]=bin.charCodeAt(i);
    return new Blob([u8],{type:type});
  }

  var flashEl=document.getElementById('bm-flash');
  function flash(m){ if(!flashEl) return; flashEl.textContent=m; flashEl.style.opacity=1;
    clearTimeout(flashEl._t2); flashEl._t2=setTimeout(function(){ flashEl.style.opacity=0; },2400); }

  var audio=new Audio();
  var active=null;   // state-a hevokê ya niha çalak

  function setIcon(st,kind){
    if(kind==='spin') st.toggle.innerHTML='<span class="tts-spin"></span>';
    else if(kind==='pause') st.toggle.innerHTML=ICON.pause;
    else st.toggle.innerHTML=ICON.play;
  }

  function kuText(ku){
    var out=''; var ns=ku.childNodes;
    for(var i=0;i<ns.length;i++){ out += (ns[i].nodeName==='BR') ? ' ' : (ns[i].textContent||''); }
    return out.replace(/\s+/g,' ').trim();
  }

  function wrapWords(st){
    if(st.wrapped) return;
    st.wrapped=true; st.words=[];
    var ku=st.ku, ns=ku.childNodes, ts=st.timestamps||[];
    if(!ts.length) return;
    if(!(ns.length===1 && ns[0].nodeType===3)) return;   // verse/dirûv: tenê deng, bê ronîkirin
    var text=ns[0].nodeValue, low=text.toLowerCase(), from=0, positions=[];
    for(var i=0;i<ts.length;i++){
      var w=(ts[i].word||'').trim();
      if(!w){ positions.push(null); continue; }
      var idx=low.indexOf(w.toLowerCase(), from);
      if(idx<0){ positions.push(null); continue; }
      positions.push({s:idx,e:idx+w.length}); from=idx+w.length;
    }
    var frag=document.createDocumentFragment(), cur=0, words=[];
    for(var j=0;j<positions.length;j++){
      var p=positions[j];
      if(!p){ words.push(null); continue; }
      if(p.s>cur) frag.appendChild(document.createTextNode(text.slice(cur,p.s)));
      var sp=document.createElement('span'); sp.className='w'; sp.textContent=text.slice(p.s,p.e);
      frag.appendChild(sp); words.push(sp); cur=p.e;
    }
    if(cur<text.length) frag.appendChild(document.createTextNode(text.slice(cur)));
    ku.replaceChild(frag, ns[0]);
    st.words=words;
  }

  function clearHighlight(st){
    if(st.words && st.lastWord>=0 && st.words[st.lastWord]) st.words[st.lastWord].classList.remove('w-on');
    st.lastWord=-1;
  }
  function highlight(st,t){
    var ts=st.timestamps, words=st.words;
    if(!ts||!ts.length||!words||!words.length) return;
    var idx=-1;
    for(var i=0;i<ts.length;i++){ if(t>=ts[i].start && t<ts[i].end){ idx=i; break; } }
    if(idx===st.lastWord) return;
    if(st.lastWord>=0 && words[st.lastWord]) words[st.lastWord].classList.remove('w-on');
    if(idx>=0 && words[idx]) words[idx].classList.add('w-on');
    st.lastWord=idx;
  }

  function getAudio(text){
    return cacheGet(text).then(function(hit){
      if(hit && hit.blob) return { url:URL.createObjectURL(hit.blob), timestamps:hit.timestamps||[] };
      return fetch(API,{ method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({text:text}) })
        .then(function(r){ return r.json().then(function(j){ if(!r.ok) throw new Error(j.error||('HTTP '+r.status)); return j; }); })
        .then(function(j){
          var blob=b64ToBlob(j.audio,'audio/wav');
          cachePut(text,{ blob:blob, timestamps:j.timestamps||[] });
          return { url:URL.createObjectURL(blob), timestamps:j.timestamps||[] };
        });
    });
  }

  function deactivate(st){
    if(active===st){ try{ audio.pause(); }catch(e){} }
    st.wrap.classList.remove('active');
    setIcon(st,'play');
    clearHighlight(st);
  }

  function start(st){
    if(active && active!==st) deactivate(active);
    active=st; st.wrap.classList.add('active');
    st.speedBtn.textContent=speedLabel(speedVal());
    setIcon(st,'spin'); st.loading=true; st.toggle.disabled=true;
    getAudio(kuText(st.ku)).then(function(d){
      st.loading=false; st.toggle.disabled=false;
      if(active!==st){ URL.revokeObjectURL(d.url); return; }
      audio.src=d.url; st.timestamps=d.timestamps||[];
      wrapWords(st);
      audio.playbackRate=speedVal(); audio.currentTime=0;
      return audio.play();
    }).catch(function(err){
      st.loading=false; st.toggle.disabled=false; setIcon(st,'play'); st.wrap.classList.remove('active');
      if(active===st) active=null;
      flash('TTS: '+((err&&err.message)||'çewtî'));
    });
  }

  function onToggle(st){
    if(st.loading) return;
    if(active===st){ if(audio.paused) audio.play(); else audio.pause(); return; }
    start(st);
  }

  audio.addEventListener('play', function(){ if(active) setIcon(active,'pause'); });
  audio.addEventListener('pause', function(){ if(active && !audio.ended) setIcon(active,'play'); });
  audio.addEventListener('ended', function(){ if(active){ setIcon(active,'play'); clearHighlight(active); try{audio.currentTime=0;}catch(e){} } });
  audio.addEventListener('timeupdate', function(){ if(active) highlight(active, audio.currentTime); });
  audio.addEventListener('error', function(){ if(active){ setIcon(active,'play'); active.wrap.classList.remove('active'); } });

  function mkBtn(cls,title,icon){ var b=document.createElement('button'); b.className=cls; b.title=title; b.innerHTML=icon; return b; }

  function ensurePlayer(sent){
    if(sent._tts) return sent._tts;
    var ku=sent.querySelector('.ku'); if(!ku) return null;
    var wrap=document.createElement('span'); wrap.className='tts';
    wrap.addEventListener('click', function(e){ e.stopPropagation(); });
    var toggle=mkBtn('tts-toggle','Bilêvke',ICON.play);
    var more=document.createElement('span'); more.className='tts-more';
    var bR=mkBtn('tts-restart','Ji nû ve',ICON.restart);
    var bB=mkBtn('tts-rw','-5s',ICON.rw);
    var bF=mkBtn('tts-ff','+5s',ICON.ff);
    var bS=document.createElement('button'); bS.className='tts-speed'; bS.title='Lez'; bS.textContent=speedLabel(speedVal());
    more.appendChild(bR); more.appendChild(bB); more.appendChild(bF); more.appendChild(bS);
    wrap.appendChild(toggle); wrap.appendChild(more);
    // di bloka îngilîzî de cih digire da ku di valahiya çepê de, li jor-çepê, radiweste
    (sent.querySelector('.orig') || sent).appendChild(wrap);
    var st={ sent:sent, ku:ku, wrap:wrap, toggle:toggle, speedBtn:bS, loading:false, wrapped:false, words:[], lastWord:-1, timestamps:[] };
    sent._tts=st;
    toggle.addEventListener('click', function(e){ e.stopPropagation(); onToggle(st); });
    bR.addEventListener('click', function(e){ e.stopPropagation(); if(active===st){ try{audio.currentTime=0;}catch(x){} if(audio.paused) audio.play(); } });
    bB.addEventListener('click', function(e){ e.stopPropagation(); if(active===st){ try{audio.currentTime=Math.max(0,audio.currentTime-5);}catch(x){} } });
    bF.addEventListener('click', function(e){ e.stopPropagation(); if(active===st){ try{audio.currentTime=Math.min(audio.duration||0,audio.currentTime+5);}catch(x){} } });
    bS.addEventListener('click', function(e){ e.stopPropagation(); speedIdx=(speedIdx+1)%SPEEDS.length; if(active===st) audio.playbackRate=speedVal(); bS.textContent=speedLabel(speedVal()); });
    return st;
  }

  // Delegasyon: dema hevokek vebe -> lîstik çêbike ; dema bigire -> rawestîne
  document.addEventListener('click', function(e){
    if(e.target.closest('.tts')) return;          // destek lîstikê bi xwe digirin
    var sent=e.target.closest('.sent'); if(!sent) return;
    if(sent.classList.contains('on')) ensurePlayer(sent);
    else if(sent._tts && active===sent._tts){ deactivate(sent._tts); active=null; }
  });

  // "Hemûyan veke" jî divê lîstikan çêbike
  var exAll=document.getElementById('ex-all');
  if(exAll) exAll.addEventListener('click', function(){
    document.querySelectorAll('.sent.on').forEach(function(s){ ensurePlayer(s); });
  });
})();
</script>

</body>
</html>
"""

doc = HTML_DOC.replace("<!--ARTICLE-->", ARTICLE)
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "index.html")
with io.open(path, "w", encoding="utf-8") as f:
    f.write(doc)

# quick stats
sent = doc.count('class="sent"')
pg = doc.count('class="pagemark"')
print("written:", path)
print("sentences:", sent, "pagemarks:", pg)
print("has run-head:", 'run-head' in doc, "| reader-bar:", 'reader-bar' in doc)