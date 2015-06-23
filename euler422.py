"""
Let H be the hyperbola defined by the equation 12<var>x</var><sup>2
</sup>  7<var>x</var><var>y</var>  12<var>y</var><sup>2</sup>  625

Next define X as the point 7 1 It can be seen that X is in H

Now we define a sequence of points in H P<sub><var>i</var></sub>  
<var>i</var> ge 1 as<ul><li> P<sub>1</sub>  13 614<li> P<sub>2</sub>  
436 4<li> For <var>i</var>  2 P<sub><var>i</var></sub> is the unique 
point in H that is different from P<sub><var>i</var>1</sub> and such 
that line P<sub><var>i</var></sub>P<sub><var>i</var>1</sub> is 
parallel to line P<sub><var>i</var>2</sub>X It can be shown that P
<sub><var>i</var></sub> is welldefined and that its coordinates are 
always rational</ul><img src=project/images/p422_hyperbola.gif>

You are given that P<sub>3</sub>   192 22924 P<sub>4</sub>  1267144 37
12 and P<sub>7</sub>  17194218091143327232 2747487667811719926784

Find P<sub><var>n</var></sub> for <var>n</var>  11<sup>14</sup> in the 
following format
If P<sub><var>n</var></sub>  <var>a</var><var>b</var> <var>c</var>
<var>d</var> where the fractions are in lowest terms and the 
denominators are positive then the answer is <var>a</var>  <var>b
</var>  <var>c</var>  <var>d</var> mod 1 000 000 007

For <var>n</var>  7 the answer would have been 806236837
"""

def euler422():
    """
    >>> euler422()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()