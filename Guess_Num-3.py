# Guess the number computer version  
import random

def guess(n):
    randNum = random.randint(1,n)
    guess=0
    
    while guess!= randNum:
        guess=int(input(f"Enter any Number between 1 and {n}: "))
        if guess<randNum :
            print("Sorry!! Your Guess is lil low, try again :)")
            # return guess
        elif guess>randNum :
            print("Sorry!! Your Guess is lil high, try agiain :)")
            # return guess  
    print(f"Yay!! The number {randNum} you guessed or entered is correct :D ")

def comp_guess(x):
    user=int(input(f"Enter a number for computer to guess between 1 and {x} ;) "))
    comp_guess=0
    while comp_guess!=user:
        comp_guess=random.randint(1,x)
        if comp_guess<user :
            print("Sorry!! Your Guess is lil low, try again Computer Mahashye :)")
            print(comp_guess)

        elif comp_guess>user :
            print("Sorry!! Your Guess is lil high, try again Computer Mahashye:)")
            print(comp_guess)
    print(comp_guess)
    print("Yay!! The Computer gussed the right number :D ")          

def computer(h):
    high=h
    low=1
    feedback=''
    # computer=0
    while feedback!='c' : 
        if high!=low :
            cg=random.randint(low,high)
        else:
            cg=high
        feedback=input(f"Please tell the computer whether the guessed number {cg} is High(h), Low(l) or Correct(c): ")
        if feedback == 'h':
            high=cg-1
        elif feedback== 'l':
            low=cg+1

    print(f"Yay!! The computer guessed your number {cg} correctly")

guess(10) #Mode 1  
comp_guess(10) #Mode 2
computer(10) #Mode 3
