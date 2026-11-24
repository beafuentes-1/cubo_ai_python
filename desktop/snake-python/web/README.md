# Snake — Neon Arcade (Browser Edition)

A lightweight, zero-dependency browser version of the classic Snake game built with vanilla HTML5 Canvas, CSS, and JavaScript. Designed to run seamlessly across desktop and mobile browsers without requiring Python, build steps, or third-party runtimes.

---

## Project Structure

```text
cubo_ai_python/
├── .github/
│   └── workflows/
│       └── snake-pages.yml          # GitHub Actions workflow for GitHub Pages deployment
├── desktop/
│   └── snake-python/
│       └── web/
│           ├── index.html           # Complete single-file application (HTML, CSS, & JS)
│           └── README.md            # Documentation for the web version
└── README.md                        # Repository root overview
```

### Inside `index.html`

Because the web game is packaged as a single self-contained file (`index.html`), its internal structure is divided into three clean layers:

1. **Styles (`<style>`)**:
   - Uses a dark neon arcade theme (`#090d17` background, `#8bff65` neon green accents).
   - Responsive CSS Grid and Flexbox layout that adapts to desktop viewports, short screens, and mobile devices (`safe-area-inset` support).
   - Automatically reveals an on-screen directional keypad (`@media (pointer: coarse), (max-width: 600px)`) on touch devices.
2. **Markup (`<main class="game">`)**:
   - **Header**: Displays the `SNAKE` brand title alongside live `SCORE` and `BEST` score cards (`aria-live="polite"`).
   - **Board Wrapper (`.board-wrap`)**: Houses the `600×600` `<canvas id="board">` element and a translucent state overlay (`#overlay`) for start, pause, and game-over screens.
   - **Controls**: Pause/Resume toolbar button, touch directional buttons (`data-dir`), and a control hint footer.
3. **Game Engine (`<script>`)**:
   - Pure JavaScript state machine and rendering loop using the HTML5 2D Canvas API.

---

## How It Works

### 1. Grid & Coordinate System
- The `<canvas>` resolution is `600×600` pixels, subdivided into a **`20×20` logical grid** (`grid = 20`), making each cell `30×30` pixels (`cell = canvas.width / grid`).
- The snake is stored as an array of `{ x, y }` grid coordinates, initialized at the center of the board (`[{ x: 10, y: 10 }, { x: 9, y: 10 }, { x: 8, y: 10 }]`) moving right.

### 2. Game States
The game transitions between four states tracked by the `state` variable:
- **`ready`**: Initial load state showing the "NEON SNAKE" start overlay.
- **`playing`**: Active game loop running via `setTimeout(tick, delay)`.
- **`paused`**: Suspends the timer and shows the "PAUSED" overlay until resumed.
- **`over`**: Triggered on collision or board completion; displays final score and a "PLAY AGAIN" prompt.

### 3. Game Loop & Dynamic Speed (`tick()`)
On every tick while `state === "playing"`:
1. **Direction Update**: Applies `nextDirection` to `direction` (buffered so rapid key presses within a single tick cannot cause an illegal 180° self-reversal).
2. **Movement & Growth**: Computes the new head position `{ x: snake[0].x + direction.x, y: snake[0].y + direction.y }` and prepends it via `snake.unshift(head)`. If the head coordinates match `food`, the tail is kept (growing the snake by 1); otherwise `snake.pop()` removes the tail.
3. **Collision Detection**:
   - **Wall collision**: Checks if `head.x` or `head.y` falls outside `0..19`.
   - **Self collision**: Checks if any segment in `snake.slice(1)` shares coordinates with `head`.
4. **Scoring & Food Spawning (`placeFood()`)**:
   - Eating food increments `score` and updates `best` in `localStorage` under the key `neon-snake-best`.
   - `placeFood()` scans the `20×20` grid for all unoccupied cells and picks one at random. If no free cells remain, the player wins with `"You filled the whole board. Incredible!"`.
5. **Progressive Difficulty**:
   - Tick interval starts at **`140ms`** and speeds up by **`10ms` for every 5 points scored**, down to a minimum cap of **`60ms`**:
     ```js
     Math.max(60, 140 - Math.floor(score / 5) * 10)
     ```

### 4. Rendering (`draw()` & `drawEyes()`)
- **Board**: Clears the canvas and draws subtle grid lines (`#18233a`).
- **Food**: Drawn as a layered glowing red apple using three offset circles (shadow, body, and white specular highlight).
- **Snake**: Drawn segment-by-segment using `ctx.roundRect()` with alternating neon greens (`#7cff5b` for the head, alternating `#39ff14` and `#20b83a` for body segments).
- **Directional Eyes**: `drawEyes(head)` positions two dark pupils on the head segment oriented toward the current movement vector.

### 5. Multi-Modal Controls
| Input Method | Action |
| :--- | :--- |
| **Arrow Keys** / **WASD** | Steer Up, Down, Left, or Right (180° instant reversal is blocked) |
| **Space** / **P** / **PAUSE Button** | Toggle Pause / Resume |
| **Enter** | Start or restart the game when not actively playing |
| **Touch Swipe** | Pointer down/up delta detection on the canvas (20px minimum threshold) |
| **On-Screen D-Pad** | Tap `▲`, `◀`, `▼`, `▶` buttons on touchscreens or narrow viewports |

---

## Play Locally

Open `index.html` directly in any modern browser. On mobile devices, copy the `web` folder to the device and open `index.html` with a browser that supports local HTML files, or serve the folder over your local network:

```bash
python3 -m http.server 8000 --directory desktop/snake-python/web
```

Then visit `http://localhost:8000` in your browser.

---

## Share a Link with GitHub Pages

The repository includes a GitHub Actions workflow (`.github/workflows/snake-pages.yml`) that automatically publishes `desktop/snake-python/web` whenever changes are pushed to `main` or `master`.

1. Push the project changes to the repository on GitHub.
2. In the repository, open **Settings → Pages** and choose **GitHub Actions** as the build and deployment source.
3. Wait for the **Publish Snake browser game** workflow to finish successfully.
4. Open the Pages URL shown in the workflow's deployment summary and share it with any computer or phone.

> **Note:** Each browser stores its own high score locally via `localStorage` (`neon-snake-best`).
