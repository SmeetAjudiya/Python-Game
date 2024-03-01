import random
computer = random.randint(1,100)
#print(computer)
status = True
i = 0
print("Guess a number between 1 and 100")
print("You have 10 guesses AVAILABLE !")
#print(i)
while i<10 and status:
    user_choice = int(input("Enter your choice:"))
    if user_choice > computer:
        print("HINT : Guess lower")
        i = i + 1
        print("Guesses left", 10-i)
    elif user_choice < computer:
        print("HINT: Guess Higher")
        i = i + 1
        print("Guesses left", 10-i)
    else:
        print("YOU WON !!")
        status = False
    if i == 10:
        print("Guesses Exhausted, YOU LOST !!!!")