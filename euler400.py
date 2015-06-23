"""
A <b>Fibonacci tree</b> is a binary tree recursively defined as<ul>
<li>T0 is the empty tree<li>T1 is the binary tree with only one node
<li>T<var>k</var> consists of a root node that has T<var>k</var>1 and 
T<var>k</var>2 as children</ul>

On such a tree two players play a takeaway game On each turn a player 
selects a node and removes that node along with the subtree rooted at 
that node
The player who is forced to take the root node of the entire tree 
loses

Here are the winning moves of the first player on the first turn for T
<var>k</var> from <var>k</var>1 to <var>k</var>6

<img src=project/images/p400_winning.png>Let <var>f</var><var>k</var> 
be the number of winning moves of the first player ie the moves for 
which the second player has no winning strategy on the first turn of 
the game when this game is played on T<var>k</var>

For example <var>f</var>5  1 and <var>f</var>10  17

Find <var>f</var>10000 Give the last 18 digits of your answer
"""

def euler400():
    """
    >>> euler400()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()