"""
We define the <i>roundedsquareroot</i> of a positive integer <var>n
</var> as the square root of <var>n</var> rounded to the nearest 
integer

The following procedure essentially Heron39s method adapted to integer 
arithmetic finds the roundedsquareroot of <var>n</var>

Let <var>d</var> be the number of digits of the number <var>n</var>
If <var>d</var> is odd set <var>x</var><sub>0</sub>  2times10<sup>
<var>d</var>1frasl2</sup>
If <var>d</var> is even set <var>x</var><sub>0</sub>  7times10<sup>
<var>d</var>2frasl2</sup>
Repeat

<img src="project/images/p255_Heron.gif" />until <var>x</var><sub>
<var>k</var>1</sub>  <var>x</var><sub><var>k</var></sub>

As an example let us find the roundedsquareroot of <var>n</var>  4321
<var>n</var> has 4 digits so <var>x</var><sub>0</sub>  7times10<sup>42
frasl2</sup>  70
<img src='project/images/p255_Example.gif'>Since <var>x</var><sub>2
</sub>  <var>x</var><sub>1</sub> we stop here
So after just two iterations we have found that the roundedsquareroot 
of 4321 is 66 the actual square root is 657343137hellip

The number of iterations required when using this method is 
surprisingly low
For example we can find the roundedsquareroot of a 5digit integer 10
000 le <var>n</var> le 99999 with an average of 32102888889 iterations 
the average value was rounded to 10 decimal places

Using the procedure described above what is the average number of 
iterations required to find the roundedsquareroot of a 14digit number 
10<sup>13</sup> le <var>n</var> lt 10<sup>14</sup>
Give your answer rounded to 10 decimal places

Note The symbols lfloor<var>x</var>rfloor and lceil<var>x</var>rceil 
represent the <dfn title='the largest integer not greater than x'>
floor function</dfn> and 
<dfn title='the smallest integer not less than x'>ceiling function
</dfn> respectively
"""

def euler255():
    """
    >>> euler255()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()