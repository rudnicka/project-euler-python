"""
Julie proposes the following wager to her sister Louise
She suggests they play a game of chance to determine who will wash the 
dishes
For this game they shall use a generator of independent random numbers 
uniformly distributed between 0 and 1
The game starts with <var>S</var>  0
The first player Louise adds to <var>S</var> different random numbers 
from the generator until <var>S</var>  1 and records her last random 
number <var>x</var>
The second player Julie continues adding to <var>S</var> different 
random numbers from the generator until <var>S</var>  2 and records 
her last random number <var>y</var>
The player with the highest number wins and the loser washes the 
dishes ie if <var>y</var>  <var>x</var> the second player wins

For e<var>x</var>ample if the first player draws 062 and 044 the first 
player turn ends since 062044  1 and <var>x</var>  044
If the second players draws 01 027 and 091 the second player turn ends 
since 06204401027091  2 and <var>y</var>  091Since <var>y</var>  <var>
x</var> the second player wins

Louise thinks about it for a second and objects Thats not fair
What is the probability that the second player wins
Give your answer rounded to 10 places behind the decimal point in the 
form 0abcdefghij
"""

def euler436():
    """
    >>> euler436()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()