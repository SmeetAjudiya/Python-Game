import random
computer = random.randint(1,100)
#print(computer)

status = True
while status:
    user_choice = int(input("Enter your choice:"))
    if user_choice > computer:
        print("HINT : Guess lower")
    elif user_choice < computer:
        print("HINT: Guess Higher")
    else:
        print("YOU WON !!")
        status = False