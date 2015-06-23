"""
A game is played with three piles of stones and two players
At her turn a player removes one or more stones from the piles However 
if she takes stones from more than one pile she must remove the same 
number of stones from each of the selected piles

In other words the player chooses some N0 and removes<ul><li>N stones 
from any single pile or</li><li>N stones from each of any two piles 2N 
total or</li><li>N stones from each of the three piles 3N total</li>
</ul>The player taking the last stones wins the game

A <i>winning configuration</i> is one where the first player can force 
a win
For example 0013 01111 and 555 are winning configurations because the 
first player can immediately remove all stones

A <i>losing configuration</i> is one where the second player can force 
a win no matter what the first player does
 For example 012 and 133 are losing configurations any legal move 
leaves a winning configuration for the second player

Consider all  losing configurations x<sub>i</sub>y<sub>i</sub>z<sub>i
</sub> where x<sub>i</sub> le y<sub>i</sub> le z<sub>i</sub> le 100
We can verify that Sigmax<sub>i</sub>y<sub>i</sub>z<sub>i</sub>  
173895 for these

Find Sigmax<sub>i</sub>y<sub>i</sub>z<sub>i</sub> where x<sub>i</sub>y
<sub>i</sub>z<sub>i</sub> ranges over the losing configurations
with x<sub>i</sub> le y<sub>i</sub> le z<sub>i</sub> le 1000
"""

def euler260():
    """
    >>> euler260()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()