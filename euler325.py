"""
A game is played with two piles of stones and two players At her turn 
a player removes a number of stones from the larger pile The number of 
stones she removes must be a positive multiple of the number of stones 
in the smaller pile

Eg let the ordered pair614 describe a configuration with 6 stones in 
the smaller pile and 14 stones in the larger pile then the first 
player can remove 6 or 12 stones from the larger pile

The player taking all the stones from a pile wins the game

A <i>winning configuration</i> is one where the first player can force 
a win For example 15 26 and 312 are winning configurations because the 
first player can immediately remove all stones in the second pile

A <i>losing configuration</i> is one where the second player can force 
a win no matter what the first player does For example 23 and 34 are 
losing configurations any legal move leaves a winning configuration 
for the second player

Define S<var>N</var> as the sum of <var>x</var><sub><var>i</var></sub>
<var>y</var><sub><var>i</var></sub> for all losing configurations 
<var>x</var><sub><var>i</var></sub><var>y</var><sub><var>i</var></sub> 
0 lt <var>x</var><sub><var>i</var></sub> lt <var>y</var><sub><var>i
</var></sub> le <var>N</var> We can verify that S10  211 and S10<sup>4
</sup>  230312207313

Find S10<sup>16</sup> mod 7<sup>10</sup>
"""

def euler325():
    """
    >>> euler325()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()