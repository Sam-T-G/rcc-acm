/* ===========================================================================
   ACM @ RCC. Deck kit engine.
   Ported 2026-09-24 from the GDG chapter's deck kit (rcc-gdg/deck-kit/deck.js).
   What changed in the port: the cover's device is the Rail, drawn down its
   edge and retracted when the deck leaves the cover; the bottom progress line
   is section names in the ledger line (components.md §7.8), not a bar; the
   GDG-only archetypes (card, compress, the semester rung) are gone.

   No build step. GSAP is optional: when it loads (cdnjs, pinned, SRI) the full
   motion score runs; when it does not, content still rises through its masks
   by CSS and everything else lands in its end state. Reduced motion, room mode,
   and a running timer make every transition a cut.

   The one architectural rule: every transition ends by calling applyState(i, b),
   which sets the whole deck to "slide i, beat b" from nothing. Animation is
   decoration laid over a state machine, so a clicker pressed six times in a
   second lands on the right slide in the right state, every time.
   =========================================================================== */
(function () {
  'use strict';

  var root = document.documentElement;
  var deck = document.querySelector('.deck');
  if (!deck) return;
  var slides = Array.prototype.filter.call(deck.children, function (el) { return el.classList.contains('slide'); });
  if (!slides.length) return;

  var KEY = 'acm-deck:' + (deck.getAttribute('data-deck') || location.pathname) + ':';
  var gsap = window.gsap || null;
  var reduceMQ = matchMedia('(prefers-reduced-motion: reduce)');
  var NS = 'http://www.w3.org/2000/svg';
  var STAGGER = 0.056;              // 8% of the beat
  var STAGGER_CAP = 5;              // six groups: 0..5

  root.classList.add('deck-live');
  root.setAttribute('data-theme', 'light');
  if (!gsap) root.classList.add('no-gsap');

  /* ---------- Utilities --------------------------------------------------- */
  function store(k, v) { try { localStorage.setItem(KEY + k, v); } catch (e) { /* private window */ } }
  function recall(k) { try { return localStorage.getItem(KEY + k); } catch (e) { return null; } }
  function clamp(x, a, b) { return Math.max(a, Math.min(b, x)); }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function ramp(x, a, b) { var t = clamp((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function one(sel, el) { return (el || document).querySelector(sel); }
  function all(sel, el) { return Array.prototype.slice.call((el || document).querySelectorAll(sel)); }
  function make(tag, cls, parent) { var el = document.createElement(tag); if (cls) el.className = cls; if (parent) parent.appendChild(el); return el; }
  function svgEl(tag, attrs, parent) {
    var el = document.createElementNS(NS, tag);
    for (var k in attrs) el.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(el);
    return el;
  }
  function r2(n) { return Math.round(n * 100) / 100; }

  /* ---------- Tokens: one source for CSS and GSAP ------------------------- */
  function token(name) { return getComputedStyle(root).getPropertyValue(name).trim(); }
  function seconds(name) {
    var v = token(name); if (!v) return 0;
    var n = parseFloat(v); return /ms$/.test(v) ? n / 1000 : n;
  }
  // Solve a cubic-bezier for y at x by bisection. x(t) is monotonic for any
  // curve whose x control points sit in [0, 1], which every token here does.
  function cubicBezier(x1, y1, x2, y2) {
    function at(t, a, b) { return ((1 - 3 * b + 3 * a) * t + (3 * b - 6 * a)) * t * t + 3 * a * t; }
    return function (x) {
      if (x <= 0) return 0; if (x >= 1) return 1;
      var lo = 0, hi = 1, t = x;
      for (var i = 0; i < 28; i++) {
        var cx = at(t, x1, x2);
        if (Math.abs(cx - x) < 1e-6) break;
        if (cx < x) lo = t; else hi = t;
        t = (lo + hi) / 2;
      }
      return at(t, y1, y2);
    };
  }
  function curve(name, fallback) {
    var m = /cubic-bezier\(([^)]+)\)/.exec(token(name));
    var p = m ? m[1].split(',').map(parseFloat) : fallback;
    return cubicBezier(p[0], p[1], p[2], p[3]);
  }
  var EASE = {
    arrive: curve('--acm-ease-arrive', [0.16, 1, 0.3, 1]),
    exit: curve('--acm-ease-exit', [0.4, 0, 1, 1]),
    standard: curve('--acm-ease-standard', [0.32, 0.72, 0, 1])
  };
  function motionOn() { return !!gsap && !reduceMQ.matches; }
  function dur(kind) { return seconds(kind === 'move' ? '--acm-dur-move' : '--acm-dur-beat'); }

  /* ---------- Units: what rises through a mask ---------------------------- */
  var TEXT = 'h1, h2, h3, p, li, .eyebrow, .label';
  var BLOCK = '.clock, .figure, .code, .callout, .qr';
  var NOSPLIT = '.notes, .qr, .cover__starts, .clock, .figure, .code, .callout, [data-static], svg, script, style';

  function splitWords(el) {
    var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null), nodes = [], words = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (node) {
      if (!node.nodeValue.trim()) return;
      var host = node.parentNode;
      if (host !== el && host.closest && host.closest(NOSPLIT)) return;
      var frag = document.createDocumentFragment();
      node.nodeValue.split(/(\s+)/).forEach(function (part) {
        if (!part) return;
        if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
        var w = make('span', 'w'), inner = make('span', 'w__in', w);
        inner.textContent = part;
        frag.appendChild(w); words.push(inner);
      });
      host.replaceChild(frag, node);
    });
    return words;
  }
  function wrapBlock(el) {
    var mask = make('div', 'blk'), inner = make('div', 'blk__in', mask);
    el.parentNode.insertBefore(mask, el); inner.appendChild(el);
    return inner;
  }
  function ensureBody(li) {
    if (one(':scope > .body', li)) return;
    var body = make('span', 'body');
    while (li.firstChild) body.appendChild(li.firstChild);
    li.appendChild(body);
  }

  // Collect a slide's units in document order: {el, beat, target}. Groups
  // (stagger indexes) are assigned by measure(), because they depend on lines.
  function buildUnits(slide) {
    var beats = all('[data-beat]', slide), units = [];
    var targets = all(TEXT + ', ' + BLOCK, slide).filter(function (el) {
      if (el.matches(BLOCK)) return !el.parentNode.closest(BLOCK);
      if (el.closest(NOSPLIT)) return false;
      var up = el.parentNode.closest(TEXT + ', ' + BLOCK);
      return !up || !slide.contains(up);
    });
    targets.forEach(function (t) {
      var host = t.closest('[data-beat]'), beat = host && slide.contains(host) ? beats.indexOf(host) + 1 : 0;
      var els = t.matches(BLOCK) ? [wrapBlock(t)] : splitWords(t);
      els.forEach(function (el) { units.push({ el: el, beat: beat, target: t }); });
    });
    return units;
  }
  // Words in the same line of the same element share a group, so a line rises
  // as one. Groups count up in reading order and stop at six.
  function measure(slide) {
    var groups = {}, last = {};
    slide._units.forEach(function (u) {
      var top = Math.round(u.el.parentNode.getBoundingClientRect().top), b = u.beat;
      if (groups[b] === undefined) { groups[b] = -1; last[b] = null; }
      var sig = last[b];
      if (!sig || sig.target !== u.target || Math.abs(sig.top - top) > 2) { groups[b]++; last[b] = { target: u.target, top: top }; }
      u.k = Math.min(groups[b], STAGGER_CAP);
      u.el.style.setProperty('--i', u.k);
    });
  }
  function unitsFor(slide, beatFrom, beatTo) {
    return slide._units.filter(function (u) { return u.beat >= beatFrom && u.beat <= beatTo; });
  }

  /* ---------- Figure: a count arriving ------------------------------------ */
  function makeFigure(slide) {
    var el = one('.figure__num', slide);
    if (!el) return null;
    var to = parseFloat(el.getAttribute('data-to') || el.textContent);
    var from = parseFloat(el.getAttribute('data-from') || '0');
    // Reserve the measured width of the end value, so a growing count never
    // pushes the unit and the end state sits flush.
    el.style.display = 'inline-block'; el.style.textAlign = 'right';
    function render(p) { el.textContent = Math.round(lerp(from, to, clamp(p, 0, 1))); }
    function reserve() {
      el.style.minWidth = ''; render(1);
      var u = deck.clientWidth / 1920 || 1;
      el.style.minWidth = 'calc(' + r2(el.getBoundingClientRect().width / u) + ' * var(--u))';
    }
    return { render: render, reserve: reserve, state: { p: 1 } };
  }

  /* ---------- Clock -------------------------------------------------------- */
  function fmt(ms) { var s = Math.ceil(ms / 1000), m = Math.floor(s / 60); s %= 60; return m + ':' + (s < 10 ? '0' : '') + s; }
  function makeClock(slide) {
    var secs = parseInt(slide.getAttribute('data-timer'), 10);
    if (!secs) return null;
    var el = one('.clock', slide);
    if (!el) {
      el = make('div', 'clock');
      make('p', 'clock__digits', el); make('span', 'clock__fill', make('span', 'clock__track', el)); make('p', 'clock__hint', el);
      (one('[data-clock-slot]', slide) || slide).appendChild(el);
    }
    var digits = one('.clock__digits', el), fill = one('.clock__fill', el), hint = one('.clock__hint', el);
    var hint0 = hint.textContent.trim() || 'T to start';
    hint.textContent = hint0;
    var c = { total: secs * 1000, left: secs * 1000, running: false, last: 0, raf: 0 };
    function paint() {
      var state = c.left <= 0 ? 'done' : c.running ? (c.left <= 10000 ? 'ending' : 'running') : (c.left === c.total ? 'idle' : 'paused');
      digits.textContent = state === 'done' ? 'Time' : fmt(c.left);
      fill.style.transform = 'scaleX(' + (c.left / c.total) + ')';
      el.setAttribute('data-state', state);
      hint.textContent = state === 'done' ? 'R to reset' : state === 'paused' ? 'Paused. T to resume' : state === 'idle' ? hint0 : 'T to pause';
    }
    function tick() {
      var now = performance.now();
      c.left = Math.max(0, c.left - (now - c.last)); c.last = now; paint();
      if (c.left > 0 && c.running) c.raf = requestAnimationFrame(tick); else c.running = false;
    }
    c.toggle = function () {
      if (c.left <= 0) return;
      c.running = !c.running;
      if (c.running) { c.last = performance.now(); c.raf = requestAnimationFrame(tick); } else cancelAnimationFrame(c.raf);
      paint();
    };
    c.reset = function () { c.running = false; cancelAnimationFrame(c.raf); c.left = c.total; paint(); };
    c.pause = function () { if (c.running) { c.running = false; cancelAnimationFrame(c.raf); paint(); } };
    paint();
    return c;
  }

  /* ---------- Chrome: ledger, counter, progress ---------------------------- */
  var chrome = make('div', 'chrome', deck); chrome.setAttribute('aria-hidden', 'true');
  var ledger = make('p', 'ledger', chrome), counter = make('p', 'counter', chrome);
  var prog = svgEl('svg', { class: 'progress', viewBox: '0 0 1920 1080', focusable: 'false' }, chrome);
  var progSegs = svgEl('g', { class: 'progress__segs' }, prog);
  var live = make('p', 'visually-hidden', document.body); live.setAttribute('aria-live', 'polite');

  // One value, R.t, runs the cover's device: 0 is the cover with its Rail full
  // height, 1 is any other slide with the Rail gone and the progress line up.
  // R.draw draws the Rail down on the opening; R.fill is how far the progress
  // line has filled, in slides.
  var BAR = { left: 96, right: 1824, y: 1026, h: 3, label: 1006, gap: 24 };
  var P = { segs: [] };
  var R = { t: 1, fill: 0, draw: 1 };
  var coverRail = null;

  function layoutProgress() {
    var V = visible(), n = V.length, runs = [];
    V.forEach(function (i, j) {
      var m = slides[i]._section, last = runs[runs.length - 1];
      if (last && last.section === m) last.n++; else runs.push({ section: m, n: 1, start: j });
    });
    var unit = (BAR.right - BAR.left - BAR.gap * (runs.length - 1)) / n, x = BAR.left;
    progSegs.textContent = '';
    P.segs = runs.map(function (r) {
      var w = r.n * unit, g = svgEl('g', {}, progSegs);
      // The cover has no section; its slot stays blank rather than a stray line.
      if (!r.section) g.style.visibility = 'hidden';
      svgEl('rect', { x: r2(x), y: BAR.y, width: r2(w), height: BAR.h, class: 'progress__track' }, g);
      var fill = svgEl('rect', { x: r2(x), y: BAR.y, width: 0, height: BAR.h, class: 'progress__fill' }, g);
      var label = svgEl('text', { x: r2(x), y: BAR.label, class: 'progress__label' }, g);
      label.textContent = r.section;
      var s = { x: x, w: w, n: r.n, start: r.start, fill: fill, label: label, fits: true };
      x += w + BAR.gap;
      return s;
    });
    P.segs.forEach(function (s) { try { s.fits = s.label.getComputedTextLength() <= s.w - 8; } catch (e) { s.fits = true; } });
  }
  function progressTarget(i) {
    if (slides[i]._kind === 'cover') return { t: 0, fill: 0 };
    var V = visible(), j = V.indexOf(i);
    return { t: 1, fill: j < 0 ? R.fill : j + 1 };
  }
  function renderProgress() {
    // The Rail draws down from the top on the opening, and on leaving the cover
    // it retracts to its foot, over the first 60% of the move.
    if (coverRail) {
      var leave = clamp(R.t / 0.6, 0, 1), s = clamp(R.draw, 0, 1) * (1 - EASE.standard(leave));
      coverRail.style.transformOrigin = R.t > 0 ? '50% 100%' : '50% 0';
      coverRail.style.transform = s >= 0.9999 ? '' : 'scaleY(' + r2(s * 10000) / 10000 + ')';
    }
    progSegs.style.opacity = ramp(R.t, 0.45, 1);
    var at = -1;
    P.segs.forEach(function (s, k) {
      var part = clamp((R.fill - s.start) / s.n, 0, 1);
      s.fill.setAttribute('width', r2(s.w * part));
      if (R.fill > s.start && R.fill <= s.start + s.n + 1e-6) at = k;
    });
    P.segs.forEach(function (s, k) {
      s.label.classList.toggle('is-past', at >= 0 && k < at);
      s.label.classList.toggle('is-current', k === at);
      // A label too wide for its segment shows only while it is the current one.
      s.label.classList.toggle('is-hidden', !s.fits && k !== at);
    });
    // A current label that overflows its segment hides the labels it would run into.
    var cur = P.segs[at];
    if (cur && !cur.fits) {
      var end = cur.x; try { end += cur.label.getComputedTextLength() + 16; } catch (e) {}
      P.segs.forEach(function (s, k) { if (k > at && s.x < end) s.label.classList.add('is-hidden'); });
    }
  }

  /* ---------- Build every slide ------------------------------------------- */
  // The countdown line goes in before anything is measured, so the cover lays
  // out once with it in place. Hidden until the start is under 30 minutes away.
  slides.forEach(function (s) {
    if (s.getAttribute('data-kind') !== 'cover' || !s.hasAttribute('data-starts') || one('.cover__starts', s)) return;
    var el = make('p', 'eyebrow cover__starts'); el.style.visibility = 'hidden'; el.textContent = 'Starts in 0:00';
    var eb = one('.eyebrow', s); s.insertBefore(el, eb || s.firstChild);
  });
  var section = '';
  slides.forEach(function (slide, i) {
    slide._i = i;
    slide._kind = slide.getAttribute('data-kind') || 'statement';
    // A slide without data-section belongs to the section before it.
    if (slide.hasAttribute('data-section')) section = slide.getAttribute('data-section');
    slide._section = slide._kind === 'cover' ? '' : section;
    all('.beats li, .board li', slide).forEach(function (li) { if (li.closest('.beats')) ensureBody(li); });
    slide._clock = makeClock(slide);
    slide._figure = makeFigure(slide);
    slide._units = buildUnits(slide);
    slide._beatEls = all('[data-beat]', slide);
    slide._videos = all('video', slide);
    // A "press" video is one more beat: the press after the last reveal plays it.
    slide._press = slide._videos.filter(function (v) { return v.getAttribute('data-play') === 'press'; });
    slide._beats = slide._beatEls.length + (slide._press.length ? 1 : 0);
  });
  coverRail = one('.slide[data-kind="cover"] .cover__rail', deck);

  /* ---------- State -------------------------------------------------------- */
  var S = { i: 0, b: 0, room: recall('room') === '1', tl: null, last: 'none', presenting: false };
  function visible() {
    if (!S.room) return slides.map(function (s, i) { return i; });
    var v = slides.map(function (s, i) { return s.hasAttribute('data-room') ? i : -1; }).filter(function (i) { return i >= 0; });
    return v.length ? v : slides.map(function (s, i) { return i; });
  }

  function setBeats(slide, b) {
    slide._beatEls.forEach(function (el, k) {
      el.classList.toggle('is-pending', k >= b);
      el.classList.toggle('is-past', k < b - 1 && el.matches('.beats li, .board li'));
    });
  }
  function resetUnits(list) { if (gsap) gsap.set(list.map(function (u) { return u.el; }), { yPercent: 0 }); }

  // The whole deck, set to "slide i, beat b", from nothing. Idempotent.
  function applyState(i, b) {
    var slide = slides[i];
    S.i = i; S.b = b;
    slides.forEach(function (s, k) {
      var on = k === i;
      s.classList.toggle('is-current', on);
      if (!on && s._clock) s._clock.pause();
    });
    setBeats(slide, b);
    resetUnits(unitsFor(slide, 0, b));
    if (slide._figure) { slide._figure.state.p = 1; slide._figure.render(1); }
    var pt = progressTarget(i); R.t = pt.t; R.fill = pt.fill; R.draw = 1; renderProgress();
    chromeText();
    if (slide !== S.lastSlide) { slides.forEach(function (s) { s._videos.forEach(function (v) { v._held = false; }); }); S.lastSlide = slide; }
    syncVideos(slide, b);
  }
  function chromeText() {
    var slide = slides[S.i], V = visible(), pos = V.indexOf(S.i);
    deck.classList.toggle('on-cover', slide._kind === 'cover');
    // The chrome takes its ink from the ground, and steps aside from a bleeding photo.
    deck.setAttribute('data-ground', slide.getAttribute('data-ground') || 'paper');
    var bleed = slide._kind === 'photo' ? (slide.getAttribute('data-layout') || 'bleed-right') : '';
    deck.classList.toggle('on-bleed-right', bleed === 'bleed-right');
    deck.classList.toggle('on-bleed-left', bleed === 'bleed-left');
    ledger.textContent = slide.getAttribute('data-ledger') || deck.getAttribute('data-ledger') || '';
    var text = pad(pos + 1) + ' / ' + pad(V.length);
    if (S.room) text += ' · Room';
    else if (pos === 0) text += ' · ? for keys';
    counter.textContent = text;
    if (history.replaceState) { try { history.replaceState(null, '', '#' + (S.i + 1)); } catch (e) { /* sandboxed frame */ } }
    renderNotes();
  }
  function announce(slide, b) {
    var V = visible(), pos = V.indexOf(slide._i), label = slide.getAttribute('aria-label');
    if (!label) { var h = one('h1, h2', slide); label = h ? h.textContent.replace(/\s+/g, ' ').trim() : ''; }
    if (b > 0 && slide._beatEls[b - 1]) live.textContent = slide._beatEls[b - 1].textContent.replace(/\s+/g, ' ').trim();
    else live.textContent = 'Slide ' + (pos + 1) + ' of ' + V.length + (label ? ': ' + label : '');
  }

  /* ---------- Video ------------------------------------------------------------ */
  // Only the current slide's videos ever run. "auto" plays on arrival (never
  // under reduced motion or in the stack); "press" plays once its beat is
  // reached. Leaving pauses everything and rewinds press videos.
  function playOK(v) { var p = v.play(); if (p && p.catch) p.catch(function () { /* blocked; the poster stays */ }); }
  function syncVideos(slide, b) {
    slides.forEach(function (s) {
      s._videos.forEach(function (v) {
        if (s !== slide || !S.presenting) {
          if (!v.paused) v.pause();
          if (v.getAttribute('data-play') === 'press' && v.currentTime) { try { v.currentTime = 0; } catch (e) {} }
          return;
        }
        var want = v.getAttribute('data-play') === 'press' ? b > s._beatEls.length : !reduceMQ.matches;
        if (v._held) want = false;
        if (want && v.paused) playOK(v); else if (!want && !v.paused) v.pause();
      });
    });
  }
  function toggleVideos() {
    var vs = slides[S.i]._videos;
    if (!vs.length) { say('No video on this slide'); return; }
    var anyPlaying = vs.some(function (v) { return !v.paused; });
    vs.forEach(function (v) { v._held = anyPlaying; if (anyPlaying) v.pause(); else playOK(v); });
  }

  /* ---------- Transitions -------------------------------------------------- */
  // cut: no motion. hold: a beat on the same slide. unfold: to or from the
  // cover. ascend: within a section. turn: into a new section, at the slower tier.
  function timerRunning() { var c = slides[S.i]._clock; return !!(c && c.running); }
  function kindOf(i, ni) {
    if (!S.presenting || reduceMQ.matches || S.room || timerRunning()) return 'cut';
    if (ni === i) return 'hold';
    var a = slides[i], z = slides[ni];
    if (a._kind === 'cover' || z._kind === 'cover') return 'unfold';
    return a._section === z._section ? 'ascend' : 'turn';
  }
  function finish() { if (S.tl) { var tl = S.tl; S.tl = null; tl.progress(1); tl.kill(); } }

  function go(ni, nb, dir) {
    finish();
    var i = S.i, b = S.b, kind = kindOf(i, ni);
    S.last = kind + (dir < 0 ? '-back' : '');
    var from = slides[i], to = slides[ni];
    // Start the ground crossfade with the move, not at the swap halfway through.
    if (kind !== 'hold') deck.setAttribute('data-ground', to.getAttribute('data-ground') || 'paper');
    if (kind === 'cut') { applyState(ni, nb); announce(to, ni === i ? nb : 0); return; }
    if (!motionOn()) { applyState(ni, nb); cssEntrance(to, ni === i ? b : -1, nb, dir); announce(to, ni === i ? nb : 0); return; }

    var beat = dur('beat'), move = dur('move'), back = dir < 0 ? 0.6 : 1;
    var tl = gsap.timeline({ onComplete: function () { if (S.tl === tl) S.tl = null; applyState(ni, nb); } });
    S.tl = tl;

    if (kind === 'hold') {
      if (dir > 0) {
        setBeats(from, nb);
        var inU = unitsFor(from, nb, nb).map(function (u) { return u.el; });
        var ks = unitsFor(from, nb, nb).map(function (u) { return u.k; });
        tl.fromTo(inU, { yPercent: 110 }, { yPercent: 0, duration: beat, ease: EASE.arrive, delay: 0, stagger: function (q) { return ks[q] * STAGGER; } });
      } else {
        var outU = unitsFor(from, b, b).map(function (u) { return u.el; });
        tl.to(outU, { yPercent: 110, duration: 0.3 * beat, ease: EASE.exit });
      }
      if (from._press.length) syncVideos(from, nb);
      announce(from, nb);
      return;
    }

    // Ascend, Turn, Unfold. Forward climbs: out goes up, in rises from below.
    // Backward runs the other way, faster.
    var D = (kind === 'ascend' ? beat : move) * back;
    var outEls = unitsFor(from, 0, b).map(function (u) { return u.el; });
    var inList = unitsFor(to, 0, nb), inEls = inList.map(function (u) { return u.el; }), inK = inList.map(function (u) { return u.k; });
    var sign = dir < 0 ? -1 : 1;
    tl.to(outEls, { yPercent: -110 * sign, duration: 0.3 * beat, ease: EASE.exit });
    // Leaving the cover, the Rail retracts while the words exit, so the first
    // content slide arrives onto an empty stage.
    var pt = progressTarget(ni);
    tl.to(R, { t: pt.t, fill: pt.fill, duration: D, ease: EASE.arrive, onUpdate: renderProgress }, 0);
    tl.add(function () {
      gsap.set(inEls, { yPercent: 110 * sign });
      slides.forEach(function (s, k) { s.classList.toggle('is-current', k === ni); });
      setBeats(to, nb);
      S.i = ni; S.b = nb;
      if (to._figure) to._figure.render(dir > 0 ? 0 : 1);
      chromeText();
      syncVideos(to, nb);
      if (from._clock) from._clock.pause();
    }, 0.3 * beat);
    tl.to(inEls, { yPercent: 0, duration: D, ease: EASE.arrive, stagger: function (q) { return inK[q] * STAGGER; } }, 0.3 * beat);
    if (dir > 0 && to._figure) { to._figure.state.p = 0; tl.to(to._figure.state, { p: 1, duration: move, ease: EASE.arrive, onUpdate: function () { to._figure.render(to._figure.state.p); } }, 0.3 * beat + 0.25); }
    announce(to, 0);
  }

  // No GSAP: the same entrances by CSS keyframes, everything else at its end state.
  function cssEntrance(slide, fromBeat, toBeat, dir) {
    if (reduceMQ.matches || !S.presenting) return;
    if (fromBeat >= 0) {                           // a beat on the same slide
      if (dir < 0 || toBeat < 1) return;
      var el = slide._beatEls[toBeat - 1]; if (!el) return;
      el.classList.remove('is-revealing'); void el.offsetWidth; el.classList.add('is-revealing');
      return;
    }
    slide.classList.remove('is-entering'); void slide.offsetWidth; slide.classList.add('is-entering');
    clearTimeout(slide._enterT);
    slide._enterT = setTimeout(function () { slide.classList.remove('is-entering'); }, 2000);
  }

  // Every press first lands the transition in flight, then reads the state.
  function next() {
    finish();
    var slide = slides[S.i];
    if (S.b < slide._beats) { go(S.i, S.b + 1, 1); return; }
    var V = visible(), pos = V.indexOf(S.i);
    if (pos < 0) pos = V.filter(function (k) { return k < S.i; }).length - 1;
    if (pos + 1 < V.length) go(V[pos + 1], 0, 1);
  }
  function prev() {
    finish();
    if (S.b > 0) { go(S.i, S.b - 1, -1); return; }
    var V = visible(), pos = V.indexOf(S.i);
    if (pos < 0) pos = V.filter(function (k) { return k < S.i; }).length;
    if (pos - 1 >= 0) { var p = V[pos - 1]; go(p, slides[p]._beats, -1); }
  }
  function jump(i) { finish(); S.last = 'cut'; applyState(i, 0); announce(slides[i], 0); }

  /* ---------- Cover: the opening, and the optional countdown ------------- */
  function coverEntrance() {
    var cover = slides[S.i];
    if (cover._kind !== 'cover' || !S.presenting) return;
    if (!motionOn()) { cssEntrance(cover, -1, 0, 1); return; }
    var list = unitsFor(cover, 0, 0), els = list.map(function (u) { return u.el; }), ks = list.map(function (u) { return u.k; });
    var tl = gsap.timeline({ onComplete: function () { if (S.tl === tl) S.tl = null; applyState(S.i, S.b); } });
    S.tl = tl;
    R.t = 0; R.fill = 0; R.draw = 0; renderProgress();
    // The Rail draws first, top to bottom, and lands exactly (ease-standard);
    // the words rise once it is most of the way down.
    tl.to(R, { draw: 1, duration: dur('move'), ease: EASE.standard, onUpdate: renderProgress }, 0.1);
    tl.fromTo(els, { yPercent: 110 }, { yPercent: 0, duration: dur('move'), ease: EASE.arrive, stagger: function (q) { return ks[q] * STAGGER; } }, 0.55);
    // Backstop on a timer, not on frames: where no animation frames run (a
    // thumbnail capture, a throttled tab) the cover would otherwise stay blank.
    setTimeout(function () { if (S.tl === tl) finish(); }, tl.duration() * 1000 + 400);
  }
  var countdown = null;
  function startCountdown() {
    var cover = slides.filter(function (s) { return s._kind === 'cover' && s.hasAttribute('data-starts'); })[0];
    var el = cover && one('.cover__starts', cover);
    if (!el) return;
    var hm = cover.getAttribute('data-starts').split(':');
    function paint() {
      var now = new Date(), at = new Date(now); at.setHours(+hm[0], +hm[1], 0, 0);
      var ms = at - now;
      el.style.visibility = ms > 0 && ms < 30 * 60000 ? 'visible' : 'hidden';
      el.textContent = 'Starts in ' + fmt(ms);
    }
    paint(); countdown = setInterval(paint, 1000);
  }

  /* ---------- Notes, help, toast ------------------------------------------ */
  var notes = make('aside', 'deck-notes', document.body); notes.hidden = true; notes.setAttribute('aria-label', 'Speaker notes');
  function renderNotes() {
    if (notes.hidden) return;
    var src = one('.notes', slides[S.i]);
    notes.innerHTML = '<h2>Notes, slide ' + (S.i + 1) + '</h2>' + (src ? src.innerHTML : '<p>No notes on this slide.</p>');
  }
  var help = make('div', 'deck-help', document.body); help.hidden = true; help.setAttribute('role', 'dialog'); help.setAttribute('aria-label', 'Keys');
  help.innerHTML = '<h2>Keys</h2><table><tbody>' + [
    ['→  Space  Page Down', 'Next beat or slide'], ['←  Page Up', 'Back'], ['Home  End', 'First, last'],
    ['T', 'Start or pause the clock'], ['V', 'Play or pause the video'], ['R', 'Reset the clock'], ['5', 'Room mode'], ['N', 'Speaker notes'],
    ['F', 'Fullscreen'], ['?', 'This help']
  ].map(function (r) { return '<tr><td>' + r[0].split('  ').map(function (k) { return '<kbd>' + k + '</kbd>'; }).join(' ') + '</td><td>' + r[1] + '</td></tr>'; }).join('') + '</tbody></table>';
  var toast = make('p', 'deck-toast', document.body), toastT = 0;
  function say(msg) { toast.textContent = msg; toast.classList.add('is-on'); clearTimeout(toastT); toastT = setTimeout(function () { toast.classList.remove('is-on'); }, 1600); }

  /* ---------- Modes -------------------------------------------------------- */
  function setRoom(on) {
    finish();
    S.room = on; store('room', on ? '1' : '0');
    layoutProgress();
    var V = visible();
    if (V.indexOf(S.i) < 0) { var after = V.filter(function (k) { return k > S.i; }); jump(after.length ? after[0] : V[V.length - 1]); }
    else applyState(S.i, S.b);
    say(on ? 'Room mode: ' + V.length + ' slides' : 'Full deck: ' + V.length + ' slides');
  }
  var FORCE_STACK = /[?&]stack\b/.test(location.search);
  function setMode() {
    var presenting = !FORCE_STACK && window.innerWidth >= 700;
    if (presenting === S.presenting) return;
    finish();
    S.presenting = presenting;
    root.classList.toggle('is-presenting', presenting);
    if (presenting) layoutProgress();
    if (!presenting) {
      slides.forEach(function (s) {
        if (gsap) gsap.set(s._units.map(function (u) { return u.el; }), { clearProps: 'transform' });
        s._beatEls.forEach(function (el) { el.classList.remove('is-pending', 'is-past'); });
        s._videos.forEach(function (v) { v.pause(); });
        if (s._figure) s._figure.render(1);
      });
      if (coverRail) coverRail.style.transform = '';
    } else applyState(S.i, S.b);
  }
  function remeasure() {
    finish();
    slides.forEach(function (s) { measure(s); if (s._figure) s._figure.reserve(); });
    layoutProgress();
    if (S.presenting) applyState(S.i, S.b);
  }

  /* ---------- Input -------------------------------------------------------- */
  document.addEventListener('keydown', function (e) {
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target;
    if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
    if (!S.presenting && e.key !== '?') return;
    var k = e.key;
    // Enter and Space belong to a focused link or button (the QR link), not to the deck.
    if ((k === 'Enter' || k === ' ') && t && t.closest && t.closest('a[href], button')) return;
    if (k === 'ArrowRight' || k === 'PageDown' || k === ' ' || k === 'Enter') { e.preventDefault(); next(); }
    else if (k === 'ArrowLeft' || k === 'PageUp' || k === 'Backspace') { e.preventDefault(); prev(); }
    else if (k === 'Home') { e.preventDefault(); jump(visible()[0]); }
    else if (k === 'End') { e.preventDefault(); var V = visible(); jump(V[V.length - 1]); }
    else if (k === 't' || k === 'T') { var c = slides[S.i]._clock; if (c) { c.toggle(); } else say('No clock on this slide'); }
    else if (k === 'r' || k === 'R') { var c2 = slides[S.i]._clock; if (c2) { c2.reset(); say('Clock reset'); } }
    else if (k === '5') setRoom(!S.room);
    else if (k === 'v' || k === 'V') toggleVideos();
    else if (k === 'n' || k === 'N') { notes.hidden = !notes.hidden; renderNotes(); }
    else if (k === 'f' || k === 'F') {
      // A sandboxed frame may refuse fullscreen; say so rather than throw.
      if (document.fullscreenElement) document.exitFullscreen();
      else if (root.requestFullscreen) { var fs = root.requestFullscreen(); if (fs && fs.catch) fs.catch(function () { say('Fullscreen is blocked here. Open the page directly.'); }); }
    }
    else if (k === '?' || k === '/') { help.hidden = !help.hidden; }
    else if (k === 'Escape') { help.hidden = true; notes.hidden = true; }
  });
  var swipe = null;
  deck.addEventListener('pointerdown', function (e) { if (e.pointerType !== 'mouse') swipe = { x: e.clientX, y: e.clientY }; });
  deck.addEventListener('pointerup', function (e) {
    if (!swipe || !S.presenting) return;
    var dx = e.clientX - swipe.x, dy = e.clientY - swipe.y; swipe = null;
    if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy)) { if (dx < 0) next(); else prev(); }
  });
  var resizeT = 0;
  window.addEventListener('resize', function () { clearTimeout(resizeT); resizeT = setTimeout(function () { setMode(); remeasure(); }, 120); });
  window.addEventListener('hashchange', function () { var n = parseInt(location.hash.slice(1), 10); if (n >= 1 && n <= slides.length && n - 1 !== S.i) jump(n - 1); });

  /* ---------- Start -------------------------------------------------------- */
  var n0 = parseInt((location.hash || '').slice(1), 10);
  S.i = n0 >= 1 && n0 <= slides.length ? n0 - 1 : 0;
  if (S.room && visible().indexOf(S.i) < 0) S.i = visible()[0];
  S.presenting = !FORCE_STACK && window.innerWidth >= 700;
  root.classList.toggle('is-presenting', S.presenting);
  slides.forEach(measure);
  layoutProgress();
  if (S.presenting) {
    applyState(S.i, 0);
    // Hold the cover below its masks until fonts land, so lines are measured
    // against the real face and nothing flashes before it rises.
    if (slides[S.i]._kind === 'cover' && motionOn()) { gsap.set(unitsFor(slides[S.i], 0, 0).map(function (u) { return u.el; }), { yPercent: 110 }); R.draw = 0; renderProgress(); }
  }
  // Start once fonts land or after a second, whichever is first. If the webfont
  // lands later, measure again (remeasure lands any entrance still running).
  var begun = false;
  function begin() {
    if (begun) return; begun = true;
    remeasure();
    if (S.presenting && slides[S.i]._kind === 'cover') coverEntrance();
    startCountdown();
  }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { if (begun) remeasure(); else begin(); });
  setTimeout(begin, 1000);

  // What the deck is doing, for deck-kit/check.mjs. Read-only.
  window.__deck = {
    state: function () {
      var V = visible();
      return { i: S.i, b: S.b, pos: V.indexOf(S.i), count: V.length, room: S.room, last: S.last,
               busy: !!S.tl, presenting: S.presenting, gsap: !!gsap,
               playing: slides.map(function (s) { return s._videos.filter(function (v) { return !v.paused; }).length; }),
               rail: { t: R.t, frac: V.length ? R.fill / V.length : 0, draw: R.draw } };
    },
    slides: slides.map(function (s) {
      return { kind: s._kind, section: s._section, videos: s._videos.length, room: s.hasAttribute('data-room'), beats: s._beats, timer: s._clock ? s._clock.total / 1000 : 0 };
    })
  };
})();
