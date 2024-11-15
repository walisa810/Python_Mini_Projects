#2. Guess the Number(Computer)

import random

def guess(x):
    random_number = random.randint(1,x)
    guess_num = 0
    while(guess_num != random_number):
        guess_num = int(input(f"Guess the number between 1 to {x}: "))
        if( guess_num == random_number):
            print("Yay!!! You are correct")
        else:
            print("Sorry!! Guess Again. ")
            if(guess_num > random_number):
                 print("Too high")
            else:
                print("Too low")

def computer_guess(x):
    low = 1
    high = 2*x
    inp = ""
    while(inp != "C" and low != high):
        guess_num = random.randint(low,high)
        print(f"Is {guess_num} too high(H), too low(L) or correct(C)? ")
        inp = input("Enter the letter : ")
        if( inp != "C"):
            if( inp == "H"):
                 high = guess_num - 1
            else:
                low = guess_num + 1
    print("Yay!!! Computer guess is correct")
x = int(input("Enter upper limit of guess game : "))
computer_guess(x)
