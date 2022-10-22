"""
Python Function to sort a list in a descending order
Args:
    An integer list
returns:
    A List in a sorted and descending order without duplicates
"""


def sort_list_in_desc_order(num_list):
    result_list = []
    range_first, range_last = 1, 100
    # Check given list is in range
    status = all(range_first <= n < range_last for n in num_list)

    # raise an exception if not in range
    if status is False:
        raise Exception('Given list is not in the expected range(1,100)')

    [result_list.append(num) for num in num_list if num not in result_list]
    return sorted(result_list, reverse=True)


# Driver Code

# List with in range
num_list_in_range = [90, 99, 55, 66, 97, 55, 66, 88, 99, 2]
print(sort_list_in_desc_order(num_list_in_range))

# List with elements not in range
num_list_not_range = [101, 99, 55, 66, 97, 55, 66, 88, 99, 2]
print(sort_list_in_desc_order(num_list_not_range))
