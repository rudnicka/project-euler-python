"""
<P>A rectilinear grid is an orthogonal grid where the spacing between 
the gridlines does not have to be equidistant<BR />An example of such 
grid is logarithmic graph paper<P>Consider rectilinear grids in the 
Cartesian coordinate system with the following properties
<ul><li>The gridlines are parallel to the axes of the Cartesian 
coordinate system</li><li>There are N2 vertical and N2 horizontal 
gridlines Hence there are N1 x N1 rectangular cells</li><li>The 
equations of the two outer vertical gridlines are x  1 and x  1</li>
<li>The equations of the two outer horizontal gridlines are y  1 and y  
1</li><li>The grid cells are colored red if they overlap with the 
<dfn title="The unit circle is the circle that has radius 1 and is centered at the origin">
unit circle</dfn> black otherwise</li></ul>For this problem we would 
like you to find the postions of the remaining N inner horizontal and 
N inner vertical gridlines so that the area occupied by the red cells 
is minimized

Eg here is a picture of the solution for N  10<P align=center>
<img src=project/images/p392_gridlines.png></P>The area occupied by 
the red cells for N  10 rounded to 10 digits behind the decimal point 
is 33469640797

Find the positions for N  400<BR /> Give as your answer the area 
occupied by the red cells rounded to 10 digits behind the decimal 
point</P>
"""

def euler392():
    """
    >>> euler392()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()