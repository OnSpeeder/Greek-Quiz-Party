"""Build the editable Inkscape study; render/validate through Inkscape MCP separately."""
from pathlib import Path
import base64
import html
import math
import random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/design/settings-study-02'
OUT.mkdir(parents=True, exist_ok=True)
parts = []
def add(s): parts.append(s)
def rect(x,y,w,h,fill,rx=24,stroke=None,sw=2):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>')
def text(x,y,t,size=40,fill='#fff4d5',anchor='start',stroke='#201037',sw=5):
    add(f'<text x="{x}" y="{y}" font-family="Impact, Arial Black, sans-serif" font-size="{size}" text-anchor="{anchor}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" paint-order="stroke fill" stroke-linejoin="round">{html.escape(t)}</text>')
def frame(x,y,w,h,inner=False):
    rect(x+4,y+12,w,h,'#10091e',36)
    rect(x,y,w,h,'url(#gold)',36,'#7f4520',4)
    rect(x+9,y+8,w-18,h-18,'url(#goldLight)',29)
    rect(x+17,y+16,w-34,h-34,'url(#purple)',24,'#d598ed',3)
    if inner: rect(x+29,y+30,w-58,h-60,'url(#well)',18,'#af6bd2',3)
def rivet(x,y,r=13):
    add(f'<circle cx="{x+2}" cy="{y+3}" r="{r+2}" fill="#47203c"/><circle cx="{x}" cy="{y}" r="{r}" fill="url(#gold)" stroke="#a66b2b" stroke-width="2"/><path d="M{x-r*.45} {y+r*.45}l{r*.9} {-r*.9}" stroke="#a6722f" stroke-width="3"/>')
def button(x,y,w,h,label,size=36,red=False):
    rect(x+3,y+8,w,h,'#1d0a30',20)
    rect(x,y,w,h,'url(#gold)',20,'#8b4d21',3)
    rect(x+7,y+6,w-14,h-14,'url(#red)' if red else 'url(#button)',15,'#fff0b9',2)
    add(f'<path d="M{x+20} {y+13}h{w-40}" stroke="#fff" stroke-opacity=".38" stroke-width="3" stroke-linecap="round"/>')
    text(x+w/2,y+h*.67,label,size,anchor='middle',sw=4 if size>30 else 2)
def toggle(x,y,w=130,h=64,on=True):
    rect(x+2,y+4,w,h,'#140d2c',h/2)
    rect(x,y,w,h,'url(#gold)',h/2,'#6e3b21',2)
    rect(x+5,y+5,w-10,h-10,'url(#switch)' if on else 'url(#well)',h/2)
    cx=x+w-h/2 if on else x+h/2
    add(f'<circle cx="{cx}" cy="{y+h/2+2}" r="{h*.43}" fill="#8b4d24"/><circle cx="{cx}" cy="{y+h/2-1}" r="{h*.41}" fill="url(#gold)" stroke="#fff0b8" stroke-width="2"/><circle cx="{cx}" cy="{y+h/2-2}" r="{h*.29}" fill="#ffe5a0"/>')
def slider(x,y,w=560,h=45,value=.57):
    rect(x+2,y+5,w,h,'#170c2c',h/2)
    rect(x,y,w,h,'url(#gold)',h/2,'#885127',2)
    rect(x+5,y+5,w-10,h-10,'url(#well)',h/2)
    rect(x+6,y+6,(w-12)*value,h-12,'url(#spectrum)',h/2)
    cx=x+w*value; r=h*.68
    add(f'<circle cx="{cx+2}" cy="{y+h/2+5}" r="{r+3}" fill="#44213a"/><circle cx="{cx}" cy="{y+h/2}" r="{r}" fill="url(#gold)" stroke="#fff0bb" stroke-width="3"/><circle cx="{cx}" cy="{y+h/2-1}" r="{r*.73}" fill="url(#goldLight)" stroke="#c18531" stroke-width="2"/>')
def gear(x,y,r=42):
    pts=[]
    for i in range(48):
        a=i*math.pi/24; radius=r if i%4 in (0,1) else r*.79
        pts.append(f'{x+math.cos(a)*radius},{y+math.sin(a)*radius}')
    add(f'<polygon points="{" ".join(pts)}" fill="url(#gold)" stroke="#7b4527" stroke-width="4"/><circle cx="{x}" cy="{y}" r="{r*.42}" fill="#5c2881" stroke="#ffdf89" stroke-width="4"/>')
def speaker(x,y,s=1):
    add(f'<g transform="translate({x},{y}) scale({s})" fill="url(#gold)" stroke="#7a4324" stroke-width="3"><path d="M-36-18h17L9-42v84L-19 18h-17Z"/><path d="M25-26q26 26 0 52m15-69q43 43 0 86" fill="none" stroke="#ffe49c" stroke-width="9" stroke-linecap="round"/></g>')
def pedestal(x,y,w,h):
    add(f'<ellipse cx="{x+w/2}" cy="{y+h+9}" rx="{w*.53}" ry="{h*.2}" fill="#0c061c" opacity=".7"/>')
    rect(x,y,w,h,'url(#purple)',8,'#af7130',4)
    add(f'<path d="M{x+20} {y+40}Q{x+w/2} {y+65} {x+w-20} {y+40}V{y+h-12}Q{x+w/2} {y+h+8} {x+20} {y+h-12}Z" fill="#53267e" stroke="#d4a34f" stroke-width="3"/><ellipse cx="{x+w/2}" cy="{y+12}" rx="{w/2}" ry="{h*.23}" fill="url(#gold)" stroke="#fff0be" stroke-width="4"/>')
def image_region(ref,x,y,w,h,vb):
    clip='crop-'+ref
    add(f'<defs><clipPath id="{clip}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath></defs><g clip-path="url(#{clip})"><svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{vb}" preserveAspectRatio="xMidYMid meet"><use xlink:href="#{ref}"/></svg></g>')

add('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="3200" height="1800" viewBox="0 0 3200 1800">')
# Correct Inkscape namespace and distinct editable layers.
parts[0]=parts[0].replace('http://www.inkscape.org/namespaces/inkscape','http://www.inkscape.org/namespaces/inkscape')
add('<title>QuizParty - Settings Study 02</title><desc>Editable landscape and portrait visual mockup. Proposed controls are illustrative, not implemented functionality.</desc><defs>')
gradients={
 'gold':[(0,'#fff5c4'),(.22,'#ffe99d'),(.46,'#f6c858'),(.72,'#b87525'),(1,'#e6ac47')],
 'goldLight':[(0,'#fff7cb'),(.5,'#ffe29a'),(1,'#eeb044')],
 'purple':[(0,'#ad5bdd'),(.12,'#8d46bc'),(.55,'#6a3597'),(1,'#45256e')],
 'well':[(0,'#291640'),(.12,'#382056'),(1,'#48276a')],
 'button':[(0,'#91edff'),(.25,'#24bde8'),(.7,'#087fc5'),(1,'#194e99')],
 'red':[(0,'#ff9e83'),(.3,'#ee604c'),(1,'#9c202b')],
 'switch':[(0,'#86e6f7'),(.5,'#29a9e0'),(1,'#315ea1')],
 'spectrum':[(0,'#08c9e7'),(.45,'#65b2ff'),(1,'#e756ca')],
 'titleBlue':[(0,'#b0f9ff'),(.25,'#48d6f4'),(.6,'#218acb'),(1,'#1659a1')],
 'tabActive':[(0,'#ffe3a0'),(.17,'#bc83d5'),(.6,'#9b56bd'),(1,'#69348f')],
}
for name,stops in gradients.items():
    horiz=name=='spectrum'
    add(f'<linearGradient id="{name}" x1="0" y1="0" x2="{1 if horiz else 0}" y2="{0 if horiz else 1}">'+''.join(f'<stop offset="{o}" stop-color="{c}"/>' for o,c in stops)+'</linearGradient>')
for ref,file,w,h in [('wide','showtime-stage-wide-v2.png',1672,941),('portrait','showtime-stage-v2.png',1024,1536),('crew','showtime-crew-v2.png',2172,724),('wave','Settings/mascot-orange.png',1261,1247)]:
    data=base64.b64encode((ROOT/'src/QuizParty.Godot/Art'/file).read_bytes()).decode()
    add(f'<image id="{ref}" width="{w}" height="{h}" xlink:href="data:image/png;base64,{data}"/>')
add('<clipPath id="phoneClip"><rect x="2310" y="80" width="850" height="1600" rx="45"/></clipPath></defs>')
add('<g inkscape:groupmode="layer" inkscape:label="01 Stage and confetti" id="stage">')
rect(0,0,3200,1800,'#100b26',0)
add('<use xlink:href="#wide" width="3200" height="1800" transform="scale(1.914)"/>')
add('<rect width="3200" height="1800" fill="#100823" opacity=".42"/>')
random.seed(22)
for i in range(75):
    x=random.randint(20,3180); y=random.randint(70,1720)
    col=['#ffc44e','#48d9f3','#f764ba','#9665dc'][i%4]
    add(f'<path d="M{x} {y}l15-5 6 14-15 5Z" fill="{col}" transform="rotate({i*31%120},{x},{y})" opacity=".8"/>')
text(70,100,'QuizParty',52,'#ffdf8e',sw=2)
text(70,151,'SETTINGS  /  VISUAL STUDY 02',23,'#b3a4da',sw=0)
add('<path d="M2265 90V1710" stroke="#af7d43" stroke-width="2" opacity=".55"/>')
add('</g><g inkscape:groupmode="layer" inkscape:label="02 Landscape 16 by 9" id="landscape" transform="translate(30,290) scale(1.14)">')
frame(170,220,1660,740)
for x in [205,1794]:
    for y in [254,925]: rivet(x,y,17)
frame(290,305,1390,540,True)
# Broad overlapping sign and tactile upper-left return button.
button(20,75,260,110,'',54)
rect(27,81,246,96,'url(#purple)',15,'#fff0b9',2)
text(190,149,'Back',54,anchor='middle')
add('<path d="M76 101 45 128l31 26v-18h24q28 0 24 28 28-49-48-45Z" fill="url(#gold)" stroke="#73412d" stroke-width="3"/>')
for d in range(12,0,-2): text(985+d,245+d,'SETTINGS',230,'#9b571d','middle','#162b5e',27)
text(985,235,'SETTINGS',230,'url(#titleBlue)','middle','#ffda73',12)
for i,label in enumerate(['AUDIO','GAMEPLAY','HELP & LEGAL']):
    y=345+i*190
    add(f'<path d="M45 {y+10}H310L350 {y+80} 310 {y+155}H45Q20 {y+155} 20 {y+130}V{y+35}Q20 {y+10} 45 {y+10}Z" fill="#170c2b" transform="translate(4,9)"/>')
    add(f'<path d="M45 {y}H310L350 {y+75} 310 {y+150}H45Q20 {y+150} 20 {y+125}V{y+25}Q20 {y} 45 {y}Z" fill="url(#gold)" stroke="#824620" stroke-width="3"/>')
    tabfill='tabActive' if i==0 else 'purple'
    add(f'<path d="M48 {y+9}H305L338 {y+75} 305 {y+140}H48Q30 {y+140} 30 {y+122}V{y+28}Q30 {y+9} 48 {y+9}Z" fill="url(#{tabfill})" stroke="#ffe9aa" stroke-width="2"/>')
    if i==0: gear(92,y+75,43); gear(132,y+39,22)
    elif i==1: speaker(97,y+72,.85)
    else: gear(100,y+72,44)
    text(235,y+94,label,42 if i<2 else 30,anchor='middle',sw=4)
text(420,410,'MUSIC',51)
toggle(880,350)
slider(420,475,585,48)
text(1080,410,'VOICE VOICE OVER',38)
toggle(1100,455,265,78)
text(1121,507,'English',38,sw=3)
text(420,635,'SFX',51)
toggle(880,575)
slider(420,700,585,48,.58)
text(1080,635,'HAPTIC FEEDBACK',38)
toggle(1110,680,150,70,False)
button(420,855,280,86,'CREDITS',38)
button(725,855,365,86,'PRIVACY POLICY',36)
button(1115,855,280,86,'RESET ALL',38,True)
pedestal(1500,920,350,125)
image_region('crew',1460,430,375,565,'650 0 430 724')
# Seated feet are editable vector trims; the original thoughtful crew face is preserved.
for x,ang in [(1530,-18),(1770,18)]:
    add(f'<g transform="rotate({ang},{x},896)"><ellipse cx="{x}" cy="896" rx="55" ry="72" fill="#35caed" stroke="#163b74" stroke-width="5"/><ellipse cx="{x}" cy="909" rx="30" ry="37" fill="#9372b5" stroke="#3f4b91" stroke-width="3"/>')
    for dx,dy in [(-24,-21),(0,-30),(24,-21)]: add(f'<ellipse cx="{x+dx}" cy="{880+dy}" rx="10" ry="14" fill="#d58fca"/>')
    add('</g>')
add('</g>')
# Portrait artboard: same hierarchy, tightly composed vertical cards.
add('<g inkscape:groupmode="layer" inkscape:label="03 Portrait 9 by 16" id="portrait-layout" transform="translate(2325,120) scale(1.72)">')
add('<svg x="0" y="0" width="480" height="850" viewBox="0 0 1024 1536" preserveAspectRatio="xMidYMid slice"><use xlink:href="#portrait"/></svg>')
frame(10,48,460,775)
add('<path d="M175 60 183 21 218 45 240 0 262 45 297 21 305 60Z" fill="url(#gold)" stroke="#9a5b25" stroke-width="3"/>')
add('<path d="M30 80 65 35H415L450 80 422 133H58Z" fill="url(#gold)" stroke="#744323" stroke-width="4"/><path d="M43 79 73 47H407L435 79 413 120H67Z" fill="url(#purple)" stroke="#fff0b9" stroke-width="2"/>')
text(242,105,'SETTINGS',65,'url(#titleBlue)','middle','#ffda73',5)
add('<circle cx="447" cy="21" r="24" fill="url(#gold)" stroke="#8b542b" stroke-width="3"/><circle cx="447" cy="20" r="18" fill="url(#purple)"/>')
text(447,31,'X',31,'#ffe7a0','middle',sw=1)
def card(y,h,label):
    frame(35,y,410,h,True)
    rect(45,y+10,390,46,'url(#purple)',12,'#ffe09a',1.5)
    text(240,y+45,label,33,anchor='middle',sw=3)
    rivet(57,y+31,8);rivet(422,y+31,8)
card(155,310,'AUDIO')
text(60,250,'MUSIC',34,sw=3);toggle(337,215,78,37)
slider(60,287,360,30,.52)
text(60,372,'SFX',34,sw=3);toggle(337,337,78,37)
slider(60,408,360,30,.52)
card(484,146,'GAMEPLAY')
rect(56,555,205,49,'#251536',10,'#9360b3',2)
text(67,589,'LANGUAGE',30,sw=3)
toggle(274,555,146,49)
# Flag glyphs are editable vectors, as requested by the visual prompt.
add('<svg x="282" y="563" width="53" height="33" viewBox="0 0 60 36"><rect width="60" height="36" fill="#173c80"/><path d="M0 0 60 36M60 0 0 36" stroke="white" stroke-width="9"/><path d="M0 0 60 36M60 0 0 36" stroke="#d53a52" stroke-width="3"/><path d="M30 0V36M0 18H60" stroke="white" stroke-width="12"/><path d="M30 0V36M0 18H60" stroke="#d53a52" stroke-width="7"/></svg>')
add('<svg x="350" y="563" width="53" height="33" viewBox="0 0 60 36"><rect width="60" height="36" fill="white"/>')
for y in range(0,36,6): rect(0,y,60,3,'#db4760',0)
rect(0,0,25,20,'#214580',0)
for x in [5,12,19]:
    for y in [4,10,16]: add(f'<circle cx="{x}" cy="{y}" r="1" fill="white"/>')
add('</svg>')
card(650,150,'HELP & LEGAL')
button(58,723,300,54,'RESET TO DEFAULT',25)
image_region('wave',317,724,175,180,'0 623.5 630.5 623.5')
add('</g>')
add('<g inkscape:groupmode="layer" inkscape:label="04 Artboard captions" id="captions">')
text(80,1660,'LANDSCAPE  /  16:9',28,'#f9d98d',sw=1)
text(2360,1710,'PORTRAIT  /  9:16',28,'#f9d98d',sw=1)
text(80,1730,'QUIZPARTY  /  SETTINGS CONCEPT  /  EDITABLE INKSCAPE MASTER',22,'#b6a6d2',sw=0)
add('</g></svg>')
(OUT/'settings-study-02.svg').write_text(''.join(parts),encoding='utf-8')
print(OUT/'settings-study-02.svg')
