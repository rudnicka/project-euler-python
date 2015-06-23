"""
A square piece of paper with integer dimensions NtimesN is placed with 
a corner at the origin and two of its sides along the <var>x</var> and 
<var>y</var>axes Then we cut it up respecting the following rules<ul>
<li>We only make straight cuts between two points lying on different 
sides of the square and having integer coordinates</li><li>Two cuts 
cannot cross but several cuts can meet at the same border point</li>
<li>Proceed until no more legal cuts can be made</li></ul>

Counting any reflections or rotations as distinct we call CN the 
number of ways to cut an NtimesN square For example C1thinspthinsp2 
and C2thinspthinsp30 shown below<div align='center'>
<img src="project/images/p270_CutSquare.gif" />
"""

def euler270():
    """
    >>> euler270()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()