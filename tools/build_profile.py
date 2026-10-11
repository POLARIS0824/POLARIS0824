"""Generate the GitHub README, original SVG assets and a local preview.

Python 3 standard library only. Edit ../profile.json, then run this script.
SVGs use system fonts and contain no JavaScript or external resources.
"""
from pathlib import Path
import argparse
import html
import json
import math
import re


PALETTES = {
    "light": dict(bg="#edf5ee", surface="#f7faf6", ink="#17291f", muted="#52685b", accent="#2f6b49", soft="#d5eadb", line="#c4d6c9", violet="#6b6185"),
    "dark": dict(bg="#17251d", surface="#1d3024", ink="#e4eee2", muted="#b3c8b6", accent="#a2dfb2", soft="#2e4d38", line="#3b5642", violet="#c1b6df"),
}


def esc(value):
    return html.escape(str(value), quote=True)


def text(x, y, value, size=16, fill="ink", weight=400, **attrs):
    extra = " ".join(f'{k.replace("_", "-")}="{esc(v)}"' for k, v in attrs.items())
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="var(--{fill})" {extra}>{esc(value)}</text>'


def rect(x, y, w, h, r=20, fill="surface", stroke=None):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="var(--{fill})"' + (f' stroke="var(--{stroke})"' if stroke else '') + '/>'


def svg(w, h, title, body, palette, animated=False):
    variables = ";".join(f"--{k}:{v}" for k, v in palette.items())
    style = f':root{{{variables}}}text{{font-family:"Segoe UI",Arial,sans-serif}}'
    if animated:
        star_a = star_path(8, 47, 23)
        star_b = star_path(8, 40, 31)
        style += '@keyframes orbit{to{transform:rotate(360deg)}}'
        style += f'@keyframes morph{{0%,100%{{d:path("{star_a}")}}50%{{d:path("{star_b}")}}}}'
        style += '.orbit{transform-box:fill-box;transform-origin:center;animation:orbit 80s linear infinite}.morph{animation:morph 10s ease-in-out infinite}'
        style += '@media(prefers-reduced-motion:reduce){.orbit,.morph{animation:none}}'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title)}"><title>{esc(title)}</title><style>{style}</style>{body}</svg>\n'


def star_path(points, outer, inner):
    coordinates = []
    for i in range(points * 2):
        angle = -math.pi / 2 + i * math.pi / points
        radius = outer if i % 2 == 0 else inner
        coordinates.append(f'{radius * math.cos(angle):.2f} {radius * math.sin(angle):.2f}')
    return 'M' + 'L'.join(coordinates) + 'Z'


def star(x, y, scale=1):
    return f'<g transform="translate({x} {y}) scale({scale})"><g class="orbit"><path class="morph" d="{star_path(8,47,23)}" fill="var(--accent)"/></g><circle r="6" fill="var(--bg)"/></g>'


def pill(x, y, label, size=12, fill="soft", ink="accent"):
    width = round(len(label) * size * .57 + 24)
    return rect(x, y, width, 28, 14, fill) + text(x+12, y+19, label, size, ink, 600), width


def phone(x, y):
    return f'<g transform="translate({x} {y}) rotate(-8 48 80)">' + rect(0,0,102,172,24,"surface","line") + rect(7,7,88,158,18,"bg") + rect(38,13,28,5,3,"line") + text(18,50,"DIARY",13,"accent",600) + rect(16,64,70,37,10,"soft") + '<path d="M25 77H66M25 88H53" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>' + rect(16,109,70,29,10,"surface") + '<path d="M26 123H65" stroke="var(--line)" stroke-width="3" stroke-linecap="round"/>' + '<circle cx="76" cy="145" r="10" fill="var(--accent)"/><path d="M72 145H80M76 141V149" stroke="var(--bg)" stroke-width="2" stroke-linecap="round"/></g>'


def hero(data, compact):
    w, h = (420,330) if compact else (846,260)
    b = rect(.5,.5,w-1,h-1,28,"bg","line")
    b += text(28,38,"ANDROID / CLIENT",12,"muted",600,letter_spacing=2)
    b += text(28,102,data['display_name'],54 if compact else 62,"ink",700,letter_spacing=-2)
    b += text(30,137,data['role'],20 if compact else 23,"ink",500)
    if compact:
        b += text(30,168,"Useful interfaces. Thoughtful data handling.",14,"muted")
        b += pill(28,186,data['availability'],10)[0]
        x=28
        for label in ['Kotlin','Compose','Coroutines','Room']:
            p,pw=pill(x,277,label,11,fill="surface",ink="muted"); b+=p; x+=pw+6
        b += star(346,239,.64)
    else:
        b += text(30,171,"Useful interfaces. Thoughtful data handling.",17,"muted")
        b += pill(28,196,data['availability'],11)[0]
        b += '<circle cx="713" cy="137" r="87" fill="var(--soft)"/><circle cx="713" cy="137" r="103" fill="none" stroke="var(--line)" stroke-dasharray="3 7"/>'
        b += phone(628,48) + star(771,76,.83)
        b += text(652,234,"KOTLIN + COMPOSE",11,"muted",600,letter_spacing=1.2)
    return w,h,b


def icon(kind,x,y):
    paths = {
        'ui':'<rect x="1" y="2" width="28" height="22" rx="4"/><path d="M1 9H29M7 15H12M7 19H21"/>',
        'storage':'<ellipse cx="15" cy="6" rx="13" ry="4"/><path d="M2 6V23C2 29 28 29 28 23V6M2 15C2 21 28 21 28 15"/>',
        'network':'<circle cx="5" cy="15" r="4"/><circle cx="25" cy="5" r="4"/><circle cx="25" cy="25" r="4"/><path d="M9 13L21 7M9 17L21 23"/>',
        'test':'<rect x="4" y="3" width="24" height="26" rx="5"/><path d="M10 16L15 21L23 11"/>',
    }
    return f'<g transform="translate({x} {y})" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{paths[kind]}</g>'


def skills(data, pair, compact):
    w,h = (420,446) if compact else (846,223)
    b=''
    for i,item in enumerate(data['skills'][pair*2:pair*2+2]):
        x=0 if compact else i*431
        y=i*223 if compact else 0
        cw=420 if compact else 415
        b += rect(x+.5,y+.5,cw-1,206,24,"bg","line")
        b += icon(item['icon'],x+24,y+24)
        b += text(x+68,y+44,f"0{pair*2+i+1}",12,"muted",600,letter_spacing=1)
        b += text(x+24,y+85,item['title'],23,"ink",600)
        for n,line in enumerate(item['lines']): b += text(x+24,y+119+n*25,line,15,"muted")
        b += text(x+24,y+182,item['tag'],10,"accent",600,letter_spacing=1.1)
    return w,h,b


def section(number,label,compact):
    w=420 if compact else 846
    b=text(0,24,f'{number:02}',12,"accent",600,letter_spacing=1) + text(37,25,label,21,"ink",600)
    # Decorative rule moves away from the label in compact variants.
    start = min(w-40,37 + len(label)*12 + 22)
    b += f'<path d="M{start} 18H{w-1}" stroke="var(--line)"/>'
    return w,38,b


def project(item,compact):
    w,h=(420,242) if compact else (846,186)
    b=rect(.5,.5,w-1,h-1,24,"bg","line")
    b+=text(24,31,item['label'],10,"accent",600,letter_spacing=.7)
    b+=text(24,73,item['name'],32,"ink",650,letter_spacing=-.7)
    lines=[]
    if compact:
        for line in item['lines']:
            words=line.split(); current=''
            for word in words:
                if len(current)+len(word)+1>44:
                    lines.append(current);current=word
                else:current=(current+' '+word).strip()
            if current:lines.append(current)
    else:lines=item['lines']
    for n,line in enumerate(lines): b+=text(24,104+n*22,line,14 if compact else 16,"muted")
    x=24
    for label in item['tags']:
        p,pw=pill(x,h-41,label,10,fill="surface",ink="muted"); b+=p;x+=pw+6
    arrow_x=w-43
    b+=f'<circle cx="{arrow_x}" cy="60" r="17" fill="var(--soft)"/><path d="M{arrow_x-5} 65L{arrow_x+5} 55M{arrow_x-4} 55H{arrow_x+5}V64" fill="none" stroke="var(--accent)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
    return w,h,b


def stack(data,compact):
    w=420 if compact else 846
    y=30;b=''
    for row in data['stack_rows']:
        b+=text(24,y,row[0],10,"accent",600,letter_spacing=1)
        x=24 if compact else 168
        py=y+12 if compact else y-19
        for label in row[1:]:
            expected=round(len(label)*11*.57+24)
            if x+expected>w-20:x=24 if compact else 168;py+=36
            p,pw=pill(x,py,label,11,fill="surface",ink="ink");b+=p;x+=pw+7
        y=py+60
    h=y-12
    return w,h,rect(.5,.5,w-1,h-1,24,"bg","line")+b


def picture(name,alt,compact=True):
    sources=''
    if compact:
        sources+=f'  <source media="(max-width: 620px) and (prefers-color-scheme: dark)" srcset="assets/{name}-dark-compact.svg">\n'
        sources+=f'  <source media="(max-width: 620px)" srcset="assets/{name}-light-compact.svg">\n'
    sources+=f'  <source media="(prefers-color-scheme: dark)" srcset="assets/{name}-dark.svg">\n'
    return f'<picture>\n{sources}  <img src="assets/{name}-light.svg" width="100%" alt="{esc(alt)}">\n</picture>'


def inline_markdown(value):
    value=html.escape(value)
    value=re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',r'<a href="\2">\1</a>',value)
    value=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',value)
    value=re.sub(r'`([^`]+)`',r'<code>\1</code>',value)
    return value


def preview_html(markdown,data):
    parts=[]
    # Only the small, controlled Markdown subset emitted below is needed.
    for block in markdown.strip().split('\n\n'):
        if block.startswith('## <picture>'):
            parts.append('<h2>'+block[3:]+'</h2>')
        elif block.startswith('<'):
            parts.append(block)
        elif block.startswith('- '):
            parts.append('<ul>'+''.join('<li>'+inline_markdown(line[2:])+'</li>' for line in block.splitlines())+'</ul>')
        else:
            parts.append('<p>'+inline_markdown(block)+'</p>')
    return '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>POLARIS · GitHub profile preview</title>
<style>
:root{color-scheme:light dark;--page:#fff;--ink:#1f2328;--muted:#59636e;--border:#d1d9e0;--link:#0969da;--code:#eff1f3}
@media(prefers-color-scheme:dark){:root{--page:#0d1117;--ink:#e6edf3;--muted:#9ba8b5;--border:#30363d;--link:#82bdff;--code:#252b34}}
*{box-sizing:border-box}body{margin:0;background:var(--page);color:var(--ink);font:15px/1.75 -apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif}
main{max-width:910px;padding:24px 30px;margin:36px auto;border:1px solid var(--border);border-radius:8px}p{margin:17px 0}picture{display:block}img{max-width:100%;height:auto;display:block}h2{margin:32px 0 18px;padding:0 0 9px;border-bottom:1px solid var(--border);line-height:1}a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}ul{padding-left:23px;margin:16px 0}li{margin:8px 0}sub{color:var(--muted)}code{font-size:13px;background:var(--code);padding:2px 5px;border-radius:5px}.preview-note{max-width:910px;margin:20px auto -15px;padding:0 10px;color:var(--muted);font-size:12px}
@media(max-width:620px){body{font-size:14px}main{margin:18px 10px;padding:16px 12px}h2{margin-top:26px}.preview-note{margin:14px 10px -5px;padding:0}}
</style></head><body><div class="preview-note">本地排版预览 · SVG 动画随系统减少动态效果设置暂停 · 浅色 / 深色随系统主题</div><main>'''+''.join(parts)+'''</main></body></html>\n'''


def build(root):
    data=json.loads((root/'profile.json').read_text(encoding='utf-8'))
    assets=root/'assets';assets.mkdir(exist_ok=True)
    components=[('hero',lambda compact:hero(data,compact),'POLARIS · Android client development · seeking an Android internship',True)]
    for i in range(2):
        components.append((f'skills-{i+1}',lambda c,i=i:skills(data,i,c),' · '.join(s['title']+': '+ ' '.join(s['lines']) for s in data['skills'][i*2:i*2+2]),False))
    labels=['What I build','Selected projects','Tech stack','Connect']
    for i,label in enumerate(labels):components.append((f'section-{i+1}',lambda c,i=i,label=label:section(i+1,label,c),label,False))
    for i,item in enumerate(data['projects']):components.append((f'project-{i+1}',lambda c,item=item:project(item,c),item['name']+'. '+' '.join(item['lines']),False))
    components.append(('stack',lambda c:stack(data,c),'Project technologies: '+', '.join(', '.join(row[1:]) for row in data['stack_rows']),False))
    for name,fn,title,animated in components:
        for theme,palette in PALETTES.items():
            for compact in [False,True]:
                w,h,body=fn(compact)
                (assets/f'{name}-{theme}{"-compact" if compact else ""}.svg').write_text(svg(w,h,title,body,palette,animated),encoding='utf-8')
    blocks=[picture('hero','POLARIS · Android 客户端开发 · 寻找 Android 实习'),data['intro'],data['focus']]
    blocks.append('## '+picture('section-1','项目中实践的能力'))
    for i in range(2):blocks.append(picture(f'skills-{i+1}',' · '.join(s['title']+': '+' '.join(s['lines']) for s in data['skills'][i*2:i*2+2])))
    blocks.append('## '+picture('section-2','精选项目'))
    for i,item in enumerate(data['projects']):
        url=f'https://github.com/{data["username"]}/{item["repo"]}'
        blocks.append(f'<a href="{url}">\n'+picture(f'project-{i+1}',item['name']+'. '+' '.join(item['lines']))+'\n</a>')
        blocks.append('\n'.join('- '+line for line in item['details']))
        blocks.append('实现与测试：'+' · '.join(f'[{label}]({url})' for label,url in item['evidence']))
    blocks.append('## '+picture('section-3','项目技术栈'))
    blocks.append(picture('stack','项目技术栈：'+', '.join(', '.join(row[1:]) for row in data['stack_rows'])))
    blocks.append('## '+picture('section-4','联系与交流'))
    blocks.append(f'[GitHub](https://github.com/{data["username"]}) · [Android 项目](https://github.com/{data["username"]}/FitLog) · [项目交流](https://github.com/{data["username"]}/FitLog/issues)')
    if data.get('contact_email'):blocks.append(f'求职联系：[{data["contact_email"]}](mailto:{data["contact_email"]})')
    blocks.append(data['contact_text'])
    blocks.append('<sub>主页按公开仓库的实现与测试源码整理。FitLog 持续开发中；项目状态与测试结果以各仓库记录为准。</sub>')
    markdown='\n\n'.join(blocks)+'\n'
    (root/'README.md').write_text(markdown,encoding='utf-8')
    (root/'preview.html').write_text(preview_html(markdown,data),encoding='utf-8')
    print(json.dumps(dict(assets=len(list(assets.glob('*.svg'))),readme_bytes=len(markdown.encode('utf-8')))))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    build(parser.parse_args().root.resolve())
