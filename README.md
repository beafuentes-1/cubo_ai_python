# cubo_ai_python

Repository housing the **Snake — Neon Arcade** browser game and automated GitHub Pages deployment pipeline.

---

## Repository Structure

```text
cubo_ai_python/
├── .github/
│   └── workflows/
│       └── snake-pages.yml          # CI/CD workflow that deploys the web game to GitHub Pages
├── desktop/
│   └── snake-python/
│       └── web/
│           ├── index.html           # Self-contained HTML5 Canvas Snake game (HTML, CSS, JS)
│           └── README.md            # Detailed guide on game architecture and how it works
└── README.md                        # Project overview
```

## Featured Project: Snake — Neon Arcade (`desktop/snake-python/web`)

A zero-dependency, responsive browser implementation of Snake featuring a neon arcade aesthetic, progressive speed scaling, local high-score persistence, and full desktop + mobile touch controls.

### How It Works at a Glance
- **Single-File Architecture**: Everything lives in [`desktop/snake-python/web/index.html`](desktop/snake-python/web/index.html) — responsive CSS layout, semantic HTML overlay/HUD, and a vanilla JavaScript 2D Canvas game engine.
- **20×20 Logical Grid**: Rendered on a `600×600` canvas (`30px` per cell) with rounded snake segments, directional eyes, and layered fruit graphics.
- **Dynamic Speed & State Machine**: Manages `ready` → `playing` ⇄ `paused` → `over` states. Tick delay starts at `140ms` and accelerates by `10ms` every 5 points down to `60ms`.
- **Cross-Device Controls**: Supports Arrow keys, WASD, Space/P to pause, touch swipe gestures on the board, and an adaptive on-screen D-pad for mobile viewports.
- **Automated Deployment**: Pushing changes under `desktop/snake-python/web/**` triggers [`.github/workflows/snake-pages.yml`](.github/workflows/snake-pages.yml) to publish the game directly to GitHub Pages.

For full implementation details, controls, and local/GitHub Pages setup instructions, see [`desktop/snake-python/web/README.md`](desktop/snake-python/web/README.md).
