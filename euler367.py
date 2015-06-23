"""
<b>Bozo sort</b> not to be confused with the slightly less efficient 
<b>bogo sort</b> consists out of checking if the input sequence is 
sorted and if not swapping randomly two elements This is repeated 
until eventually the sequence is sorted

If we consider all permutations of the first 4 natural numbers as 
input the expectation value of the number of swaps averaged over all 4 
input sequences is 2475
The already sorted sequence takes 0 steps 

In this problem we consider the following variant on bozo sort
If the sequence is not in order we pick three elements at random and 
shuffle these three elements randomly
All 36 permutations of those three elements are equally likely 
The already sorted sequence will take 0 steps
If we consider all permutations of the first 4 natural numbers as 
input the expectation value of the number of shuffles averaged over 
all 4 input sequences is 275 
Consider as input sequences the permutations of the first 11 natural 
numbers
Averaged over all 11 input sequences what is the expected number of 
shuffles this sorting algorithm will perform

Give your answer rounded to the nearest integer
"""

def euler367():
    """
    >>> euler367()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()