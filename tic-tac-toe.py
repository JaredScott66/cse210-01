


def board_update(player_input, player):
    grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]   
    
    for i in range(len(grid)):
        if i == str(player_input):
            grid[i] = "X"
               

            #result = print(grid[0] + "|" + grid[1] + "|" + grid[2]), print(grid[3] + "|" + grid[4] + "|" + grid[5]), print(grid[6] + "|" + grid[7] + "|" + grid[8])
        return grid




def main():
    side = "x"
    player = input("Give ")
    board = board_update(player, side)
    print(board)
if __name__ == "__main__":
    main()