#!/usr/bin/env python3
"""Build an abridged visual narrative, one fragment per panel."""
from pathlib import Path
from html import escape
ROOT=Path(__file__).parent
# Each tuple is an image, exact source-panel bounds, time, relevant fragment, alt.
def p(image,box,time,text,alt): return (image,box,time,text,alt)
TL=(8,8,748,487);TR=(768,8,760,487);BL=(8,507,748,503);BR=(768,507,760,503)
chapters=[('Friday',[
('wide',[p('rain-walk',None,'7:00 PM','It was supposed to be summer. An endless November followed me home.','A lone man walks home through a rainy city.')]),
('wide',[p('doner-shop',None,'9:30 PM','A woman sits a few metres away. I lower my eyes and return to my screen. Tomorrow.','A man looks at his phone in a döner shop while a woman watches from another table.')]),
('wide',[p('friday-night',(8,8,1518,401),'11:30 PM','Rain at the window. The room is cold. I keep wandering, without moving.','The man sits alone looking out at rain and tram lights.')]),
('dream',[p('friday-night',(8,425,752,585),'2:00 AM','Since childhood, I have told myself stories to fall asleep. The princesses became real women.','The man lies in bed imagining a knight, dragon and princess.'),p('friday-night',(779,425,746,585),'In the story','She sees through my cheerful charade. A fleeting smile, and I belong somewhere.','In his fantasy, the man raises a beer while a woman smiles at him.')]),
]),('Saturday',[
('pair',[p('saturday-morning',TL,'11:00 AM','I hold the pillow like a lover. Her warmth lingers. Outside, only rain.','The man hugs his pillow in bed.'),p('saturday-morning',TR,'12:30 PM','No messages. No food. Coffee and pills. Thirteen hours before bed again.','He opens an empty fridge beside coffee, supplements and a silent phone.')]),
('pair',[p('saturday-morning',BL,'Before leaving','I tell myself this room is a choice. Style. Comfort. Splendid isolation.','The man stands at his apartment window.'),p('saturday-morning',BR,'Across the street','Behind the glass, I watch people step into lives I never join.','Through the window, he watches people going out together.')]),
('pair',[p('saturday-day',(12,12,780,475),'2:00 PM','I chose imaginary company. The price is loneliness. Then, suddenly, the sky clears.','The man grips his shirt as sunshine breaks through the clouds.'),p('saturday-day',(808,12,710,475),'2:15 PM','“The usual?” A smile, a nod. Recognition is almost a conversation.','A smiling waitress brings his usual bagel and coffee.')]),
('pair',[p('saturday-day',(12,505,808,501),'4:30 PM','From terrace to terrace. Watching people. Burning quietly in the sun.','He wanders alone beneath an umbrella in the heat.'),p('saturday-day',(839,505,679,501),'Three poems','I could choose to call someone. But what if they don’t answer?','He writes at a café table with his phone in hand.')]),
('wide',[p('lovers-become-trees',None,'9:00 PM','Her head rests on his shoulder. I imagine them taking root, keeping each other company across countless seasons.','An elderly couple holds hands beneath a tree whose branches become embracing lovers.')]),
('night',[p('saturday-night',TR,'11:30 PM','The paths empty. The trees disappear into blackness.','An empty park path under dim street lamps.'),p('saturday-night',(12,531,751,477),'A passing thought','A sudden accident. A lit phone on the asphalt. I wish I had more time.','An imagined accident: a hand and phone beside a car tyre.')]),
('pair',[p('saturday-night',(780,529,365,478),'1:00 AM','For a second, I hope to meet a neighbour. The second passes.','He climbs a narrow dark wooden staircase.'),p('saturday-night',(1152,534,366,467),'Back in bed','My daily streak survives. I fall asleep with the phone on my chest.','He sleeps with his phone on his chest while rain hits the window.')]),
]),('Sunday',[
('wide',[p('winter-room',None,'7:00 AM','A blizzard covers the window. Outside, no one. The cold has become a world.','The man faces a large window engulfed by a blizzard.')]),
('narrow',[p('sunday-flashbacks',TR,'10:00 AM','No food. No pills. No Internet. Dust settles over everything I called home.','He shivers on the couch beside dusty glasses and an empty fridge.')]),
('memory',[p('sunday-flashbacks',(12,521,763,488),'11:30 AM · A memory','Once, in a café, I asked to join her. She said yes. We spoke for an hour. Then she left.','A remembered conversation with a woman at a sunny café.'),p('sunday-flashbacks',(800,521,720,488),'1:00 PM · A fantasy','Another table. Another life. Her eyes locked on mine, as though nothing else mattered.','He imagines an intimate dinner with the woman among friends.')]),
('absence',[p('sunday-later',(13,10,700,497),'3:30 PM','Nothing left to carry me into tomorrow. Alone, with no one calling, I vanish.','The man lies awake in bed looking at the ceiling.'),p('sunday-later-empty',(13,10,700,497),'','Not even a shadow.','The same room and bed, now empty.')]),
]),('Later',[
('wide',[p('sunday-later',(731,11,790,495),'September','The city is warm again. Lovers make their promises. Some will become trees.','Couples walk and embrace beneath leafy trees near busy terraces.')]),
('pair',[p('sunday-later',(13,526,811,479),'New arrivals','The agent opens the door to a family. They love the couch, the windows, the old-fashioned charm.','An estate agent welcomes parents and their child into the apartment.'),p('sunday-later',(846,526,674,479),'At home','The father takes his vitamins and smiles. He feels at home.','The new father sits with coffee and a pill box, surrounded by his family.')]),
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
  content.append(f'<div class="sequence {treatment}">'+''.join(cards)+'</div>')
 sections.append(f'<section id="{name.lower()}" class="chapter"><header class="chapter-title"><span>0{ci+1}</span><h2>{name}</h2></header>'+''.join(content)+'</section>')
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#eeeae2"><meta name="description" content="Friday — a story in images and fragments."><title>Friday — Bande Dessinée</title><link rel="preload" as="image" href="assets/rain-walk.png"><link rel="stylesheet" href="style.css"></head><body><div class="progress" aria-hidden="true"><span id="progress-fill"></span></div><header class="masthead"><a class="brand" href="#friday">Friday</a><nav aria-label="Chapters">'''+''.join(f'<a href="#{name.lower()}">{name}</a>' for name,_ in chapters)+'''</nav></header><main>'''+''.join(sections)+'''</main><footer><a href="#friday">Friday</a><span>A story in images &amp; fragments</span></footer><script src="script.js" defer></script></body></html>'''
(ROOT/'dist/index.html').write_text(page)
print(f'Built {n} individually captioned panels in {len(chapters)} chapters')
