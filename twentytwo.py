# Hangman Game:
# Write a program that asks the user to guess a word by suggesting letters.
# For each incorrect guess, draw a part of a hangman's gallows.
# If the user guesses the word correctly, print a congratulatory message.

a="Belt"
p = "The word consists of 4 letters"
opt = True
won = False
while opt:
    for i in a:
        x=input("Enter a word:")
        if x==a:
            won=True
            break
        else:
            print(i)                            
    if a == 'y':
        continue
    else:
        opt = False