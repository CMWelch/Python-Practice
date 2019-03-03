import Classes


def wager(player):
    '''
    :param player: Player that is placing the bet
    :return: The bet amount
    '''
    while True:
        try:
            b = int(input("Place a bet: "))
            if b <= player.chips:
                player.bet(b)
                return b
            else:
                print(f"You don't have that many chips. Enter a valid number.\nPlayer chip total is: {player.chips}")
        except:
            print("Please enter a number")


def print_players(player, dealer, num=0):

    '''

    :param player:  Player Object
    :param dealer: Dealer object
    :return: Nothing
    '''
    print(player.__str__())
    print("Player's total is: ", player.total, "\n")
    if num == 1:
        print(dealer.__str__(), "\nUnknown")
    else:
        print(dealer.__str__())
    print("Dealer's total is: ", dealer.total, "\n")
    print("------------------------------------------\n")


def run():
    #This variable initializes player chips and keeps track of chip totals when creating new player objects
    player_chips = 100

    while True:
        print("Welcome to Black Jack: ")
        #Initialize Deck Object
        deck = Classes.Deck()
        deck.shuffle()

        #Initialize Player Objects
        dealer = Classes.Player("Dealer")
        player = Classes.Player("Player", player_chips)

        #Ask user for bet amount
        print("Player Chips: ", player.chips)
        amount = wager(player)

        #Deal Cards
        print("Dealing Cards!\n")
        player.hand(deck.deal())
        dealer.hand(deck.deal())
        player.hand(deck.deal())
        facedown = deck.deal()



        stay = False
        #Hit or Stay for player
        while player.total < 21 and not stay:
            print_players(player, dealer, 1)

            stay = False
            action = input("Would you like to hit or stay? H for hit, S for stay: ").upper()
            print(action)
            while action != "H" and action != "S":
                action = input("Please enter H or S: ").upper()
            if action == "H":
                player.hand(deck.deal())
            elif action == "S":
                stay = True

        #Checks if player busted
        if player.total > 21:
            print("Player Bust, you lose")
        else:
            dealer.hand(facedown)
            print_players(player, dealer)

            if dealer.total > player.total:
                print("Dealer wins")

            #Dealer hits until 21, PUSH, or Bust
            while dealer.total < 21:
                dealer.hand(deck.deal())
                print_players(player, dealer)

                if dealer.total > 21:
                    print("Dealer Bust, YOU WIN!")
                    win = amount + amount
                    player.win(win)
                elif dealer.total == 21 and player.total == 21:
                    print("Both 21, PUSH.")
                elif 21 > dealer.total > player.total:
                    print("Dealer wins")
                    break
                elif dealer.total == 21:
                    print("Dealer 21, dealer wins")

        #Update global player chip variable
        player_chips = player.chips

        #Check game state
        if player.chips == 0:
            print("Out of chips. Game Over!")
            break
        else:
            action = input("Would you like to keep playing? Y or N: ").upper()
            print(action)
            while action != "Y" and action != "N":
                action = input("Please enter Y or N: ").upper()
            if action == "N":
                break


run()
