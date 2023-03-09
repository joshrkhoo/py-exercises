"""
Given a list, return the number of numbers smaller than x

Example:

number_of_numbers_smaller_than_x([1, 2, 3, 10], 5) -> 3
1, 2 and 3 are smaller than 5
10 is not smaller than 5
Therefore, there are 3 numbers smaller than 5

Can you do this without creating another list?

Hint: can you simply keep track of the count as you go?
"""

def number_of_numbers_smaller_than_x(numbers: list[int], x: int) -> int:
    """
    get list of numbers
    what is x?
    check if numbers in list are smaller than x 
        if they are append them to another list
            print that list

    # List for numbers smaller than x (where they will be appended to)
    num_smaller_than_x = []
    # for index values in numbers do something...
    for i in range(len(numbers)):
    # if numbers corresponding to each index value are smaller than x...    
        if numbers[i] < x:
    # Append numbers smaller than x to list created above
            num_smaller_than_x.append(numbers[i])
    # return the length of the list of numbers smaller than x
    return len(num_smaller_than_x)
"""
    #initial value of count is assigned 0
    count = 0 
    # for index values in range of length of list 'numbers' do something... 
    for i in range(len(numbers)):
    # iterates through each index number at each index value and checks if they are
    # smaller than x
        if numbers[i] < x:
    # count adds 1 each time a number is smaller than x
            count += 1
    return count

"""
count of numbers smaller than x = 0 (initial val)
    iterate through list 
        check each number against x 
            if number in list is smaller than x
                increase the count by 1 for each number 
"""


if __name__ == "__main__":
    list1 = [1, 2, 3, 10]
    x = 5
    answer = 3
    output = number_of_numbers_smaller_than_x(list1, x)
    print(list1, x, output)
    assert answer == output, "answer does not equal output"

