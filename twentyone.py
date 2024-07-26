# Quiz Program:
# Write a program that asks the user 5 trivia questions.
# Keep track of the user's score.
# Print the final score and a message based on the score.

print("Welcome to our quiz")
a1 = "Ques 1\nCapital of Nepal"
print(a1)
b = input("Enter your answer: ").capitalize()
if b == "Kathmandu":
    print("your answer is correct")
else:
    print("get better")