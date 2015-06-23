"""
One variant of NG de Bruijns <b>silver dollar</b> game can be 
described as follows

On a strip of squares a number of coins are placed at most one coin 
per square Only one coin called the <b>silver dollar</b> has any value 
Two players take turns making moves At each turn a player must make 
either a <i>regular</i> or a <i>special</i> move

A <i>regular</i> move consists of selecting one coin and moving it one 
or more squares to the left The coin cannot move out of the strip or 
jump on or over another coin

Alternatively the player can choose to make the <i>special</i> move of 
pocketing the leftmost coin rather than making a regular move If no 
regular moves are possible the player is forced to pocket the leftmost 
coin

The winner is the player who pockets the silver dollar
<div align='center'><img src="project/images/p344_silverdollar.gif" />
"""

def euler344():
    """
    >>> euler344()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()