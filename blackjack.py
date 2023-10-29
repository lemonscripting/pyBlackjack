#known bugs:
#N case for quitting not working

#dependencies
import random

#init the list of cards that will be used in the game
cards = [
    11 ,11, 11, 11, #represent ace, a logic is needed to determine if it is consided 1 or 11 //if exceed 21 and have ace then -10
    2, 2, 2, 2, 
    3, 3, 3, 3, 
    4, 4, 4, 4, 
    5, 5, 5, 5, 
    6, 6, 6, 6, 
    7, 7, 7, 7, 
    8, 8, 8, 8, 
    9, 9, 9, 9,
    10, 10, 10, 10, #normal 10
    10, 10, 10, 10, #jack
    10, 10, 10, 10, #queen
    10, 10, 10, 10 #king
    ] 

#52 cards in this deck
#what we want to do is to use random.randint with a range of 1 to 52 to pick out the cards
#the cards picked out will be removed from the array

#init card pile of player and dealer
dealerPile = []
playerPile = []

dealerDrawed = []
playerDrawed = []
#output cards
'''
print("Player Cards:", "\n")
for item in dealerDrawed:
    print(item, end=" ")
print("\n")

playerDrawed.append()
'''
for i in range (5):
    temp = cards[random.randint(0,len(cards)-1)] #array is 0 indexed
    dealerPile.append(temp)
    cards.remove(temp)

#prints the pile of cards the dealer is taking [for debugging usage]
for item in dealerPile:
    print(item, end=" ")
print("\n")

for i in range (5):
    temp = cards[random.randint(0,len(cards)-1)] #array is 0 indexed
    playerPile.append(temp)
    cards.remove(temp)

#prints the pile of cards the dealer is taking [for debugging usage]
for item in playerPile:
    print(item, end=" ")
print("\n")

playerBalance = 100

def askIfQuit():
    end_choice = input("Do you want to end the game [Y/N]: ")
    if end_choice.upper() == "Y":
        quit()
    else:
        quit()
        #return

def checkBust():
    if (playerTotal > 21):
        if 1 in playerDrawed:
            playerTotal - 10
        else:
            global playerBalance
            playerBalance = playerBalance - bet
            
            print("[BUST] You lost $", bet, "Your balance is $", playerBalance)
            askIfQuit()

def outputFinal():
    #output player cards
    print("Player Cards:", "\n")
    for item in playerDrawed:
        print(item, end=" ")
    print("\n")

    #output dealer cards
    print("Dealer Cards:", "\n")
    for item in dealerDrawed:
        print(item, end=" ")
    print("\n")

while True:

    bet = int(input("Welcome to a game of blackjack. How much do you wish to bet? Your available balance is $" + str(playerBalance) + ": "))

    if (bet > playerBalance):
        shortage = bet - playerBalance 
        print("insufficient amount, please place a smaller bat. You are short of $", shortage)

    else:
        #main loop
        global loop_count
        loop_count = 0

        print("Dealer's hand:", "\n", dealerPile[loop_count], "and ", dealerPile[loop_count+1], "\n")
        dealerDrawed.append(dealerPile[loop_count])
        dealerDrawed.append(dealerPile[loop_count+1])
        dealerTotal = dealerPile[loop_count] + dealerPile[loop_count+1]
        print("dealer total = ", dealerTotal)

        print("Player's hand:", "\n", playerPile[loop_count], "and",playerPile[loop_count+1], "\n")
        playerDrawed.append(playerPile[loop_count])
        playerDrawed.append(playerPile[loop_count+1])
        playerTotal = playerPile[loop_count] + playerPile[loop_count+1]
        print("player total = ", playerTotal)

        quit_choice = input("Do you want to quit [Y/N]")

        if (quit_choice == "Y"):
            lost = bet/2
            playerBalance = playerBalance - lost
            print("you lost $",lost,". Your balance now is $",playerBalance)
            #end_choice = input("Do you want to end the game [Y/N]")
            askIfQuit()

        else:
            print("proceed to hitting / standing")
            #blackjack cases

            if (playerTotal == 21 and dealerTotal == 21):
                print("[PUSH] Your bet has been returned. Your balance is $", playerBalance)
                askIfQuit()
                continue #patch for incapability of using "continue in functions"
            if (playerTotal == 21 and dealerTotal != 21):
                winAmt = bet*1.5
                playerBalance = playerBalance + winAmt
                print("[BLACKJACK] Blackjack pays 3 to 2. You won $", winAmt, "Your balance is $", playerBalance)
                askIfQuit()
                continue #patch for incapability of using "continue in functions"
            if (playerTotal != 21 and dealerTotal == 21):
                playerBalance = playerBalance - bet
                print("[DEALER BLACKJACK] You lost $", bet, "Your balance is $", playerBalance)
                askIfQuit()
                continue #patch for incapability of using "continue in functions"
            #hitting/standing for non-blackjack cases

            for i in range(3):
                draw_card = 2

                gameAction = input("do you want to Hit or Stand [H/S]")
                if (gameAction == "H"):
                    playerDrawed.append(playerPile[draw_card])
                    playerTotal = playerTotal + playerPile[draw_card]
                    outputFinal()
                    '''
                    print("Player Cards:", "\n")
                    for item in playerDrawed:
                         print(item, end=" ")
                    print("\n")
                    '''
                    checkBust()
                    draw_card += 1
                else:
                    print("-------------CALCULATING-------------")

                    outputFinal()
                    if (dealerTotal > playerTotal):
                        playerBalance = playerBalance - bet
                        print("[DEALER WINS] You lost $", bet, "Your balance is $", playerBalance)
                        askIfQuit()

                    while (dealerTotal < 17):
                        print("-------------DEALER-DRAWING-CARD-------------")
                        dealerTotal = dealerTotal + dealerPile[draw_card]
                        dealerDrawed.append(dealerPile[draw_card])
                        outputFinal()
                        if (playerTotal != 21 and len(dealerDrawed) == 5):
                            playerBalance = playerBalance - bet
                            print("[DEALER REACHED 5 CARDS] You lost $", bet, "Your balance is $", playerBalance)
                            askIfQuit()
                        if (dealerTotal > 21):
                            if 1 in dealerDrawed:
                                dealerTotal - 10
                            else:
                                playerBalance = playerBalance + bet
                                print("[DEALER BUST] You won $", bet, "Your balance is $", playerBalance)
                                askIfQuit()
                    print("-------------RESULTS-------------")
                    outputFinal()
                    if (dealerTotal > playerTotal):
                        playerBalance = playerBalance - bet
                        print("[DEALER WINS] You lost $", bet, "Your balance is $", playerBalance)
                        askIfQuit()
                    else:
                        playerBalance = playerBalance + bet
                        print("[PLAYER WINS] You won $", bet, "Your balance is $", playerBalance)
                        askIfQuit()    
