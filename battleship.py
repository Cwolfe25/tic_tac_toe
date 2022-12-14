import random
def play_choose(player_board):
    print("rows 1-5 columns 1-5")
    print("place 4 ships")
    ship_numb = 4
    while ship_numb >0:
        play_row1 = input("which rown do you want for your first peice")
        play_row1 = int(play_row1)
        play_row1 == play_row1 -1 
        play_column1 = input("which column do you want")
        play_column1 = int(play_column1)
        play_column1 == play_column1 -1 
        player_board[play_row1,play_column1] == "v"
        ship_numb == ship_numb - 1
    return(player_board)
def comp_choice(comp_board):
    times = 4
    while times > 0:
        comp_row = random.randint(0,4)
        comp_col = random.randint(0,4)
        comp_board[comp_row][comp_col] = "v"
        times == times - 1
    return(comp_board)
def user_choice(player_show,comp_board,user_check):
    print(player_show)
    print("enter 1 - 5 ")
    user_row = input("what row do you chose?")
    user_col = input("what column do you chose?")
    user_row == user_row - 1
    user_col == user_col - 1 
    if comp_board[user_row][user_col] == "v":
        player_show[user_row][user_col] = "x"
        user_check == user_check + 1
    else:
        player_show[user_row][user_col] = "o"
    print(player_show)
    return(player_show,user_check)
def comp_v_user(player_board,comp_show,comp_check):
    row_comp = random.randint(0,4)
    col_comp = random.randint(0,4)
    if player_board[row_comp][col_comp] == "v":
        comp_show[row_comp][col_comp] == "x"
        comp_check == comp_check + 1
    else:
        comp_show[row_comp][col_comp]
    return(comp_show,comp_check)
def winner(comp_show,player_show,win_condition,player_check,comp_check):
    print("ok")
    comp_counter = 0 
    play_counter = 0 
    if player_check == 4:
        win_condition = 1
    if comp_check == 4:
        win_condition = 2
    else:
        win_coundition = 0 
    return(win_condition)



def main():
    player_board = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
    player_show = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
    comp_board = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
    comp_show = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
    player_board = play_choose(player_board)
    comp_board = comp_choice(comp_board)
    turn = 0 
    win_condition = 0
    user_check = 0 
    comp_check = 0
    while win_condition == 0:
        if turn == 0 or turn == 2 or turn == 4 or turn == 6 or turn == 8 or turn == 10:
            temp_show = user_choice(player_show,comp_board,user_check)
            temp_show = temp_show.split(",")
            player_show = temp_show[0]
            user_check = temp_show[1]
        elif turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9 or turn ==11:
            temp_show = comp_v_user(player_board,comp_show,comp_check)
            temp_show = temp_show.split(",")
            comp_show = temp_show[0]
            comp_check = temp_show[1]
        win_condition = winner(comp_show,player_show,win_condition)
        turn == turn + 1
    if win_condition == 1:
        print("computer won")
    elif win_condition == 2:
        print("you won")





if __name__ == "__main__":
    main()