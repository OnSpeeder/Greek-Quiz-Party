"""Derive runtime vector skins from the Inkscape study's actual gradient definitions."""
from pathlib import Path
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
source = ET.parse(root/'docs/design/settings-study-02/settings-study-02.svg').getroot()
ns = '{http://www.w3.org/2000/svg}'
ET.register_namespace('', ns[1:-1])
defs = '<defs>' + ''.join(ET.tostring(g, encoding='unicode') for g in source.iter(ns+'linearGradient')) + '</defs>'
dest = root/'src/QuizParty.Godot/Art/Settings'
def save(name,w,h,body):
    (dest/(name+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{defs}{body}</svg>',encoding='utf-8')
def box(x,y,w,h,r,fill,stroke='',sw=2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke or "none"}" stroke-width="{sw}"/>'
frame=box(2,8,252,246,30,'#130c29')+box(2,2,252,246,30,'url(#gold)','#9a5929',3)+box(10,10,236,230,24,'url(#goldLight)')+box(17,17,222,216,19,'url(#purple)','#d598ed',2)
for x in (27,229):
    for y in (27,225):
        frame+=f'<circle cx="{x}" cy="{y}" r="8" fill="url(#gold)" stroke="#a66b2b" stroke-width="2"/><path d="M{x-4} {y+4}l8-8" stroke="#a6722f" stroke-width="2"/>'
save('frame-main',256,256,frame)
save('frame-card',128,128,box(1,4,126,122,22,'#1c102f')+box(1,1,126,122,22,'url(#gold)')+box(7,7,114,110,17,'url(#well)','#ba7fdd',2))
for state,fill in [('normal','url(#button)'),('hover','#15618a'),('active','url(#tabActive)'),('pressed','#23529a'),('disabled','#343141'),('danger','url(#red)')]:
    save('button-'+state,192,96,box(2,7,188,87,22,'#1d0a30')+box(2,1,188,88,22,'url(#gold)','#8b4d21',2)+box(8,7,176,75,16,fill,'#fff0b9',2)+'<path d="M22 13H169" stroke="#fff" stroke-opacity=".4" stroke-width="3" stroke-linecap="round"/>')
for state,fill in [('normal','url(#purple)'),('active','url(#tabActive)')]:
    save('tab-'+state,256,112,'<path d="M20 7H225L254 56 225 105H20Q2 105 2 87V25Q2 7 20 7Z" fill="url(#gold)" stroke="#824620" stroke-width="3"/>'+f'<path d="M22 15H221L244 56 221 97H22Q10 97 10 85V27Q10 15 22 15Z" fill="{fill}" stroke="#ffe9aa" stroke-width="2"/>')
save('slider-fill',128,24,box(1,2,126,20,10,'url(#gold)')+box(4,5,120,14,7,'url(#spectrum)'))
save('slider-track',128,24,box(1,2,126,20,10,'url(#gold)')+box(4,5,120,14,7,'url(#well)'))
save('mascot-plinth',512,180,box(8,35,496,130,8,'url(#purple)','#af7130',4)+'<path d="M30 60Q256 100 482 60V145Q256 178 30 145Z" fill="#53267e" stroke="#d4a34f" stroke-width="3"/><ellipse cx="256" cy="40" rx="248" ry="35" fill="url(#gold)" stroke="#fff0be" stroke-width="4"/>')
print('Exported Inkscape study gradients and skin components:',dest)
