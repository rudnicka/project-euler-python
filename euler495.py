"""
Let <var>W</var><var>n</var><var>k</var> be the number of ways in 
which <var>n</var> can be written as the product of <var>k</var> 
distinct positive integers

For example <var>W</var>1444  7 There are 7 ways in which 144 can be 
written as a product of 4 distinct positive integers

<ul><li>144  1times2times4times18</li><li>144  1times2times8times9
</li><li>144  1times2times3times24</li><li>144  1times2times6times12
</li><li>144  1times3times4times12</li><li>144  1times3times6times8
</li><li>144  2times3times4times6</li></ul>

Note that permutations of the integers themselves are not considered 
distinct

Furthermore <var>W</var>10010 modulo 1 000 000 007  287549200

Find <var>W</var>1000030 modulo 1 000 000 007
"""

def euler495():
    """
    >>> euler495()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()