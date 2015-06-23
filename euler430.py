"""
<var>N</var> disks are placed in a row indexed 1 to <var>N</var> from 
left to right
Each disk has a black side and white side Initially all disks show 
their white side

At each turn two not necessarily distinct integers <var>A</var> and 
<var>B</var> between 1 and <var>N</var> inclusive are chosen uniformly 
at random
All disks with an index from <var>A</var> to <var>B</var> inclusive 
are flipped

The following example shows the case <var>N</var>  8 At the first turn 
<var>A</var>  5 and <var>B</var>  2 and at the second turn <var>A
</var>  4 and <var>B</var>  6

<img src="project/images/p430_flips.gif" />

Let E<var>N</var> <var>M</var> be the expected number of disks that 
show their white side after <var>M</var> turns
We can verify that E3 1  109 E3 2  53 E10 4 asymp 5157 and E100 10 
asymp 51893

Find E10<sup>10</sup> 4000
Give your answer rounded to 2 decimal places behind the decimal point
"""

def euler430():
    """
    >>> euler430()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()