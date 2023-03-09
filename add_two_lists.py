"""
Given two lists of equal length, add corresponding numbers together into a new list

Example:

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

answer_list = [6, 6, 6, 6, 6]

explanation: [1+5, 2+4...]
"""

def add_two_lists(list1: list[int], list2: list[int]) -> list[int]:
    """
    list3 = adding the lists together
    get corresponding index values of list1 and list2 and add them together
        once added append them to list3
    """
    list3 = []
    # index values in range of list1 do...
    for i in range(len(list1)):
    # a is assigned to the addition of list1 and list2 
        a = i + i
    #append values of a to list3
        list3.append(a)
    return list3


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 4, 3, 2, 1]
    answer_list = [6, 6, 6, 6, 6]
    output = add_two_lists(list1, list2)
    print(list1, list2, output)
    assert len(list1) == len(output), "list lengths must be the same"
    for i in range(len(output)):
        assert answer_list[i] == output[i], "wrong answer"

