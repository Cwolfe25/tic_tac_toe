"""
Created on Dec 5, 2022

@author: CWolfe25
"""
def main():
    board = [["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]]
    win_condition = 0
    turn = 0
    print("Test")
    while win_condition == 0:
        if turn == 0 or turn == 2 or turn == 4 or turn == 6 or turn == 8:
            print("x turn")
            choice = input("what row do you want to put X 1-9")
            choice = int(choice)
            if choice == 1:
                board[0][0] = "x"
            elif choice == 2:
                board[0][1] = "x"
            elif choice == 3:
                board[0][2] = "x"
            elif choice == 4:
                board[1][0] = "x" 
            elif choice == 5:
                board[1][1] = "x"
            elif choice == 6:
                board[1][2] = "x"
            elif choice == 7:
                board[2][0] = "x"
            elif choice == 8:
                board[2][1] = "x"
            elif choice == 9:
                board[2][2] = "x"
            else:
                print("enter in a number from 1-9")
        elif turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9:
            print("O turn")
            choice = input("what row do you want to put X 1-9")
            choice = int(choice)
            if choice == 1:
                board[0][0] = "O"
            elif choice == 2:
                board[0][1] = "O"
            elif choice == 3:
                board[0][2] = "O"
            elif choice == 4:
                board[1][0] = "O" 
            elif choice == 5:
                board[1][1] = "O"
            elif choice == 6:
                board[1][2] = "O"
            elif choice == 7:
                board[2][0] = "O"
            elif choice == 8:
                board[2][1] = "O"
            elif choice == 9:
                board[2][2] = "O"
            else:
                print("enter in a number from 1-9")
        turn = turn + 1
        print(board)
        win_condition = win(board,win_condition,turn)
        if win_condition == 1:
            print("x won")
        elif win_condition == 2:
            print("O won")
        elif win_condition == 3:
            print("its a tie")
        else:
            print("something went wrong")



def win(board,win_condition,turn):
    if board[0][0] == "x" and board[1][0] == "x" and board[2][0] == "x":
        win_condition = 1
    elif board[0][0] == "x" and board[0][1] == "x" and board[0][2] == "x":
        win_condition = 1
    elif board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x":
        win_condition = 1
    elif board[0][2] == "x" and board[1][1] == "x" and board[2][0] == "x":
        win_condition = 1
    elif board[1][0] == "x" and board[1][1] == "x" and board[1][2] == "x":
        win_condition = 1
    elif board[2][0] == "x" and board[2][1] == "x" and board[2][2] == "x":
        win_condition = 1
    elif board[0][1] == "x" and board[1][1] == "x" and board[2][1] == "x":
        win_condition = 1
    elif board[0][2] == "x" and board[1][2] == "x" and board[2][2] == "x":
        win_condition = 1
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        win_condition = 2
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        win_condition = 2
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        win_condition = 2
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        win_condition = 2
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        win_condition = 2
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        win_condition = 2
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        win_condition = 2
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        win_condition = 2
    elif turn <= 0: 
        win_condition = 3 
    else:
        win_condition = 0
    return win_condition


if __name__ == "__main__":
    main()