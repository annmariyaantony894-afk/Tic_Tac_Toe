# Tic Tac Toe Game - Two Players

WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


def show_board(cells):
    print()
    for row in range(3):
        a, b, c = cells[row * 3: row * 3 + 3]
        print(a, "|", b, "|", c)
        if row < 2:
            print("--+---+--")


def has_won(cells):
    for x, y, z in WINNING_LINES:
        if cells[x] != " " and cells[x] == cells[y] == cells[z]:
            return True
    return False


def ask_move(cells):
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if move < 0 or move > 8:
            print("Enter a number from 1 to 9.")
        elif cells[move] != " ":
            print("Position already taken.")
        else:
            return move


def play_round():
    cells = [" "] * 9
    current = "X"

    for turn in range(9):
        show_board(cells)
        print("Player", current, "turn")

        cells[ask_move(cells)] = current

        if has_won(cells):
            show_board(cells)
            print("Player", current, "wins!")
            return

        current = "O" if current == "X" else "X"

    show_board(cells)
    print("Game Draw!")


def main():
    while True:
        play_round()

        choice = input("Play again? (yes/no): ").strip().lower()

        if choice != "yes":
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()