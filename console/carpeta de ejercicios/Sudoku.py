"""Sudoku terminal game with a more polished and interactive experience."""

PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"
DIM = "\033[2m"


def allowed(board, row, col, number):
    for i in range(9):
        if i != col and board[row][i] == number:
            return False
        if i != row and board[i][col] == number:
            return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if (r, c) != (row, col) and board[r][c] == number:
                return False
    return True


def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for n in range(1, 10):
                    if allowed(board, r, c, n):
                        board[r][c] = n
                        if solve(board):
                            return True
                        board[r][c] = 0
                return False
    return True


def style_cell(value, fixed):
    if value == 0:
        return f"{DIM}. {RESET}"
    if fixed:
        return f"{YELLOW}{value}{RESET}"
    return f"{GREEN}{value}{RESET}"


def display(board, message=""):
    print("\n" + "=" * 38)
    print(f"{BOLD}{CYAN}        SUDOKU TERMINAL{RESET}")
    print("=" * 38)
    print(f"{DIM}   1  2  3   4  5  6   7  8  9{RESET}")
    print(f"{DIM} +-----+-----+-----+{RESET}")

    for r in range(9):
        row_cells = []
        for c in range(9):
            value = board[r][c]
            fixed = PUZZLE[r][c] != 0
            row_cells.append(f" {style_cell(value, fixed):^3} ")
        line = " | ".join(
            " ".join(row_cells[i:i + 3]) for i in range(0, 9, 3)
        )
        print(f"{r + 1:>2} | {line} |")
        if r in (2, 5):
            print(f"{DIM} +-----+-----+-----+{RESET}")
    print(f"{DIM} +-----+-----+-----+{RESET}")
    if message:
        print(f"{BOLD}{BLUE}{message}{RESET}\n")


def complete(board):
    return all(
        1 <= board[r][c] <= 9 and allowed(board, r, c, board[r][c])
        for r in range(9) for c in range(9)
    )


def help_text():
    print(f"\n{BOLD}{CYAN}INSTRUCCIONES{RESET}")
    print("- Escribe una jugada como: 1 3 5")
    print("- Para borrar: 1 3 0")
    print("- Para pista: hint 1 3")
    print("- Para verificar: check")
    print("- Para reiniciar: reset")
    print("- Para ayuda: help")
    print("- Para salir: quit")
    print("- Cada fila, columna y bloque 3x3 debe tener números 1–9 sin repetir.")


def main():
    board = [row[:] for row in PUZZLE]
    solution = [row[:] for row in PUZZLE]

    if not solve(solution):
        print(f"{RED}El puzzle no tiene solución.{RESET}")
        return

    print(f"{BOLD}{CYAN}Bienvenido a Sudoku{RESET}")
    help_text()

    message = "Empieza a jugar."
    while True:
        display(board, message)
        if complete(board):
            print(f"\n{BOLD}{GREEN}¡Felicidades! Resolveste el Sudoku.{RESET}")
            return

        raw = input(f"{BOLD}{CYAN}Tu movimiento > {RESET}").strip().lower()
        if not raw:
            message = "Escribe una jugada o 'help'."
            continue

        parts = raw.split()
        if parts == ["quit"]:
            print(f"{YELLOW}Gracias por jugar.{RESET}")
            return
        if parts == ["help"]:
            help_text()
            message = "Necesitas ayuda."
            continue
        if parts == ["reset"]:
            board = [row[:] for row in PUZZLE]
            message = "Puzzle reiniciado."
            continue
        if parts == ["check"]:
            errors = [
                (r + 1, c + 1)
                for r in range(9)
                for c in range(9)
                if board[r][c] and board[r][c] != solution[r][c]
            ]
            message = (
                f"Hay errores en: {errors}"
                if errors else "Todo va bien hasta ahora."
            )
            continue

        hint = parts[0] == "hint"
        values = parts[1:] if hint else parts

        if len(values) != (2 if hint else 3):
            message = "Formato incorrecto. Ejemplo: 1 3 5 o hint 1 3"
            continue

        try:
            numbers = [int(v) for v in values]
        except ValueError:
            message = "Solo se permiten números enteros."
            continue

        r, c = numbers[0] - 1, numbers[1] - 1
        if not (0 <= r < 9 and 0 <= c < 9):
            message = "Fila y columna deben estar entre 1 y 9."
            continue
        if PUZZLE[r][c] != 0:
            message = "Esa celda es un número fijo; no puedes modificarla."
            continue

        n = solution[r][c] if hint else numbers[2]
        if not 0 <= n <= 9:
            message = "El valor debe estar entre 0 y 9."
            continue

        if n and not allowed(board, r, c, n):
            message = "Ese número repite en fila, columna o bloque."
            continue

        board[r][c] = n
        message = f"Celda ({r + 1}, {c + 1}) actualizada."


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Juego cerrado.{RESET}")
