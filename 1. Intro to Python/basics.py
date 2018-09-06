# Basics of input() and print function


input()   #Blank input accepts a value
print('Hi')
print ("Hi")

# Assign input to a variable and display

number = input()
print(number)


# Give the user a hint of what to enter

number1 = input("Enter a number: ")
print("User has entered", number1)

# Show syntax error due to a word with ' mark in it such as  can't

"""
print('This statement can't be displayed')

print("This statement can't be displayed")
"""
print('''This statement "can't" be displayed''')

print('This statement can\'t be displayed')

# String literal
print("\n")
print("\\n")

# Print sequence of strings such as letters/punctuation marks/numbers/letters
print("5"*6)

# Separate output using comma delimiter
print(5,6,7)

# Usage of sep to separate the output and end to display to override the new line after a print statement and display something else
print('Hello',30,80.3)

print('Hello',30, 80.3, sep=',')

print('Hello',30, 80.3, sep=',',end="!!")







