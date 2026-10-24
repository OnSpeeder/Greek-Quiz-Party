"""Recreate the supplied settings composition as self-contained vector artwork.

Python standard library only. No game assets or previous studies are modified.
Run Inkscape separately for raster previews and portable outlined lettering.
"""
from pathlib import Path
from html import escape
import math
import random
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/design/settings-study-03'
OUT.mkdir(parents=True, exist_ok=True)
parts = []


def add(s):
    parts.append(s)


def group(id_, label=None, transform=None, layer=False, extra=''):
    add(f'<g id="{id_}"'
        + (f' inkscape:label="{escape(label)}"' if label else '')
        + (' inkscape:groupmode="layer"' if layer else '')
        + (f' transform="{transform}"' if transform else '') + f' {extra}>')


def end():
    add('</g>')


def rect(x, y, w, h, fill, r=20, stroke=None, sw=2, extra=''):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" ry="{r}" fill="{fill}"'
        + (f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '') + f' {extra}/>')


def path(d, fill, stroke=None, sw=2, extra=''):
    add(f'<path d="{d}" fill="{fill}"'
        + (f' stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"' if stroke else '')
        + f' {extra}/>')


def ellipse(cx, cy, rx, ry, fill, stroke=None, sw=2, extra=''):
    add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}"'
        + (f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '') + f' {extra}/>')


def text(x, y, label, size=38, anchor='start', fill='#FFF8E5', stroke='#24102E', sw=5, extra=''):
    family = 'Impact' if 'font-family="Impact"' in extra else 'Arial Rounded MT Bold, Arial, sans-serif'
    extra = extra.replace('font-family="Impact"', '')
    add(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{family}" '
        f'font-weight="bold" font-size="{size}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
        f'paint-order="stroke fill" stroke-linejoin="round" {extra}>{escape(label)}</text>')


def rivet(x, y, r=12):
    ellipse(x+1, y+3, r+2, r+2, '#30102E', extra='opacity=".65"')
    ellipse(x, y, r, r, 'url(#gold)', '#985120', 2)
    ellipse(x-2, y-3, r*.66, r*.66, 'none', '#FFF2AF', 1.5)
    path(f'M{x-r*.5} {y+r*.5}l{r} {-r}', 'none', '#AE752F', 3)
    path(f'M{x-r*.5-1} {y+r*.5-2}l{r} {-r}', 'none', '#FFE7A0', 1)


def frame(id_, x, y, w, h, recess=False, radius=48):
    group(id_, 'Gold bevel / purple frame')
    rect(x+3, y+12, w, h, '#10081F', radius, extra='filter="url(#shadow)"')
    rect(x, y+5, w, h, '#9B5822', radius, '#48203D', 3)
    rect(x, y, w, h, 'url(#gold)', radius, '#B8792C', 3)
    rect(x+7, y+5, w-14, h-12, 'none', radius-5, '#FFF3B8', 3)
    rect(x+17, y+16, w-34, h-34, 'url(#panel)', radius-13, '#8E4D24', 3)
    rect(x+23, y+22, w-46, h-46, 'none', radius-17, '#B96BDD', 3)
    if recess:
        rect(x+39, y+43, w-78, h-88, 'url(#recess)', radius-25, '#9F5AC6', 3)
        path(f'M{x+57} {y+49}H{x+w-60}', 'none', '#28113E', 6, 'opacity=".5"')
    end()


def knob(id_, cx, cy, r):
    group(id_, 'Gold thumb — movable independently')
    ellipse(cx+2, cy+5, r+2, r+2, '#30152B', extra='opacity=".7"')
    ellipse(cx, cy+2, r, r, '#A56224', '#6B3526', 2)
    ellipse(cx, cy-1, r, r, 'url(#gold)', '#FFE5A0', 2)
    ellipse(cx, cy-2, r*.75, r*.75, 'url(#knob)', '#BA7F2E', 2)
    path(f'M{cx-r*.56} {cy-r*.2}A{r*.6} {r*.6} 0 0 1 {cx+r*.3} {cy-r*.55}',
         'none', '#FFF6C8', 2.5)
    end()


def toggle(id_, x, y, w=122, h=60, on=True, label=None):
    group(id_, 'Active toggle' if on else 'Inactive toggle', extra=f'data-state="{"on" if on else "off"}"')
    group(id_+'_track', 'Track')
    rect(x+1, y+5, w, h, '#23112D', h/2)
    rect(x, y, w, h, 'url(#gold)', h/2, '#895024', 2)
    rect(x+5, y+5, w-10, h-10, 'url(#blue)' if on else 'url(#off)', h/2-4, '#5B2C5F', 2)
    path(f'M{x+h/2} {y+8}H{x+w-h/2}', 'none', '#FFF5BE', 2, 'opacity=".45"')
    end()
    if label:
        text(x+22, y+h*.66, label, h*.47, sw=3)
    knob(id_+'_thumb', x+w-h/2 if on else x+h/2, y+h/2, h*.40)
    end()


def slider(id_, x, y, w, h=42, value=.6):
    group(id_, f'Slider — {round(value*100)} percent', extra=f'data-value="{value}"')
    group(id_+'_track', 'Recessed pill track')
    rect(x+1, y+4, w, h, '#24102D', h/2)
    rect(x, y, w, h, 'url(#gold)', h/2, '#834821', 2)
    rect(x+5, y+5, w-10, h-10, 'url(#off)', h/2-4, '#241035', 2)
    end()
    group(id_+'_fill', 'Cyan / periwinkle fill')
    rect(x+6, y+6, (w-12)*value, h-12, 'url(#spectrum)', h/2-5)
    path(f'M{x+18} {y+9}H{x+(w-12)*value}', 'none', '#B6FFFF', 2, 'opacity=".7"')
    end()
    knob(id_+'_thumb', x+6+(w-12)*value, y+h/2, h*.64)
    end()


def button(id_, x, y, w, h, label, size=32, red=False):
    group(id_, label)
    rect(x+2, y+7, w, h, '#24102D', 20, extra='filter="url(#smallShadow)"')
    rect(x, y+3, w, h, '#A85B1E', 20)
    rect(x, y, w, h, 'url(#gold)', 20, '#834523', 2)
    rect(x+7, y+6, w-14, h-14, 'url(#red)' if red else 'url(#blue)', 15, '#FFF0A5', 2)
    rect(x+12, y+11, w-24, h-24, 'none', 11, '#C92A2A' if red else '#1C67B2', 2)
    path(f'M{x+24} {y+12}H{x+w-24}', 'none', '#FFFFFF', 3, 'opacity=".45"')
    text(x+w/2, y+h*.67, label, size, 'middle', sw=4)
    end()


def gear(x, y, r):
    pts=[]
    for i in range(48):
        a=i*math.pi/24
        radius=r if i%4 in (0, 1) else r*.80
        pts.append((x+math.cos(a)*radius, y+math.sin(a)*radius))
    d='M'+'L'.join(f'{a:.2f} {b:.2f}' for a,b in pts)+'Z'
    path(d, '#2B1336', extra='transform="translate(1,4)" filter="url(#smallShadow)"')
    path(d, 'url(#gold)', '#72402D', 3)
    ellipse(x, y, r*.45, r*.45, '#7E3BA6', '#FFE09C', 3)
    ellipse(x, y+2, r*.32, r*.32, '#3B1C62', '#A96834', 2)


def tab(id_, x, y, w, h, label, active=False, icon='gear'):
    group(id_, label + (' — selected' if active else ' — inactive'))
    # Rounded rectangles own the frame. A small arrowhead extends the active tab.
    rect(x+2, y+8, w, h, '#291035', 27, extra='filter="url(#smallShadow)"')
    rect(x, y, w, h, 'url(#gold)', 27, '#AE6E28', 3)
    rect(x+8, y+7, w-16, h-16, 'url(#tab)' if active else 'url(#panel)', 21, '#FFF0B2', 2)
    if active:
        path(f'M{x+w-43} {y+3}Q{x+w-26} {y+3} {x+w-15} {y+22}L{x+w+23} {y+h/2-9}'
             f'Q{x+w+30} {y+h/2} {x+w+23} {y+h/2+9}L{x+w-15} {y+h-22}'
             f'Q{x+w-26} {y+h-3} {x+w-43} {y+h-3}Z', 'url(#gold)', '#B7792C', 2)
        path(f'M{x+w-43} {y+11}H{x+w-34}L{x+w+17} {y+h/2}L{x+w-34} {y+h-11}H{x+w-43}',
             'url(#tab)', '#FFF0B2', 2)
        gear(x+64, y+68, 33)
        gear(x+107, y+36, 19)
        text(x+139, y+83, label, 34, sw=4)
    else:
        if icon=='speaker':
            group(id_+'_speaker', 'Gold speaker icon', f'translate({x+w/2-15},{y+50})')
            path('M-42-16H-26L0-38Q6-41 6-34V34Q6 41 0 38L-26 16H-42Z', 'url(#gold)', '#7D402A', 3)
            path('M22-22Q43 0 22 22M38-36Q71 0 38 36', 'none', '#66322D', 9)
            path('M22-24Q43-2 22 20M38-38Q71-2 38 34', 'none', '#FFDB7A', 6)
            end()
        else:
            gear(x+w/2, y+52, 39)
        text(x+w/2, y+h-24, label, 28 if len(label)>10 else 30, 'middle', sw=4)
    end()


def title_letters(id_, x, y, label, size, spacing, curve=0):
    group(id_, 'Dimensional gold lettering — editable text')
    n=len(label)
    for index, letter in enumerate(label):
        dx=(index-(n-1)/2)*spacing
        t=(index-(n-1)/2)/((n-1)/2)
        yy=y+curve*t*t
        group(f'{id_}_{index}', letter, f'rotate({t*4:.2f},{x+dx:.2f},{yy:.2f})')
        for offset, color, width in [(12,'#10152D',16),(8,'#154574',15),(3,'#1B6CA8',13),(-1,'#5AB5E7',10)]:
            text(x+dx, yy+offset, letter, size, 'middle', color, color, width,
                 'font-stretch="condensed" font-family="Impact"')
        text(x+dx, yy-3, letter, size, 'middle', 'url(#titleGold)', '#9B5B1D', 4,
             'font-family="Impact"')
        text(x+dx, yy-5, letter, size, 'middle', 'none', '#FFF3AC', 1.2,
             'font-family="Impact"')
        end()
    end()


def stage(id_, w, h, seed):
    group(id_, 'Stage / spotlights / columns / confetti', layer=True)
    rect(0,0,w,h,'url(#stage)',0)
    ellipse(w*.51,h*.98,w*.68,h*.20,'url(#floor)')
    for yy in [-120,-81,-56]:
        path(f'M-50 {yy}Q{w/2} {h*.27+yy} {w+50} {yy}', 'none', '#AC763A', 9, 'opacity=".18"')
    # Fluted columns and elliptical capitals remain vector geometry.
    for cx in [-8,w+9]:
        group(f'{id_}_column_{int(cx)}', 'Fluted stage column')
        rect(cx-52,105,104,h-155,'url(#column)',24)
        for off in [-35,-15,12,34]:
            path(f'M{cx+off} 144V{h-72}', 'none', '#A16449', 5, 'opacity=".18"')
        for yy in [114,155,h-91,h-58]:
            ellipse(cx,yy,70,18,'url(#column)', '#A66A34', 3, 'opacity=".65"')
        end()
    for j,(x,rot,col) in enumerate([(w*.17,-26,'#B04CEA'),(w*.83,26,'#B04CEA'),(w*.04,-30,'#26BDEB')]):
        group(f'{id_}_spotlight_{j}', 'Stage spotlight', f'translate({x},12) rotate({rot})')
        path('M-13 0L-180 560Q0 650 180 560L13 0Z', 'url(#beamPurple)' if j<2 else 'url(#beamBlue)', extra='opacity=".35"')
        rect(-23,-40,46,78,'#161127',18,'#292443',3)
        ellipse(0,26,21,12,col,extra='opacity=".6"')
        end()
    for ry,col in [(100,'#342057'),(69,'#BD8035'),(49,'#0EA4D5')]:
        ellipse(w*.52,h*.95,w*.52,ry,'none',col,4, 'opacity=".32"')
    rng=random.Random(seed)
    for i in range(55 if w>1000 else 27):
        x=rng.uniform(32,w-32); y=rng.uniform(60,h-30)
        color=['#FFC657','#36D5ED','#E94DA7','#9565D9'][i%4]
        group(f'{id_}_confetti_{i}', transform=f'translate({x:.1f},{y:.1f}) rotate({rng.randrange(180)})')
        if i%6==0:
            path('M0-13Q3-2 13 0Q3 3 0 14Q-3 3-13 0Q-3-3 0-13Z',color)
        else:
            path('M-6-5Q0-2 7-5L7 5Q0 9-6 5Z',color,extra='opacity=".85"')
        end()
    end()


def fur_lines(id_, orange=False):
    """Short curved vector locks give the mascots soft texture without a bitmap."""
    group(id_, 'Fine fur locks', extra='fill="none" stroke-linecap="round"')
    rng=random.Random(48 if orange else 22)
    # Body silhouette is narrower at the neck; locks stay in the central belly.
    for i in range(125):
        y=rng.uniform(285,490)
        half=76 if y>345 else 70
        x=rng.uniform(200-half,200+half)
        length=rng.uniform(7,20)
        col=('#FFE6A3' if orange else '#B4FAFF') if i%3 else ('#E3961C' if orange else '#188CC2')
        path(f'M{x:.1f} {y:.1f}q{-4 if x<200 else 4} {length*.4:.1f} {rng.uniform(-4,4):.1f} {length:.1f}',
             'none', col, rng.uniform(1.3,2.8), 'opacity=".24"')
    end()


def blue_mascot(x, y, scale):
    group('mascot_blue', 'Blue fluffy thinker / glasses / paws', f'translate({x},{y}) scale({scale})', layer=True)
    group('mascot_blue_silhouette', 'Body and fluffy silhouette')
    # Feathered outline around shoulders and haunches.
    path('M133 245C90 253 71 285 75 327L58 317 69 346 54 350 72 370 60 386 77 392'
         'C56 435 73 479 102 498L89 510 113 513C146 540 254 537 289 512L310 513 299 497'
         'C335 472 338 433 321 392L339 385 325 370 337 347 323 348 330 318 313 328'
         'C322 287 293 255 264 246Z', 'url(#blueFur)', '#0867A5', 3)
    path('M159 321Q204 293 248 324L244 346 260 362 249 371 266 390 254 405 265 421'
         'C275 460 250 507 207 513C160 517 132 479 137 441L128 424 139 413 130 395'
         'L144 384 137 366 154 354Z', 'url(#belly)', '#69D9E8', 2)
    end()
    fur_lines('mascot_blue_body_fur')
    group('mascot_blue_head', 'Tufted head')
    path('M94 254L71 262 80 239 57 248 70 222 50 231 66 207 48 212 62 191 44 198'
         'C46 177 56 166 72 151L53 156C62 128 83 113 109 104L84 101Q105 77 138 81'
         'Q120 57 99 63Q123 37 155 58L148 33Q177 40 190 66Q196 33 181 17'
         'Q216 28 221 72Q241 32 239 23Q262 47 245 83Q272 58 297 62L277 83'
         'Q304 78 320 96L291 107Q324 119 338 142L320 140 340 162 326 163 348 187'
         'L332 185 347 208 333 208 345 232 329 228 336 253 317 248 322 267 300 260'
         'C277 292 123 297 94 254Z', 'url(#blueFace)', '#147FAF', 3)
    # Sweeping locks on the quiff and cheeks.
    for d in ['M87 129Q127 79 172 116','M73 151Q110 117 153 119','M153 70Q182 75 194 113',
              'M203 51Q220 81 209 112','M260 77Q234 92 230 119','M297 106Q269 100 254 127',
              'M65 201Q80 179 101 177','M72 224Q86 208 103 208','M303 178Q326 190 330 203',
              'M300 216Q320 222 327 239','M107 249Q126 268 144 269','M260 261Q286 253 297 242']:
        path(d,'none','#7AFAFF',3,'opacity=".48"')
    end()
    group('mascot_blue_eyes', 'Expressive eyes')
    for cx,cy,ang in [(143,189,13),(253,174,18)]:
        ellipse(cx,cy,37,44,'url(#eyeWhite)','#25486A',3, f'transform="rotate({ang},{cx},{cy})"')
        ellipse(cx+7,cy-2,18,26,'#07588E','#0D2E54',3)
        ellipse(cx+10,cy-4,10,20,'#08152D')
        ellipse(cx+2,cy-15,8,10,'white')
        ellipse(cx+17,cy+8,3,4,'#A2F8FF')
    path('M111 141Q132 124 157 135M227 125Q246 105 272 113','none','#302144',10)
    path('M111 138Q132 121 157 132M227 122Q246 102 272 110','none','#53315D',3)
    end()
    group('mascot_blue_glasses', 'Round black glasses')
    path('M108 184L73 191M284 159L308 151','none','#18182E',11)
    for cx,cy in [(144,190),(254,174)]:
        ellipse(cx,cy,47,48,'none','#16162D',11)
        ellipse(cx,cy-1,44,45,'none','#623D7D',5)
        path(f'M{cx-32} {cy-27}Q{cx-7} {cy-47} {cx+22} {cy-35}', 'none','#B58AC5',2.5)
    path('M189 179Q202 165 209 174','none','#21182E',9)
    end()
    group('mascot_blue_expression', 'Thoughtful smile')
    path('M185 231Q195 222 205 228Q213 233 207 237Q193 239 185 231Z','#187EB2')
    path('M164 247Q194 264 223 241','none','#124C78',4)
    path('M169 251Q174 266 186 258Z','#FFFCE2','#1B5D7B',1.5)
    end()
    group('mascot_blue_arms', 'Folded arm and hand on chin')
    path('M292 298C326 308 328 346 308 366C278 390 214 379 166 365Q144 363 143 340'
         'Q147 320 173 326L252 335Q272 295 292 298Z','url(#blueFur)','#138AB8',3)
    path('M114 302C88 319 92 362 124 372C155 381 179 347 204 322L231 300'
         'Q260 284 250 269Q246 261 237 265L247 248Q252 232 239 230Q228 231 218 251'
         'Q212 263 209 278Q188 264 182 274Q175 284 188 301L165 320Q133 292 114 302Z',
         'url(#blueFace)','#117EAD',3)
    path('M208 279Q214 288 211 300M230 274Q241 270 247 278M225 293Q240 285 248 291',
         'none','#158ABD',2)
    for cx,cy in [(113,322),(123,346),(140,333),(285,347)]:
        ellipse(cx,cy,8,12,'#188FC5',extra='opacity=".7"')
    end()
    group('mascot_blue_paws', 'Feet and pink pads')
    for cx,cy,angle in [(111,476,-24),(294,480,17)]:
        group('mascot_blue_paw_'+str(cx),transform=f'rotate({angle},{cx},{cy})')
        ellipse(cx,cy,46,67,'url(#blueFace)','#086EA4',3)
        ellipse(cx,cy+14,26,36,'url(#paw)','#59618E',3)
        for dx,dy in [(-23,-27),(0,-38),(22,-29)]:
            ellipse(cx+dx,cy+dy,9,13,'url(#paw)','#58608F',2)
        path(f'M{cx+22} {cy-48}Q{cx+39} {cy-37} {cx+39} {cy-15}','none','#9BF9FF',3)
        end()
    end()
    end()


def pedestal(x, y, w, h):
    group('mascot_blue_pedestal', 'Purple and gold cylindrical plinth', layer=True)
    path(f'M{x} {y}H{x+w}V{y+h}Q{x+w/2} {y+h+35} {x} {y+h}Z', 'url(#plinth)', '#9C5E33', 4)
    for xx,ww in [(x+22,w*.21),(x+w*.37,w*.26),(x+w*.76,w*.18)]:
        path(f'M{xx} {y+45}Q{xx+ww/2} {y+56} {xx+ww} {y+45}L{xx+ww} {y+h-15}'
             f'Q{xx+ww/2} {y+h-3} {xx} {y+h-15}Z','none','url(#gold)',5)
    path(f'M{x} {y-4}H{x+w}V{y+20}Q{x+w/2} {y+58} {x} {y+20}Z','url(#gold)','#B06C2B',3)
    ellipse(x+w/2,y-3,w/2,29,'url(#plinthTop)','#FFE8AC',3)
    end()


def orange_mascot(x, y, scale):
    group('mascot_orange', 'Orange fluffy waving mascot', f'translate({x},{y}) scale({scale})', layer=True)
    group('mascot_orange_body', 'Body and belly')
    path('M124 300Q91 338 104 399L90 406 107 418 94 434 110 441 103 465'
         'L120 463 117 491Q194 524 274 494L269 475 286 468 275 450 289 443 277 427'
         'Q300 358 272 310Z','url(#orangeFur)','#C35A0B',3)
    path('M163 339Q205 322 243 351L235 372 247 388 234 401 246 418 238 435 251 454'
         'L242 472 250 499Q198 517 145 494L151 475 143 458 154 444 143 425 154 409'
         'L144 391 159 376Z','url(#orangeBelly)')
    end()
    fur_lines('mascot_orange_body_fur',True)
    group('mascot_orange_wave', 'Raised waving hand')
    path('M140 341Q106 352 77 315L55 278Q23 263 22 243Q22 233 33 235L49 245'
         'L27 217Q17 204 27 199Q35 193 48 207L62 222L50 187Q46 174 58 171'
         'Q69 169 75 187L85 215L88 184Q90 171 101 175Q112 180 108 196L106 226'
         'Q127 204 135 217Q140 226 124 245L112 272Q136 288 157 304Z',
         'url(#orangeFace)','#C65D0B',3)
    path('M54 248Q70 239 82 246Q94 252 94 268M78 277Q75 287 82 295',
         'none','#DF7B0D',3)
    for d in ['M78 310Q103 332 125 327','M82 299Q109 322 137 320','M88 289Q114 309 142 310']:
        path(d,'none','#FFD767',2.5,'opacity=".65"')
    end()
    group('mascot_orange_head', 'Furry head / swept quiff')
    path('M117 306L96 311 105 288 86 294 96 271 78 277 88 255 73 262 87 238'
         'L74 244Q78 216 98 194L82 198Q97 173 117 164L99 159 126 149'
         'Q106 131 108 113Q128 129 151 125Q125 107 134 87Q153 112 184 108'
         'Q157 81 171 62Q183 94 218 93Q202 70 217 48Q224 74 253 83'
         'Q281 98 307 71Q315 99 292 120Q321 117 339 98Q343 129 319 146'
         'Q348 141 358 125Q361 155 335 173L353 173 338 191 356 193 343 211'
         'L359 217 345 231 358 244 344 251 352 273 336 271 341 291 322 288'
         'L325 307 307 301Q267 337 206 335Q148 337 117 306Z',
         'url(#orangeFace)','#D36508',3)
    for d in ['M132 140Q176 146 199 175','M151 118Q197 132 215 163','M183 103Q220 118 233 155',
              'M224 94Q246 123 251 151','M307 118Q279 129 272 163','M108 216Q90 238 93 254',
              'M319 204Q338 220 339 236','M105 268Q122 282 131 282','M302 290Q321 278 327 262']:
        path(d,'none','#FFE16A',3,'opacity=".7"')
    end()
    group('mascot_orange_face', 'Happy eyes / smiling open mouth')
    for cx,cy,angle in [(167,220,10),(269,227,-12)]:
        ellipse(cx,cy,32,42,'url(#eyeWhite)','#A65415',3,f'transform="rotate({angle},{cx},{cy})"')
        ellipse(cx+5,cy+8,16,25,'#7C2D14','#4F1B18',2)
        ellipse(cx+6,cy+9,10,20,'#241226')
        ellipse(cx+1,cy-2,7,9,'#FFFFFF')
        ellipse(cx+12,cy+19,3,4,'#FFD6A1')
    path('M140 172Q157 153 184 170M252 177Q276 163 293 185','none','#7B3015',9)
    path('M201 246Q216 236 231 248Q225 258 214 257Z','#C06013')
    path('M145 263Q205 301 295 271Q275 339 219 340Q170 336 145 263Z',
         '#4D1322','#A84B13',3)
    path('M162 277L179 282Q178 299 168 294ZM272 281L287 277Q281 295 274 292Z','#FFF5DC')
    path('M190 323Q195 299 221 307Q239 299 252 321Q222 344 190 323Z','url(#tongue)')
    path('M220 310L222 326','none','#CD4250',2)
    ellipse(133,257,20,11,'#FFB72F',extra='opacity=".6"')
    ellipse(304,267,18,10,'#FFB72F',extra='opacity=".6"')
    end()
    group('mascot_orange_lower_paw', 'Hand resting on chest')
    path('M292 350Q319 354 323 382Q325 414 303 424Q284 430 273 416L260 400'
         'Q248 392 254 381Q257 374 268 380Q260 362 270 357Q277 352 282 363Q278 349 292 350Z',
         'url(#orangeFace)','#CB640A',3)
    path('M273 378Q284 381 289 392M284 367Q297 371 302 381','none','#DF7C13',2.5)
    end()
    end()


def section(id_, x, y, w, h, label):
    group(id_, label + ' section', layer=True)
    rect(x+2,y+7,w,h,'#221031',28,extra='filter="url(#smallShadow)"')
    rect(x,y,w,h,'url(#gold)',28,'#925328',2)
    rect(x+5,y+5,w-10,h-10,'url(#recess)',23,'#AC65CA',2)
    rect(x+5,y+5,w-10,76,'url(#panel)',22)
    rect(x+5,y+42,w-10,38,'url(#panel)',0)
    path(f'M{x+7} {y+79}H{x+w-7}','none','#241038',7,'opacity=".45"')
    path(f'M{x+8} {y+76}H{x+w-8}','none','#BB76D4',3)
    rivet(x+33,y+39,11)
    rivet(x+w-33,y+39,11)
    text(x+w/2,y+55,label,35,'middle',sw=4)
    end()


def flags(x,y):
    group('portrait_language_selector', 'Language capsule / UK and US vector flags')
    rect(x+1,y+5,192,65,'#281039',32)
    rect(x,y,192,65,'url(#gold)',32,'#8F4E26',2)
    rect(x+6,y+6,180,53,'url(#off)',27)
    group('flag_uk', 'United Kingdom',f'translate({x+22},{y+14})',extra='clip-path="url(#clip_flag)"')
    rect(0,0,65,39,'#163B89',3)
    path('M1 2L64 37M64 2L1 37','none','#FFF6E8',10)
    path('M1 2L64 37M64 2L1 37','none','#D82B48',4)
    path('M32 0V39M0 19H65','none','#FFF6E8',13)
    path('M32 0V39M0 19H65','none','#D82B48',7)
    rect(0,0,65,39,'none',3,'#FFE5AC',1)
    end()
    group('flag_us', 'United States',f'translate({x+107},{y+14})')
    rect(0,0,65,39,'#FFF7E8',2)
    for i in range(7): rect(0,i*6,65,3,'#CA2B40',0)
    rect(0,0,28,23,'#193F82',0)
    for row in range(4):
        for col in range(5):
            ellipse(3+col*5.2+(row%2)*1.5,3+row*5.3,.8,.8,'#FFF7E8')
    rect(0,0,65,39,'none',2,'#FFE5AC',1)
    end()
    end()


add('<?xml version="1.0" encoding="UTF-8"?>')
add('<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" '
    'xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" width="2800" height="1400" viewBox="0 0 2800 1400">')
add('<title>QuizParty — Settings / dual orientation vector recreation</title>')
add('<desc>Original path-drawn recreation of the supplied cartoon settings reference. Left: 1920 by 1080. '
    'Right: 675 by 1200. All stage art, controls, flags and mascots are vectors. English labels and illustrative states follow the requested study.</desc>')
add('<sodipodi:namedview id="namedview" pagecolor="#0B071A" inkscape:document-units="px">'
    '<inkscape:page x="0" y="0" width="2800" height="1400" inkscape:label="Dual orientation sheet"/>'
    '</sodipodi:namedview><defs>')
gradients={
    'gold':[(0,'#FFF6C2'),(.18,'#FFE9A0'),(.43,'#F9C846'),(.70,'#B87B14'),(1,'#F0B94B')],
    'knob':[(0,'#FFF3B3'),(.46,'#FFE493'),(1,'#F5B340')],
    'titleGold':[(0,'#FFF4AE'),(.45,'#FFDF64'),(.49,'#FFD553'),(1,'#F3A023')],
    'panel':[(0,'#9E4FCC'),(.25,'#813BB3'),(1,'#5E2B97')],
    'tab':[(0,'#B360DA'),(.45,'#9B4FC9'),(1,'#8140B5')],
    'recess':[(0,'#32154E'),(.08,'#452469'),(1,'#482471')],
    'off':[(0,'#28103E'),(.35,'#4B1D73'),(1,'#7A369D')],
    'blue':[(0,'#82EDFA'),(.2,'#30BCEB'),(.55,'#2D82D8'),(1,'#1A57A4')],
    'red':[(0,'#FFAD83'),(.22,'#F25A43'),(.67,'#C92A2A'),(1,'#9F1A34')],
    'spectrum':[(0,'#00F2FE'),(.55,'#4FACFE'),(1,'#A263E9')],
    'column':[(0,'#0E102A'),(.26,'#2C1944'),(.5,'#503052'),(.7,'#1D102E'),(1,'#0B1027')],
    'plinth':[(0,'#281444'),(.2,'#64309B'),(.45,'#8F45C1'),(.64,'#51257F'),(1,'#241138')],
    'plinthTop':[(0,'#B56C26'),(.3,'#F4BB59'),(.48,'#FFF6BB'),(.65,'#FCD67A'),(1,'#C2792F')],
    'blueFur':[(0,'#71F7FF'),(.28,'#31D8EE'),(.65,'#1EB3DF'),(1,'#087DBB')],
    'blueFace':[(0,'#9CFBFF'),(.32,'#3DE7F7'),(.7,'#21C1E5'),(1,'#139DD0')],
    'belly':[(0,'#BEF8FF'),(.5,'#E1FFFF'),(1,'#74D5EB')],
    'paw':[(0,'#FFBDD5'),(.4,'#E89CBF'),(1,'#C573A3')],
    'eyeWhite':[(0,'#D5E9F8'),(.30,'#FFFFFF'),(1,'#FCF8F0')],
    'orangeFur':[(0,'#FFE276'),(.25,'#FFBB25'),(.65,'#FF9911'),(1,'#E57508')],
    'orangeFace':[(0,'#FFE985'),(.3,'#FFD144'),(.65,'#FFB51D'),(1,'#F2910C')],
    'orangeBelly':[(0,'#FFF0AD'),(.6,'#FFE4A0'),(1,'#FFC054')],
    'tongue':[(0,'#FF9C81'),(1,'#EF4D5D')],
}
for id_,stops in gradients.items():
    horizontal=id_ in ['spectrum','column','plinth','plinthTop']
    add(f'<linearGradient id="{id_}" x1="0%" y1="0%" x2="{100 if horizontal else 0}%" y2="{0 if horizontal else 100}%">'
        +''.join(f'<stop offset="{off}" stop-color="{col}"/>' for off,col in stops)+'</linearGradient>')
add('<radialGradient id="stage" cx="52%" cy="48%" r="75%"><stop stop-color="#26205B"/><stop offset=".65" stop-color="#12092B"/><stop offset="1" stop-color="#080A20"/></radialGradient>'
    '<radialGradient id="floor"><stop stop-color="#1955A2"/><stop offset=".5" stop-color="#1B1744"/><stop offset="1" stop-color="#0B081D"/></radialGradient>'
    '<linearGradient id="beamPurple" x2="0" y2="1"><stop stop-color="#B83AF0" stop-opacity=".8"/><stop offset="1" stop-color="#9D30D4" stop-opacity="0"/></linearGradient>'
    '<linearGradient id="beamBlue" x2="0" y2="1"><stop stop-color="#3DE4FF" stop-opacity=".9"/><stop offset="1" stop-color="#168CE4" stop-opacity="0"/></linearGradient>'
    '<filter id="shadow" x="-.12" y="-.2" width="1.3" height="1.5" color-interpolation-filters="sRGB"><feGaussianBlur stdDeviation="8"/></filter>'
    '<filter id="smallShadow" x="-.15" y="-.2" width="1.4" height="1.5" color-interpolation-filters="sRGB"><feGaussianBlur stdDeviation="3"/></filter>'
    '<clipPath id="clip_landscape"><rect width="1920" height="1080" rx="16"/></clipPath>'
    '<clipPath id="clip_portrait"><rect width="675" height="1200" rx="16"/></clipPath>'
    '<clipPath id="clip_flag"><rect width="65" height="39" rx="3"/></clipPath>'
    '</defs>')

group('sheet_background','Sheet / captions',layer=True)
rect(0,0,2800,1400,'#0B071A',0)
text(42,62,'SETTINGS  /  VECTOR RECREATION',23,fill='#EACB8D',sw=0,extra='letter-spacing="3"')
text(42,105,'LANDSCAPE  ·  1920 × 1080',16,fill='#978AAE',sw=0,extra='letter-spacing="2"')
text(2079,63,'PORTRAIT  ·  675 × 1200',16,fill='#978AAE',sw=0,extra='letter-spacing="2"')
text(42,1335,'03   /   CARTOON SHOWTIME',19,fill='#B4A3CA',sw=0,extra='letter-spacing="2"')
text(1962,1335,'EDITABLE VECTOR ART',16,'end',fill='#7E7197',sw=0,extra='letter-spacing="2"')
end()

group('landscape','01 Landscape — 16:9', 'translate(42,165)',layer=True,extra='clip-path="url(#clip_landscape)"')
stage('landscape_stage',1920,1080,18)
group('landscape_main_frame','Main panel / gold screws',layer=True)
frame('landscape_frame_outer',225,206,1505,712)
for xx in [268,1687]:
    for yy in [250,874]: rivet(xx,yy,15)
end()
group('landscape_inner_panel','Recessed settings panel',layer=True)
frame('landscape_frame_inner',349,296,1280,624,True,42)
rivet(390,878,14)
end()
group('landscape_navigation','Back and sidebar tabs',layer=True)
group('btn_back','Back')
rect(60,44,250,109,'#382046',27,extra='filter="url(#smallShadow)"')
rect(60,37,250,109,'url(#gold)',27,'#9B6029',3)
rect(68,44,234,92,'url(#panel)',21,'#FFF1B3',2)
path('M111 63L86 83 111 104V90H126Q150 90 145 108Q140 120 123 121Q154 132 160 109Q166 77 126 75H111Z',
     'url(#gold)','#7B382C',3)
text(181,110,'Back',38,sw=4)
end()
tab('tab_audio',69,316,317,146,'AUDIO',True)
tab('tab_gameplay',88,488,260,169,'GAMEPLAY',icon='speaker')
tab('tab_help_legal',88,681,260,169,'HELP & LEGAL')
end()
group('landscape_title','SETTINGS sign',layer=True)
title_letters('landscape_title_letters',970,224,'SETTINGS',182,106,17)
end()
group('landscape_controls','Two column controls',layer=True)
text(448,460,'MUSIC',39)
toggle('toggle_music',877,413,136,64)
slider('slider_music',448,500,564,46,.60)
text(448,660,'SFX',39)
toggle('toggle_sfx',877,614,136,64)
slider('slider_sfx',448,700,564,46,.60)
text(1084,456,'VOICE VOICE OVER',32,sw=4)
toggle('toggle_voice_over',1113,493,232,70,True,'English')
text(1084,656,'HAPTIC FEEDBACK',32,sw=4)
toggle('toggle_haptic_feedback',1119,689,142,65,False)
end()
group('landscape_actions','Bottom action buttons',layer=True)
button('btn_credits',432,820,259,76,'CREDITS',31)
button('btn_privacy_policy',719,820,339,76,'PRIVACY POLICY',30)
button('btn_reset_all',1086,820,267,76,'RESET ALL',32,True)
end()
pedestal(1490,899,392,218)
blue_mascot(1488,344,.96)
end()

group('portrait','02 Portrait — 9:16','translate(2079,86)',layer=True,extra='clip-path="url(#clip_portrait)"')
stage('portrait_stage',675,1200,31)
group('portrait_frame','Main portrait frame',layer=True)
frame('portrait_frame_outer',43,150,589,946,False,40)
end()
group('portrait_banner','Ornate title banner / crown crest',layer=True)
group('portrait_crest','Gold shell crown')
path('M246 86Q253 62 284 70Q276 39 292 26Q309 41 311 58Q302 13 324 0'
     'Q342 12 338 57Q352 17 369 26Q378 49 358 70Q390 54 407 86Z','url(#gold)','#9F632A',3)
path('M271 79Q299 59 321 86M300 33L325 80M328 16L330 76M365 41L342 81M363 82Q386 69 396 84',
     'none','#FFEB9F',3)
ellipse(334,85,39,35,'url(#gold)','#AC6C24',3)
end()
path('M49 145H21L8 173 25 198H68M626 145H652L667 173 648 198H611',
     'url(#gold)','#A16028',4)
path('M44 151H27L19 172 31 188H57M627 151H645L656 173 643 188H621','url(#panel)','#FFE6A0',2)
path('M107 94Q338 61 566 94Q578 95 582 111L588 129L616 148Q634 163 616 181'
     'L588 203L581 223Q578 238 558 234Q338 207 113 234Q94 237 91 220L84 202'
     'L59 184Q39 169 59 151L84 129L91 110Q94 96 107 94Z','url(#gold)','#A05A26',4)
path('M110 105Q338 76 562 105L577 139L608 166L577 194L566 220Q337 190 106 220'
     'L95 193L65 168L95 139Z','url(#panel)','#FFE99F',3)
for xx,yy in [(110,123),(105,202),(566,124),(567,202),(81,166),(595,166)]: rivet(xx,yy,5)
title_letters('portrait_title_letters',336,184,'SETTINGS',70,44,8)
end()
group('btn_close','Close settings',layer=True)
ellipse(602,46,36,39,'#20112B',extra='filter="url(#smallShadow)"')
ellipse(600,41,35,37,'url(#gold)','#A5642C',2)
ellipse(600,40,28,30,'url(#panel)','#FFF1B0',2)
path('M589 28L611 51M611 28L589 51','none','#663238',11)
path('M589 26L611 49M611 26L589 49','none','url(#gold)',8)
end()
section('portrait_audio_section',80,264,515,377,'AUDIO')
group('portrait_audio_controls','Portrait audio controls',layer=True)
text(106,404,'MUSIC',36,sw=4)
slider('portrait_slider_music',108,428,458,38,.50)
text(106,527,'SFX',36,sw=4)
toggle('portrait_toggle_sfx',458,486,108,52)
slider('portrait_slider_sfx',108,557,458,38,.50)
end()
section('portrait_gameplay_section',80,659,515,208,'GAMEPLAY')
group('portrait_gameplay_controls','Language selector',layer=True)
text(106,808,'LANGUAGE',32,sw=4)
flags(374,760)
end()
section('portrait_help_legal_section',80,886,515,196,'HELP & LEGAL')
group('portrait_help_controls','Reset action',layer=True)
button('btn_reset_to_default',108,993,374,68,'RESET TO DEFAULT',24)
end()
orange_mascot(365,960,.64)
end()
add('</svg>')

master=OUT/'settings-study-03.svg'
master.write_text('\n'.join(parts),encoding='utf-8')

# Exact orientation exports share the same document-space coordinates and defs.
ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('inkscape','http://www.inkscape.org/namespaces/inkscape')
ET.register_namespace('sodipodi','http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd')
for name,x,y,w,h in [('landscape',42,165,1920,1080),('portrait',2079,86,675,1200)]:
    root=ET.parse(master).getroot()
    for child in list(root):
        if child.tag.endswith('namedview') or (child.tag.endswith('}g') and child.get('id')!=name):
            root.remove(child)
    root.set('width',str(w)); root.set('height',str(h)); root.set('viewBox',f'{x} {y} {w} {h}')
    ET.ElementTree(root).write(OUT/f'settings-{name}.svg',encoding='utf-8',xml_declaration=True)

print(f'Created master + exact 16:9 / 9:16 orientation SVGs in {OUT}')
