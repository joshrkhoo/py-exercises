"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Write a program that returns a list that contains only the elements that are common
between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

x = []

for elem in a:
    if elem in b: 
       x.append(elem)
print(list((dict.fromkeys(x))))










"""
NOTES
- dict.fromkeys()
    - dict creates a dictionary, there cannot be duplicates in a dict
    - fromkeys() 
        - function
        - returns a dictionary with the specified keys and value





PSEUDO CODE
1. create a list for common elems
2. find elems that are common between a and b
3. do not include duplicates
4. print list


"""
