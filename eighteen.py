# Rock, Paper, Scissors:
# Write a program that asks the user to choose Rock, Paper, or Scissors.
# Generate a random choice for the computer.
# Determine the winner based on the game's rules.
# Print the result.

import random
l=["Rock","Paper","Scissors"]
pt = 0
cpt=0
opt = True
while opt:
    a = random.choice(l)
    x=input("Enter Rock, Papar or Scissors: ")
    print(a)
    if x==a:
        print("Draw")
    elif x=="Rock" and a=="Scissors":
        pt+=10
        b = input("Do you wish to continue? y/n")
        if b == "y":
            opt = True
        else:
            opt = False
            print(pt,cpt)
    elif x=="Rock" and a=="Paper":
        cpt+=10
        b= input("Do you wish to continue? y/n")
        if b== "y":
            opt = True
        else:
            opt = False
            print(pt,cpt)
    elif x=="Paper" and a=="Scissors":
        cpt+=10
        b = input("Do you wish to continue? y/n")
        if b == "y":
            opt = True
        else:
            opt = False
            print(pt,cpt)
    elif x=="Paper" and a=="Rock":
        pt+=10
        b = input("Do you wish to continue? y/n")
        if b == "y":
            opt = True
        else:
            opt = False
            print(pt,cpt)
    elif x=="Scissors" and a=="Paper":
        pt+=10
        b = input("Do you wish to continue? y/n")
        if b == "y":
            opt = True
        else:
            opt = False
            print(pt,cpt)
    elif x=="Scissors" and a=="Rock":
        cpt+=10
        b = input("Do you wish to continue? y/n")
        if b == "y":
            opt = True
        else:
            opt = False
            print(pt,cpt)
    else:
        print("Enter from the given 3 output")
