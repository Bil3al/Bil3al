"""Generate Bilal's self-contained GitHub artwork with Python's standard library."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)
INK, MUTED, LIME, CYAN = '#f1f4e9', '#a6b5bd', '#dcfa73', '#70e1e8'


def text(x, y, value, size=16, color=INK, weight=400, extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" {extra}>{escape(value)}</text>'


def rect(x, y, w, h, fill='#12232b', stroke='#30434b', rx=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" rx="{rx}"/>'


def line(x1, y1, x2, y2, color='#30434b', extra=''):
    return f'<path d="M{x1} {y1}H{x2}" stroke="{color}" fill="none" {extra}/>' if y1 == y2 else f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" fill="none" {extra}/>'


def save(name, height, title, content):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">Identité de Bilal Malih : développement full stack, intelligence artificielle et systèmes RAG.</desc>
<defs>
 <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#a6b5bd" stroke-opacity=".07"/></pattern>
 <radialGradient id="glow"><stop stop-color="#70e1e8" stop-opacity=".16"/><stop offset="1" stop-color="#70e1e8" stop-opacity="0"/></radialGradient>
 <style>
 text{{font-family:'Segoe UI',Arial,sans-serif}} .mono{{font-family:Consolas,monospace;letter-spacing:2px}}
 .orbit{{transform-origin:968px 244px;animation:orbit 40s linear infinite}}
 .flow{{stroke-dasharray:6 10;animation:flow 4s linear infinite}}
 .pulse{{animation:pulse 4s ease-in-out infinite}}
 @keyframes orbit{{to{{transform:rotate(360deg)}}}}
 @keyframes flow{{to{{stroke-dashoffset:-96}}}}
 @keyframes pulse{{50%{{opacity:.4}}}}
 @media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
 </style>
</defs>
<rect width="1200" height="{height}" rx="18" fill="#0b181e"/>
<rect width="1200" height="{height}" rx="18" fill="url(#grid)"/>
{content}
</svg>'''
    (ASSETS / name).write_text(svg, encoding='utf-8')


hero = text(48, 49, 'BM / ENGINEERING NOTES', 14, LIME, 600, 'class="mono"')
hero += text(1152, 49, 'MAROC · BIL3AL', 13, MUTED, extra='text-anchor="end" class="mono"')
hero += line(48, 73, 1152, 73)
hero += '<circle cx="968" cy="244" r="215" fill="url(#glow)"/>'
hero += text(48, 131, 'ÉLÈVE INGÉNIEUR ENSIAS / SOFTWARE & AI', 15, CYAN, 600, 'class="mono"')
hero += text(43, 220, 'BILAL', 100, INK, 800)
hero += text(43, 315, 'MALIH', 100, LIME, 800)
hero += text(50, 361, 'Du logiciel robuste à l’IA qui agit.', 23)
hero += text(50, 396, 'Full stack · RAG · Systèmes multi-agents', 23, MUTED)
hero += line(48, 438, 1152, 438)
hero += text(48, 478, 'SPRING BOOT  /  REACT  /  GENERATIVE AI', 14, MUTED, extra='class="mono"')
hero += text(1152, 478, 'CODE → CONNECT → CREATE', 13, CYAN, extra='text-anchor="end" class="mono"')
for radius in [94, 146, 190]:
    hero += f'<circle cx="968" cy="244" r="{radius}" fill="none" stroke="#30434b"/>'
hero += '<g class="orbit"><ellipse cx="968" cy="244" rx="190" ry="65" fill="none" stroke="#70e1e8" stroke-width="1.5" transform="rotate(-35 968 244)"/><circle cx="968" cy="54" r="6" fill="#dcfa73"/><circle cx="822" cy="244" r="4" fill="#70e1e8"/></g>'
hero += rect(905, 181, 126, 126, '#dcfa73', '#dcfa73', 24)
hero += text(968, 262, 'BM', 49, '#0b181e', 800, 'text-anchor="middle"')
hero += rect(788, 357, 360, 44, '#12232b')
hero += '<circle class="pulse" cx="810" cy="379" r="4" fill="#dcfa73"/>'
hero += text(830, 384, 'À LA RECHERCHE D’UN PFE', 13, LIME, extra='class="mono"')
save('hero.svg', 512, 'Bilal Malih — Élève ingénieur ENSIAS, full stack et IA, recherche de stage PFE', hero)

stack = text(40, 49, '01 / CAPABILITY ATLAS', 14, LIME, 600, 'class="mono"')
stack += text(40, 96, 'Du produit au modèle.', 35, weight=700)
stack += text(1160, 96, 'UNE STACK, PLUSIEURS DIMENSIONS', 12, MUTED, extra='class="mono" text-anchor="end"')
cards = [
 ('01', 'Backend & Architecture', 'Java 21 · Spring Boot · FastAPI', 'Spring Security · REST · gRPC'),
 ('02', 'Frontend & Realtime', 'React · TypeScript · JavaScript', 'WebSocket · HTML · CSS · PWA'),
 ('03', 'Agentic AI & Retrieval', 'Python · LangGraph · Ollama', 'RAG · BM25 · Reranking · DeBERTa'),
 ('04', 'Data & Vector Search', 'PostgreSQL · MySQL · MongoDB', 'Redis · Neo4j · Qdrant · ChromaDB'),
 ('05', 'Platform & Observability', 'Docker · Kubernetes · Helm · Trivy', 'Prometheus · Loki · Jenkins · CI/CD'),
 ('06', 'Engineering Practices', 'POO · SOLID · Design Patterns', 'Microservices · JUnit · Git · Jira', 'Agile · Travail en équipe'),
]
for i, (number, title, *rows) in enumerate(cards):
    x, y = 40 + (i % 2) * 568, 130 + (i // 2) * 174
    stack += rect(x, y, 552, 158)
    stack += text(x+20, y+33, number, 13, CYAN, extra='class="mono"')
    stack += text(x+62, y+35, title, 23, weight=650)
    stack += line(x+20, y+53, x+532, y+53)
    for j, row in enumerate(rows):
        stack += text(x+20, y+84+j*25, row, 18, MUTED)
save('stack.svg', 666, 'Stack technique de Bilal Malih — six domaines', stack)

pipeline = text(40, 49, '02 / INTELLIGENCE IN MOTION', 14, LIME, 600, 'class="mono"')
pipeline += text(40, 98, 'Connecter les données à l’intelligence.', 35, weight=700)
pipeline += text(40, 132, 'SciCheck AI : recherche hybride, agents locaux et validation des citations.', 19, MUTED)
for i, (label, title, detail) in enumerate([
 ('01 / SOURCE', 'Articles arXiv', 'Assertions scientifiques'),
 ('02 / RETRIEVE', 'Recherche hybride', 'BM25 · Chroma · reranker'),
 ('03 / REASON', 'Agents locaux', 'LangGraph · Ollama · NLI'),
 ('04 / VALIDATE', 'Vérification', 'Posture · citations'),
]):
    x = 40+i*287
    pipeline += rect(x, 179, 259, 145)
    pipeline += text(x+18, 210, label, 12, CYAN, extra='class="mono"')
    pipeline += text(x+18, 253, title, 23, weight=650)
    pipeline += text(x+18, 292, detail, 16, MUTED)
    if i < 3:
        pipeline += line(x+259, 251, x+287, 251, LIME, 'stroke-width="2" class="flow"')
pipeline += line(40, 361, 1160, 361)
pipeline += text(40, 399, 'SCICHECK AI / RAG AGENTIQUE LOCAL', 13, LIME, extra='class="mono"')
pipeline += text(1160, 399, 'RECHERCHER → RAISONNER → VÉRIFIER', 12, MUTED, extra='class="mono" text-anchor="end"')
save('intelligence.svg', 436, 'SciCheck AI — arXiv, recherche hybride, agents locaux et vérification des citations', pipeline)

evidence = text(40, 49, '03 / BEYOND THE CODE', 14, LIME, 600, 'class="mono"')
evidence += text(40, 98, 'Apprendre. Construire. S’engager.', 35, weight=700)
for i, (value, label, detail) in enumerate([
    ('1er / 250+', 'MAJOR DE PROMOTION', 'Licence · Sciences maths & informatique'),
    ('2e PLACE', 'HACKATHON D.A.T.A / INPT', 'Computer vision appliquée à la santé'),
    ('10+', 'ÉVÉNEMENTS ORGANISÉS', 'Avec l’ENSIAS IT Club'),
]):
    x = 40 + i*379
    evidence += rect(x, 130, 362, 164)
    evidence += text(x+20, 186, value, 38, LIME, 750)
    evidence += text(x+20, 227, label, 12, CYAN, 600, 'class="mono"')
    evidence += text(x+20, 266, detail, 15, MUTED)
save('highlights.svg', 326, 'Major sur plus de 250 étudiants, deuxième au hackathon D.A.T.A et organisation de plus de dix événements', evidence)

footer = text(40, 47, 'BUILD SOMETHING MEANINGFUL.', 14, LIME, 600, 'class="mono"')
footer += text(40, 103, 'Une idée complexe. Une solution élégante.', 36, weight=700)
footer += text(40, 149, 'Construisons des systèmes intelligents, accessibles et utiles.', 22, MUTED)
footer += line(40, 181, 1160, 181)
footer += text(40, 217, 'BILAL MALIH / BIL3AL', 13, CYAN, extra='class="mono"')
footer += text(1160, 217, 'FULL STACK × APPLIED AI', 13, LIME, extra='class="mono" text-anchor="end"')
save('footer.svg', 250, 'Collaborer avec Bilal Malih — full stack et IA appliquée', footer)
print('Generated 5 SVG assets in', ASSETS)
