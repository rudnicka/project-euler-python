"""
Let <var>n</var> be a positive integer Suppose there are stations at 
the coordinates <var>x</var> <var>y</var>  2<sup><var>i</var></sup> 
mod <var>n</var> 3<sup><var>i</var></sup> mod <var>n</var> for 0 le 
<var>i</var> le 2<var>n</var> We will consider stations with the same 
coordinates as the same station

We wish to form a path from 0 0 to <var>n</var> <var>n</var> such that 
the x and y coordinates never decrease
Let S<var>n</var> be the maximum number of stations such a path can 
pass through

For example if <var>n</var>  22 there are 11 distinct stations and a 
valid path can pass through at most 5 stations Therefore S22  5The 
case is illustrated below with an example of an optimal path

<img src=project/images/p411_longpath.png>

It can also be verified that S123  14 and S10000  48

Find sum S<var>k</var><sup>5</sup> for 1 le <var>k</var> le 30
"""

def euler411():
    """
    >>> euler411()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()