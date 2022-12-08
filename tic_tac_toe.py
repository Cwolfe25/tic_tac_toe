"""
Created on Dec 5, 2022

@author: CWolfe25
"""
def main():
    """
    This is the main of my function and it forms the tic tac toe board
    local variables:
        Board = list
        win_condition = int
        turn = int
        choice = int
    Board is the variable that is where the tic tac toe is being played
    win_condition shows who won the game and is being checked
    turn is the amount of plays that game has had
    choice is which place on the board that they want to change to an x or O
    
    """
    board = [["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]]
    win_condition = 0
    turn = 0
    print("Test")
    while win_condition == 0:                                                   #this will end the game when a winner is found
        if turn == 0 or turn == 2 or turn == 4 or turn == 6 or turn == 8:       #this shows the turn that alternates into x
            print("O turn")
            x_row = input("what row do you want")
            x_col = input("what column do oyu want")
            x_row = int(x_row)
            x_col = int(x_col)
            x_row == x_row - 1
            x_col == x_col - 1
            if x_row > 2 or x_row <0:
                print("enter in a valid row")
            elif x_col > 2 or x_col <0:
                print("enter in a valid column")
            elif board[x_row][x_col] == "x" or board[x_row][x_col] == "O":
                print("this has already been chosen")   
            else:
                board[x_row][x_col] == "O"
        elif turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9:        #This see's if its Os turn
            print("O turn")
            O_row = input("what row do you want")
            O_col = input("what column do oyu want")
            O_row = int(O_row)
            O_col = int(O_col)
            O_row == O_row - 1
            O_col == O_col - 1
            if O_row > 2 or O_row <0:
                print("enter in a valid row")
            elif O_col > 2 or O_col <0:
                print("enter in a valid column")
            elif board[O_row][O_col] == "x" or board[O_row][O_col] == "O":
                print("this has already been chosen")   
            else:
                board[O_row][O_col] == "O"
        turn = turn + 1
        print(board)
        win_condition = win(board,win_condition,turn)                           #checks to see if ther is a winner
        if win_condition == 1:                                                  #see's if x has won
            print("x won")
        elif win_condition == 2:                                                #see's if O has won
            print("O won")
        elif win_condition == 3:                                                #see's if its a tie
            print("its a tie")
        else:
            print("something went wrong")



def win(board,win_condition,turn):
    """
    checks to see if every win condition is true for both x and O
    variables
        board = list
        win_condition = int
        turn = int
    these are the same variables as th main
    """
    if board[0][0] == "x" and board[1][0] == "x" and board[2][0] == "x":            #checks to see if every x win condition is right
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
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":                      #checks to see if any O is true
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
        win_condition = 3                                                                   #checks for a tie
    else:
        win_condition = 0
    return win_condition


if __name__ == "__main__":
    main()