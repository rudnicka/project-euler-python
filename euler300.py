"""
In a very simplified form we can consider proteins as strings 
consisting of hydrophobic H and polar P elements eg HHPPHHHPHHPH 
For this problem the orientation of a protein is important eg HPP is 
considered distinct from PPH Thus there are 2<sup><var>n</var></sup> 
distinct proteins consisting of <var>n</var> elements

When one encounters these strings in nature they are always folded in 
such a way that the number of HH contact points is as large as 
possible since this is energetically advantageous
As a result the Helements tend to accumulate in the inner part with 
the Pelements on the outside
Natural proteins are folded in three dimensions of course but we will 
only consider protein folding in <u>two dimensions</u>

The figure below shows two possible ways that our example protein 
could be folded HH contact points are shown with red dots
<div align='center'><img src="project/images/p300_protein.gif" />
"""

def euler300():
    """
    >>> euler300()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()