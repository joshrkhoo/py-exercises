"""
1. Create a program that asks the user to enter their name and their age. 

2. Print out a message addressed to them that tells them the year that    
    they will turn 100 years old.

https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
"""
import datetime

name = input("What is your name?")
age = int(input("What is your age?"))

print("I am " + name  + " and i am "  + str(age) + " years old")

years = 100 - age

print ("I will turn 100 in " + str(years) +" years")

today = datetime.date.today()
year = today.year 
print (year)

print ("You will be 100 years old in " + str(years + year))

"""
1. 100 minus age = number of years till they turn 100
2. print variable of number of years
3. get current date
4. add number of years to current date 
5. get that date
"""

"""
What I learnt
    - input() function
    - manipulating strings using the function 'int()'
    - using the function str() 
    - concatenate: combine
    - how to get current date
""" 