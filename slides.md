---
layout: center
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: "ECHO: Edge–Cloud Humanoid Control"
lineNumbers: false
drawings:
  persist: false
mdc: true
clicks: 0
preload: false
glowSeed: 229
routerMode: hash
---

<!-- Slide 1: Title with Video Background -->

<div class="video-bg-grid">
  <video autoplay muted loop playsinline><source src="/videos/sim/walk 5 step.mp4" type="video/mp4"></video>
  <video autoplay muted loop playsinline><source src="/videos/sim/fly kick.mp4" type="video/mp4"></video>
  <video autoplay muted loop playsinline><source src="/videos/real/do jumping jacks.mp4" type="video/mp4"></video>
  <video autoplay muted loop playsinline><source src="/videos/real/wave right hand.mp4" type="video/mp4"></video>
  <video autoplay muted loop playsinline><source src="/videos/sim/a man walks forward then squats.mp4" type="video/mp4"></video>
  <video autoplay muted loop playsinline><source src="/videos/real/a person is playing a violin.mp4" type="video/mp4"></video>
</div>
<div class="video-bg-overlay"></div>

<div class="title-content flex flex-col items-center justify-center text-center">
  <div class="section-tag mb-6" style="color: #60a5fa;">Anonymous Submission</div>
  <h1 style="font-size: 2.6em; line-height: 1.15; font-weight: 800; letter-spacing: -0.02em;">
    ECHO
  </h1>
  <div mt-2 text-xl opacity-80 font-light style="max-width: 700px;">
    An Edge–Cloud Framework for<br/>
    <span style="background: linear-gradient(135deg, #60a5fa, #a78bfa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 700;">Language-Driven Whole-Body Control</span><br/>
    of Humanoid Robots
  </div>
  <div mt-8 flex gap-4 text-sm opacity-50>
    <div flex items-center gap-1><div i-carbon:machine-learning-model /> Diffusion Generation</div>
    <div>·</div>
    <div flex items-center gap-1><div i-carbon:edge-cluster /> Edge–Cloud</div>
    <div>·</div>
    <div flex items-center gap-1><div i-carbon:bot /> Unitree G1</div>
  </div>
</div>

---
class: py-8
glowSeed: 100
---

# Challenges in Language-to-Humanoid Control

<span>Why existing approaches fall short for real-world deployment</span>

<div mt-6 />

<div grid grid-cols-3 gap-4 h-72>

<div border="1 solid white/8" rounded-xl overflow-hidden bg="white/3" backdrop-blur-sm>
  <div flex items-center bg="red-800/30" px-4 py-2.5>
    <div i-carbon:warning-alt text-red-300 text-lg mr-2 />
    <div font-semibold text-sm>End-to-End Latency</div>
  </div>
  <div px-4 py-3 flex flex-col gap-2.5>
    <div>
      <div text-sm font-medium>On-board compute bottleneck</div>
      <div text-xs opacity-60>Large language-action models compete with high-freq control</div>
    </div>
    <div>
      <div text-sm font-medium>Latency vs. expressivity</div>
      <div text-xs opacity-60>Can't scale semantics without sacrificing real-time stability</div>
    </div>
    <div>
      <div text-sm font-medium>Safety enforcement</div>
      <div text-xs opacity-60>Single network solves grounding + dynamics simultaneously</div>
    </div>
  </div>
</div>

<div border="1 solid white/8" rounded-xl overflow-hidden bg="white/3" backdrop-blur-sm>
  <div flex items-center bg="amber-800/30" px-4 py-2.5>
    <div i-carbon:connect text-amber-300 text-lg mr-2 />
    <div font-semibold text-sm>Retargeting Overhead</div>
  </div>
  <div px-4 py-3 flex flex-col gap-2.5>
    <div>
      <div text-sm font-medium>Morphology mismatch</div>
      <div text-xs opacity-60>Human body model ≠ robot kinematics</div>
    </div>
    <div>
      <div text-sm font-medium>Error accumulation</div>
      <div text-xs opacity-60>Multi-stage pipeline amplifies drift</div>
    </div>
    <div>
      <div text-sm font-medium>Redundant DoFs</div>
      <div text-xs opacity-60>Human parameterization includes unused degrees of freedom</div>
    </div>
  </div>
</div>

<div border="1 solid white/8" rounded-xl overflow-hidden bg="white/3" backdrop-blur-sm>
  <div flex items-center bg="violet-800/30" px-4 py-2.5>
    <div i-carbon:locked text-violet-300 text-lg mr-2 />
    <div font-semibold text-sm>Latent Coupling</div>
  </div>
  <div px-4 py-3 flex flex-col gap-2.5>
    <div>
      <div text-sm font-medium>Tightly co-trained interfaces</div>
      <div text-xs opacity-60>Latent spaces entangled with downstream policies</div>
    </div>
    <div>
      <div text-sm font-medium>No cross-platform portability</div>
      <div text-xs opacity-60>Migrating requires complete interface realignment</div>
    </div>
    <div>
      <div text-sm font-medium>Limited interpretability</div>
      <div text-xs opacity-60>Black-box latent representations lack transparency</div>
    </div>
  </div>
</div>

</div>

<div mt-4 flex justify-center>
  <div
    border="1 solid white/10" bg="white/4" backdrop-blur-sm
    rounded-xl px-6 py-3 flex items-center gap-3
  >
    <div i-carbon:idea text-yellow-300 text-xl />
    <span text-base><strong>ECHO</strong> strictly decouples generation (cloud) from execution (edge)</span>
  </div>
</div>
---
class: py-8
glowSeed: 205
---

# Cloud Generator + Edge Tracker

<span>Two-module design bridged by a compact 38D robot-native representation</span>

<div mt-4 grid grid-cols-2 gap-6>

<div border="1 solid white/8" rounded-xl overflow-hidden bg="white/3" backdrop-blur-sm>
  <div bg="blue-800/30" px-4 py-2.5 flex items-center>
    <div i-carbon:cloud text-blue-300 text-lg mr-2 />
    <span font-bold text-sm>Cloud: Diffusion Generator</span>
  </div>
  <div px-4 py-3 flex flex-col gap-2>
    <div flex items-center gap-2>
      <div i-carbon:text-link--analysis text-blue-300 min-w-5 />
      <span text-sm>CLIP ViT-B/32 text encoding + cross-attention</span>
    </div>
    <div flex items-center gap-2>
      <div i-carbon:chart-network text-blue-300 min-w-5 />
      <span text-sm>1D Conv UNet with AdaGN residual blocks</span>
    </div>
    <div flex items-center gap-2>
      <div i-carbon:timer text-blue-300 min-w-5 />
      <span text-sm>DDIM 10 steps → <strong>~1s</strong> cloud latency</span>
    </div>
    <div flex items-center gap-2>
      <div i-carbon:settings-adjust text-blue-300 min-w-5 />
      <span text-sm>CFG scale 2.5, trained on retargeted HumanML3D</span>
    </div>
    <div mt-2 bg="black/20" rounded-lg p-3>
      <div text-xs opacity-70 mb-1>38D Representation per frame:</div>
      <div font-mono text-xs>
        <span text-blue-300>29D</span> joints + <span text-cyan-300>2D</span> root vel + <span text-green-300>1D</span> height + <span text-violet-300>6D</span> rotation
      </div>
    </div>
  </div>
</div>

<div border="1 solid white/8" rounded-xl overflow-hidden bg="white/3" backdrop-blur-sm>
  <div bg="green-800/30" px-4 py-2.5 flex items-center>
    <div i-carbon:edge-cluster text-green-300 text-lg mr-2 />
    <span font-bold text-sm>Edge: RL Tracker</span>
  </div>
  <div px-4 py-3 flex flex-col gap-2>
    <div flex items-center gap-2>
      <div i-carbon:machine-learning-model text-green-300 min-w-5 />
      <span text-sm>Asymmetric Actor-Critic Teacher policy (PPO)</span>
    </div>
    <div flex items-center gap-2>
      <div i-carbon:education text-green-300 min-w-5 />
      <span text-sm>Student distillation + Evidential Deep Regression</span>
    </div>
    <div flex items-center gap-2>
      <div i-carbon:reflect-horizontal text-green-300 min-w-5 />
      <span text-sm>Morphological symmetry loss → no limping</span>
    </div>
    <div flex items-center gap-2>
      <div i-carbon:renew text-green-300 min-w-5 />
      <span text-sm>Domain randomization for sim-to-real</span>
    </div>
    <div mt-2 bg="black/20" rounded-lg p-3 flex items-center gap-3>
      <div i-carbon:restart text-amber-300 text-xl min-w-6 />
      <div>
        <div text-xs font-bold>Fall Recovery</div>
        <div text-xs opacity-70>IMU-triggered autonomous recovery from pre-built motion library</div>
      </div>
    </div>
  </div>
</div>

</div>

<div mt-3 flex justify-center gap-6 text-xs opacity-60>
  <div flex items-center gap-1><div i-carbon:connection-signal /> WebSocket streaming at 50 FPS</div>
  <div>·</div>
  <div flex items-center gap-1><div i-carbon:bot /> Unitree G1 (29-DoF EDU)</div>
  <div>·</div>
  <div flex items-center gap-1><div i-carbon:checkmark-outline /> Zero hardware fine-tuning</div>
</div>

---
class: py-6
glowSeed: 140
---

# Sim-to-Real Results: Locomotion

<div class="section-tag" style="color: #60a5fa;">🚶 Walking · Running · Navigation</div>

<div mt-3 class="result-grid-3x2">

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/walk 5 step.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/walk 5 step.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"walk 5 steps"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/walk forward turn left.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/walk forward turn left.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"walk forward, then turn left"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/walk in a circle.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/walk in a circle.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"walk in a circle"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/a person is walking backward.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/a person is walking backward.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"walking backward"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/a person moves ahead.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/a person moves ahead.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"a person moves ahead"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/he is running straight and stopped.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/he is running straight and stopped.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"running straight and stopped"</div>
</div>

</div>

---
class: py-6
glowSeed: 170
---

# Sim-to-Real Results: Upper Body

<div class="section-tag" style="color: #a78bfa;">🎻 Gestures · Interaction · Manipulation</div>

<div mt-3 class="result-grid-3x2">

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/wave right hand.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/wave right hand.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"wave right hand"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/a person is playing a violin.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/a person is playing a violin.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"playing a violin"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/a person is drinking water.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/a person is drinking water.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"drinking water"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/a person wipes a window with their right hand in large circles.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/a person wipes a window with their right hand in large circles.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"wipes window in circles"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/a person moves an object from the left side and moves it to the right side.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/a person moves an object from the left side and moves it to the right side.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"moves object left to right"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/a person swivels their right leg then their left leg.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/a person swivels their right leg then their left leg.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"swivels right then left leg"</div>
</div>

</div>

---
class: py-6
glowSeed: 200
---

# Sim-to-Real Results: Dynamic + Combat

<div class="section-tag" style="color: #f87171;">⚡ Jumping · 🥊 Combat · 🏋️ Full-Body</div>

<div mt-3 class="result-grid-3x2">

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/do jumping jacks.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/do jumping jacks.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"do jumping jacks"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/a person is jumping from side to side.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/a person is jumping from side to side.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"jumping from side to side"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/jumps up in a tight twirl.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/jumps up in a tight twirl.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"jumps up in a tight twirl"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/a man throwing a punch with right hand.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/a man throwing a punch with right hand.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"throwing a punch"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/fly kick.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/fly kick.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"fly kick"</div>
</div>

<div class="video-cell">
  <div class="badge-row"><span class="badge-sim">Simulation</span><span class="badge-real">Real Robot</span></div>
  <div class="video-pair">
    <video autoplay muted loop playsinline><source src="/videos/sim/a person is practicing squats.mp4" type="video/mp4"></video>
    <video autoplay muted loop playsinline><source src="/videos/real/a person is practicing squats.mp4" type="video/mp4"></video>
  </div>
  <div class="prompt-label">"practicing squats"</div>
</div>

</div>

---
layout: center
glowSeed: 250
---

# Results and Contributions

<div mt-4 grid grid-cols-2 gap-6>

<div>
  <div border="1 solid white/8" rounded-xl overflow-hidden bg="white/3" backdrop-blur-sm>
    <div bg="blue-800/30" px-4 py-2 flex items-center>
      <div i-carbon:chart-evaluation text-blue-300 mr-2 />
      <span font-bold text-sm>Generation Quality (vs. Baselines)</span>
    </div>
    <div px-3 py-3 flex flex-col gap-1>
      <div flex text-xs border-b="1 solid white/10" pb-1 mb-1>
        <div flex-1 opacity-60>Metric</div>
        <div w-20 text-center opacity-60>Best Prior</div>
        <div w-20 text-center text-blue-400 font-bold>ECHO</div>
      </div>
      <div flex text-xs py-0.5>
        <div flex-1>FID (lower better)</div>
        <div w-20 text-center>0.037</div>
        <div w-20 text-center text-blue-400 font-bold>0.029</div>
      </div>
      <div flex text-xs py-0.5>
        <div flex-1>R-Precision Top-1</div>
        <div w-20 text-center>0.683</div>
        <div w-20 text-center text-blue-400 font-bold>0.686</div>
      </div>
      <div flex text-xs py-0.5>
        <div flex-1>MM. Distance</div>
        <div w-20 text-center>0.414</div>
        <div w-20 text-center text-blue-400 font-bold>0.343</div>
      </div>
      <div flex text-xs py-0.5>
        <div flex-1>MSS (Safety)</div>
        <div w-20 text-center>0.527</div>
        <div w-20 text-center text-blue-400 font-bold>0.484</div>
      </div>
    </div>
  </div>

  <div mt-3 grid grid-cols-3 gap-2>
    <div class="stat-card">
      <div class="stat-value">100%</div>
      <div class="stat-label">Success Rate</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">~1s</div>
      <div class="stat-label">Cloud Latency</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">38D</div>
      <div class="stat-label">Compact Repr.</div>
    </div>
  </div>
</div>

<div flex flex-col gap-3>
  <div border="1 solid white/8" rounded-xl bg="white/3" backdrop-blur-sm p-4>
    <div flex items-center mb-2>
      <div i-carbon:checkmark-outline text-green-400 mr-2 />
      <span font-bold text-sm>Key Contributions</span>
    </div>
    <div flex flex-col gap-2 text-sm>
      <div flex items-start gap-2>
        <div i-carbon:arrow-right text-blue-300 min-w-4 mt-0.5 />
        <span>Edge-Cloud paradigm: stream diffusion motion, execute on-board</span>
      </div>
      <div flex items-start gap-2>
        <div i-carbon:arrow-right text-blue-300 min-w-4 mt-0.5 />
        <span>Robot-native 38D velocity-based interface, retargeting-free</span>
      </div>
      <div flex items-start gap-2>
        <div i-carbon:arrow-right text-blue-300 min-w-4 mt-0.5 />
        <span>Novel metrics: MSS (safety) and RTC (trajectory consistency)</span>
      </div>
      <div flex items-start gap-2>
        <div i-carbon:arrow-right text-blue-300 min-w-4 mt-0.5 />
        <span>Real-robot deployment on Unitree G1, zero hardware fine-tuning</span>
      </div>
    </div>
  </div>

  <div border="1 solid white/8" rounded-xl bg="violet-900/20" backdrop-blur-sm p-4>
    <div flex items-center mb-2>
      <div i-carbon:growth text-violet-300 mr-2 />
      <span font-bold text-sm>Future Directions</span>
    </div>
    <div text-sm opacity-80>
      Integrate visual feedback for a Vision-Language-Action (VLA) architecture enabling obstacle-aware motion synthesis
    </div>
  </div>

  <div mt-auto text-center text-xs opacity-40>
    Code and models will be released upon acceptance.
  </div>
</div>

</div>
