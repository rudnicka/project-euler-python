"""
A natural number N that can be written as the sum and product of a 
given set of at least two natural numbers <i>a</i><sub>1</sub> <i>a
</i><sub>2</sub>   <i>a</i><sub><i>k</i></sub> is called a productsum 
number N  <i>a</i><sub>1</sub>  <i>a</i><sub>2</sub>    <i>a</i><sub>
<i>k</i></sub>  <i>a</i><sub>1</sub> times <i>a</i><sub>2</sub> times  
times <i>a</i><sub><i>k</i></sub>

For example 6  1  2  3  1 times 2 times 3

For a given set of size <i>k</i> we shall call the smallest N with 
this property a minimal productsum number The minimal productsum 
numbers for sets of size <i>k</i>  2 3 4 5 and 6 are as follows

<i>k</i>2 4  2 times 2  2  2
<i>k</i>3 6  1 times 2 times 3  1  2  3
<i>k</i>4 8  1 times 1 times 2 times 4  1  1  2  4
<i>k</i>5 8  1 times 1 times 2 times 2 times 2   1  1  2  2  2
<i>k</i>6 12  1 times 1 times 1 times 1 times 2 times 6  1  1  1  1  2  
6

Hence for 2le<i>k</i>le6 the sum of all the minimal productsum numbers 
is 46812  30 note that 8 is only counted once in the sum

In fact as the complete set of minimal productsum numbers for 2le<i>k
</i>le12 is 4 6 8 12 15 16 the sum is 61

What is the sum of all the minimal productsum numbers for 2le<i>k</i>
le12000
"""

def euler88():
    """
    >>> euler88()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()