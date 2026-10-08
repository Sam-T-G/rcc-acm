/* ===========================================================================
   ACM @ RCC deck kit. The career disk: a plug-in slide kind (data-kind="disk").
   Loaded as a module before deck.js; registers window.DeckKinds.disk.

   The slide's HTML is the source of truth: ol.stations > li, one per role, each
   with data-majors="CS:0.6,DS:0.4" and data-tier (classic, growing, new). The
   engine places every role on a disk of majors, CS (theory) at one pole and ME
   (physical) at the other, and flies a camera between them, one station per
   beat. Beat 0 is the overview, beats 1..N the stations, beat N+1 the finale.
   Every word on screen stays in the DOM (the station card), so it is crisp,
   searchable, and held to the type floors; the canvas only draws.

   Entering from the slide before it, the page shatters: that slide is redrawn
   onto a sheet from its real word positions, cracks, and breaks into shards
   while the camera punches through into space. Reduced motion is a cut.
   =========================================================================== */
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';

const MAJORS = [
  { key: 'CS', name: 'Computer science', deg: 0 },
  { key: 'CompE', name: 'Computer engineering', deg: 60 },
  { key: 'EE', name: 'Electrical engineering', deg: 120 },
  { key: 'ME', name: 'Mechanical engineering', deg: 180 },
  { key: 'DS', name: 'Data science', deg: 300 },
];
const THEORY = new THREE.Color('#4d9fff'), HOT = new THREE.Color('#fff4ea'), PHYSICAL = new THREE.Color('#ff4d00');
const SPACE = new THREE.Color('#0e0a09');
const R_IN = 5.2, R_OUT = 11.2;
const TIER_R = { classic: 6.6, growing: 8.3, new: 10.0 };
const clamp = (x, a, b) => Math.max(a, Math.min(b, x));
const smooth = (x) => { x = clamp(x, 0, 1); return x * x * (3 - 2 * x); };
const ramp = (x, a, b) => smooth((x - a) / (b - a));
const inOut = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
const outExpo = (t) => (t >= 1 ? 1 : 1 - Math.pow(2, -10 * t));

// Theory to physical: 0 at CS, 1 at ME, along either arc.
function physicality(deg) { const d = Math.abs(((deg % 360) + 360) % 360); return (d > 180 ? 360 - d : d) / 180; }
function spectrum(t) {
  const c = new THREE.Color();
  return t < 0.5 ? c.copy(THEORY).lerp(HOT, t / 0.5) : c.copy(HOT).lerp(PHYSICAL, (t - 0.5) / 0.5);
}
function angleOf(majors) {
  let x = 0, y = 0;
  for (const [k, w] of Object.entries(majors)) {
    const m = MAJORS.find((q) => q.key === k); if (!m) continue;
    const a = THREE.MathUtils.degToRad(m.deg); x += Math.cos(a) * w; y += Math.sin(a) * w;
  }
  if (Math.hypot(x, y) < 1e-3) { const first = MAJORS.find((q) => q.key === Object.keys(majors)[0]); return first ? first.deg + 90 : 0; }
  return (THREE.MathUtils.radToDeg(Math.atan2(y, x)) + 360) % 360;
}
// Disk lies in the XZ plane; CS (0 deg) points away from the overview camera.
function onDisk(deg, r, y = 0) { const a = THREE.MathUtils.degToRad(deg); return new THREE.Vector3(Math.sin(a) * r, y, -Math.cos(a) * r); }

const SPRITES = [];
function textSprite(text, opts = {}) {
  const s = drawSprite(null, text, opts); SPRITES.push([s, text, opts]); return s;
}
// Webfonts land after the scene is built; every label is redrawn once they do.
function drawSprite(into, text, { font = '700 64px Inter', color = '#ffffff', height = 1, pad = 24, letter = 0 } = {}) {
  const c = document.createElement('canvas'), g = c.getContext('2d');
  g.font = font; if (letter) g.letterSpacing = letter + 'px';
  const w = Math.ceil(g.measureText(text).width) + pad * 2, h = Math.ceil(parseInt(font.match(/(\d+)px/)[1], 10) * 1.5) + pad;
  c.width = w * 2; c.height = h * 2; g.scale(2, 2);
  g.font = font; if (letter) g.letterSpacing = letter + 'px';
  g.fillStyle = color; g.textBaseline = 'middle'; g.fillText(text, pad, h / 2);
  const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 4;
  if (into) { const old = into.material.map; into.material.map = tex; into.material.needsUpdate = true; if (old) old.dispose(); into.scale.set(height * w / h, height, 1); return into; }
  // Screen-sized: height is a fraction of the view's height, whatever the distance.
  const mat = new THREE.SpriteMaterial({ map: tex, transparent: true, depthWrite: false, toneMapped: false, sizeAttenuation: false });
  const s = new THREE.Sprite(mat); s.scale.set(height * w / h, height, 1); s.center.set(0.5, 0.5);
  return s;
}
function glowTexture(inner = 'rgba(255,255,255,1)') {
  const c = document.createElement('canvas'); c.width = c.height = 128; const g = c.getContext('2d');
  const r = g.createRadialGradient(64, 64, 0, 64, 64, 64);
  r.addColorStop(0, inner); r.addColorStop(0.25, 'rgba(255,255,255,0.35)'); r.addColorStop(1, 'rgba(255,255,255,0)');
  g.fillStyle = r; g.fillRect(0, 0, 128, 128);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}

function readStations(slide) {
  return [...slide.querySelectorAll('.stations > li')].map((li, i) => {
    const majors = {};
    (li.getAttribute('data-majors') || 'CS:1').split(',').forEach((p) => { const [k, w] = p.split(':'); majors[k.trim()] = parseFloat(w) || 1; });
    const deg = angleOf(majors);
    return { li, i, majors, deg, tier: li.getAttribute('data-tier') || 'growing', name: (li.querySelector('h3') || li).textContent.trim() };
  });
}
// Neighbors at the same tier get pushed apart so no two beacons overlap.
function relax(st) {
  for (let pass = 0; pass < 60; pass++) {
    for (let a = 0; a < st.length; a++) for (let b = a + 1; b < st.length; b++) {
      const A = st[a], B = st[b]; const pa = onDisk(A.deg, A.r), pb = onDisk(B.deg, B.r);
      const d = pa.distanceTo(pb); if (d > 1.9) continue;
      let dd = ((B.deg - A.deg + 540) % 360) - 180; if (Math.abs(dd) < 0.01) dd = 0.01;
      const push = (1.9 - d) * 3.2 * Math.sign(dd);
      A.deg -= push; B.deg += push;
    }
  }
}

function build(slide, api) {
  const stations = readStations(slide);
  if (!stations.length) return null;
  // ?card=<name> on the URL tries a station-card design without editing the deck.
  try { const q = new URLSearchParams(location.search).get('card'); if (q) slide.dataset.card = q; } catch (e) {}
  // data-card="mix": each station docks its card right (dock) or left (codex), picked
  // by a hash of its name so the run is the same every time, never three alike in a row.
  const MIX = slide.dataset.card === 'mix';
  if (MIX) {
    let run = 0, last = '';
    stations.forEach((st) => {
      let h = 0; for (const ch of st.name) h = (h * 31 + ch.charCodeAt(0)) >>> 0;
      let side = (h >> 3) & 1 ? 'dock' : 'codex';
      if (side === last && run >= 2) side = side === 'dock' ? 'codex' : 'dock';
      run = side === last ? run + 1 : 1; last = side; st.side = side; st.li.dataset.side = side;
    });
    slide.dataset.card = stations[0].side;
  }
  stations.forEach((s) => { s.r = TIER_R[s.tier] || TIER_R.growing; s.deg0 = s.deg; });
  // A station code (STN 07 / 32) leads each card's tier line, as text the checks can measure.
  // Each card's tier line becomes a ring map (the disk's three rings, this one lit) and
  // a badge whose fill grows with the tier: outline, half, solid. Shape carries the
  // tier, not hue (slide rules: no hue on tiers). The words stay the same text.
  const SVGN = 'http://www.w3.org/2000/svg', RING = { classic: 1, growing: 2, new: 3 };
  // The ring's line, in the deck's own pitch: the middle is what you know, the edge is new.
  const TIER_DESC = { classic: 'the ones you know', growing: 'on the rise', new: 'booming with AI' };
  stations.forEach((s, k) => {
    const tier = s.li.querySelector('.st__tier'); if (!tier || tier.querySelector('.st__code')) return;
    const word = tier.textContent.trim();
    tier.textContent = '';
    const code = document.createElement('span'); code.className = 'st__code';
    code.textContent = 'STN ' + String(k + 1).padStart(2, '0') + ' / ' + stations.length;
    const map = document.createElementNS(SVGN, 'svg'); map.setAttribute('class', 'st__ring'); map.setAttribute('viewBox', '0 0 40 40'); map.setAttribute('aria-hidden', 'true');
    [7, 13, 19].forEach((r, i) => {
      const c = document.createElementNS(SVGN, 'circle'); c.setAttribute('cx', '20'); c.setAttribute('cy', '20'); c.setAttribute('r', String(r));
      c.setAttribute('class', i + 1 === RING[s.tier] ? 'is-here' : ''); map.appendChild(c);
    });
    const badge = document.createElement('span'); badge.className = 'st__badge'; badge.textContent = word;
    const desc = document.createElement('span'); desc.className = 'st__tierdesc'; desc.textContent = TIER_DESC[s.tier] || '';
    tier.append(code, map, badge, desc);
  });
  relax(stations);
  const N = stations.length;

  // The presenter's run sheet and the phone remote never show the scene: no WebGL
  // there, but the same number of presses, so "next press" stays in step.
  const VIEWQ = (/[?&]view=(mirror|presenter|remote|runsheet)\b/.exec(location.search) || [])[1] || '';
  if (VIEWQ && VIEWQ !== 'mirror') {
    return { beats: N + 1, set() {}, go() {}, enter() {}, leave() {}, busy() { return false; }, finish() {}, sleep() {}, resize() {} };
  }
  // A preview frame in the presenter window draws at half resolution, a few times a
  // second, and cuts between stations, so the projector's scene keeps the GPU.
  const MIRROR = VIEWQ === 'mirror';

  // ---------- DOM: canvas under the HUD
  const host = document.createElement('div'); host.className = 'disk__canvas'; host.setAttribute('aria-hidden', 'true');
  slide.insertBefore(host, slide.firstChild);
  slide.classList.add('has-scene');
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: 'high-performance' }); }
  catch (e) { host.remove(); slide.classList.remove('has-scene'); return null; }
  renderer.setPixelRatio(MIRROR ? 0.5 : Math.min(2, window.devicePixelRatio || 1));
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 0.9;
  renderer.setClearColor(SPACE, 1);
  host.appendChild(renderer.domElement);

  const scene = new THREE.Scene(); scene.fog = new THREE.FogExp2(SPACE, 0.006);
  const camera = new THREE.PerspectiveCamera(45, 16 / 9, 0.05, 2000);
  const composer = new EffectComposer(renderer);
  composer.addPass(new RenderPass(scene, camera));
  const bloom = new UnrealBloomPass(new THREE.Vector2(960, 540), 0.55, 0.45, 0.62); composer.addPass(bloom);
  composer.addPass(new OutputPass());

  // ---------- Space: stars, streaks for the warp, two faint nebulae
  const starGeo = new THREE.BufferGeometry(), SN = 5000, sp = new Float32Array(SN * 3), sc = new Float32Array(SN * 3);
  for (let i = 0; i < SN; i++) {
    const r = 120 + Math.random() * 500, th = Math.random() * Math.PI * 2, ph = Math.acos(2 * Math.random() - 1);
    sp.set([r * Math.sin(ph) * Math.cos(th), r * Math.cos(ph) * 0.6, r * Math.sin(ph) * Math.sin(th)], i * 3);
    const c = spectrum(Math.random()).lerp(new THREE.Color('#ffffff'), 0.7); sc.set([c.r, c.g, c.b], i * 3);
  }
  starGeo.setAttribute('position', new THREE.BufferAttribute(sp, 3)); starGeo.setAttribute('color', new THREE.BufferAttribute(sc, 3));
  const stars = new THREE.Points(starGeo, new THREE.PointsMaterial({ size: 1.6, sizeAttenuation: true, vertexColors: true, transparent: true, opacity: 0.9, depthWrite: false, fog: false }));
  scene.add(stars);
  // Warp streaks: short lines along the flight path, shown only while the camera punches through.
  const WN = 900, wp = new Float32Array(WN * 6);
  for (let i = 0; i < WN; i++) {
    const a = Math.random() * Math.PI * 2, rr = 3 + Math.random() * 22, z = 20 + Math.random() * 110, y = 22 + Math.sin(a) * rr, x = Math.cos(a) * rr;
    wp.set([x, y, z, x, y, z + 2 + Math.random() * 6], i * 6);
  }
  const warpGeo = new THREE.BufferGeometry(); warpGeo.setAttribute('position', new THREE.BufferAttribute(wp, 3));
  const warp = new THREE.LineSegments(warpGeo, new THREE.LineBasicMaterial({ color: '#ffd9c2', transparent: true, opacity: 0, blending: THREE.AdditiveBlending, depthWrite: false, fog: false }));
  scene.add(warp);
  const glow = glowTexture();
  [[THEORY, new THREE.Vector3(-60, 10, -120), 170], [PHYSICAL, new THREE.Vector3(70, -20, 110), 190]].forEach(([col, pos, size]) => {
    const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: glow, color: col, transparent: true, opacity: 0.16, blending: THREE.AdditiveBlending, depthWrite: false, fog: false }));
    s.position.copy(pos); s.scale.set(size, size, 1); scene.add(s);
  });

  // ---------- The disk
  const diskGroup = new THREE.Group(); scene.add(diskGroup);
  const diskMat = new THREE.ShaderMaterial({
    transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide,
    uniforms: { uReveal: { value: 1 }, uTime: { value: 0 }, uTheory: { value: THEORY }, uHot: { value: HOT }, uPhys: { value: PHYSICAL }, uFocus: { value: -1 } },
    vertexShader: 'varying vec2 vP; void main(){ vP = position.xy; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }',
    fragmentShader: `
      varying vec2 vP; uniform float uReveal, uTime, uFocus; uniform vec3 uTheory, uHot, uPhys;
      const float PI = 3.14159265;
      void main(){
        float r = length(vP);
        float a = atan(vP.x, vP.y); // 0 at CS, clockwise positive
        float deg = mod(degrees(a) + 360.0, 360.0);
        float phys = (deg > 180.0 ? 360.0 - deg : deg) / 180.0;
        vec3 col = phys < 0.5 ? mix(uTheory, uHot, phys / 0.5) : mix(uHot, uPhys, (phys - 0.5) / 0.5);
        float rn = (r - ${R_IN.toFixed(2)}) / ${(R_OUT - R_IN).toFixed(2)};
        float bands = smoothstep(0.035, 0.0, abs(fract(rn * 6.0) - 0.5) - 0.465);
        float ticks = step(0.985, fract(deg / 5.0)) * smoothstep(0.0, 0.1, rn) * (1.0 - smoothstep(0.9, 1.0, rn));
        float edge = smoothstep(0.03, 0.0, rn) + smoothstep(0.97, 1.0, rn);
        float body = 0.025 + 0.035 * (1.0 - rn);
        float sweep = step(deg, uReveal * 360.0 + 0.001) * smoothstep(uReveal * 360.0 + 0.001, uReveal * 360.0 - 12.0, deg + (1.0 - uReveal) * 0.0);
        float head = uReveal < 1.0 ? smoothstep(10.0, 0.0, abs(deg - uReveal * 360.0)) : 0.0;
        float focus = uFocus >= 0.0 ? 0.55 + 0.45 * smoothstep(40.0, 0.0, min(abs(deg - uFocus), 360.0 - abs(deg - uFocus))) : 1.0;
        float pulse = 0.5 + 0.5 * sin(uTime * 1.2 - rn * 6.0);
        float alpha = (body + bands * 0.22 + ticks * 0.35 + edge * 0.75) * focus * (0.85 + 0.15 * pulse);
        alpha = alpha * max(sweep, 0.0) + head * 0.9;
        gl_FragColor = vec4(col * alpha, alpha);
      }`,
  });
  const diskMesh = new THREE.Mesh(new THREE.RingGeometry(R_IN, R_OUT, 360, 12), diskMat);
  diskMesh.rotation.x = -Math.PI / 2; diskGroup.add(diskMesh);
  // Floor grid far below, fading with distance.
  const grid = new THREE.GridHelper(260, 104, '#3a2a24', '#22181' + '5');
  grid.position.y = -3.2; grid.material.transparent = true; grid.material.opacity = 0.35; grid.material.depthWrite = false; diskGroup.add(grid);
  // Major labels just outside the rim, and the two ends named.
  const majorSprites = MAJORS.map((m) => {
    const col = '#' + spectrum(physicality(m.deg)).getHexString();
    const s = textSprite(m.name.toUpperCase(), { font: '600 56px "JetBrains Mono"', color: col, height: 0.036, letter: 6 });
    s.position.copy(onDisk(m.deg, R_OUT + 2.6, 0.6)); diskGroup.add(s);
    return s;
  });
  const ends = [['THEORY', 0], ['PHYSICAL', 180]].map(([t, deg]) => {
    const s = textSprite(t, { font: '500 44px "JetBrains Mono"', color: '#b9aba6', height: 0.03, letter: 10 });
    s.position.copy(onDisk(deg, R_OUT + 2.6, -0.45)); diskGroup.add(s); return s;
  });

  // ---------- Stations
  const pick = [];
  stations.forEach((st) => {
    const col = spectrum(physicality(st.deg)), p = onDisk(st.deg, st.r);
    const g = new THREE.Group(); g.position.copy(p); diskGroup.add(g);
    const H = st.tier === 'new' ? 3.4 : st.tier === 'growing' ? 2.6 : 1.9;
    const beam = new THREE.Mesh(new THREE.CylinderGeometry(0.035, 0.035, H, 8, 1, true), new THREE.MeshBasicMaterial({ color: col, transparent: true, opacity: 0.85, blending: THREE.AdditiveBlending, depthWrite: false }));
    beam.position.y = H / 2; g.add(beam);
    const node = new THREE.Mesh(new THREE.SphereGeometry(0.13, 24, 16), new THREE.MeshBasicMaterial({ color: col.clone().multiplyScalar(1.15), transparent: true }));
    node.position.y = H; g.add(node);
    const halo = new THREE.Mesh(new THREE.RingGeometry(0.34, 0.42, 48), new THREE.MeshBasicMaterial({ color: col, transparent: true, opacity: 0.8, side: THREE.DoubleSide, blending: THREE.AdditiveBlending, depthWrite: false }));
    halo.rotation.x = -Math.PI / 2; halo.position.y = 0.02; g.add(halo);
    const label = textSprite(st.name, { font: '600 52px Inter', color: '#fbf6f3', height: 0.032 });
    label.position.y = H + 0.62; g.add(label);
    const hit = new THREE.Mesh(new THREE.SphereGeometry(0.7, 8, 8), new THREE.MeshBasicMaterial({ visible: false }));
    hit.position.y = H * 0.6; hit.userData.beat = st.i + 1; g.add(hit); pick.push(hit);
    st.li.style.setProperty('--st', '#' + col.getHexString());
    Object.assign(st, { g, beam, node, halo, label, H, col, pos: p });
  });

  if (document.fonts && document.fonts.load) {
    Promise.all(['600 56px "JetBrains Mono"', '500 44px "JetBrains Mono"', '600 52px Inter'].map((f) => document.fonts.load(f)))
      .then(() => SPRITES.forEach(([sp, text, opts]) => drawSprite(sp, text, opts))).catch(() => {});
  }

  // ---------- The shatter sheet: the previous slide redrawn, cut into shards
  const SHEET_Z = 104, SHEET_Y = 26, CAM0 = new THREE.Vector3(0, SHEET_Y, SHEET_Z + 10);
  let sheet = null;
  function makeSheet(from) {
    if (sheet) { scene.remove(sheet); sheet.geometry.dispose(); sheet.material.map && sheet.material.map.dispose(); sheet.material.dispose(); sheet = null; }
    const fov = THREE.MathUtils.degToRad(camera.fov), Hs = 2 * 10 * Math.tan(fov / 2), Ws = Hs * camera.aspect;
    // Texture: paper, then every visible word of the slide at its real position.
    const cw = 1920, ch = Math.round(1920 / camera.aspect), c = document.createElement('canvas'); c.width = cw; c.height = ch;
    const g = c.getContext('2d'), dr = api.deck.getBoundingClientRect(), k = cw / dr.width;
    const bg = getComputedStyle(api.deck).backgroundColor; g.fillStyle = bg && bg !== 'rgba(0, 0, 0, 0)' ? bg : '#fdf8f7'; g.fillRect(0, 0, cw, ch);
    if (from) {
      from.querySelectorAll('.w__in, .eyebrow, .label').forEach((el) => {
        if (el.closest('.notes') || (el.querySelector && el.querySelector('.w__in'))) return;
        const r = el.getBoundingClientRect(); if (!r.width) return;
        const cs = getComputedStyle(el); g.font = `${cs.fontStyle} ${cs.fontWeight} ${parseFloat(cs.fontSize) * k}px ${cs.fontFamily}`;
        if (cs.letterSpacing !== 'normal') g.letterSpacing = parseFloat(cs.letterSpacing) * k + 'px'; else g.letterSpacing = '0px';
        g.fillStyle = cs.color; g.textBaseline = 'alphabetic';
        const txt = cs.textTransform === 'uppercase' ? el.textContent.toUpperCase() : el.textContent;
        const lh = parseFloat(cs.fontSize) * k;
        g.fillText(txt, (r.left - dr.left) * k, (r.top - dr.top) * k + lh * 0.95);
      });
    }
    const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace;
    // Jittered grid, two triangles a cell, each triangle its own shard.
    const CX = 18, CY = 10, pts = [];
    for (let y = 0; y <= CY; y++) for (let x = 0; x <= CX; x++) {
      const edge = x === 0 || y === 0 || x === CX || y === CY;
      pts.push([x / CX + (edge ? 0 : (Math.random() - 0.5) * 0.7 / CX), y / CY + (edge ? 0 : (Math.random() - 0.5) * 0.7 / CY)]);
    }
    const P = [], UV = [], BA = [], CEN = [], RND = [];
    const at = (x, y) => pts[y * (CX + 1) + x];
    const tri = (a, b, cc) => {
      const cx = (a[0] + b[0] + cc[0]) / 3, cy = (a[1] + b[1] + cc[1]) / 3;
      const rnd = [Math.random(), Math.random(), Math.random(), Math.random()];
      [[a, [1, 0, 0]], [b, [0, 1, 0]], [cc, [0, 0, 1]]].forEach(([q, bary]) => {
        P.push((q[0] - 0.5) * Ws, (0.5 - q[1]) * Hs, 0); UV.push(q[0], 1 - q[1]); BA.push(...bary);
        CEN.push((cx - 0.5) * Ws, (0.5 - cy) * Hs, 0); RND.push(...rnd);
      });
    };
    for (let y = 0; y < CY; y++) for (let x = 0; x < CX; x++) {
      const a = at(x, y), b = at(x + 1, y), cc = at(x, y + 1), d = at(x + 1, y + 1);
      if ((x + y) % 2) { tri(a, b, d); tri(a, d, cc); } else { tri(a, b, cc); tri(b, d, cc); }
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.Float32BufferAttribute(P, 3)); geo.setAttribute('uv', new THREE.Float32BufferAttribute(UV, 2));
    geo.setAttribute('bary', new THREE.Float32BufferAttribute(BA, 3)); geo.setAttribute('cen', new THREE.Float32BufferAttribute(CEN, 3)); geo.setAttribute('rnd', new THREE.Float32BufferAttribute(RND, 4));
    const mat = new THREE.ShaderMaterial({
      transparent: true, depthWrite: false, side: THREE.DoubleSide, toneMapped: false,
      uniforms: { map: { value: tex }, uCrack: { value: 0 }, uT: { value: 0 }, uW: { value: Ws }, uH: { value: Hs }, uCrackCol: { value: new THREE.Color('#ff6a1a') } },
      vertexShader: `
        attribute vec3 bary; attribute vec3 cen; attribute vec4 rnd; varying vec2 vUv; varying vec3 vB; varying float vFade;
        uniform float uCrack, uT, uW, uH;
        mat3 rot(vec3 ax, float an){ ax = normalize(ax); float s = sin(an), c = cos(an), o = 1.0 - c;
          return mat3(o*ax.x*ax.x + c, o*ax.x*ax.y + ax.z*s, o*ax.z*ax.x - ax.y*s,
                      o*ax.x*ax.y - ax.z*s, o*ax.y*ax.y + c, o*ax.y*ax.z + ax.x*s,
                      o*ax.z*ax.x + ax.y*s, o*ax.y*ax.z - ax.x*s, o*ax.z*ax.z + c); }
        void main(){
          vUv = uv; vB = bary;
          vec3 local = position - cen;
          float d = length(cen.xy / vec2(uW, uH));            // 0 center, ~0.7 corner
          float delay = d * 0.35 + rnd.w * 0.12;
          float t = clamp((uT - delay) / (1.0 - delay * 0.6), 0.0, 1.0);
          float e = t * t;
          vec3 dir = normalize(vec3(cen.xy + (rnd.xy - 0.5) * 0.6, 0.0) + vec3(0.0, 0.0, 0.001));
          vec3 vel = dir * (6.0 + rnd.x * 10.0) + vec3(0.0, 0.0, 9.0 + rnd.y * 14.0);
          local = rot(vec3(rnd.x - 0.5, rnd.y - 0.5, rnd.z - 0.5), e * (4.0 + rnd.z * 8.0)) * local * (1.0 - 0.35 * e);
          vec3 p = cen + local + vel * e;
          p.z += uCrack * (0.18 * (1.0 - d)) * (0.5 + rnd.z);  // the page bows toward you as it cracks
          vFade = 1.0 - smoothstep(0.35, 0.95, t);
          gl_Position = projectionMatrix * modelViewMatrix * vec4(p, 1.0);
        }`,
      fragmentShader: `
        uniform sampler2D map; uniform float uCrack, uT; uniform vec3 uCrackCol; varying vec2 vUv; varying vec3 vB; varying float vFade;
        void main(){
          vec4 c = texture2D(map, vUv);
          float edge = 1.0 - smoothstep(0.0, 0.035, min(vB.x, min(vB.y, vB.z)));
          vec3 col = mix(c.rgb, uCrackCol * 3.0, edge * uCrack);
          col += uCrackCol * edge * uT * 2.0;
          gl_FragColor = vec4(col, vFade);
        }`,
    });
    sheet = new THREE.Mesh(geo, mat); sheet.position.set(0, SHEET_Y, SHEET_Z); scene.add(sheet);
  }

  // ---------- Views
  const tmp = new THREE.Vector3();
  // Card designs (data-card on the slide) that frame the beacon somewhere other
  // than above a bottom band; the leader line runs from the beacon to the card.
  const FRAME = { dock: { x: -0.79, y: 0.0 }, codex: { x: 0.79, y: 0.0 }, omni: { x: 0.0, y: 0.42 } };
  const kindOf = (st) => (st && st.side) || slide.dataset.card;
  const VIEW_OVER = { pos: new THREE.Vector3(3, 24, 25), target: new THREE.Vector3(-7, -2, 0), fov: 46 };
  const VIEW_END = { pos: new THREE.Vector3(0, 34, 16), target: new THREE.Vector3(-5, 0, 0), fov: 44 };
  function viewFor(b) {
    if (b <= 0) return VIEW_OVER;
    if (b > N) return VIEW_END;
    const st = stations[b - 1], out = tmp.set(st.pos.x, 0, st.pos.z).normalize().clone();
    const side = new THREE.Vector3(-out.z, 0, out.x);
    // From the center side, high, looking outward over the beacon: the hole in the
    // middle of the disk is empty, so nothing stands between, and the rest of the
    // ring and the sky are the background.
    // Looking outward, `side` is the camera's right; stand a little left of the
    // beacon and aim left of it, so it sits right of center, clear of the card.
    // The card is a band along the bottom, so the beacon centers above it: aim below it.
    const pos = st.pos.clone().addScaledVector(out, -4.4).addScaledVector(side, -0.6).add(new THREE.Vector3(0, st.H + 2.6, 0));
    const F = FRAME[kindOf(st)];
    if (F) {
      // Aim so the beacon's middle lands at F (x, y in -1..1), clear of the card.
      const P = st.pos.clone().add(new THREE.Vector3(0, st.H * 0.6, 0));
      const fwd = P.clone().sub(pos), L = fwd.length(); fwd.normalize();
      const right = new THREE.Vector3().crossVectors(fwd, new THREE.Vector3(0, 1, 0)).normalize(), up = new THREE.Vector3().crossVectors(right, fwd);
      const hh = L * Math.tan(THREE.MathUtils.degToRad(42) / 2), hw = hh * (16 / 9);
      return { pos, target: P.addScaledVector(right, -F.x * hw).addScaledVector(up, -F.y * hh), fov: 42 };
    }
    const target = st.pos.clone().add(new THREE.Vector3(0, st.H * 0.5 - 1.7, 0)).addScaledVector(side, -0.4).addScaledVector(out, 0.8);
    return { pos, target, fov: 42 };
  }
  const cam = { pos: VIEW_OVER.pos.clone(), target: VIEW_OVER.target.clone(), fov: 45 };
  function applyCam(orbit = 0) {
    const p = cam.pos.clone();
    if (orbit) { const rel = p.clone().sub(cam.target); rel.applyAxisAngle(new THREE.Vector3(0, 1, 0), orbit); p.copy(cam.target).add(rel); }
    camera.position.copy(p); camera.fov = cam.fov; camera.updateProjectionMatrix(); camera.lookAt(cam.target);
  }

  // ---------- State and animation
  const S = { beat: 0, awake: false, anim: null, t0: 0, raf: 0, frames: 0, reveal: 1, pop: 1, drag: 0, dragV: 0, idle: 0 };
  function setFocus(b) {
    const cur = b >= 1 && b <= N ? b - 1 : -1;
    diskMat.uniforms.uFocus.value = cur >= 0 ? stations[cur].deg : -1;
    stations.forEach((st, k) => {
      const on = cur < 0 || k === cur;
      // Overview and finale show beacons and majors; a station's name shows when you visit it.
      st.label.material.opacity = k === cur && !FRAME[kindOf(st)] ? 1 : 0;
      st.beam.material.opacity = on ? 0.9 : 0.07;
      st.halo.material.opacity = on ? 0.9 : 0.08;
      st.node.material.opacity = on ? 1 : 0.14;
      st.node.scale.setScalar(k === cur ? 1.6 : 1);
    });
    stations.forEach((st, k) => st.li.classList.toggle('is-on', k === cur));
    slide.classList.toggle('is-overview', cur < 0);
    slide.classList.toggle('is-finale', b > N);
  }
  function applyPop(p) {
    stations.forEach((st, k) => {
      const t = clamp(p * (N + 4) - k * 0.9, 0, 1), s = t <= 0 ? 0.0001 : outBack(t);
      st.g.scale.set(s, s, s);
    });
    majorSprites.concat(ends).forEach((s) => { s.material.opacity = ramp(p, 0.05, 0.5); });
  }
  function outBack(t) { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2); }

  function sideTo(b) { const st = stations[b - 1]; if (MIX && st) slide.dataset.card = st.side; }
  function snapTo(b) {
    S.anim = null; S.beat = b; slide.classList.remove('is-flying'); sideTo(b);
    const v = viewFor(b); cam.pos.copy(v.pos); cam.target.copy(v.target); cam.fov = v.fov;
    S.reveal = 1; S.pop = 1; diskMat.uniforms.uReveal.value = 1; applyPop(1);
    if (sheet) sheet.visible = false; warp.material.opacity = 0; bloom.strength = 0.85;
    slide.classList.add('is-arrived'); setFocus(b);
  }
  function fly(b) {
    const from = { pos: cam.pos.clone(), target: cam.target.clone(), fov: cam.fov }, to = viewFor(b);
    const long = (S.beat === 0 || b === 0 || b > N || S.beat > N);
    const d = from.pos.distanceTo(to.pos), D = clamp(0.9 + d * 0.045, 1.1, long ? 2.2 : 1.7);
    S.beat = b; setFocus(b);
    S.anim = { kind: 'fly', from, to, D, t0: performance.now(), lift: clamp(d * 0.18, 0.6, 4.5) };
    slide.classList.add('is-flying');
  }
  function portal(from) {
    makeSheet(from);
    S.beat = 0; setFocus(0); slide.classList.remove('is-arrived');
    S.reveal = 0; S.pop = 0; diskMat.uniforms.uReveal.value = 0; applyPop(0);
    cam.pos.copy(CAM0); cam.target.set(0, SHEET_Y, SHEET_Z); cam.fov = 45; sheet.visible = true;
    // Compile the shard shader now, and start the clock on the first drawn frame,
    // so a compile stall never eats the crack.
    applyCam(); try { renderer.compile(scene, camera); } catch (e) {}
    S.anim = { kind: 'portal', D: 4.2, t0: null };
  }
  const flight = new THREE.CatmullRomCurve3([CAM0.clone(), new THREE.Vector3(0, SHEET_Y + 1, SHEET_Z - 18), new THREE.Vector3(0, 24, 58), new THREE.Vector3(0, 19, 32), VIEW_OVER.pos.clone()]);
  const aimFrom = new THREE.Vector3(0, SHEET_Y, SHEET_Z - 40);
  function step(now) {
    const A = S.anim;
    if (A && A.kind === 'fly') {
      const t = clamp((now - A.t0) / (A.D * 1000), 0, 1), e = inOut(t);
      cam.pos.lerpVectors(A.from.pos, A.to.pos, e); cam.pos.y += Math.sin(Math.PI * e) * A.lift;
      cam.target.lerpVectors(A.from.target, A.to.target, inOut(clamp(t * 1.15, 0, 1)));
      cam.fov = A.from.fov + (A.to.fov - A.from.fov) * e;
      // The old card has folded by now; a mixed deck takes the new station's side.
      if (now - A.t0 > 520 || t > 0.7) sideTo(S.beat);
      // The card starts to open as the camera settles, not after it stops.
      if (t > 0.78) slide.classList.remove('is-flying');
      if (t >= 1) S.anim = null;
    } else if (A && A.kind === 'portal') {
      if (A.t0 === null) A.t0 = now;
      const s = (now - A.t0) / 1000, u = sheet.material.uniforms;
      u.uCrack.value = ramp(s, 0.05, 0.5);
      u.uT.value = clamp((s - 0.5) / 1.5, 0, 1);
      bloom.strength = 0.85 + 1.6 * Math.exp(-Math.pow((s - 0.62) / 0.18, 2));
      const shake = s < 0.55 ? 0.03 * ramp(s, 0.1, 0.5) : 0;
      const f = inOut(clamp((s - 0.45) / 3.1, 0, 1));
      cam.pos.copy(flight.getPointAt(f)); cam.pos.x += (Math.random() - 0.5) * shake; cam.pos.y += (Math.random() - 0.5) * shake;
      cam.target.lerpVectors(new THREE.Vector3(0, SHEET_Y, SHEET_Z), aimFrom, ramp(s, 0.4, 1.4)).lerp(VIEW_OVER.target, ramp(s, 1.4, 3.4));
      cam.fov = 45 + 26 * Math.sin(Math.PI * clamp((s - 0.45) / 2.2, 0, 1)) - 0 * s;
      warp.material.opacity = 0.9 * Math.sin(Math.PI * clamp((s - 0.55) / 1.9, 0, 1));
      S.reveal = ramp(s, 2.0, 3.6); diskMat.uniforms.uReveal.value = S.reveal;
      S.pop = clamp((s - 2.6) / 1.6, 0, 1); applyPop(S.pop);
      if (s > 2.2) sheet.visible = false;
      if (s > 3.2) slide.classList.add('is-arrived');
      if (s >= A.D) { S.anim = null; bloom.strength = 0.85; warp.material.opacity = 0; }
    }
    // Idle life: slow drift of the sky, beacons breathing, gentle orbit on the overview.
    diskMat.uniforms.uTime.value = now / 1000;
    stars.rotation.y = now / 1000 * 0.004;
    stations.forEach((st, k) => { st.halo.scale.setScalar(1 + 0.18 * Math.sin(now / 520 + k)); });
    if (!S.anim && (S.beat === 0 || S.beat > N)) S.idle += 0.00018 * 16; else S.idle *= 0.94;
    S.drag += S.dragV; S.dragV *= 0.9; if (!dragging) S.drag *= 0.93;
    applyCam(S.idle * (S.beat > N ? 1 : 0.35) + S.drag);
  }
  // The leader: an SVG over the scene, from the beacon to the card.
  const SVGNS = 'http://www.w3.org/2000/svg';
  const leader = document.createElementNS(SVGNS, 'svg'); leader.setAttribute('class', 'disk__leader'); leader.setAttribute('viewBox', '0 0 1920 1080'); leader.setAttribute('aria-hidden', 'true');
  const lPath = document.createElementNS(SVGNS, 'path'); lPath.setAttribute('pathLength', '1'); lPath.setAttribute('class', 'leader__line');
  const lRing = document.createElementNS(SVGNS, 'circle'); lRing.setAttribute('r', '34'); lRing.setAttribute('class', 'leader__ring');
  const lDot = document.createElementNS(SVGNS, 'circle'); lDot.setAttribute('r', '7'); lDot.setAttribute('class', 'leader__dot');
  const lEnd = document.createElementNS(SVGNS, 'rect'); lEnd.setAttribute('width', '12'); lEnd.setAttribute('height', '12'); lEnd.setAttribute('class', 'leader__end');
  leader.append(lPath, lRing, lDot, lEnd); host.after(leader);
  function drawLeader(bx, by) {
    const li = slide.querySelector('.stations > li.is-on'), kind = slide.dataset.card;
    if (!li || !FRAME[kind]) { lPath.setAttribute('d', ''); return; }
    const sr = slide.getBoundingClientRect(), k = 1920 / sr.width, r = li.getBoundingClientRect();
    const L = (r.left - sr.left) * k, R = (r.right - sr.left) * k, T = (r.top - sr.top) * k;
    let ax, ay, d;
    if (kind === 'omni') {
      ax = clamp(bx, L + 60, R - 60); ay = T;
      d = `M${bx} ${by + 40} L${bx} ${by + 70} L${ax} ${ay - 40} L${ax} ${ay}`;
    } else {
      const toRight = kind === 'dock';
      ax = toRight ? L : R; ay = T + 64;
      const elbow = toRight ? ax - 90 : ax + 90, dx = toRight ? 1 : -1;
      const sx = bx + dx * 40, run = Math.abs(elbow - sx), dy = clamp(ay - by, -run, run);
      d = `M${sx} ${by} L${sx + dx * Math.abs(dy)} ${by + dy} L${elbow} ${ay} L${ax} ${ay}`;
    }
    lPath.setAttribute('d', d);
    lEnd.setAttribute('x', (ax - 6).toFixed(1)); lEnd.setAttribute('y', (ay - 6).toFixed(1));
  }
  // Where the visited beacon sits on screen, in stage pixels (1920 x 1080):
  // --bx, --by for its head, --gx, --gy for its foot. Cards anchor to these.
  const proj = new THREE.Vector3(); let lastB = '';
  function track() {
    const st = S.beat >= 1 && S.beat <= N ? stations[S.beat - 1] : null;
    if (!st) return;
    camera.updateMatrixWorld();
    proj.set(st.pos.x, st.pos.y + st.H, st.pos.z).project(camera);
    const bx = (proj.x + 1) * 960, by = (1 - proj.y) * 540;
    proj.set(st.pos.x, st.pos.y, st.pos.z).project(camera);
    const gx = (proj.x + 1) * 960, gy = (1 - proj.y) * 540;
    const li = slide.querySelector('.stations > li.is-on');
    const key = [bx, by, gx, gy].map((v) => v.toFixed(1)).join() + (li ? li.offsetHeight : 0);
    if (key === lastB) return; lastB = key;
    slide.style.setProperty('--bx', bx.toFixed(1)); slide.style.setProperty('--by', by.toFixed(1));
    slide.style.setProperty('--gx', gx.toFixed(1)); slide.style.setProperty('--gy', gy.toFixed(1));
    [lRing, lDot].forEach((c) => { c.setAttribute('cx', bx.toFixed(1)); c.setAttribute('cy', by.toFixed(1)); });
    drawLeader(Math.round(bx), Math.round(by));
  }
  let lastDraw = 0;
  function loop(now) {
    if (!S.awake) return;
    if (MIRROR && now - lastDraw < 250) { S.raf = requestAnimationFrame(loop); return; }
    lastDraw = now;
    step(now); track(); composer.render(); S.frames++;
    S.raf = requestAnimationFrame(loop);
  }
  function wake() { if (S.awake) return; S.awake = true; resize(); S.raf = requestAnimationFrame(loop); }
  function sleep() { S.awake = false; cancelAnimationFrame(S.raf); }
  function resize() {
    const r = slide.getBoundingClientRect(); if (!r.width) return;
    renderer.setSize(r.width, r.height, false); composer.setSize(r.width, r.height);
    bloom.resolution.set(r.width / 2, r.height / 2);
    camera.aspect = r.width / r.height; camera.updateProjectionMatrix();
  }

  // ---------- Pointer: drag to look around, click a beacon to fly to it
  let dragging = false, down = null;
  host.addEventListener('pointerdown', (e) => { down = { x: e.clientX, y: e.clientY, t: performance.now() }; dragging = true; host.setPointerCapture(e.pointerId); });
  host.addEventListener('pointermove', (e) => { if (!dragging || !down) return; const dx = e.movementX || 0; S.dragV = clamp(S.dragV - dx * 0.0009, -0.05, 0.05); });
  host.addEventListener('pointerup', (e) => {
    dragging = false;
    if (!down) return;
    const moved = Math.hypot(e.clientX - down.x, e.clientY - down.y); down = null;
    if (moved > 6) return;
    const r = renderer.domElement.getBoundingClientRect();
    const ray = new THREE.Raycaster(); ray.setFromCamera(new THREE.Vector2(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1), camera);
    const hit = ray.intersectObjects(pick, false)[0];
    if (hit) api.beat(hit.object.userData.beat);
  });

  // ---------- Spectrum legend (a canvas, drawn once, no CSS gradient)
  const legend = slide.querySelector('.disk__legend canvas');
  if (legend) {
    const g = legend.getContext('2d'), w = legend.width, h = legend.height;
    for (let x = 0; x < w; x++) { g.fillStyle = '#' + spectrum(x / (w - 1)).getHexString(); g.fillRect(x, 0, 1, h); }
  }

  window.__disk = { stats: () => ({ frames: S.frames, beat: S.beat, awake: S.awake, busy: !!S.anim, N, reveal: S.reveal, anim: S.anim && S.anim.kind,
    camToView: cam.pos.distanceTo(viewFor(S.beat).pos), camera: camera.position.toArray().map((v) => Math.round(v * 10) / 10), idle: S.idle, stations: stations.map((s) => ({ name: s.name, deg: Math.round(s.deg), r: s.r })) }) };

  return {
    beats: N + 1,
    set(b) { wake(); snapTo(b); },
    go(b) { wake(); if (api.reduce.matches || MIRROR) snapTo(b); else fly(b); },
    enter(b, dir, animate, from) {
      wake();
      if (animate && dir > 0 && b === 0) portal(from);
      else if (animate) { snapTo(b); } else snapTo(b);
    },
    leave() {},
    busy() { return !!S.anim; },
    finish() { const b = S.beat; snapTo(b); },
    sleep() { sleep(); },
    resize() { if (S.awake) resize(); },
  };
}

window.DeckKinds = window.DeckKinds || {};
window.DeckKinds.disk = build;
