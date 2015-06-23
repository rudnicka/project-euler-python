"""
Let SA represent the sum of elements in set A of size <i>n</i> We 
shall call it a special sum set if for any two nonempty disjoint 
subsets B and C the following properties are true
<ol style="list-style-type:lower-roman;"><li>SB ne SC that is sums of 
subsets cannot be equal</li><li>If B contains more elements than C 
then SB gt SC</li></ol>

For this problem we shall assume that a given set contains <i>n</i> 
strictly increasing elements and it already satisfies the second rule

Surprisingly out of the 25 possible subset pairs that can be obtained 
from a set for which <i>n</i>  4 only 1 of these pairs need to be 
tested for equality first rule Similarly when <i>n</i>  7 only 70 out 
of the 966 subset pairs need to be tested

For <i>n</i>  12 how many of the 261625 subset pairs that can be 
obtained need to be tested for equality

NOTE This problem is related to <a href="problem=103">Problem 103</a> 
and <a href="problem=105">Problem 105</a>
"""

def euler106():
    """
    >>> euler106()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()