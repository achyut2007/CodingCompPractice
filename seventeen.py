# Guessing Game:
# Write a program that asks the user to guess a number between 1 and 100.
# If the user's guess is higher than the number, print "Too high!"
# If the user's guess is lower than the number, print "Too low!"
# If the user's guess is correct, print "Congratulations! You won!"

import random
opt = True
y = random.randint(1,100)
while opt:
    x=int(input("Enter a number: "))
    if x==y:
        print("You won")
        a = input("Do you wish to continue? y/n")
        if a == "y":
            opt = True
        else:
            opt = False
    elif x<y:
        print("Too low")
        a = input("Do you wish to continue? y/n")
        if a == "y":
            opt = True
        else:
            opt = False
    else:
        print("too high")
        a = input("Do you wish to continue? y/n")
        if a == "y":
            opt = True
        else:
            opt = False
    
