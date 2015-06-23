"""
It is possible to show that the square root of two can be expressed as 
an infinite continued fraction

radic 2  1  12  12  12     1414213

By expanding this for the first four iterations we get

1  12  32  15
1  12  12  75  14
1  12  12  12  1712  141666
1  12  12  12  12  4129  141379

The next three expansions are 9970 239169 and 577408 but the eighth 
expansion 1393985 is the first example where the number of digits in 
the numerator exceeds the number of digits in the denominator

In the first onethousand expansions how many fractions contain a 
numerator with more digits than denominator
"""

def euler57():
    """
    >>> euler57()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()