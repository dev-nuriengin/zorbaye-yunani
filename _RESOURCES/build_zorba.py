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

ARTICLE = build_article(10, CH10) + "\n" + build_article(11, CH11) + "\n" + build_article(12, CH12) + "\n" + build_article(13, CH13) + "\n" + build_article(14, CH14)

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
  .sent{ cursor:pointer; }
  .sent:hover .ku{ background:rgba(120,90,30,0.10); }
  .sent .orig{ display:none; }
  .sent.on .orig{
    display:block; text-indent:0; text-align:left;
    margin:3mm 0 3.5mm 7mm; padding:1mm 0 1mm 5mm;
    border-left:2px solid #b9a77d; font-style:italic;
    color:#6b5d44; font-size:0.92em;
  }
  .sent.on .orig::before{ content:"\201C"; }
  .sent.on .orig::after{ content:"\201D"; }

  /* ---- Bilêvkirin (TTS): lîstika dengî ya her hevokê ---- */
  .tts{ display:none; }
  .sent.on .tts{
    display:inline-flex; align-items:center; gap:4px; vertical-align:middle;
    margin:2mm 0 1mm 7mm; text-indent:0; user-select:none;
  }
  .tts button{
    -webkit-appearance:none; appearance:none; cursor:pointer;
    display:inline-flex; align-items:center; justify-content:center;
    width:24px; height:24px; padding:0; border-radius:50%;
    background:#f7f0db; border:0.6px solid #8a7a55; color:#5a4a22; line-height:0;
  }
  .tts button:hover{ background:#fff; }
  .tts button:disabled{ cursor:default; opacity:.7; }
  .tts svg{ width:13px; height:13px; display:block; fill:currentColor; }
  .tts-speed{ width:auto !important; padding:0 7px !important; border-radius:12px !important;
    font:600 10px "Georgia",serif; line-height:1 !important; }
  /* destek lîstikê yên zêde: tenê dema çalak xuya dibin */
  .tts-more{ display:none; align-items:center; gap:4px; }
  .tts.active .tts-more{ display:inline-flex; }
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
    .run-head{ background:#fff; border-bottom-color:#111; }
    .run-head .rh-en{ color:#333; }
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
  var ICON={
    play:'<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>',
    pause:'<svg viewBox="0 0 24 24"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>',
    restart:'<svg viewBox="0 0 24 24"><path d="M12 5V2L7 6l5 4V7a5 5 0 1 1-5 5H5a7 7 0 1 0 7-7z"/></svg>',
    rw:'<svg viewBox="0 0 24 24"><path d="M11 6v12L3 12zM20 6v12l-8-6z"/></svg>',
    ff:'<svg viewBox="0 0 24 24"><path d="M13 6v12l8-6zM4 6v12l8-6z"/></svg>'
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
    sent.appendChild(wrap);
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