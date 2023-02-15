"""
Create a program that asks the user for a number and then prints out a list of all the
divisors of that number. (If you don’t know what a divisor is, it is a number that 
divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

"""

num = int(input("Type a number"))
x = []
a = range(1,num+1)

for elem in a:
    if num % elem == 0:
        x.append(elem)
print(x)









"""
NOTES

Creating a list
    - x = range(number1, number2) 
    - the second number is not included in the list 
    
PSEUDO CODE
1. get user to input number 
2. find divisors of that number
3. put those divisors into a list
4. print the list 

"""
