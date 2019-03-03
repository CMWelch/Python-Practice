from IPython.display import clear_output


def print_board(num=0, char="   ",  moves=[["{1}", "{2}", "{3}"], ["{4}", "{5}", "{6}"], ["{7}", "{8}", "{9}"]]):

    board_dict = {"h_line": "- - - - - - - - - - - - - - - - -", "v_space": "\n", "v_line": "          |           |   ", "h_space": "    "}
    #moves = [["{1}", "{2}", "{3}"], ["{4}", "{5}", "{6}"], ["{7}", "{8}", "{9}"]]
    #"--------------------------------"

    if num == 1:
        moves[0][0] = char
    if num == 2:
        moves[0][1] = char
    if num == 3:
        moves[0][2] = char
    if num == 4:
        moves[1][0] = char
    if num == 5:
        moves[1][1] = char
    if num == 6:
        moves[1][2] = char
    if num == 7:
        moves[2][0] = char
    if num == 8:
        moves[2][1] = char
    if num == 9:
        moves[2][2] = char

    print(board_dict["v_line"])
    print(f"  ", moves[0][0], "  ", "|   ", moves[0][1], "   |", "  ", moves[0][2], " ")
    print(board_dict["v_line"])
    print(board_dict["h_line"])
    print(board_dict["v_line"])
    print(f"  ", moves[1][0], "  ", "|   ", moves[1][1], "   |", "  ", moves[1][2], " ")
    print(board_dict["v_line"])
    print(board_dict["h_line"])
    print(board_dict["v_line"])
    print(f"  ", moves[2][0], "  ", "|   ", moves[2][1], "   |", "  ", moves[2][2], " ")
    print(board_dict["v_line"], "\n")

    return moves


def check_win(board):

    #Horizontal Wins
    if board[0][0] == board[0][1] == board[0][2]:
        return True
    elif board[1][0] == board[1][1] == board[1][2]:
        return True
    elif board[2][0] == board[2][1] == board[2][2]:
        return True

    #Veritcal Wins
    elif board[0][0] == board[1][0] == board[2][0]:
        return True
    elif board[0][1] == board[1][1] == board[2][1]:
        return True
    elif board[0][2] == board[1][2] == board[2][2]:
        return True

    #Diagonal Wins
    elif board[0][0] == board[1][1] == board[2][2]:
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        return True

    #No wins
    else:
        return False



def run():
    play = True
    moves = [["{1}", "{2}", "{3}"], ["{4}", "{5}", "{6}"], ["{7}", "{8}", "{9}"]]
    played = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_plays = 0

    while True:
        while num_plays < 9:

            # Start Game
            print("Player 1 is X's. Player 2 is O's.\n")
            moves = print_board(0, "   ", moves)

            #Player 1 Input
            p1 = int(input("Player 1, input a number where you would like to make a play: "))

            #Check if legal move
            if p1 in played:
                played.remove(p1)
            else:
                invalid = True
                while invalid:
                    p1 = int(input("This is not a legal move. Choose a valid play: \n"))
                    if p1 in played:
                        invalid = False
                        played.remove(p1)

            moves = print_board(p1, " X ", moves)
            num_plays += 1



            #Check if player has won or drawn
            if check_win(moves):
                print("Player 1 wins!\n")
                break
            if num_plays == 9:
                print("It's a draw! \n")
                break
                
            #Player 2 Input
            p2 = int(input("Player 2, Input a number where you would like to make a play: "))
            # Check if legal move
            if p2 in played:
                played.remove(p2)
            else:
                invalid = True
                while invalid:
                    p2 = int(input("This is not a legal move. Choose a valid play: \n"))
                    if p2 in played:
                        invalid = False
                        played.remove(p2)

            moves = print_board(p2, " O ", moves)
            num_plays += 1

            #Check if player has won
            if check_win(moves):
                print("Player 2 wins!\n")
                break

        x = input("Would you like to play again? Y or N: \n")
        if x.lower() == "n":
            print("Thank you for playing!")
            break

run()