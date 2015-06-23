"""
Alice and Bob have enjoyed playing <b>Nim</b> every day However they 
finally got bored of playing ordinary threeheap Nim
So they added an extra rule

 Must not make two heaps of the same size

The triple <var>a</var><var>b</var><var>c</var> indicates the size of 
three heaps
Under this extra rule 245 is one of the losing positions for the next 
player

To illustrate
 Alice moves to 243
 Bob   moves to 043
 Alice moves to 023
 Bob   moves to 021

Unlike ordinary threeheap Nim 012 and its permutations are the end 
states of this game

For an integer <var>N</var> we define F<var>N</var> as the sum of 
<var>a</var><var>b</var><var>c</var> for all the losing positions for 
the next player with 0 < <var>a</var> < <var>b</var> < <var>c</var> 
< <var>N</var>

For example F8  42 because there are 4 losing positions for the next 
player 135 146 236 and 245
We can also verify that F128  496062

Find the last 9 digits of F10<sup>18</sup>
"""

def euler488():
    """
    >>> euler488()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()