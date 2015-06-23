"""
Let <var>s<sub>k</sub></var> be the number of 1rsquos when writing the 
numbers from 0 to <var>k</var> in binary
For example writing 0 to 5 in binary we have 0 1 10 11 100 101 There 
are seven 1rsquos so <var>s</var><sub>5</sub>  7
The sequence S  <var>s<sub>k</sub></var>  <var>k</var> ge 0 starts 0 1 
2 4 5 7 9 12 

A game is played by two players Before the game starts a number <var>n
</var> is chosen A counter <var>c</var> starts at 0 At each turn the 
player chooses a number from 1 to <var>n</var> inclusive and increases 
<var>c</var> by that number The resulting value of <var>c</var> must 
be a member of S If there are no more valid moves the player loses

For example
Let <var>n</var>  5 <var>c</var> starts at 0
Player 1 chooses 4 so <var>c</var> becomes 0  4  4
Player 2 chooses 5 so <var>c</var> becomes 4  5  9
Player 1 chooses 3 so <var>c</var> becomes 9  3  12
etc
Note that <var>c</var> must always belong to S and each player can 
increase <var>c</var> by at most <var>n</var>

Let M<var>n</var> be the highest number the first player can choose at 
her first turn to force a win and M<var>n</var>  0 if there is no such 
move For example M2  2 M7  1 and M20  4

Given SigmaM<var>n</var><sup>3</sup>  8150 for 1 le <var>n</var> le 20

Find SigmaM<var>n</var><sup>3</sup> for 1 le <var>n</var> le 1000
"""

def euler391():
    """
    >>> euler391()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()