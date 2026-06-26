def display_board(board):
    """Display the current game board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")
    

def get_move(player, board):
    """Get a valid move from the player."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move, choose a number from 1 to 9.")
            elif board[move] != " ":
                print("That space is already taken.")
            else:
                return move
        except ValueError:
            print("Please enter a valid number.")


def check_win(board, player):
    """Check whether the given player has a winning combination."""
    win_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_patterns)


def check_draw(board):
    """Check whether the game is a draw."""
    return all(space != " " for space in board)


def main():
    """Run the Tic-tac-toe game loop."""
    print("Welcome to Tic-tac-toe!")
    board = [" "] * 9
    current_player = "X"

    while True:
        display_board(board)
        move = get_move(current_player, board)
        board[move] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"



if __name__ == "__main__":
    main()