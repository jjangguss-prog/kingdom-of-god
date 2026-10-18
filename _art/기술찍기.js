// 탑 4단계 기술의 예시 화면 찍기 v0.2 (2026-10-18). 시험용(게임에는 들어가지 않음)
// 사용: 스크린샷서버.py(kog-shot, 8770)로 index.html을 열고, 창을 1600×900으로 키운 뒤 콘솔에서
//   eval(await fetch('/_art/기술찍기.js').then(r=>r.text())); await SKH.run('priest_bless');   // 또는 SKH.runAll('priest')
// 판 4 갈대 상자(낮, 특별한 일 없음)에 탑 하나를 세워 그 기술만 3단계로 익히고, 그 기술이 눈에 보이는 순간(글자·빛·투사체)을 기다려
// 세 장을 _art/sk_raw/<이름>_<n>.jpg로 남긴다. 화면은 탑 전체와 기술이 일어난 곳이 다 들어오게 16:9로 자르고, 세겔 숫자는 빼고 찍는다.
// 고른 장은 art/sk/<가지>_<기술>.jpg로 옮긴다(index.html의 기술 카드).
(() => {
  const k = __kog, SID = 4, W = 1280, H = 720;
  const live = e => e.state === 'walk' || e.state === 'fight';
  const txt = (G, s) => G.texts.some(t => t.s === s && t.t < .5);
  const T = G => G.towers.find(t => t.branch);
  async function save(name, cx, cy, gw, mark, G) {
    const cv = document.getElementById('cv'), s = cv.width / W, gh = gw * 9 / 16;
    const c2 = document.createElement('canvas'); c2.width = 480; c2.height = 270;
    const g = c2.getContext('2d'); g.imageSmoothingQuality = 'high';
    g.drawImage(cv, (cx - gw / 2) * s, (cy - gh / 2) * s, gw * s, gh * s, 0, 0, 480, 270);
    if (mark) mark(g, (x, y) => [(x - cx + gw / 2) * 480 / gw, (y - cy + gh / 2) * 270 / gh], 480 / gw, G);
    const b = await new Promise(r => c2.toBlob(r, 'image/jpeg', .88));
    return (await fetch('/_shot?name=' + name, { method: 'POST', body: b })).status;
  }
  // 덧그림: 늘어난 사거리나 빨라진 탑처럼 눈에 안 보이는 효과를 금빛 점선 고리와 글로 표시
  const ring = (g, P, k2, x, y, r, col, lab) => { const [px, py] = P(x, y); g.save(); g.strokeStyle = col; g.lineWidth = 3; g.setLineDash([7, 6]); g.beginPath(); g.ellipse(px, py, r * k2, r * k2 * .55, 0, 0, Math.PI * 2); g.stroke(); g.restore();
    if (lab) { g.save(); g.font = 'bold 15px sans-serif'; g.textAlign = 'center'; g.lineWidth = 4; g.strokeStyle = 'rgba(40,22,8,.9)'; const ly = Math.max(16, py - r * k2 * .55 - 8); g.strokeText(lab, px, ly); g.fillStyle = '#fff1c2'; g.fillText(lab, px, ly); g.restore(); } };
  const label = (g, x, y, t) => { g.save(); g.font = 'bold 15px sans-serif'; g.textAlign = 'center'; g.lineWidth = 4; g.strokeStyle = 'rgba(40,22,8,.9)'; g.strokeText(t, x, Math.max(16, y)); g.fillStyle = '#fff1c2'; g.fillText(t, x, Math.max(16, y)); g.restore(); };
  const arrow = (g, x1, y1, x2, y2) => { const a = Math.atan2(y2 - y1, x2 - x1); g.save(); g.strokeStyle = 'rgba(255,214,110,.95)'; g.fillStyle = 'rgba(255,214,110,.95)'; g.lineWidth = 3; g.setLineDash([7, 5]); g.beginPath(); g.moveTo(x1, y1); g.lineTo(x2 - Math.cos(a) * 8, y2 - Math.sin(a) * 8); g.stroke(); g.setLineDash([]); g.beginPath(); g.moveTo(x2, y2); g.lineTo(x2 - Math.cos(a - .45) * 13, y2 - Math.sin(a - .45) * 13); g.lineTo(x2 - Math.cos(a + .45) * 13, y2 - Math.sin(a + .45) * 13); g.closePath(); g.fill(); g.restore(); };
  const near = (G, x, y, r, f) => G.enemies.filter(e => live(e) && Math.hypot(e.x - x, e.y - y) < r && (!f || f(e))).slice(0, 6).map(e => [e.x, e.y - 30]);
  const tx = (G, s, dy) => { const t = G.texts.find(t => t.s === s); return t ? [[t.x - 40, t.y - 10], [t.x + 40, t.y + (dy || 40)]] : []; };
  const rally = (G, dy) => { const t = T(G), us = G.units.filter(u => u.tw === t && u.state === 'ok'); return [[t.rally.x - 50, t.rally.y - (dy || 80)], [t.rally.x + 50, t.rally.y + 20], ...us.map(u => [u.x, u.y - 40])]; };
  // 기술 장면: spot(탑 자리), line·branch, sk(익힐 기술 번호), wave, cond(G,t)(찍을 순간), pts(G)(꼭 들어올 곳), help(곁에 세울 탑 [자리,계열,단계]), hard(적 피해 배율), mark(덧그림)
  const S = {};
  // 제사장
  S.priest_bless = { spot: 10, line: 'levi', branch: 'priest', sk: 0, help: [[5, 'shep', 3]], wave: [['soldier', 14, .7, 0, 0], ['shield', 6, 1.2, 3, 0]], hard: 3, cond: G => G.fx.filter(f => f.k === 'plus').length >= 4, pts: G => G.fx.filter(f => f.k === 'plus').map(f => [f.x, f.y + 20]),
    mark: (g, P, s, G) => { g.save(); g.font = 'bold 22px sans-serif'; g.textAlign = 'center'; g.lineWidth = 4; g.strokeStyle = 'rgba(20,50,10,.85)'; g.fillStyle = '#9ef07a'; for (const u of G.units) if (u.state === 'ok' && u.tw && u.tw.line === 'shep') { const [x, y] = P(u.x, u.y - 46); g.strokeText('+', x, y); g.fillText('+', x, y); } g.restore(); } };
  S.priest_gate = { spot: 10, line: 'levi', branch: 'priest', sk: 1, wave: [['soldier', 12, .7, 0, 0], ['shield', 4, 1.2, 2, 0]], cond: G => G.units.some(u => u.gk && u.target && live(u.target)), wait: .6, pts: G => { const u = G.units.find(u => u.gk); return [[u.x, u.y - 60], [u.x, u.y + 10]]; } };
  S.priest_rod = { spot: 10, line: 'levi', branch: 'priest', sk: 2, help: [[5, 'shep', 1]], wave: [['giant', 3, 3, 0, 0], ['soldier', 10, .8, 1, 0]], hard: 6, cond: G => txt(G, '다시 일어남'), wait: .15, pts: G => tx(G, '다시 일어남') };
  // 찬양대
  S.choir_song = { spot: 10, line: 'levi', branch: 'choir', sk: 0, pre: G => { T(G).songCd = 16; }, wave: [['soldier', 16, .45, 0, 0], ['raider', 8, .5, 2, 0]], cond: G => txt(G, '노래를 시작할 때에'), wait: .35, pts: G => near(G, 479, 341, 170, e => e.stun > 0) };
  S.choir_timbrel = { spot: 10, line: 'levi', branch: 'choir', sk: 1, help: [[5, 'watch', 3], [2, 'art', 3]], wave: [['shield', 14, .5, 0, 0], ['centurion', 4, 1, 2, 0]], cond: (G, t) => G.projs.some(p => p.k === 'stone') && G.projs.some(p => p.k === 'arrow' || p.k === 'bolt') && G.enemies.filter(e => live(e) && Math.hypot(e.x - 520, e.y - 420) < 180).length >= 3, pts: G => [[440, 330], [660, 470], [467, 470]],
    mark: (g, P, s) => { for (const [x, y] of [[467, 437], [634, 453]]) ring(g, P, s, x, y - 20, 46, 'rgba(255,214,110,.95)', '빨리!'); } };
  S.choir_turn = { spot: 10, line: 'levi', branch: 'choir', sk: [0, 2], pre: G => { T(G).songCd = 16; }, wave: [['soldier', 18, .4, 0, 0], ['raider', 8, .45, 2, 0]], cond: G => G.fx.some(f => f.k === 'ring' && f.col === '255,200,160'), wait: .1, pts: G => G.fx.filter(f => f.k === 'ring' && f.col === '255,200,160').map(f => [f.x, f.y]),
    mark: (g, P, s, G) => { const f = G.fx.find(f => f.k === 'ring' && f.col === '255,200,160'); if (f) { const [x, y] = P(f.x, f.y + 40); label(g, x, y, '서로 쳐요'); } } };
  // 순금 등잔대
  S.menorah_seven = { spot: 10, line: 'art', branch: 'menorah', sk: 0, wave: [['soldier', 20, .35, 0, 0]], cond: G => G.fx.some(f => f.k === 'chain' && f.pts.length >= 7 && f.t < .08), pts: G => G.fx.find(f => f.k === 'chain' && f.pts.length >= 7).pts };
  S.menorah_spirit = { spot: 10, line: 'art', branch: 'menorah', sk: 1, wave: [['soldier', 20, .35, 0, 0]], cond: G => G.fx.some(f => f.k === 'ring' && f.col === '255,226,140' && f.t < .12) && G.enemies.filter(e => live(e) && Math.hypot(e.x - 479, e.y - 341) < 120).length >= 3, pts: G => [[364, 341], [594, 341], [479, 410]] };
  S.menorah_shine = { spot: 10, line: 'art', branch: 'menorah', sk: 2, wave: [['soldier', 12, .8, 0, 0]], cond: G => G.fx.some(f => f.k === 'chain' && f.t < .08 && Math.hypot(f.pts[1][0] - 479, f.pts[1][1] - 341) > 150), pts: G => G.fx.find(f => f.k === 'chain').pts, gw: 520,
    mark: (g, P, s) => ring(g, P, s, 479, 341, 178 * 1.24, 'rgba(255,214,110,.9)', '앞을 비추라') };
  // 요단 동편 용사
  S.jordan_draw = { spot: 10, line: 'watch', branch: 'jordan', sk: 0, wave: [['shield', 14, .9, 0, 0]], cond: G => txt(G, '활을 당겨'), wait: .2, pts: G => tx(G, '활을 당겨') };
  S.jordan_deer = { spot: 10, line: 'watch', branch: 'jordan', sk: 1, wave: [['soldier', 24, .4, 0, 0]], cond: G => { const t = T(G); return G.enemies.filter(e => live(e) && Math.hypot(e.x - 479, e.y - 341) < 300).length >= 3 && G.fx.some(f => f.k === 'spark' && f.x === t.x && Math.abs(f.y - (t.y - 90)) < 1 && f.t < .05); }, wait: .1, pts: G => G.projs.filter(p => p.k === 'snipe').map(p => [p.tx, p.ty]).concat(near(G, 479, 341, 300)),
    mark: (g, P, s, G) => { const t = T(G), [x, y] = P(t.x, t.y - 150); g.save(); g.font = 'bold 15px sans-serif'; g.textAlign = 'center'; g.lineWidth = 4; g.strokeStyle = 'rgba(40,22,8,.9)'; g.strokeText('곧바로 다음 화살', x, Math.max(16, y)); g.fillStyle = '#fff1c2'; g.fillText('곧바로 다음 화살', x, Math.max(16, y)); g.restore(); } };
  S.jordan_lead = { spot: 10, line: 'watch', branch: 'jordan', sk: 2, wave: [['whisper', 10, .7, 0, 0], ['fear', 4, 1.4, 2, 0]], cond: G => G.projs.some(p => p.k === 'snipe' && p.tg && p.tg.def.fly && Math.hypot(p.x - p.tx, p.y - p.ty) < 120), pts: G => G.projs.filter(p => p.k === 'snipe').map(p => [p.tx, p.ty - 20]), gw: 520,
    mark: (g, P, s) => ring(g, P, s, 479, 341, 240 * 1.24, 'rgba(255,214,110,.9)', '앞장선 용사') };
  // 나실인
  S.nazirite_spirit = { spot: 10, line: 'shep', branch: 'nazirite', sk: 0, wave: [['giant', 3, 2.5, 0, 0], ['soldier', 10, .7, 1, 0]], cond: G => txt(G, '여호와의 영'), wait: .3, pts: G => rally(G, 90) };
  S.nazirite_lion = { spot: 10, line: 'shep', branch: 'nazirite', sk: 1, wave: [['giant', 4, 2.5, 0, 0]], cond: G => G.units.some(u => u.naz && u.target && u.target.type === 'giant' && u.target.state === 'fight') && G.units.filter(u => u.naz && u.target).length >= 2, wait: .5, pts: G => rally(G, 110) };
  S.nazirite_last = { spot: 10, line: 'shep', branch: 'nazirite', sk: 2, wave: [['giant', 5, 1.5, 0, 0]], hard: 5, cond: G => txt(G, '이번만 나를 강하게 하사'), wait: .2, pts: G => tx(G, '이번만 나를 강하게 하사', 60) };
  // 다윗의 용사들
  S.mighty_abishai = { spot: 10, line: 'shep', branch: 'mighty', sk: 0, wave: [['soldier', 16, .5, 0, 0]], cond: G => G.fx.some(f => f.k === 'thrust' && f.t < .12), pts: G => { const f = G.fx.find(f => f.k === 'thrust'); return [[f.x1, f.y1 - 40], [f.x2, f.y2 + 30]]; } };
  S.mighty_benaiah = { spot: 10, line: 'shep', branch: 'mighty', sk: 1, wave: [['shield', 10, .7, 0, 0], ['giant', 2, 3, 2, 0]], cond: G => txt(G, '브나야의 일격'), wait: .15, pts: G => tx(G, '브나야의 일격', 70) };
  S.mighty_three = { spot: 10, line: 'shep', branch: 'mighty', sk: 2, wave: [['soldier', 20, .45, 0, 0]], cond: G => G.units.some(u => u.dash), wait: .12, pts: G => G.units.filter(u => u.mighty).flatMap(u => [[u.x, u.y - 40]].concat(u.dash ? [[u.dash.x, u.dash.y - 30]] : [])),
    mark: (g, P, s, G) => { for (const u of G.units.filter(u => u.mighty && u.dash)) { const [x1, y1] = P(u.x, u.y - 16), [x2, y2] = P(u.dash.x, u.dash.y - 16); arrow(g, x1, y1, x2, y2); } } };
  // 베냐민 궁수
  S.benjamin_twin = { spot: 10, line: 'watch', branch: 'benjamin', sk: 0, wave: [['soldier', 16, .5, 0, 0]], cond: G => { const a = G.projs.filter(p => p.k === 'arrow' && Math.hypot(p.x - 479, p.y - 260) < 70); return a.length >= 2 && new Set(a.map(p => p.tg)).size >= 2; }, pts: G => G.projs.filter(p => p.k === 'arrow').map(p => [p.tx, p.ty]),
    mark: (g, P, s, G) => { const t = T(G), tg = [...new Set(G.projs.filter(p => p.k === 'arrow' && p.tg).map(p => p.tg))].slice(0, 2); for (const e of tg) { const [x1, y1] = P(t.x, t.y - 100), [x2, y2] = P(e.x, e.y - 22); arrow(g, x1, y1, x2, y2); } const [lx, ly] = P(t.x, t.y - 150); label(g, lx, ly, '한 번에 둘'); } };
  S.benjamin_sling = { spot: 10, line: 'watch', branch: 'benjamin', sk: 1, wave: [['raider', 12, .6, 0, 0]], cond: G => G.projs.some(p => p.k === 'bsling' && Math.hypot(p.x - p.tx, p.y - p.ty) < 60), pts: G => G.projs.filter(p => p.k === 'bsling').map(p => [p.tx, p.ty]) };
  S.benjamin_left = { spot: 10, line: 'watch', branch: 'benjamin', sk: 2, wave: [['soldier', 16, .5, 0, 0]], cond: G => txt(G, '틀림없이!'), wait: .2, pts: G => tx(G, '틀림없이!') };
  // 웃시야의 기계
  S.uzziah_big = { spot: 10, line: 'art', branch: 'uzziah', sk: 0, wave: [['giant', 3, 2, 0, 0], ['soldier', 8, .8, 1, 0]], cond: G => G.projs.some(p => p.k === 'stone' && p.main && p.t / p.dur > .9), pts: G => G.projs.filter(p => p.main).flatMap(p => [[p.tx, p.ty - 70], [p.tx, p.ty + 25]]),
    mark: (g, P, s, G) => { const p = G.projs.find(p => p.main); if (p) { const [x, y] = P(p.tx, p.ty - 70); label(g, x, y, '큰 돌'); } } };
  S.uzziah_bolt = { spot: 10, line: 'art', branch: 'uzziah', sk: 1, wave: [['soldier', 18, .4, 0, 0]], cond: G => G.projs.filter(p => p.k === 'arrow' && p.ph).length >= 3, wait: .08, pts: G => G.projs.filter(p => p.k === 'arrow' && p.ph).map(p => [p.tx, p.ty]) };
  S.uzziah_corner = { spot: 10, line: 'art', branch: 'uzziah', sk: 2, wave: [['ram', 2, 3, 0, 0], ['soldier', 6, .9, 1, 0]], cond: G => G.projs.some(p => p.k === 'stone' && p.t / p.dur > .85 && G.enemies.some(e => e.type === 'ram' && live(e) && Math.hypot(e.x - p.tx, e.y - p.ty) < 50)), pts: G => G.enemies.filter(e => e.type === 'ram' && live(e)).map(e => [e.x, e.y - 40]), gw: 540,
    mark: (g, P, s) => ring(g, P, s, 479, 341, 205 * 1.24, 'rgba(255,214,110,.9)', '성 모퉁이 망대') };

  async function run(name, n = 3, gap = .1) {
    const o = S[name]; if (!o) return 'no ' + name;
    for (let i = 1; i <= 21; i++) k.BEST[i] = 3;
    k.STAGES[SID].waves = [o.wave, [['soldier', 1, 1, 0, 0]]];
    k.STAGES[SID].dmgMul = o.hard || 1;
    k.start(SID, 'moses'); const G = k.G; if (G.coach) G.coach.off = true; G.hold = false;
    G.noHero = true; G.hero.state = 'away'; G.hero.x = G.hero.y = -999;
    G.gold = 1e6;
    for (const [sp, l, tier] of o.help || []) { k.build(sp, l); for (let i = 1; i < tier; i++) k.upgrade(sp); }
    k.build(o.spot, o.line); k.upgrade(o.spot); k.upgrade(o.spot); k.branch(o.spot, o.branch);
    for (const i of [].concat(o.sk)) for (let j = 0; j < 3; j++) k.skill(o.spot, i);
    if (o.pre) o.pre(G);
    k.callWave();
    let t = 0, hit = null, got = 0, fr = null;
    for (let f = 0; f < 60 * 70; f++) {
      k.sim(1 / 60); t += 1 / 60;
      if (hit == null) { let c = false; try { c = o.cond(G, t); } catch (e) { } if (c) hit = t; continue; }
      if (t >= hit + (o.wait || 0) + got * gap) {
        G.texts = G.texts.filter(x => !/^[+-]\d+( 세겔)?$/.test(x.s));   // 세겔 숫자는 빼고 찍는다
        k.draw();
        if (!fr) {   // 첫 장에서 자리를 정해 세 장 모두 같은 자리로
          const tw = T(G); let pts = [[tw.x - 34, tw.y - 112], [tw.x + 34, tw.y + 22]];
          try { pts = pts.concat(o.pts(G, t)); } catch (e) { }
          const x0 = Math.min(...pts.map(p => p[0])) - 50, x1 = Math.max(...pts.map(p => p[0])) + 50, y0 = Math.min(...pts.map(p => p[1])) - 40, y1 = Math.max(...pts.map(p => p[1])) + 40;
          const gw = Math.min(W, Math.max(o.gw || 340, x1 - x0, (y1 - y0) * 16 / 9)), gh = gw * 9 / 16;
          fr = [Math.max(gw / 2, Math.min(W - gw / 2, (x0 + x1) / 2)), Math.max(gh / 2, Math.min(H - gh / 2, (y0 + y1) / 2)), gw];
        }
        await save(name + '_' + (++got), fr[0], fr[1], fr[2], o.mark, G);
        if (got >= n) break;
      }
    }
    k.STAGES[SID].dmgMul = 1;
    return name + (hit == null ? ' 못 찍음' : ' ' + got + '장 ' + hit.toFixed(1) + '초');
  }
  window.SKH = { S, run, save, async runAll(only) { const out = []; for (const nm of Object.keys(S)) if (!only || nm.startsWith(only)) out.push(await run(nm)); return out; } };
})();
