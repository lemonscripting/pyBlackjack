#known bugs
#exception case handling
#error handling

import random

cards = [
    11 ,11, 11, 11, 
    2, 2, 2, 2, 
    3, 3, 3, 3, 
    4, 4, 4, 4, 
    5, 5, 5, 5, 
    6, 6, 6, 6, 
    7, 7, 7, 7, 
    8, 8, 8, 8, 
    9, 9, 9, 9,
    10, 10, 10, 10, 
    10, 10, 10, 10, 
    10, 10, 10, 10, 
    10, 10, 10, 10 
    ] 

playerBalance = 100
break_case = False

dealerPile = []
playerPile = []
dealerDrawed = []
playerDrawed = []

def initPile():
    dealerPile.clear()
    playerPile.clear()
    dealerDrawed.clear()
    playerDrawed.clear()

    for i in range (5):
        temp = cards[random.randint(0,len(cards)-1)] 
        dealerPile.append(temp)
        cards.remove(temp)

    for i in range (5):
        temp = cards[random.randint(0,len(cards)-1)] 
        playerPile.append(temp)
        cards.remove(temp)

def askIfQuit():
    end_choice = input("Do you want to end the game [Y/N]:")
    if end_choice.upper() == "Y":
        quit()
    else:
        global break_case
        break_case = True
        return
    
        #return 
        #quit()

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
    print("\n")

    print("Player Cards:", "\n")
    for item in playerDrawed:
        print(item, end=" ")
    print("\n")

    print("Dealer Cards:", "\n")
    for item in dealerDrawed:
        print(item, end=" ")
    print("\n")

while True:
    initPile()

    #global break_case
    break_case = False # this is the biggest scope available so no need to call as global // global only used when modifying

    bet = int(input("Welcome to a game of blackjack. How much do you wish to bet? Your available balance is $" + str(playerBalance) + ": "))
    

    if (bet > playerBalance):
        shortage = bet - playerBalance 
        print("Insufficient amount, please place a smaller bat. You are short of $", shortage)
        continue
        
    if (bet < 0.1):
        print("Invalid amount. Please enter a larger amount.")
        continue
    

    print("Dealer's hand:", "\n", dealerPile[0], "and ", dealerPile[1], "\n")
    dealerDrawed.append(dealerPile[0])
    dealerDrawed.append(dealerPile[1])
    dealerTotal = dealerPile[0] + dealerPile[1]

    print("Player's hand:", "\n", playerPile[0], "and",playerPile[1], "\n")
    playerDrawed.append(playerPile[0])
    playerDrawed.append(playerPile[1])
    playerTotal = playerPile[0] + playerPile[1]

    quit_choice = input("Do you want to quit - returns 50% of bet amount [Y/N]")

    if (quit_choice == "Y"):
        lost = bet/2
        playerBalance = playerBalance - lost
        print("you lost $",lost,". Your balance now is $",playerBalance)
        askIfQuit()
        continue

    else:
        if (break_case == True):
            continue

        print("proceed to hitting / standing")

        if (playerTotal == 21 and dealerTotal == 21):
            print("[PUSH] Your bet has been returned. Your balance is $", playerBalance)
            askIfQuit()
            continue
        if (playerTotal == 21 and dealerTotal != 21):
            winAmt = bet*1.5
            playerBalance = playerBalance + winAmt
            print("[BLACKJACK] Blackjack pays 3 to 2. You won $", winAmt, "Your balance is $", playerBalance)
            askIfQuit()
            continue
        if (playerTotal != 21 and dealerTotal == 21):
            playerBalance = playerBalance - bet
            print("[DEALER BLACKJACK] You lost $", bet, "Your balance is $", playerBalance)
            askIfQuit()
            continue

        for i in range(3):
            if (break_case == True):
                continue
            draw_card = 2

            gameAction = input("do you want to Hit or Stand [H/S]")
            if (gameAction == "H"):
                playerDrawed.append(playerPile[draw_card])
                playerTotal = playerTotal + playerPile[draw_card]
                outputFinal()
                checkBust()
                draw_card += 1
                
            else:
                if (break_case == True):
                    continue

                print("-------------CALCULATING-------------")

                outputFinal()
                if (dealerTotal > playerTotal):
                    playerBalance = playerBalance - bet
                    print("[DEALER WINS] You lost $", bet, "Your balance is $", playerBalance)
                    askIfQuit()
                    continue

                while (dealerTotal < 17):
                    if (break_case == True):
                        continue
                    print("-------------DEALER-DRAWING-CARD-------------")
                    dealerTotal = dealerTotal + dealerPile[draw_card]
                    dealerDrawed.append(dealerPile[draw_card])
                    outputFinal()
                    if (playerTotal != 21 and len(dealerDrawed) == 5 and dealerTotal < 22):
                        playerBalance = playerBalance - bet
                        print("[DEALER REACHED 5 CARDS] You lost $", bet, "Your balance is $", playerBalance)
                        askIfQuit()
                        continue

                    if (dealerTotal > 21):
                        if (break_case == True):
                            continue
                        
                        if 1 in dealerDrawed:
                            dealerTotal - 10
                        else:
                            if (break_case == True):
                                continue
                            playerBalance = playerBalance + bet
                            print("[DEALER BUST] You won $", bet, "Your balance is $", playerBalance)
                            askIfQuit()
                            continue

                print("-------------RESULTS-------------")
                outputFinal()
                if (dealerTotal == playerTotal):
                    playerBalance = playerBalance
                    print("[PUSH] Your bet has been returned. Your balance is $", playerBalance)
                    askIfQuit()
                    continue
                    
                if (dealerTotal > playerTotal):
                    playerBalance = playerBalance - bet
                    print("[DEALER WINS] You lost $", bet, "Your balance is $", playerBalance)
                    askIfQuit()
                    continue
                else:
                    if (break_case == True):
                        continue
                    playerBalance = playerBalance + bet
                    print("[PLAYER WINS] You won $", bet, "Your balance is $", playerBalance)
                    askIfQuit()   
                    continue 
