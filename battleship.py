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


def main():
    player_board = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
    player_show = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
    comp_board = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
    player_board = play_choose(player_board)




if __name__ == "__main__":
    main()