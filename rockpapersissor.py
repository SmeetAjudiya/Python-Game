import random
#game_list = ['r','p','s']
#computer = random.choice(game_list)
while True :
    user = input("Enter your choice r,p or s (Input anything else to end):")
    game_list = ['r','p','s']
    computer = random.choice(game_list)
    print(computer)
    if user == computer:
        print("TIE")
    elif user == 'r' and computer == 's':
        print("USER WON")
    elif user == 'r' and computer == 'p':
        print("COMPUTER WON")
    elif user == 'p' and computer == 's':
        print("COMPUTER WON")
    elif user == 'p' and computer == 'r':
        print("USER WON")
    elif user == 's' and computer == 'r':
        print("COMOUTER WON")
    elif user == 's' and computer == 'p':
        print("USER WON")
    else:
        print("GAME ENDS")
        break
