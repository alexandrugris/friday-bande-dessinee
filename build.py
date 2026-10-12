#!/usr/bin/env python3
"""Build an abridged visual narrative, one fragment per panel."""
from pathlib import Path
from html import escape
SOURCE = (Path(__file__).parent / "story.txt").read_text()
ROOT=Path(__file__).parent
# Each tuple is an image, exact source-panel bounds, time, relevant fragment, alt.
def p(image,box,time,text,alt):
 parts = text.split(' || ')
 assert all(part in SOURCE for part in parts), "Caption must use verbatim source passages"
 return (image,box,time,' '.join(parts),alt)
TL=(8,8,748,487);TR=(768,8,760,487);BL=(8,507,748,503);BR=(768,507,760,503)
chapters=[('Friday',[
('wide',[p('rain-walk',None,'7:00 PM','Undefined gray days under an undefined gray sky. It was supposed to be summer, yet an endless November wrapped us all in its wet embrace.','A lone man walks home through a rainy city.')]),
('wide',[p('doner-shop',None,'9:30 PM','I select a Turkish fast food nearby, more to ensure my failure to meaningfully engage with anyone than for its culinary appeal. || For a second I have the sensation that she will lift her eyes in my direction, so I quickly bow mine.','A man looks at his phone in a döner shop while a woman watches from another table.')]),
('wide',[p('friday-night',(8,8,1518,401),'11:30 PM','From my armchair I look through the window. The night came, dark. The heavy rain turned into a drizzle, long, infinite, cold.','The man sits alone looking out at rain and tram lights.')]),
('dream',[p('friday-night',(8,425,752,585),'2:00 AM','Since I was a small child I told myself stories to fall asleep. || In the beginning I was prince charming fighting with the dragon. A few years later the idea of a princess started popping in. Then it all became about the princess.','The man lies in bed imagining a knight, dragon and princess.'),p('friday-night',(779,425,746,585),'A bedtime fantasy','I catch her lowering her eyes while a secret smile blushes briefly on her cheeks','In his fantasy, the man raises a beer while a woman smiles at him.')]),
]),('Saturday',[
('pair',[p('saturday-morning',TL,'11:00 AM','She is thin and delicate in her movements, contrasting sharply with the rest of the crowd. || I wake up late with a headache. I hold my pillow in my arms like a dear lover. Her image still lingers in my mind.  The warmth of the sheets is soothing. Her warmth.','The man hugs his pillow in bed.'),p('saturday-morning',TR,'12:30 PM','On the kitchen table, my pills. I don’t need to hide them anywhere or keep them in order.','He opens an empty fridge beside coffee, supplements and a silent phone.')]),
('pair',[p('saturday-morning',BL,'Before leaving','I stop for a second and look around my apartment, decorated in 50s fashion, with a pink couch and worn out lamps, large windows and a washing machine.','The man stands at his apartment window.'),p('saturday-morning',BR,'Across the street','I am watching from behind the window pane people stopping at the kebab shop, then going to clubs and bars, dressed in their fancy clothes, men and women, dancing the dance of mating and social connection.','Through the window, he watches people going out together.')]),
('pair',[p('saturday-day',(12,12,780,475),'2:00 PM','My burst of silent rage cleared the sky and now a bright sun and a blue sky sit above us, in stark contrast to just a few hours earlier.','The man grips his shirt as sunshine breaks through the clouds.'),p('saturday-day',(808,12,710,475),'2:15 PM','Despite the sparsity of our interaction, the gentle recognition, the smile, the nod have a pleasant familiarity and it brightens my day.','A smiling waitress brings his usual bagel and coffee.')]),
('pair',[p('saturday-day-summer-v2',(12,505,808,501),'4:30 PM','I spend the rest of my day wandering the city from terrace to terrace. I like watching people. I like the green and the sun.','He strolls contentedly through the sunny city in an elegant linen shirt and tailored trousers.'),p('saturday-day-summer-v2',(839,505,679,501),'Three poems','I could choose to call someone\nBut what if they don’t answer?','He sits calmly at a café, holding his phone in one hand and writing with a pen in the other.')]),
('tree-dream',[p('trees-dream',(8, 8, 748, 487),'9:00 PM','Next to me on the bench, an old couple. They approached me earlier and asked if I minded if they sat. They were holding hands. I watch them with the corner of my eye how they are just sitting there, not saying a word, her head resting on his shoulder.','The solitary man watches an elderly couple holding hands on the bench.'),p('trees-dream',(780, 8, 748, 487),'','I imagine them sitting like this forever, gaining roots, eternal, keeping each other company across countless seasons. Connection is atemporal, a moment frozen in time while the time passes.','He watches roots grow beneath the couple as they begin to become trees.'),p('trees-dream',(8, 527, 748, 487),'','You don’t grow old, you grow roots and transcend - a tree hugging another tree, with new lovers holding hands and exchanging their first kisses under your eternal shadow.','Over his shoulder, the elderly lovers become two intertwined trees.'),p('lovers-become-trees-color',None,'','I think all true lovers eventually become trees - this is why there are so many of them in our parks.','The original image: elderly lovers, their embrace echoed in the branches above.'),p('trees-dream',(780, 527, 748, 487),'','They were all once sitting on benches, her head leaning on his shoulder. Then they grew roots. Time passed, the benches were worn by the elements and disappeared. But the lovers remained.','New lovers kiss beneath the embracing trees; the old bench has disappeared.')]),
('night',[p('saturday-night',TR,'11:30 PM','It’s full dark and the park alleys are empty. The trees first turned to shadows, then became indistinguishable from the surrounding blackness.','An empty park path under dim street lamps.'),p('saturday-night',(12,531,751,477),'A passing thought','A sudden, absurd, accidental death would fit me properly. Coming from nowhere and going to nowhere. Disappeared, forgotten, nothing - the resting argument of my life. I wish I had more time though.','An imagined accident: a hand and phone beside a car tyre.')]),
('pair',[p('saturday-night',(780,529,365,478),'1:00 AM','For a brief second I hope I bump into a neighbour but that second passes.','He climbs a narrow dark wooden staircase.'),p('saturday-night',(1152,534,366,467),'Back in bed','Not before long I fall asleep with an empty mind and my phone on my chest.','He sleeps with his phone on his chest while rain hits the window.')]),
]),('Sunday',[
('wide',[p('winter-room',None,'7:00 AM','I wake up to the sound of the blizzard. I look through the window and I see snow covering almost all of the glass.','The man faces a large window engulfed by a blizzard.')]),
('narrow',[p('sunday-flashbacks',TR,'10:00 AM','A sense of old and stale - the couch, the dust, the wine glasses, my pyjamas, my flip-flops.','He shivers on the couch beside dusty glasses and an empty fridge.')]),
('memory',[p('sunday-flashbacks',(12,521,763,488),'11:30 AM · A flashback','I asked her if I could join her. She said yes and looked at me with an inquisitive and slightly amused look.','A remembered conversation with a woman at a sunny café.'),p('sunday-flashbacks',(800,521,720,488),'1:00 PM · A fantasy',"We talk, our eyes locked, as if it's only me and her and nothing else matters.",'He imagines an intimate dinner with the woman among friends.')]),
('absence',[p('sunday-later',(13,10,700,497),'3:30 PM','I lie in bed, eyes riveted towards the ceiling. I have nothing left to get me moving to the next day.','The man lies awake in bed looking at the ceiling.'),p('sunday-later-empty',(13,10,700,497),'','Alone, with no one to see me, with no one calling, I vanish.','The same room and bed, now empty.')]),
]),('Later',[
('wide',[p('later-color',(731,11,790,495),'September','Soon November will come but until then lovers are busy making their promises.','Couples walk and embrace beneath leafy trees near busy terraces.')]),
('pair',[p('later-color',(13,526,811,479),'New arrivals','The real estate agent opens the door and welcomes a family: a mother, a father and a child.','An estate agent welcomes parents and their child into the apartment.'),p('later-color',(846,526,674,479),'At home','He smiles with a warm smile. He feels at home.','The new father sits with coffee and a pill box, surrounded by his family.')]),
])]
def panel(item,n):
 image,box,time,text,alt=item
 if box:
  x,y,w,h=box
  art=f'<svg role="img" aria-labelledby="art-{n}" viewBox="{x} {y} {w} {h}"><title id="art-{n}">{escape(alt)}</title><image href="assets/{image}.png" width="1536" height="1024" /></svg>'
 else: art=f'<img src="assets/{image}.png" alt="{escape(alt)}" '+('fetchpriority="high"' if n==0 else 'loading="lazy" decoding="async"')+'>'
 return f'<figure class="panel"><div class="art">{art}</div><figcaption><span class="time">{escape(time)}</span><p>{escape(text)}</p></figcaption></figure>'
n=0;sections=[]
for ci,(name,groups) in enumerate(chapters):
 content=[]
 for treatment,items in groups:
  cards=[]
  for item in items: cards.append(panel(item,n));n+=1
  prefix = suffix = ''
  if treatment == 'memory':
   anchor = '<svg role="img" aria-label="He remains alone in his cold room" viewBox="768 8 760 487"><image href="assets/sunday-flashbacks.png" width="1536" height="1024" /></svg>'
   prefix = '<div class="reality-anchor">'+anchor+'<span class="thought-trail" aria-hidden="true">○ · · ·</span></div>'
   cue = 'My mind wanders back to the witty woman in my beer-hall  fantasy.'
   returning = 'A shiver. It’s so cold and the damp air.'
   assert cue in SOURCE and returning in SOURCE
   cards[1] = cards[1].replace('<div class="art">', '<p class="inner-cue">'+escape(cue)+'</p><div class="art">', 1)
   suffix = '<div class="return-to-room"><span class="thought-trail" aria-hidden="true">· · · ○</span>'+anchor+'<p>'+escape(returning)+'</p></div>'
  content.append(f'<div class="sequence {treatment}">'+prefix+''.join(cards)+suffix+'</div>')
 sections.append(f'<section id="{name.lower()}" class="chapter"><header class="chapter-title"><span>0{ci+1}</span><h2>{name}</h2></header>'+''.join(content)+'</section>')
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#eeeae2"><meta name="description" content="Friday — a story in images and fragments."><title>Friday — Bande Dessinée</title><link rel="preload" as="image" href="assets/rain-walk.png"><link rel="stylesheet" href="style.css"></head><body><div class="progress" aria-hidden="true"><span id="progress-fill"></span></div><header class="masthead"><a class="brand" href="#friday">Friday</a><nav aria-label="Chapters">'''+''.join(f'<a href="#{name.lower()}">{name}</a>' for name,_ in chapters)+'''</nav></header><main>'''+''.join(sections)+'''</main><footer><a href="#friday">Friday</a><span>A story in images &amp; fragments</span></footer><script src="script.js" defer></script></body></html>'''
(ROOT/'dist/index.html').write_text(page)
print(f'Built {n} individually captioned panels in {len(chapters)} chapters')
