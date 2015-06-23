"""
An integer is called <strong><var>B</var>smooth</strong> if none of 
its prime factors is greater than <var>B</var>

Let S<sub><var>B</var></sub><var>n</var> be the largest <var>B</var>
smooth divisor of <var>n</var>
Examples
S<sub>1</sub>10  1
S<sub>4</sub>2100  12
S<sub>17</sub>2496144  5712

Define F<var>n</var>  sum<sub>1le<var>B</var>le<var>n</var></sub> sum
<sub>0le<var>r</var>le<var>n</var></sub> S<sub><var>B</var></sub>C
<var>n</var><var>r</var> Here C<var>n</var><var>r</var> denotes the 
binomial coefficient
Examples
F11  3132
F1 111 mod 1 000 000 993  706036312
F111 111 mod 1 000 000 993  22156169

Find F11 111 111 mod 1 000 000 993
"""

def euler468():
    """
    >>> euler468()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()