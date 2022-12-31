import random
def play_choose(player_board):
    """
    takes
        player_board
    returns
        player board
    variables
        ship_numb = int
        play_choice = str
    ship_numb tracks the amount of ships the player has placed
    play_choice is the place where the player places a ship
    """
    print("rows 1-5 columns 1-5")
    print("place 4 ships")
    ship_numb = 4
    while ship_numb >0:
        print("enter in A-e and 1-5 for cords")
        play_choice = input("what cord do you want")
        if play_choice == "A1" or play_choice == "a1":                              #yeah this whole thing is super inefficent but like I need to do it in a way I understand and can make work
            player_board[0][0] = "v"                                                #this gets every possible place on the board
        elif play_choice == "A2" or play_choice == "a2":
            player_board[0][1] = "v"
        elif play_choice == "A3" or play_choice == "a3":
            player_board[0][2] = "v"
        elif play_choice == "A3" or play_choice == "a3":
            player_board[0][3] = "v"
        elif play_choice == "A4" or play_choice == "a4":
            player_board[0][3] = "v"
        elif play_choice == "A5" or play_choice == "a5":
            player_board[0][4] = "v"
        elif play_choice == "B1" or play_choice == "b1":
            player_board[1][0] = "v"
        elif play_choice == "B2" or play_choice == "b2":
            player_board[1][1] = "v"
        elif play_choice == "B3" or play_choice == "b3":
            player_board[1][2] = "v"
        elif play_choice == "B4" or play_choice == "b4":
            player_board[1][3] = "v"
        elif play_choice == "B5" or play_choice == "b5":
            player_board[1][4] = "v"
        elif play_choice == "C1" or play_choice == "c1":
            player_board[2][0] = "v"
        elif play_choice == "C2" or play_choice == "c2":
            player_board[2][1] = "v"
        elif play_choice == "C3" or play_choice == "c3":
            player_board[2][2] = "v"
        elif play_choice == "C4" or play_choice == "c4":
            player_board[2][3] = "v"
        elif play_choice == "C5" or play_choice == "c5":
            player_board[2][4] = "v"
        elif play_choice == "D1" or play_choice == "d1":
            player_board[3][0] = "v"
        elif play_choice == "D2" or play_choice == "d2":
            player_board[3][1] = "v"
        elif play_choice == "D3" or play_choice == "d3":
            player_board[3][2] = "v"
        elif play_choice == "D4" or play_choice == "d4":
            player_board[3][3] = "v"
        elif play_choice == "D5" or play_choice == "d5":
            player_board[3][4] = "v"
        elif play_choice == "E1" or play_choice == "e1":
            player_board[4][0] = "v"
        elif play_choice == "E2" or play_choice == "e2":
            player_board[4][1] = "v"
        elif play_choice == "E3" or play_choice == "e3":
            player_board[4][2] = "v"
        elif play_choice == "E4" or play_choice == "e4":
            player_board[4][3] = "v"
        elif play_choice == "E5" or play_choice == "e5":
            player_board[4][4] = "v"
        ship_numb = ship_numb - 1
    print(player_board)
    return(player_board)                                                                    #returns the updated board to main
def comp_choice(comp_board):
    """
    takes
        comp_board
    returns
        comp_board
    variables
        times = int
        comp_row = int 
        comp_col = int
    times is the amount of ships placed by the comp
    comp_row is the randomly generated row
    comp_col is the randomly generated column

    """
    times = 4
    while times > 0:                                                                        #allows for the computer to place 4 ships
        comp_row = random.randint(0,4)                                                      #generates the cords for the ships
        comp_col = random.randint(0,4)
        comp_board[comp_row][comp_col] = "v"                                                #places a mark on the computers board
        times = times - 1
    return(comp_board)
def user_choice(player_show,comp_board):
    """
    takes 
        player_show
        comp_board
    returns
        player_show
    variables
        play_choice = str
    play_choice is where the player chooses to guess where the computers ship is 
    """
    print(player_show)
    print("enter in A-e and 1-5 for cords")
    play_choice = input("what cord do you want")
    if play_choice == "A1" or play_choice == "a1":                              #yeah this whole thing is super inefficent but like I need to do it in a way I understand and can make work
        if comp_board[0][0] == "v":                                             #for any posible place on the board that the player could chose it sees if a computers ship is there then adds a hit or a miss onto the play show
            player_show[0][0] = "x"
            
        else:
            player_show[0][0] = "o"
    elif play_choice == "A2" or play_choice == "a2":
        if comp_board[0][1] == "v":
            player_show[0][1] = "x"
            
        else:
            player_show[0][1] = "o"
    elif play_choice == "A3" or play_choice == "a3":
        if comp_board[0][2] == "v":
            player_show[0][2] = "x"
            
        else:
            player_show[0][2] = "o"
    elif play_choice == "A4" or play_choice == "a4":
        if comp_board[0][3] == "v":
            player_show[0][3] = "x"
            
        else:
            player_show[0][3] = "o"
    elif play_choice == "A5" or play_choice == "a5":
        if comp_board[0][4] == "v":
            player_show[0][4] = "x"
            
        else:
            player_show[0][4] = "o"
    elif play_choice == "B1" or play_choice == "b1":
        if comp_board[1][0] == "v":
            player_show[1][0] = "x"
            
        else:
            player_show[1][0] = "o"
    elif play_choice == "B2" or play_choice == "b2":
        if comp_board[1][1] == "v":
            player_show[1][1] = "x"
            
        else:
            player_show[1][1] = "o"
    elif play_choice == "B3" or play_choice == "b3":
        if comp_board[1][2] == "v":
            player_show[1][2] = "x"
            
        else:
            player_show[1][2] = "o"
    elif play_choice == "B4" or play_choice == "b4":
        if comp_board[1][3] == "v":
            player_show[1][3] = "x"
            
        else:
            player_show[1][3] = "o"
    elif play_choice == "B5" or play_choice == "b5":
        if comp_board[1][4] == "v":
            player_show[1][4] = "x"
            
        else:
            player_show[1][4] = "o"
    elif play_choice == "C1" or play_choice == "c1":
        if comp_board[2][0] == "v":
            player_show[2][0] = "x"
            
        else:
            player_show[2][0] = "o"
    elif play_choice == "C2" or play_choice == "c2":
        if comp_board[2][1] == "v":
            player_show[2][1] = "x"
            
        else:
            player_show[2][1] = "o"
    elif play_choice == "C3" or play_choice == "c3":
        if comp_board[2][2] == "v":
            player_show[2][2] = "x"
            
        else:
            player_show[2][2] = "o"
    elif play_choice == "C4" or play_choice == "c4":
        if comp_board[2][3] == "v":
            player_show[2][3] = "x"
            
        else:
            player_show[2][3] = "o"
    elif play_choice == "C5" or play_choice == "c5":
        if comp_board[2][4] == "v":
            player_show[2][4] = "x"
            
        else:
            player_show[2][4] = "o"
    elif play_choice == "D1" or play_choice == "d1":
        if comp_board[3][0] == "v":
            player_show[3][0] = "x"
            
        else:
            player_show[3][0] = "o"
    elif play_choice == "D2" or play_choice == "d2":
        if comp_board[3][1] == "v":
            player_show[3][1] = "x"
            
        else:
            player_show[3][1] = "o"
    elif play_choice == "D3" or play_choice == "d3":
        if comp_board[3][2] == "v":
            player_show[3][2] = "x"
            
        else:
            player_show[3][2] = "o"
    elif play_choice == "D4" or play_choice == "d4":
        if comp_board[3][3] == "v":
            player_show[3][3] = "x"
            
        else:
            player_show[3][3] = "o"
    elif play_choice == "D5" or play_choice == "d5":
        if comp_board[3][4] == "v":
            player_show[3][4] = "x"
            
        else:
            player_show[3][4] = "o"
    elif play_choice == "E1" or play_choice == "e1":
        if comp_board[4][0] == "v":
            player_show[4][0] = "x"
            
        else:
            player_show[4][0] = "o"
    elif play_choice == "E2" or play_choice == "e2":
        if comp_board[4][1] == "v":
            player_show[4][1] = "x"
            
        else:
            player_show[4][1] = "o"
    elif play_choice == "E3" or play_choice == "e3":
        if comp_board[4][2] == "v":
            player_show[4][2] = "x"
            
        else:
            player_show[4][2] = "o"
    elif play_choice == "E4" or play_choice == "e4":
        if comp_board[4][3] == "v":
            player_show[4][3] = "x"
            
        else:
            player_show[4][3] = "o"
    elif play_choice == "E5" or play_choice == "e5":
        if comp_board[4][4] == "v":
            player_show[4][4] = "x"
            
        else:
            player_show[4][4] = "o"
    print(player_show)
    return(player_show)
def comp_v_user(player_board,comp_show):
    """
    takes 
        player_board
        comp_show
    returns
        comp_show
    """
    row_comp = random.randint(0,4)                                                      #generates random coardnets to see if a ship is there
    col_comp = random.randint(0,4)
    if player_board[row_comp][col_comp] == "v":                                         #sees if a players ship is there then places it on the comp show
        comp_show[row_comp][col_comp] = "x"
    else:
        comp_show[row_comp][col_comp] = "o"
    return(comp_show)
def winner(win_condition,player_show,comp_show):
    """
    takes 
        win_condition
        player_show
        comp_show
    returns 
        win_condition
    variables
        play_counter = int
        comp_counter = int
        x = int
    play_counter is the amount of hits the player has
    comp_counter is the amount of hits the computer has
    x is just x and is a hit
    """
    print("ok")
    x = "x"
    play_counter = 0
    comp_counter = 0 
    for item in player_show:                                                                #these for loops track the amount of hits the player and computer has
        if item == x:
            play_counter = play_counter + 1
    for item in comp_show:
        if item == x:
            comp_counter = comp_counter + 1 
    if play_counter == 4:                                                                   #sees if the player or computer has sunk all of the ships
        win_condition = 1
    if comp_counter == 4:
        win_condition = 2
    return(win_condition)



def main():
    """
    variables
        player_board
        player_show
        comp_board
        comp_show
        turn
        win_condition
    player_board is the board that the player places their ships on
    player_show is the board that the player sees inbetween turns and tracks their hits and misses
    comp_board is where the computer places its ships
    comp_show is where the computers generated hits and misses are placed
    turn is the amount of plays that have happened in the game
    win_condition is tacking who has won
    """
    player_board = [['A1','A2','A3','A4','A5'],['B1','B2','B3','B4','B5'],['C1','C2','C3','C4','C5'],['D1','D2','D3','D4','D5'],['E1','E2','E3','E4','E5']]
    player_show = [['A1','A2','A3','A4','A5'],['B1','B2','B3','B4','B5'],['C1','C2','C3','C4','C5'],['D1','D2','D3','D4','D5'],['E1','E2','E3','E4','E5']]
    comp_board = [['A1','A2','A3','A4','A5'],['B1','B2','B3','B4','B5'],['C1','C2','C3','C4','C5'],['D1','D2','D3','D4','D5'],['E1','E2','E3','E4','E5']]
    comp_show = [['A1','A2','A3','A4','A5'],['B1','B2','B3','B4','B5'],['C1','C2','C3','C4','C5'],['D1','D2','D3','D4','D5'],['E1','E2','E3','E4','E5']]
    player_board = play_choose(player_board)                                                #all of the boards are above
    comp_board = comp_choice(comp_board)                                                    #these are making the boards
    turn = 0 
    win_condition = 0

    while win_condition == 0:                                                               #before a winner is decided
        if turn == 0 or turn == 2 or turn == 4 or turn == 6 or turn == 8 or turn == 10 or turn == 12 or turn == 14 or turn == 16 or turn == 18:     #even turns are the player odd is the computer
            player_show = user_choice(player_show,comp_board)                               #allows for the user to choose
            turn = turn + 1
        elif turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9 or turn ==11 or turn == 13 or turn == 15 or turn == 17 or turn == 19:
            comp_show = comp_v_user(player_board,comp_show)
            turn = turn + 1
        win_condition = winner(comp_show,player_show,win_condition)
    if win_condition == 1:                                                                  #prints who won
        print("computer won")
    elif win_condition == 2:
        print("you won")





if __name__ == "__main__":
    main()