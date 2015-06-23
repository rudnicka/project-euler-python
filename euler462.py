"""
A <b>3smooth number</b> is an integer which has no prime factor larger 
than 3 For an integer <var>N</var> we define S<var>N</var> as the set 
of 3smooth numbers less than or equal to <var>N</var>  For example S20   
1 2 3 4 6 8 9 12 16 18 

We define F<var>N</var> as the number of permutations of S<var>N</var> 
in which each element comes after all of its proper divisors

This is one of the possible permutations for <var>N</var>  20
 1 2 4 3 9 8 16 6 18 12
This is not a valid permutation because 12 comes before its divisor 6
 1 2 4 3 9 8 <b>12</b> 16 <b>6</b> 18

We can verify that F6  5 F8  9 F20  450 and F1000 asymp 88521816557e21
Find F10<sup>18</sup> Give as your answer its scientific notation 
rounded to ten digits after the decimal point
When giving your answer use a lowercase e to separate mantissa and 
exponent Eg if the answer is 112233445566778899 then the answer format 
would be 11223344557e17
"""

def euler462():
    """
    >>> euler462()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()