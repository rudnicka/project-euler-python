"""
On the Euclidean plane an ant travels from point A0 1 to point B<var>d
</var> 1 for an integer <var>d</var>

In each step the ant at point <var>x</var><sub>0</sub> <var>y</var>
<sub>0</sub> chooses one of the lattice points <var>x</var><sub>1
</sub> <var>y</var><sub>1</sub> which satisfy <var>x</var><sub>1</sub> 
ge 0 and <var>y</var><sub>1</sub> ge 1 and goes straight to <var>x
</var><sub>1</sub> <var>y</var><sub>1</sub> at a constant velocity 
<var>v</var> The value of <var>v</var> depends on <var>y</var><sub>0
</sub> and <var>y</var><sub>1</sub> as follows<ul><li> If <var>y</var>
<sub>0</sub>  <var>y</var><sub>1</sub> the value of <var>v</var> 
equals <var>y</var><sub>0</sub></li><li> If <var>y</var><sub>0</sub> 
ne <var>y</var><sub>1</sub> the value of <var>v</var> equals <var>y
</var><sub>1</sub>  <var>y</var><sub>0</sub>  ln<var>y</var><sub>1
</sub>  ln<var>y</var><sub>0</sub></li></ul>

The left image is one of the possible paths for <var>d</var>  4 First 
the ant goes from A0 1 to P<sub>1</sub>1 3 at velocity 3  1  ln3  ln1 
asymp 18205 Then the required time is sqrt5  18205 asymp 12283
From P<sub>1</sub>1 3 to P<sub>2</sub>3 3 the ant travels at velocity 
3 so the required time is 2  3 asymp 06667 From P<sub>2</sub>3 3 to B4 
1 the ant travels at velocity 1  3  ln1  ln3 asymp 18205 so the 
required time is sqrt5  18205 asymp 12283
Thus the total required time is 12283  06667  12283  31233

The right image is another path The total required time is calculated 
as 098026  1  098026  296052 It can be shown that this is the quickest 
path for <var>d</var>  4

<img src=project/images/p460_ant.jpg>

Let F<var>d</var> be the total required time if the ant chooses the 
quickest path For example F4 asymp 2960516287
We can verify that F10 asymp 4668187834 and F100 asymp 9217221972

Find F10000 Give your answer rounded to nine decimal places
"""

def euler460():
    """
    >>> euler460()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()