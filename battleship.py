import random
def play_choose(player_board):
    print("rows 1-5 columns 1-5")
    print("place 4 ships")
    ship_numb = 4
    while ship_numb >0:
        print("enter in A-e and 1-5 for cords")
        play_choice = input("what cord do you want")
        if play_choice == "A1" or play_choice == "a1":                              #yeah this whole thing is super inefficent but like I need to do it in a way I understand and can make work
            player_board[0][0] = "v"
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
    return(player_board)
def comp_choice(comp_board):
    times = 4
    while times > 0:
        comp_row = random.randint(0,4)
        comp_col = random.randint(0,4)
        comp_board[comp_row][comp_col] = "v"
        times = times - 1
    print(comp_board)
    return(comp_board)
def user_choice(player_show,comp_board):
    print(player_show)
    print("enter in A-e and 1-5 for cords")
    play_choice = input("what cord do you want")
    if play_choice == "A1" or play_choice == "a1":                              #yeah this whole thing is super inefficent but like I need to do it in a way I understand and can make work
        if comp_board[0][0] == "v":
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
    row_comp = random.randint(0,4)
    col_comp = random.randint(0,4)
    if player_board[row_comp][col_comp] == "v":
        comp_show[row_comp][col_comp] = "x"
    else:
        comp_show[row_comp][col_comp] = "o"
    return(comp_show)
def winner(win_condition,player_show,comp_show):
    print("ok")
    x = "x"
    play_counter = 0
    comp_counter = 0 
    for item in player_show:
        if item == x:
            play_counter = play_counter + 1
    for item in comp_show:
        if item == x:
            comp_counter = comp_counter + 1 
    if play_counter == 4:
        win_condition = 1
    if comp_counter == 4:
        win_condition = 2
    return(win_condition)



def main():
    player_board = [['A1','A2','A3','A4','A5'],['B1','B2','B3','B4','B5'],['C1','C2','C3','C4','C5'],['D1','D2','D3','D4','D5'],['E1','E2','E3','E4','E5']]
    player_show = [['A1','A2','A3','A4','A5'],['B1','B2','B3','B4','B5'],['C1','C2','C3','C4','C5'],['D1','D2','D3','D4','D5'],['E1','E2','E3','E4','E5']]
    comp_board = [['A1','A2','A3','A4','A5'],['B1','B2','B3','B4','B5'],['C1','C2','C3','C4','C5'],['D1','D2','D3','D4','D5'],['E1','E2','E3','E4','E5']]
    comp_show = [['A1','A2','A3','A4','A5'],['B1','B2','B3','B4','B5'],['C1','C2','C3','C4','C5'],['D1','D2','D3','D4','D5'],['E1','E2','E3','E4','E5']]
    player_board = play_choose(player_board)
    comp_board = comp_choice(comp_board)
    turn = 0 
    win_condition = 0

    while win_condition == 0:
        if turn == 0 or turn == 2 or turn == 4 or turn == 6 or turn == 8 or turn == 10:
            player_show = user_choice(player_show,comp_board)
            turn = turn + 1
        elif turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9 or turn ==11:
            comp_show = comp_v_user(player_board,comp_show)
            turn = turn + 1
        win_condition = winner(comp_show,player_show,win_condition)
    if win_condition == 1:
        print("computer won")
    elif win_condition == 2:
        print("you won")





if __name__ == "__main__":
    main()