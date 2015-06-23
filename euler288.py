"""
For any prime <var>p</var> the number N<var>p</var><var>q</var> is 
defined byN<var>p</var><var>q</var>  sum<sub><var>n</var>0 to <var>q
</var></sub> T<sub><var>n</var></sub><var>p</var><sup><var>n</var>
</sup>
 with T<sub><var>n</var></sub> generated by the following random 
number generator

S<sub>0</sub>  290797
S<sub><var>n</var>1</sub>  S<sub><var>n</var></sub><sup>2</sup> mod 
50515093
T<sub><var>n</var></sub>  S<sub><var>n</var></sub> mod <var>p</var>

Let Nfac<var>p</var><var>q</var> be the factorial of N<var>p</var>
<var>q</var>
Let NF<var>p</var><var>q</var> be the number of factors <var>p</var> 
in Nfac<var>p</var><var>q</var>

You are given that NF310000 mod 3<sup>20</sup>624955285

Find NF6110<sup>7</sup> mod 61<sup>10</sup>
"""

def euler288():
    """
    >>> euler288()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()