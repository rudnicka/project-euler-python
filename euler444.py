"""
A group of <var>p</var> people decide to sit down at a round table and 
play a lotteryticket trading game Each person starts off with a 
randomlyassigned unscratched lottery ticket Each ticket when scratched 
reveals a wholepound prize ranging anywhere from pound1 to pound<var>p
</var> with no two tickets alike The goal of the game is for each 
person to maximize his ticket winnings upon leaving the game

An arbitrary person is chosen to be the first player Going around the 
table each player has only one of two options

1 The player can scratch his ticket and reveal its worth to everyone 
at the table
2 The player can trade his unscratched ticket for a previous players 
scratched ticket and then leave the game with that ticket The previous 
player then scratches his newlyacquired ticket and reveals its worth 
to everyone at the table

The game ends once all tickets have been scratched All players still 
remaining at the table must leave with their currentlyheld tickets

Assume that each player uses the optimal strategy for maximizing the 
expected value of his ticket winnings 

Let E<var>p</var> represent the expected number of players left at the 
table when the game ends in a game consisting of <var>p</var> players 
eg E111  52912 when rounded to 5 significant digits

Let S<sub>1</sub><var>N</var>  
<img style="vertical-align:middle" src="project/images/p444_sum.png" /> 
E<var>p</var>
Let S<sub><var>k</var></sub><var>N</var>  
<img style="vertical-align:middle" src="project/images/p444_sum.png" /> 
S<sub><var>k</var>1</sub><var>p</var> for <var>k</var> gt 1

Find S<sub>20</sub>10<sup>14</sup> and write the answer in scientific 
notation rounded to 10 significant digits Use a lowercase e to 
separate mantissa and exponent eg S<sub>3</sub>100  5983679014e5
"""

def euler444():
    """
    >>> euler444()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()