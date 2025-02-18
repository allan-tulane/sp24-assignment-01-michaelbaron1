"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x - 1)
        rb = foo(x - 2)
        return ra + rb


def longest_run(mylist, key):
    count = 0
    largest_count = 0
    for i in range(len(mylist)):
        if mylist[i] == key:
            count += 1
        else:
            if count > largest_count:
                largest_count = count
            count = 0
    if count > largest_count:
        largest_count = count
    return largest_count



class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        

def longest_run_recursive(mylist, key):
    ### TODO
    if len(mylist) == 0:
        return Result(0, 0, 0, True)
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    mid = len(mylist) // 2
    left_result = longest_run_recursive(mylist[:mid], key)
    right_result = longest_run_recursive(mylist[mid:], key)

    if left_result.is_entire_range:
        updated_left_size = left_result.left_size + right_result.left_size
    else:
        updated_left_size = left_result.left_size

    if right_result.is_entire_range:
        updated_right_size = right_result.right_size + left_result.right_size
    else:
        updated_right_size = right_result.right_size

    if mylist[mid] == key and mylist[mid - 1] == key:
        middle_run = left_result.right_size + right_result.left_size

    else:
        middle_run = 0

    new_longest_size = max(left_result.longest_size, right_result.longest_size, middle_run)

    new_is_entire_range = left_result.is_entire_range and right_result.is_entire_range

    return Result(updated_left_size, updated_right_size, new_longest_size, new_is_entire_range)




