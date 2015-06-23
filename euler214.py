"""
Let phi be Eulers totient function ie for a natural number <var>n
</var>phi<var>n</var> is the number of <var>k</var> 1 le <var>k</var> 
le <var>n</var> for which gcd<var>k</var><var>n</var>  1

By iterating phi each positive integer generates a decreasing chain of 
numbers ending in 1
Eg if we start with 5 the sequence 5421 is generated
Here is a listing of all chains with length 4
<div style="text-align:right; margin-right:350px;">5421
7621
8421
9621
10421
12421
14621
18621
"""

def euler214():
    """
    >>> euler214()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()