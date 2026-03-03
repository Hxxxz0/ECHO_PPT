import re

with open("slides.md", "r") as f:
    content = f.read()

# Replace all 2col back to 2x2
content = content.replace('class="result-grid-2col"', 'class="result-grid-2x2"')

# Locomotion splits
content = content.replace(
    '''  <div class="prompt-label">"walk forward, then turn left"</div>
</div>

</div>

---
class: py-6
glowSeed: 145
---

# Sim-to-Real Results: Locomotion (Cont.)

<div class="section-tag" style="color: #60a5fa;">🚶 Walking · Running · Navigation</div>

<div mt-3 class="result-grid-2x2">

<div class="video-cell">''',
    '''  <div class="prompt-label">"walk forward, then turn left"</div>
</div>

<div class="video-cell">'''
)

# Upper Body splits
content = content.replace(
    '''  <div class="prompt-label">"a person is playing a violin"</div>
</div>

</div>

---
class: py-6
glowSeed: 165
---

# Sim-to-Real Results: Upper Body (Cont.)

<div class="section-tag" style="color: #a78bfa;">🎻 Gestures · Interaction · Manipulation</div>

<div mt-3 class="result-grid-2x2">

<div class="video-cell">''',
    '''  <div class="prompt-label">"a person is playing a violin"</div>
</div>

<div class="video-cell">'''
)

# Dynamic splits
content = content.replace(
    '''  <div class="prompt-label">"jumping from side to side"</div>
</div>

</div>

---
class: py-6
glowSeed: 185
---

# Sim-to-Real Results: Dynamic Motions (Cont.)

<div class="section-tag" style="color: #34d399;">⚡ Jumping · Full-Body Dynamics</div>

<div mt-3 class="result-grid-2x2">

<div class="video-cell">''',
    '''  <div class="prompt-label">"jumping from side to side"</div>
</div>

<div class="video-cell">'''
)

# Combat splits
content = content.replace(
    '''</div>

---
class: py-6
glowSeed: 205
---

# Sim-to-Real Results: Combat + Whole-Body (Cont.)

<div class="section-tag" style="color: #f87171;">🥊 Combat · ��️ Complex Motions</div>

<div mt-3 class="result-grid-3col">''',
    '''</div>

<div mt-3 class="result-grid-3col">'''
)

# More Motions splits
content = content.replace(
    '''  <div class="prompt-label">"running straight and stopped"</div>
</div>

</div>

---
class: py-6
glowSeed: 225
---

# Sim-to-Real Results: More Motions (Cont.)

<div class="section-tag" style="color: #fbbf24;">🌟 Additional Demonstrations</div>

<div mt-3 class="result-grid-2x2">

<div class="video-cell">''',
    '''  <div class="prompt-label">"running straight and stopped"</div>
</div>

<div class="video-cell">'''
)

with open("slides.md", "w") as f:
    f.write(content)

print("Restored slides successfully!")
