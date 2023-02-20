"""
Exercise 2 

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""
number = int(input("give me a number "))
if number % 2 != 0: #number is odd
    print("The number you chose is odd")
elif number % 4 == 0: #number is divisible by 4
    print ("Your number is a multiple of 4")
else: #number is even
    print("The number you chose is even")

num1 = int(input("Give me a number, this will be divided by divisor "))
divisor = int((input("Give me a number. This will act as your divisor ")))

if num1 % divisor == 0:
    print("your divisor divides evenly into num1")
else:
    print("There is a remainder when your number is divided by divisor")



"""
NOTES FOR THE EXERCISE

modulus operator 
- % 
- gives us the remainder when dividing a number by another number
- "5 modulo 3 is 2"

conditionals
- when a program needs to decide something, it checks whether some condition is satisfied
- "if statements"

"""
