import random

def print_board(board):
    print("|".join(board[0]))
    print("-" * 11)
    print("|".join(board[1]))
    print("-" * 11)
    print("|".join(board[2]))

def get_input(board):
    # board = [[" " for _ in range(3)] for _ in range(3)]
    while True:
        i = int(input('Input an available number from 1 to 9: '))
        match i:
            case 1:
                input_row, input_col = 0, 0
            case 2:
                input_row, input_col = 0, 1
            case 3:
                input_row, input_col = 0, 2
            case 4:
                input_row, input_col = 1, 0
            case 5:
                input_row, input_col = 1, 1
            case 6:
                input_row, input_col = 1, 2
            case 7:
                input_row, input_col = 2, 0
            case 8:
                input_row, input_col = 2, 1
            case 9:
                input_row, input_col = 2, 2
            case defualt:
                print('Invalid input')
                continue
        if board[input_row][input_col] != "   ":
            print('This cell is occupied, select an empty cell')
        else:
            board[input_row][input_col] = " O "
            # print(board)
            break

def get_comp_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == "   ":
            board[row][col] = " X "
            break

def check_win(board, symbol):
    # check horizontally
    for row in board:
        if all(cell == symbol for cell in row):
            return True
        
    # check vertically
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    # check daigonally
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False

def check_full(board):
    # board = [[" " for _ in range(3)] for _ in range(3)]
    # if " " in board:
        # print('No')
    # else:
        # print('Yes')
    # if "   " in board:
    #     return False
    # else:
    #     return True
    
    for row in board:
        if "   " in row:
            return False
    return True

def main():
    board = [["   " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")

    while True:
        # display board
        print_board(board)
        # player starts first
        get_input(board)
        print_board(board)
        # check if player wins or if the board is full
        if check_win(board, " O "):
            print('You win')
            break
        elif check_full(board):
            print('It is a tie')
            break
        get_comp_move(board)
        print('Computer\'s move: ')
        print_board(board)
        if check_win(board, " X "):
            print('You lose')
            break
        elif check_full(board):
            print('It is a tie')
            break

if __name__ == "__main__":
    main()