'''
Created on Nov 8, 2022

@author: CWolfe25
'''

def main():
    board = [['1','2','3'],['4','5','6'],['7','8','9']]
    win_condition = 0
    turn = 0
    print("Test")
    count = 0 
    while count == 0:
        if board [0][0] == "x" and board [1][0] == "x" and board [2][0] == "x":
            win_condition = 1
        elif board [0][0] == "x" and board [0][1] == "x" and board [0][2] == "x":
            win_condition = 1
        elif board [0][0] == "x" and board [1][1] == "x" and board [2][2] == "x":
            win_condition = 1
        elif board [0][2] == "x" and board [1][1] == "x" and board [2][0] == "x":
            win_condition = 1
        elif board [1][0] == "x" and board [1][1] == "x" and board [1][2] == "x":
            win_condition = 1
        elif board [2][0] == "x" and board [2][1] == "x" and board [2][2] == "x":
            win_condition = 1
        elif board [0][1] == "x" and board [1][1] == "x" and board [2][1] == "x":
            win_condition = 1
        elif board [0][2] == "x" and board [1][2] == "x" and board [2][2] == "x":
            win_condition = 1
        elif board [0][0] == "O" and board [1][0] == "O" and board [2][0] == "O":
            win_condition = 2
        elif board [0][0] == "O" and board [0][1] == "O" and board [0][2] == "O":
            win_condition = 2
        elif board [0][0] == "O" and board [1][1] == "O" and board [2][2] == "O":
            win_condition = 2
        elif board [0][2] == "O" and board [1][1] == "O" and board [2][0] == "O":
            win_condition = 2
        elif board [1][0] == "O" and board [1][1] == "O" and board [1][2] == "O":
            win_condition = 2
        elif board [2][0] == "O" and board [2][1] == "O" and board [2][2] == "O":
            win_condition = 2
        elif board [0][1] == "O" and board [1][1] == "O" and board [2][1] == "O":
            win_condition = 2
        elif board [0][2] == "O" and board [1][2] == "O" and board [2][2] == "O":
            win_condition = 2
        else:
            win_condition = 0
        count = count+1
    if win_condition == 0:
        if turn == 0 or turn == 2 or turn == 4 or turn == 6 or turn == 8:
            print("enter in 0,1,2")
            print("for row 0 = top 1 = middle 2 = bottom")
            print("for column 0 = left 1 = middle 2 = right")
            row_x = input("what row do you want to put X")
            column_x = input("which column do you want to put X")
            row_x = int(row_x)
            column_x = int(column_x)
            if row_x == 0 or row_x == 1 or row_x == 2 and column_x == 0 or column_x == 1 or column_x == 2:
                print(board[row_x][column_x])
                board[row_x][column_x] = "x"
        elif turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9:
            print("enter in 0,1,2")
            print("for row 0 = top 1 = middle 2 = bottom")
            print("for column 0 = left 1 = middle 2 = right")
            row_O = input("what row do you want to put O")
            column_O = input("which column do you want to put O")
            row_O = int(row_O)
            column_O = int(column_O)
            if row_O == 0 or row_O == 1 or row_O == 2 and column_O == 0 or column_O == 1 or column_O == 2:
                board[row_O][column_O] = "O"
        turn = turn + 1
        print(board)
    elif win_condition == 1:
        print("x won")
    elif win_condition == 2:
        print("O won")
    elif win_condition == 0 and turn >10:
        print("its a tie")
    else:
        print("something went wrong")






if __name__ == '__main__':
    main()