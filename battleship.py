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
def user_choice(player_show,comp_board):
    print(player_show)
    print("enter 1 - 5 ")
    user_row = input("what row do you chose?")
    user_col = input("what column do you chose?")
    user_row == user_row - 1
    user_col == user_col - 1 
    if comp_board[user_row][user_col] == "v":
        player_show[user_row][user_col] = "x"
    else:
        player_show[user_row][user_col] = "o"
    print(player_show)
    return(player_show,comp_show)
def comp_v_user(player_board):
    row_comp = random.randint(0,4)
    col_comp = random.randint(0,4)
    if player_board[row_comp][col_comp] == "v":


def main():
    player_board = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
    player_show = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
    comp_board = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
    comp_show = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
    player_board = play_choose(player_board)
    comp_board = comp_choice(comp_board)
    turn = 0 
    win_condition = 0
    while win_condition == 0:
        if turn == 0 or turn == 2 or turn == 4 or turn == 6 or turn == 8 or turn == 10:
            player_choice = user_choice(player_show,comp_board)
        turn == turn + 1





if __name__ == "__main__":
    main()