"""
Consider the following set of dice with nonstandard pips

Die A 1 4 4 4 4 4
Die B 2 2 2 5 5 5
Die C 3 3 3 3 3 6

A game is played by two players picking a die in turn and rolling it 
The player who rolls the highest value wins

If the first player picks die A and the second player picks die B we 
get
Psecond player wins  <sup>7</sup><sub>12</sub>  <sup>1</sup><sub>2
</sub>

If the first player picks die B and the second player picks die C we 
get
Psecond player wins  <sup>7</sup><sub>12</sub>  <sup>1</sup><sub>2
</sub>

If the first player picks die C and the second player picks die A we 
get
Psecond player wins  <sup>25</sup><sub>36</sub>  <sup>1</sup><sub>2
</sub>

So whatever die the first player picks the second player can pick 
another die and have a larger than 50 chance of winning
A set of dice having this property is called a <b>nontransitive set of 
dice</b>

We wish to investigate how many sets of nontransitive dice exist We 
will assume the following conditions<ul><li>There are three sixsided 
dice with each side having between 1 and <var>N</var> pips inclusive
</li><li>Dice with the same set of pips are equal regardless of which 
side on the die the pips are located</li><li>The same pip value may 
appear on multiple dice if both players roll the same value neither 
player wins</li><li>The sets of dice ABC BCA and CAB are the same set
</li></ul>

For <var>N</var>  7 we find there are 9780 such sets
How many are there for <var>N</var>  30 
"""

def euler376():
    """
    >>> euler376()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()