# String Manipulation:
# Write a program that asks the user for a string.
# Print the string in reverse order.
# # Print the string with all vowels removed.

x=input("Enter a string: ")
b=x[::-1]
print(b)
s = ""
for i in x:
    if i in "AEIOUaeiou":
        pass
    else:
        s += i
print(s)
