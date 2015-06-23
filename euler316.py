"""
Let <var>p</var>  <var>p<sub><font size="-2">1</font></sub> p<sub>
<font size="-2">2</font></sub> p<sub><font size="-2">3</font></sub>
</var>  be an infinite sequence of random digits selected from 0123456
789 with equal probability
It can be seen that <var>p</var> corresponds to the real number 0<var>
p<sub><font size="-2">1</font></sub> p<sub><font size="-2">2</font>
</sub> p<sub><font size="-2">3</font></sub></var>  
It can also be seen that choosing a random real number from the 
interval 01 is equivalent to choosing an infinite sequence of random 
digits selected from 0123456789 with equal probability

For any positive integer <var>n</var> with <var>d</var> decimal digits 
let <var>k</var> be the smallest index such that 
 <var>p<sub><small>k</small> </sub></var><var>p<sub><small>k1</small>
</sub></var> <var>p<sub><small>kd1</small></sub></var> are the decimal 
digits of <var>n</var> in the same order
Also let <var>g</var><var>n</var> be the expected value of <var>k
</var> it can be proven that <var>g</var><var>n</var> is always finite 
and interestingly always an integer number

For example if <var>n</var>  535 then
for <var>p</var>  31415926<b>535</b>897 we get <var>k</var>  9
for <var>p</var>  35528714365004956000049084876408468<b>535</b>4 we 
get <var>k</var>  36
etc and we find that <var>g</var>535  1008

Given that 
<img style="vertical-align:middle" src="project/images/p316_decexp1.gif" /> 
find 
<img style="vertical-align:middle" src="project/images/p316_decexp2.gif" />
<u><i>Note</i></u> 
<img style="vertical-align:middle" src="project/images/p316_decexp3.gif" /> 
represents the floor function
"""

def euler316():
    """
    >>> euler316()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()