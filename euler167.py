"""
For two positive integers a and b the Ulam sequence Uab is defined by 
Uab<sub>1</sub>  a Uab<sub>2</sub>  b and for k  2Uab<sub>k</sub> is 
the smallest integer greater than Uab<sub>k1</sub> which can be 
written in exactly one way as the sum of two distinct previous members 
of Uab

For example the sequence U12 begins with
1 2 3  1  2 4  1  3 6  2  4 8  2  6 11  3  8
5 does not belong to it because 5  1  4  2  3 has two representations 
as the sum of two previous members likewise 7  1  6  3  4

Find sumU22<var>n</var>1<sub><var>k</var></sub> for 2 le <var>n</var> 
le10 where <var>k</var>  10<sup>11</sup>
"""

def euler167():
    """
    >>> euler167()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()