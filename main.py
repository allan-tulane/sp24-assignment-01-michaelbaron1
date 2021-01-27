"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    ###

def longest_run(mylist, key):
    ### TODO

    ###


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
    

def longest_run_recursive(mylist, key):    
    ### TODO
    ###

def _longest_run_recursive(mylist, key):
    # returns Result object
    if len(mylist) == 1:
        if mylist[0] == key:            
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    
    # each thread spawns more threads
    result1 = _longest_run_recursive(mylist[:len(mylist)//2], key)
    result2 = _longest_run_recursive(mylist[len(mylist)//2:], key)
    return combine_results(result1, result2)
    ###

def combine_results(result1, result2):
###TODO
###

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

def test_longest_run_recursive():
    assert longest_run_recursive([6,12,12,6], 12).longest_size == 2
    assert longest_run_recursive([12,12,12,6], 12).longest_size == 3
    assert longest_run_recursive([6,12,12,12], 12).longest_size == 3
    assert longest_run_recursive([12,6,6,6], 12).longest_size == 1
    assert longest_run_recursive([12,6,6,12], 12).longest_size == 1
    assert longest_run_recursive([12,12,12,12], 12).longest_size == 4

def test_longest_run_recursive_hard():
    """
    This is a hard corner case that requires left_size and
    right_size to be calculated correctly when only one half 
    has is_entire_range==True.

    [6 12] [12 12] [12 6] [6 6]
    """
    assert longest_run_recursive([6, 12, 12, 12, 12, 6, 6, 6], 12).longest_size == 4



