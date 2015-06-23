"""
For any two strings of digits A and B we define F<sub>AB</sub> to be 
the sequence ABABBABABBAB in which each term is the concatenation of 
the previous two

Further we define D<sub>AB</sub><var>n</var> to be the <var>n</var>
<sup>th</sup> digit in the first term of F<sub>AB</sub> that contains 
at least <var>n</var> digits

Example

Let A1415926535 B8979323846 We wish to find D<sub>AB</sub>35 say

The first few terms of F<sub>AB</sub> are
1415926535
8979323846
14159265358979323846
897932384614159265358979323846
1415926535897932384689793238461415<span style="color: #FF0000"><b>9
</b></span>265358979323846

Then D<sub>AB</sub>35 is the 35<sup>th</sup> digit in the fifth term 
which is 9

Now we use for A the first 100 digits of pi behind the decimal point

14159265358979323846264338327950288419716939937510 
58209749445923078164062862089986280348253421170679 

and for B the next hundred digits

82148086513282306647093844609550582231725359408128 
48111745028410270193852110555964462294895493038196 

Find sum<sub><var>n</var>  0117</sub>   10<sup><var>n</var></sup>times 
D<sub>AB</sub>12719<var>n</var>times7<sup><var>n</var></sup> 
"""

def euler230():
    """
    >>> euler230()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()