"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[1:5:4])
#This prints [2]

x = input("type a string: ")
b = []
for elem in x:
   b.append(elem)
print(b)
c = b[::-1]
print(c)
if b == c: 
    print("string is a palindrome")
else:
    print("string is not a palindrome")

"""
NOTES

1. list indexing
- start counting lists from number 0
- use var[] to get the elem of the list
- or use[:] to get a range not including the last elem chosen
    - a[1,2,3,4,5]
    - a[0:3] would give [1,2,3] (easy way to get sublists between two indices)
    - a third number in indexing counts how often you should read from the list
        - [1:5:4] would mean:
            give numbers in list between num1 and num5, starting at num1 and goin up by 4s

PSEUDO CODE
1. ask user for a string
2. convert string into list
3. add string elements to a list
4. check if list reads same forward and backward
5. tell user if palindrome or not 

"""

