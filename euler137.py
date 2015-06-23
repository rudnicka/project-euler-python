"""
Consider the infinite polynomial series A<sub>F</sub><i>x</i>  <i>x
</i>F<sub>1</sub>  <i>x</i><sup>2</sup>F<sub>2</sub>  <i>x</i><sup>3
</sup>F<sub>3</sub>   where F<sub><i>k</i></sub> is the <i>k</i>th 
term in the Fibonacci sequence 1 1 2 3 5 8   that is F<sub><i>k</i>
</sub>  F<sub><i>k</i>minus1</sub>  F<sub><i>k</i>minus2</sub> F<sub>1
</sub>  1 and F<sub>2</sub>  1

For this problem we shall be interested in values of <i>x</i> for 
which A<sub>F</sub><i>x</i> is a positive integer
<table cellpadding='0' cellspacing='0' border='0'><tr><td>Surprisingly 
A<sub>F</sub>12</td><td>  </td><td>121  12<sup>2</sup>1  12<sup>3
</sup>2  12<sup>4</sup>3  12<sup>5</sup>5  </td></tr><tr><td> </td>
<td>  </td><td>12  14  28  316  532  </td></tr><tr><td> </td><td>  
</td><td>2</td></tr></table>

The corresponding values of <i>x</i> for the first five natural 
numbers are shown below<div style='text-align:center;'>
<table cellspacing='0' cellpadding='2' border='1' align='center'>
<tr style='background-color:#c1daf9;'><td><b><i>x</i></b></td>
<td width='50'><b>A<sub>F</sub><i>x</i></b></td></tr><tr><td>radic2
minus1</td><td>1</td></tr><tr><td>12</td><td>2</td></tr><tr><td>radic
13minus23</td><td>3</td></tr><tr><td>radic89minus58</td><td>4</td>
</tr><tr><td>radic34minus35</td><td>5</td></tr></table>
"""

def euler137():
    """
    >>> euler137()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()