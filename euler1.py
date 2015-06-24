"""
If we list all the natural numbers below 10 that are multiples of 3 or 
5 we get 3 5 6 and 9 The sum of these multiples is 23

Find the sum of all the multiples of 3 or 5 below 1000
"""

def euler1(n):
    """
    >>> euler1(10)
    23
    """
    return sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0)

if __name__ == "__main__":
    print euler1(10)
    print euler1(1000)
    import doctest
    doctest.testmod()