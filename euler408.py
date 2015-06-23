"""
Lets call a lattice point <var>x</var> <var>y</var> <i>inadmissible
</i> if <var>x</var> <var>y</var> and <var>x</var>  <var>y</var> are 
all positive perfect squares
For example 9 16 is inadmissible while 0 4 3 1 and 9 4 are not

Consider a path from point <var>x</var><sub>1</sub> <var>y</var><sub>1
</sub> to point <var>x</var><sub>2</sub> <var>y</var><sub>2</sub> 
using only unit steps north or east
Lets call such a path <i>admissible</i> if none of its intermediate 
points are inadmissible

Let P<var>n</var> be the number of admissible paths from 0 0 to <var>n
</var> <var>n</var>
It can be verified that P5  252 P16  596994440 and P1000 mod 1 000 000 
007  341920854

Find P10 000 000 mod 1 000 000 007
"""

def euler408():
    """
    >>> euler408()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()