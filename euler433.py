"""
<P>Let E<var>x</var><sub>0</sub> <var>y</var><sub>0</sub> be the 
number of steps it takes to determine the greatest common divisor of 
<var>x</var><sub>0</sub> and <var>y</var><sub>0</sub> with <b>Euclids 
algorithm</b> More formally<BR /><var>x</var><sub>1</sub>  <var>y
</var><sub>0</sub> <var>y</var><sub>1</sub>  <var>x</var><sub>0</sub> 
mod <var>y</var><sub>0</sub><BR /><var>x<sub>n</sub></var>  <var>y
</var><sub><var>n</var>1</sub> <var>y</var><sub><var>n</var></sub>  
<var>x</var><sub><var>n</var>1</sub> mod <var>y</var><sub><var>n</var>
1</sub><BR />E<var>x</var><sub>0</sub> <var>y</var><sub>0</sub> is the 
smallest <var>n</var> such that <var>y</var><sub><var>n</var></sub>  0
</P><P>We have E11  1 E106  3 and E610  4</P><P>Define SN as the sum 
of E<var>xy</var> for 1 le <var>xy</var> le N<BR/>We have S1  1 S10  
221 and S100  39826</P><P>Find S5middot10<sup>6</sup></P>
"""

def euler433():
    """
    >>> euler433()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()