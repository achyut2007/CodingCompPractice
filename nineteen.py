# Grade Calculator:
# Write a program that asks the user for their marks in three subjects.
# Calculate the average marks.
# Print the grade based on the average marks (e.g., A, B, C, etc.).

a=int(input("Enter your marks for English: "))
b=int(input("Enter your marks for Maths: "))
c=int(input("Enter your marks for Science: "))
d=((a+b+c)/300)*100
if d>=80:
    print("A Grade")
elif d<80 and d>=60:
    print("B Grade")
elif d<60 and d>=30:
    print("C Grade, get better")
else:
    print("padh le bsdk")

