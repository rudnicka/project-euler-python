"""
Let us define a <i>balanced sculpture</i> of order <var>n</var> as 
follows<ul><li>A 
<dfn title="An arrangement of identical squares connected through shared edges; holes are allowed.">
polyomino</dfn> made up of <var>n</var>1 tiles known as the <i>blocks
</i> <var>n</var> tiles
 and the <i>plinth</i> remaining tile</li><li>the plinth has its 
centre at position <var>x</var>thinspthinsp0 <var>y</var>thinspthinsp0
</li><li>the blocks have <var>y</var>coordinates greater than zero so 
the plinth is the unique lowest tile</li><li>the centre of mass of all 
the blocks combined has <var>x</var>coordinate equal to zero</li></ul>

When counting the sculptures any arrangements which are simply 
reflections about the <var>y</var>axis are <u>not</u> counted as 
distinct For example the 18 balanced sculptures of order 6 are shown 
below note that each pair of mirror images about the <var>y</var>axis 
is counted as one sculpture<div align='center'>
<img src="project/images/p275_sculptures2.gif" />
"""

def euler275():
    """
    >>> euler275()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()