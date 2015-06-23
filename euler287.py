"""
The quadtree encoding allows us to describe a 2<sup><var>N</var></sup>
times2<sup><var>N</var></sup>  black and white image as a sequence of 
bits 0 and 1 Those sequences are to be read from left to right like 
this<ul><li>the first bit deals with the complete 2<sup><var>N</var>
</sup>times2<sup><var>N</var></sup> region</li><li>0 denotes a split
the current 2<sup><var>n</var></sup>times2<sup><var>n</var></sup> 
region is divided into 4 subregions of dimension 2<sup><var>n</var>1
</sup>times2<sup><var>n</var>1</sup>
the next bits contains the description of the top left top right 
bottom left and bottom right subregions  in that order</li><li>10 
indicates that the current region contains only black pixels</li><li>
11 indicates that the current region contains only white pixels</li>
</ul>

Consider the following 4times4 image colored marks denote places where 
a split can occur<div align='center'>
<img src="project/images/p287_quadtree.gif" />
"""

def euler287():
    """
    >>> euler287()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()