"""
The following game is a classic example of Combinatorial Game Theory

Two players start with a strip of <var>n</var> white squares and they 
take alternate turns
On each turn a player picks two contiguous white squares and paints 
them black
The first player who cannot make a move loses

<ul><li>If <var>n</var>  1 there are no valid moves so the first 
player loses automatically</li><li>If <var>n</var>  2 there is only 
one valid move after which the second player loses</li><li>If <var>n
</var>  3 there are two valid moves but both leave a situation where 
the second player loses</li><li>If <var>n</var>  4 there are three 
valid moves for the first player she can win the game by painting the 
two middle squares</li><li>If <var>n</var>  5 there are four valid 
moves for the first player shown below in red but no matter what she 
does the second player blue wins</li></ul><div align='center'>
<img src="project/images/p306_pstrip.gif" />
"""

def euler306():
    """
    >>> euler306()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()