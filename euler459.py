"""
The flipping game is a two player game played on a N by N square board
Each square contains a disk with one side white and one side black
The game starts with all disks showing their white side

A turn consists of flipping all disks in a rectangle with the 
following properties

<ul><li>the upper right corner of the rectangle contains a white disk
</li><li>the rectangle width is a perfect square 1 4 9 16 </li><li>the 
rectangle height is a 
<dfn title="The triangular numbers are defined as &frac12; n(n + 1) for positive integer n.">
triangular number</dfn> 1 3 6 10 </li></ul>

<img src=project/images/p459-flipping-game-0.png>

Players alternate turns A player wins by turning the grid all black

Let WN be the number of 
<dfn title="The first move of a strategy that ensures a win no matter what the opponent plays.">
winning moves</dfn> for the first player on a N by N board with all 
disks white assuming perfect play
W1  1 W2  0 W5  8 and W10<sup>2</sup>  31395

For N5 the first players eight winning first moves are

<img src=project/images/p459-flipping-game-1.png>

<img src=project/images/p459-flipping-game-2.png>

Find W10<sup>6</sup>
"""

def euler459():
    """
    >>> euler459()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()