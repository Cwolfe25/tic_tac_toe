"""
Created on Dec 5, 2022

@author: CWolfe25
"""
def main():
    """
    variable identity
        board = list
        win_condition = int
        turn = int
        choice = int
    board is where the area being manipulated that the player and computer play on 
    win_condition is what checks to see who won
    turn is the amount of turns that have past and it checks for ties
    choice is the cord that the player puts their x
    """
    board = [["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]]
    win_condition = 0                                                                               #here is where the variables are assigned 
    turn = 0
    print("Test")
    while win_condition == 0:
        if turn == 0 or turn == 2 or turn == 4 or turn == 6 or turn == 8:                           #if its the players turn they choose where to put X
            print("x turn")                                                                         #player 1 is automaticaly x
            choice = input("what row do you want to put X 1-9")                                     #player 1 chooses where
            choice = int(choice)
            if choice >= 1 and choice <= 9:                                                         #limits dumb imputs
                if choice == 1:                                                                     #all posibilities for player choice
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
                print("you forfit your turn for being stupid")                                      #punishes player 2 for disobeying directions 
        elif turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9:                         #player 2 is always O
            print("O turn")                                                                         #does the same thing as x with asking the player for the cords then placing O in
            choice = input("what row do you want to put X 1-9")
            choice = int(choice)
            if choice >= 1 and choice <= 9:
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
                print("you forfit your turn because you are stupid")
        turn = turn + 1                                                                             #tracks turns
        prints(board)
        win_condition = win(board,win_condition,turn)                                               #runs the win function
        if win_condition == 1:                                                                      #posibilities for winner
            print("x won")
        elif win_condition == 2:
            print("O won")
        elif win_condition == 3:
            print("its a tie")


def win(board,win_condition,turn):
    """ 
    takes 
        board
        win_condition
        turn
    returns 
        win_condition
    variables 
        board
        turn
        win_condition
    """
    if board[0][0] == "x" and board[1][0] == "x" and board[2][0] == "x":                               #a ton of if statements for every way we could win
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
def prints(board):
    """
    takes:
    board
    
    """
    for row in range(0,3):                                                                  #goes through every row and prints it 
        print(board[row])

if __name__ == "__main__":
    main()