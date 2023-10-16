import random

def print_board(board):
    # for row in board:
    #     print(" | ".join(row))
    #     print("-" * 9)
    print(" | ".join(board[0]))
    print("-" * 9)
    print(" | ".join(board[1]))
    print("-" * 9)
    print(" | ".join(board[2]))

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row col): ").split())
            if board[row][col] == " ":
                return row, col
            else:
                print("That cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter your move as 'row col' (e.g., '0 1').")

def get_computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = "O"

        if check_win(board, "O"):
            print_board(board)
            print("You win!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print_board(board)
        print("Computer's turn:")
        computer_row, computer_col = get_computer_move(board)
        board[computer_row][computer_col] = "X"

        if check_win(board, "X"):
            print_board(board)
            print("Computer wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()