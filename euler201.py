"""
For any set A of numbers let sumA be the sum of the elements of A
Consider the set B  13681011
 There are 20 subsets of B containing three elements and their sums 
are

sum136  10
sum138  12
sum1310  14
sum1311  15
sum168  15
sum1610  17
sum1611  18
sum1810  19
sum1811  20
sum11011  22
sum368  17
sum3610  19
sum3611  20
sum3810  21
sum3811  22
sum31011  24
sum6810  24
sum6811  25
sum61011  27
sum81011  29

Some of these sums occur more than once others are unique
For a set A let UAk be the set of unique sums of kelement subsets of A 
in our example we find UB3  1012141821252729 and sumUB3  156

Now consider the 100element set S  1<sup>2</sup> 2<sup>2</sup>   100
<sup>2</sup>
S has 100891344545564193334812497256 50element subsets

Determine the sum of all integers which are the sum of exactly one of 
the 50element subsets of S ie find sumUS50
"""

def euler201():
    """
    >>> euler201()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()