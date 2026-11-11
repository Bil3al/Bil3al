"""Build a local preview of this README's Markdown subset (stdlib only)."""
from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def inline(value):
    value = re.sub(r'`([^`]+)`', lambda m: '<code>'+escape(m[1])+'</code>', value)
    value = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', value)
    value = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', value)
    return value


result, paragraph, in_code, in_table, in_list = [], [], False, False, False


def flush():
    if paragraph:
        result.append('<p>'+inline(' '.join(paragraph))+'</p>')
        paragraph.clear()


for row in (ROOT/'README.md').read_text(encoding='utf-8').splitlines():
    if row.startswith('```'):
        flush()
        result.append('</code></pre>' if in_code else '<pre><code>')
        in_code = not in_code
        continue
    if in_code:
        result.append(escape(row)+'\n')
        continue
    if in_table and not row.startswith('|'):
        result.append('</table></div>')
        in_table = False
    if in_list and not row.startswith('- '):
        result.append('</ul>')
        in_list = False
    if row.startswith('|'):
        flush()
        if re.fullmatch(r'[| :\-]+', row):
            continue
        header = not in_table
        if header:
            result.append('<div class="table-scroll"><table>')
            in_table = True
        tag = 'th' if header else 'td'
        result.append('<tr>'+''.join(f'<{tag}>{inline(cell.strip())}</{tag}>' for cell in row.strip('|').split('|'))+'</tr>')
    elif row.startswith('- '):
        flush()
        if not in_list:
            result.append('<ul>')
            in_list = True
        result.append('<li>'+inline(row[2:])+'</li>')
    elif row.startswith('#'):
        flush()
        level = len(row)-len(row.lstrip('#'))
        result.append(f'<h{level}>{inline(row[level:].strip())}</h{level}>')
    elif row.startswith('> '):
        flush()
        result.append('<blockquote>'+inline(row[2:])+'</blockquote>')
    elif row.startswith('<') or row == '---':
        flush()
        result.append('<hr>' if row == '---' else row)
    elif not row.strip():
        flush()
    else:
        paragraph.append(row)
flush()
style = '''
*{box-sizing:border-box}body{margin:0;background:#080f13;color:#f1f4e9;font:17px/1.75 'Segoe UI',Arial,sans-serif}
main{max-width:1200px;margin:auto;padding:28px 24px 60px}img{max-width:100%;height:auto}a{color:#dcfa73;text-underline-offset:4px}
h2{margin:48px 0 22px;font-size:26px}h3{margin-top:30px;color:#70e1e8}p,li{color:#b9c8ce}strong{color:#f1f4e9}
pre{padding:24px;background:#12232b;border:1px solid #30434b;border-radius:12px;overflow:auto;line-height:1.6}
code{font-family:Consolas,monospace;background:#12232b;padding:3px 5px;color:#dcfa73;font-size:.85em}
pre code{padding:0;color:#b9c8ce}.table-scroll{overflow-x:auto}table{width:100%;border-collapse:collapse;margin:24px 0}
th,td{padding:16px;text-align:left;border:1px solid #30434b;vertical-align:top}th{background:#12232b;color:#70e1e8}
td:first-child{min-width:210px}summary{cursor:pointer;color:#70e1e8}details{padding:16px;border:1px solid #30434b;border-radius:10px;margin-top:20px}
blockquote{margin:32px 0;padding:16px 24px;border-left:3px solid #dcfa73;color:#a6b5bd}hr{border:0;border-top:1px solid #30434b;margin:32px 0}
@media(max-width:640px){main{padding:16px}body{font-size:15px}h2{font-size:23px}}
'''
(ROOT/'preview.html').write_text('<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Bilal Malih — Neural Blueprint</title><style>'+style+'</style><main>'+''.join(result)+'</main></html>', encoding='utf-8')
print('Built preview.html from README.md')
