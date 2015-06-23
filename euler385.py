"""
<P>For any triangle <var>T</var> in the plane it can be shown that 
there is a unique ellipse with largest area that is completely inside 
<var>T</var><P align=center>
<img src=project/images/p385_ellipsetriangle.png></P><P>For a given 
<var>n</var> consider triangles <var>T</var> such that<BR /> the 
vertices of <var>T</var> have integer coordinates with absolute value 
le n and <BR /> the <b>foci</b><sup>1</sup> of the largestarea ellipse 
inside <var>T</var> are radic130 and radic130<BR />Let A<var>n</var> 
be the sum of the areas of all such triangles<P>For example if <var>n
</var>  8 there are two such triangles Their vertices are 434380 and 4
34380 and the area of each triangle is 36 Thus A8  36  36  72</P><P>It 
can be verified that A10  252 A100  34632 and A1000  3529008</P><P>
Find A1 000 000 000</P><P><sup>1</sup>The <b>foci</b> plural of <b>
focus</b> of an ellipse are two points A and B such that for every 
point P on the boundary of the ellipse <var>AP</var>  <var>PB</var> is 
constant
"""

def euler385():
    """
    >>> euler385()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()