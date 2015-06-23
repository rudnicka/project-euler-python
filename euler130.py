"""
A number consisting entirely of ones is called a repunit We shall 
define R<i>k</i> to be a repunit of length <i>k</i> for example R6  
111111

Given that <i>n</i> is a positive integer and GCD<i>n</i> 10  1 it can 
be shown that there always exists a value <i>k</i> for which R<i>k</i> 
is divisible by <i>n</i> and let A<i>n</i> be the least such value of 
<i>k</i> for example A7  6 and A41  5

You are given that for all primes <i>p</i> gt 5 that <i>p</i> minus 1 
is divisible by A<i>p</i> For example when <i>p</i>  41 A41  5 and 40 
is divisible by 5

However there are rare composite values for which this is also true 
the first five examples being 91 259 451 481 and 703

Find the sum of the first twentyfive composite values of <i>n</i> for 
which
GCD<i>n</i> 10  1 and <i>n</i> minus 1 is divisible by A<i>n</i>
"""

def euler130():
    """
    >>> euler130()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()