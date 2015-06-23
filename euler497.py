"""
Bob is very familiar with the famous mathematical puzzlegame Tower of 
Hanoi which consists of three upright rods and disks of different 
sizes that can slide onto any of the rods The game begins with a stack 
of <var>n</var> disks placed on the leftmost rod in descending order 
by size The objective of the game is to move all of the disks from the 
leftmost rod to the rightmost rod given the following restrictions<ol>
<li>Only one disk can be moved at a time</li><li>A valid move consists 
of taking the top disk from one stack and placing it onto another 
stack or an empty rod</li><li>No disk can be placed on top of a 
smaller disk</li></ol>

Moving on to a variant of this game consider a long room <var>k</var> 
units square tiles wide labeled from 1 to <var>k</var> in ascending 
order Three rods are placed at squares <var>a</var> <var>b</var> and 
<var>c</var> and a stack of <var>n</var> disks is placed on the rod at 
square <var>a</var>

Bob begins the game standing at square <var>b</var> His objective is 
to play the Tower of Hanoi game by moving all of the disks to the rod 
at square <var>c</var> However Bob can only pick up or set down a disk 
if he is on the same square as the rod  stack in question

Unfortunately Bob is also drunk On a given move Bob will either 
stumble one square to the left or one square to the right with equal 
probability unless Bob is at either end of the room in which case he 
can only move in one direction Despite Bobs inebriated state he is 
still capable of following the rules of the game itself as well as 
choosing when to pick up or put down a disk

The following animation depicts a sideview of a sample game for <var>n
</var>  3 <var>k</var>  7 <var>a</var>  2 <var>b</var>  4 and <var>c
</var>  6

<img src=project/images/p497_hanoi.gif>

Let E<var>n</var><var>k</var><var>a</var><var>b</var><var>c</var> be 
the expected number of squares that Bob travels during a single 
optimallyplayed game A game is played optimally if the number of disk
pickups is minimized

Interestingly enough the result is always an integer For example E2513
5  60 and E3204917  2358

Find the last nine digits of sum<sub>1le<var>n</var>le10000</sub> E
<var>n</var>10<sup><var>n</var></sup>3<sup><var>n</var></sup>6<sup>
<var>n</var></sup>9<sup><var>n</var></sup>
"""

def euler497():
    """
    >>> euler497()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()