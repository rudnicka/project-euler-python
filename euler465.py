"""
The <i>kernel</i> of a polygon is defined by the set of points from 
which the entire polygons boundary is visible We define a <i>polar 
polygon</i> as a polygon for which the origin is <u>strictly</u> 
contained inside its kernel

For this problem a polygon can have collinear consecutive vertices 
However a polygon still cannot have selfintersection and cannot have 
zero area

For example only the first of the following is a polar polygon the 
kernels of the second third and fourth do not strictly contain the 
origin and the fifth does not have a kernel at all

<img src=project/images/p465_polygons.png>

Notice that the first polygon has three consecutive collinear vertices

Let P<var>n</var> be the number of polar polygons such that the 
vertices <var>x</var> <var>y</var> have integer coordinates whose 
absolute values are not greater than <var>n</var>

Note that polygons should be counted as different if they have 
different set of edges even if they enclose the same area For example 
the polygon with vertices 00031130 is distinct from the polygon with 
vertices 0003113010

For example P1  131 P2  1648531 P3  1099461296175 and P343 mod 1 000 
000 007  937293740

Find P7<sup>13</sup> mod 1 000 000 007
"""

def euler465():
    """
    >>> euler465()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()