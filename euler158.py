"""
Taking three different letters from the 26 letters of the alphabet 
character strings of length three can be formed
Examples are abc hat and zyx
When we study these three examples we see that for abc two characters 
come lexicographically after its neighbour to the left
 For hat there is exactly one character that comes lexicographically 
after its neighbour to the left For zyx there are zero characters that 
come lexicographically after its neighbour to the left
In all there are 10400 strings of length 3 for which exactly one 
character comes lexicographically after its neighbour to the left

We now consider strings of <var>n</var> le 26 different characters 
from the alphabet
 For every <var>n</var> p<var>n</var> is the number of strings of 
length <var>n</var> for which exactly one character comes 
lexicographically after its neighbour to the left 

What is the maximum value of p<var>n</var>
"""

def euler158():
    """
    >>> euler158()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()