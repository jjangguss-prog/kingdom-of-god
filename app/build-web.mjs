// 웹 게임(../index.html + ../art)을 안드로이드 앱 안의 www로 묶는다. 글꼴은 처음 한 번 내려받아 앱에 넣는다(인터넷 없이도 돌게).
// 사용: node build-web.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const GAME = path.join(HERE, '..');
const WWW = path.join(HERE, 'app', 'src', 'main', 'assets', 'www');
const FONTS = path.join(HERE, 'fonts');   // 내려받은 글꼴(저장소에 함께 둔다)
const FONT_CSS = 'https://fonts.googleapis.com/css2?family=Jua&family=Gowun+Batang:wght@400;700&family=Gowun+Dodum&display=swap';
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36';

async function fonts() {
  const css = path.join(FONTS, 'fonts.css');
  if (fs.existsSync(css)) return;
  fs.mkdirSync(FONTS, { recursive: true });
  let text = await (await fetch(FONT_CSS, { headers: { 'User-Agent': UA } })).text();
  const urls = [...new Set([...text.matchAll(/url\((https:[^)]+)\)/g)].map(m => m[1]))];
  let i = 0;
  for (const u of urls) {
    const name = `f${String(i++).padStart(3, '0')}.woff2`;
    const buf = Buffer.from(await (await fetch(u, { headers: { 'User-Agent': UA } })).arrayBuffer());
    fs.writeFileSync(path.join(FONTS, name), buf);
    text = text.split(u).join(name);
  }
  fs.writeFileSync(css, text);
  console.log('글꼴', urls.length, '개 받음');
}

function copyDir(a, b) {
  fs.mkdirSync(b, { recursive: true });
  for (const f of fs.readdirSync(a)) {
    const s = path.join(a, f), d = path.join(b, f);
    if (fs.statSync(s).isDirectory()) copyDir(s, d); else fs.copyFileSync(s, d);
  }
}

await fonts();
fs.rmSync(WWW, { recursive: true, force: true });
fs.mkdirSync(WWW, { recursive: true });
let html = fs.readFileSync(path.join(GAME, 'index.html'), 'utf8');
html = html.replace(/<link rel="preconnect"[^>]*>\s*/g, '')
           .replace(/<link rel="stylesheet" href="https:\/\/fonts\.googleapis\.com[^>]*>/, '<link rel="stylesheet" href="fonts/fonts.css">');
html = '<!doctype html><html lang="ko"><head><meta charset="utf-8">'
     + '<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">'
     + '</head><body>\n' + html + '\n</body></html>\n';
fs.writeFileSync(path.join(WWW, 'index.html'), html);
copyDir(path.join(GAME, 'art'), path.join(WWW, 'art'));
if (fs.existsSync(path.join(GAME, 'music'))) copyDir(path.join(GAME, 'music'), path.join(WWW, 'music'));   // 배경 음악(관현악·합창)
copyDir(FONTS, path.join(WWW, 'fonts'));
console.log('www 준비 끝:', WWW);
