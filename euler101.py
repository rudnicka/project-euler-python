"""
If we are presented with the first <var>k</var> terms of a sequence it 
is impossible to say with certainty the value of the next term as 
there are infinitely many polynomial functions that can model the 
sequence

As an example let us consider the sequence of cube numbers This is 
defined by the generating function 
<var>u</var><sub><var>n</var></sub>  <var>n</var><sup>3</sup> 1 8 27 
64 125 216 

Suppose we were only given the first two terms of this sequence 
Working on the principle that quotsimple is bestquot we should assume 
a linear relationship and predict the next term to be 15 common 
difference 7 Even if we were presented with the first three terms by 
the same principle of simplicity a quadratic relationship should be 
assumed

We shall define OP<var>k</var> <var>n</var> to be the <var>n</var>
<sup>th</sup> term of the optimum polynomial generating function for 
the first <var>k</var> terms of a sequence It should be clear that OP
<var>k</var> <var>n</var> will accurately generate the terms of the 
sequence for <var>n</var> le <var>k</var> and potentially the <i>first 
incorrect term</i> FIT will be OP<var>k</var> <var>k</var>1 in which 
case we shall call it a <i>bad OP</i> BOP

As a basis if we were only given the first term of sequence it would 
be most sensible to assume constancy that is for <var>n</var> ge 2 OP1 
<var>n</var>  <var>u</var><sub>1</sub>

Hence we obtain the following OPs for the cubic sequence
<div style='margin-left:50px;'><table><tr><td>OP1 <var>n</var>  1</td>
<td>1 <span style='color:red;'><b>1</b></span> 1 1 </td></tr><tr><td>
OP2 <var>n</var>  7<var>n</var>minus6</td><td>1 8 
<span style='color:red;'><b>15</b></span> </td></tr><tr><td>OP3 <var>n
</var>  6<var>n</var><sup>2</sup>minus11<var>n</var>6     </td><td>1 8 
27 <span style='color:red;'><b>58</b></span> </td></tr><tr><td>OP4 
<var>n</var>  <var>n</var><sup>3</sup></td><td>1 8 27 64 125 </td>
</tr></table>
"""

def euler101():
    """
    >>> euler101()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()