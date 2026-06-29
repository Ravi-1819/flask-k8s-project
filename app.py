from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mickey Mouse 3D</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: #0a0a0f;
    overflow: hidden;
    width: 100vw;
    height: 100vh;
    cursor: none;
  }
  canvas { display: block; }
  #trail-container {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
  }
  #mickey-wrap {
    position: fixed;
    pointer-events: none;
    z-index: 10;
    transform: translate(-50%, -50%);
    transition: none;
    filter: drop-shadow(0 0 18px #ffe066cc) drop-shadow(0 0 40px #ff66aa88);
  }
  #label {
    position: fixed;
    bottom: 24px;
    left: 50%;
    transform: translateX(-50%);
    color: #ffffff44;
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
    letter-spacing: 3px;
    text-transform: uppercase;
    pointer-events: none;
    z-index: 20;
  }
</style>
</head>
<body>
<canvas id="trail-container"></canvas>
<div id="mickey-wrap">
  <svg id="mickey-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 220" width="110" height="121">
    <defs>
      <!-- 3D ear gradient left -->
      <radialGradient id="earL" cx="35%" cy="30%" r="60%">
        <stop offset="0%" stop-color="#555"/>
        <stop offset="60%" stop-color="#1a1a1a"/>
        <stop offset="100%" stop-color="#0a0a0a"/>
      </radialGradient>
      <!-- 3D ear gradient right -->
      <radialGradient id="earR" cx="65%" cy="30%" r="60%">
        <stop offset="0%" stop-color="#555"/>
        <stop offset="60%" stop-color="#1a1a1a"/>
        <stop offset="100%" stop-color="#0a0a0a"/>
      </radialGradient>
      <!-- 3D head gradient -->
      <radialGradient id="headGrad" cx="40%" cy="30%" r="65%">
        <stop offset="0%" stop-color="#606060"/>
        <stop offset="45%" stop-color="#222"/>
        <stop offset="100%" stop-color="#080808"/>
      </radialGradient>
      <!-- Face skin gradient -->
      <radialGradient id="faceGrad" cx="40%" cy="35%" r="65%">
        <stop offset="0%" stop-color="#f5d8b0"/>
        <stop offset="70%" stop-color="#e8b87a"/>
        <stop offset="100%" stop-color="#c48a40"/>
      </radialGradient>
      <!-- Eye shine -->
      <radialGradient id="eyeShine" cx="30%" cy="30%" r="60%">
        <stop offset="0%" stop-color="#ffffff"/>
        <stop offset="100%" stop-color="#88ccff00"/>
      </radialGradient>
      <!-- Nose gradient -->
      <radialGradient id="noseGrad" cx="35%" cy="30%" r="65%">
        <stop offset="0%" stop-color="#553333"/>
        <stop offset="100%" stop-color="#1a0808"/>
      </radialGradient>
      <!-- Glowing rim -->
      <filter id="glow">
        <feGaussianBlur stdDeviation="3.5" result="coloredBlur"/>
        <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>

    <!-- Shadow under mickey -->
    <ellipse cx="100" cy="218" rx="44" ry="7" fill="#000" opacity="0.45"/>

    <!-- Ears -->
    <circle cx="48" cy="52" r="36" fill="url(#earL)" stroke="#333" stroke-width="1.2"/>
    <circle cx="152" cy="52" r="36" fill="url(#earR)" stroke="#333" stroke-width="1.2"/>
    <!-- Ear highlight rims -->
    <circle cx="48" cy="52" r="36" fill="none" stroke="#ffffff18" stroke-width="2"/>
    <circle cx="152" cy="52" r="36" fill="none" stroke="#ffffff18" stroke-width="2"/>
    <!-- Ear top shine -->
    <ellipse cx="38" cy="38" rx="10" ry="7" fill="#ffffff22" transform="rotate(-20,38,38)"/>
    <ellipse cx="162" cy="38" rx="10" ry="7" fill="#ffffff22" transform="rotate(20,162,38)"/>

    <!-- Head -->
    <circle cx="100" cy="118" r="72" fill="url(#headGrad)" stroke="#2a2a2a" stroke-width="1.5"/>
    <!-- Head rim light -->
    <circle cx="100" cy="118" r="72" fill="none" stroke="#ffffff14" stroke-width="3"/>
    <!-- Head top shine -->
    <ellipse cx="78" cy="78" rx="22" ry="13" fill="#ffffff18" transform="rotate(-25,78,78)"/>

    <!-- Face oval (skin) -->
    <ellipse cx="100" cy="130" rx="48" ry="44" fill="url(#faceGrad)"/>

    <!-- Eyes white -->
    <ellipse cx="80" cy="112" rx="14" ry="15" fill="#f0f0f0"/>
    <ellipse cx="120" cy="112" rx="14" ry="15" fill="#f0f0f0"/>

    <!-- Pupils -->
    <circle cx="83" cy="114" r="9" fill="#111"/>
    <circle cx="123" cy="114" r="9" fill="#111"/>
    <!-- Eye shine -->
    <circle cx="79" cy="110" r="4" fill="url(#eyeShine)" opacity="0.9"/>
    <circle cx="119" cy="110" r="4" fill="url(#eyeShine)" opacity="0.9"/>
    <!-- Tiny sparkle dot -->
    <circle cx="86" cy="118" r="1.5" fill="#ffffff88"/>
    <circle cx="126" cy="118" r="1.5" fill="#ffffff88"/>

    <!-- Nose -->
    <ellipse cx="100" cy="134" rx="12" ry="8" fill="url(#noseGrad)" filter="url(#glow)"/>
    <ellipse cx="97" cy="131" rx="4" ry="2.5" fill="#ffffff33"/>

    <!-- Smile -->
    <path d="M80 148 Q100 166 120 148" fill="none" stroke="#8b5a2b" stroke-width="3" stroke-linecap="round"/>
    <!-- Cheek blush -->
    <ellipse cx="72" cy="140" rx="12" ry="7" fill="#ff8888" opacity="0.22"/>
    <ellipse cx="128" cy="140" rx="12" ry="7" fill="#ff8888" opacity="0.22"/>

    <!-- Tongue peek -->
    <path d="M83 155 Q100 165 117 155" fill="#e87070" opacity="0.7"/>

    <!-- White gloves hands -->
    <circle cx="28" cy="185" r="22" fill="#f0f0f0" stroke="#ddd" stroke-width="1"/>
    <circle cx="172" cy="185" r="22" fill="#f0f0f0" stroke="#ddd" stroke-width="1"/>
    <!-- Glove shine -->
    <ellipse cx="22" cy="176" rx="7" ry="5" fill="#ffffff88" transform="rotate(-20,22,176)"/>
    <ellipse cx="165" cy="176" rx="7" ry="5" fill="#ffffff88" transform="rotate(20,165,176)"/>

    <!-- Red shorts suggestion -->
    <path d="M62 178 Q100 200 138 178 L130 210 Q100 220 70 210 Z" fill="#cc2222" opacity="0.85"/>
    <path d="M95 178 L105 178 L108 212 L92 212 Z" fill="#aa1111" opacity="0.6"/>
    <!-- Yellow buttons -->
    <circle cx="90" cy="190" r="4" fill="#ffe066" filter="url(#glow)"/>
    <circle cx="110" cy="190" r="4" fill="#ffe066" filter="url(#glow)"/>

    <!-- Shoes -->
    <ellipse cx="72" cy="213" rx="22" ry="9" fill="#111" stroke="#333" stroke-width="1"/>
    <ellipse cx="128" cy="213" rx="22" ry="9" fill="#111" stroke="#333" stroke-width="1"/>
    <!-- Shoe shine -->
    <ellipse cx="65" cy="208" rx="8" ry="3" fill="#ffffff22" transform="rotate(-10,65,208)"/>
    <ellipse cx="121" cy="208" rx="8" ry="3" fill="#ffffff22" transform="rotate(-10,121,208)"/>
  </svg>
</div>

<div id="label">✨ Move your cursor</div>

<script>
  const canvas = document.getElementById('trail-container');
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  });

  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let mickeyX = mouseX;
  let mickeyY = mouseY;
  const mickeyWrap = document.getElementById('mickey-wrap');
  const mickeySvg = document.getElementById('mickey-svg');
  const stars = [];
  const trails = [];

  // Generate background stars
  for (let i = 0; i < 180; i++) {
    stars.push({
      x: Math.random() * window.innerWidth,
      y: Math.random() * window.innerHeight,
      r: Math.random() * 1.6 + 0.2,
      alpha: Math.random() * 0.7 + 0.1,
      twinkleSpeed: Math.random() * 0.02 + 0.005
    });
  }

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    // Add sparkle trail
    for (let i = 0; i < 3; i++) {
      trails.push({
        x: e.clientX + (Math.random() - 0.5) * 20,
        y: e.clientY + (Math.random() - 0.5) * 20,
        r: Math.random() * 5 + 2,
        alpha: 1,
        color: Math.random() > 0.5 ? '#ffe066' : (Math.random() > 0.5 ? '#ff66aa' : '#66ccff'),
        vx: (Math.random() - 0.5) * 1.5,
        vy: (Math.random() - 0.5) * 1.5 - 0.5,
        decay: Math.random() * 0.03 + 0.02
      });
    }
  });

  let time = 0;
  function animate() {
    requestAnimationFrame(animate);
    time += 0.012;

    // Clear
    ctx.fillStyle = 'rgba(10,10,15,0.18)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw stars
    for (const s of stars) {
      s.alpha += Math.sin(time * s.twinkleSpeed * 60) * 0.008;
      s.alpha = Math.max(0.05, Math.min(0.95, s.alpha));
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255,255,255,${s.alpha})`;
      ctx.fill();
    }

    // Draw trail particles
    for (let i = trails.length - 1; i >= 0; i--) {
      const t = trails[i];
      t.x += t.vx;
      t.y += t.vy;
      t.alpha -= t.decay;
      t.r *= 0.97;
      if (t.alpha <= 0) { trails.splice(i, 1); continue; }
      ctx.save();
      ctx.globalAlpha = t.alpha;
      ctx.beginPath();
      ctx.arc(t.x, t.y, t.r, 0, Math.PI * 2);
      // Glow
      const grad = ctx.createRadialGradient(t.x, t.y, 0, t.x, t.y, t.r);
      grad.addColorStop(0, t.color);
      grad.addColorStop(1, t.color + '00');
      ctx.fillStyle = grad;
      ctx.fill();
      ctx.restore();
    }

    // Smooth mickey follow
    mickeyX += (mouseX - mickeyX) * 0.1;
    mickeyY += (mouseY - mickeyY) * 0.1;

    // 3D tilt effect based on mouse position
    const cx = window.innerWidth / 2;
    const cy = window.innerHeight / 2;
    const tiltX = ((mouseY - cy) / cy) * 18;
    const tiltY = ((mouseX - cx) / cx) * -18;
    const scaleVal = 1 + Math.sin(time * 1.5) * 0.04;

    mickeyWrap.style.left = mickeyX + 'px';
    mickeyWrap.style.top = mickeyY + 'px';
    mickeySvg.style.transform =
      `perspective(500px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale(${scaleVal})`;

    // Dynamic glow color cycle
    const hue = (time * 40) % 360;
    mickeyWrap.style.filter =
      `drop-shadow(0 0 16px hsla(${hue},90%,65%,0.7)) drop-shadow(0 0 40px hsla(${hue+40},80%,55%,0.4))`;
  }

  animate();
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
