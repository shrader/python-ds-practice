import math

def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    curr_num = 1

    small_factors = []
    large_factors = []


    while curr_num <= math.sqrt(num):
        if num % curr_num == 0:
            small_factors.append(curr_num)
            large_factors.append(num//curr_num)
        curr_num += 1
    
    return small_factors + large_factors[::-1]



