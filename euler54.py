"""
In the card game poker a hand consists of five cards and are ranked 
from lowest to highest in the following way<ul><li><b>High Card</b> 
Highest value card</li><li><b>One Pair</b> Two cards of the same value
</li><li><b>Two Pairs</b> Two different pairs</li><li><b>Three of a 
Kind</b> Three cards of the same value</li><li><b>Straight</b> All 
cards are consecutive values</li><li><b>Flush</b> All cards of the 
same suit</li><li><b>Full House</b> Three of a kind and a pair</li>
<li><b>Four of a Kind</b> Four cards of the same value</li><li><b>
Straight Flush</b> All cards are consecutive values of same suit</li>
<li><b>Royal Flush</b> Ten Jack Queen King Ace in same suit</li></ul>

The cards are valued in the order
2 3 4 5 6 7 8 9 10 Jack Queen King Ace

If two players have the same ranked hands then the rank made up of the 
highest value wins for example a pair of eights beats a pair of fives 
see example 1 below But if two ranks tie for example both players have 
a pair of queens then highest cards in each hand are compared see 
example 4 below if the highest cards tie then the next highest cards 
are compared and so on

Consider the following five hands dealt to two players
<div style="text-align:center;"><table><tr><td><b>Hand</b></td><td> 
</td><td><b>Player 1</b></td><td> </td><td><b>Player 2</b></td><td> 
</td><td><b>Winner</b></td></tr><tr><td style="vertical-align:top;">
<b>1</b></td><td> </td><td>5H 5C 6S 7S KD
<div class="note">Pair of Fives
"""

def euler54():
    """
    >>> euler54()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()