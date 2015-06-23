"""
<P>The Collatz sequence is defined asa_i1  left  largefrac a_i 2 atop 
3 a_i1 textif a_itext is even atop textif a_itext is odd right</P><P>
The Collatz conjecture states that starting from any positive integer 
the sequence eventually reaches the cycle 1421<BR />We shall define 
the sequence prefix <var>pn</var> for the Collatz sequence starting 
with <var>a<sub>1</sub>  n</var> as the subsequence of all numbers not 
a power of 2 2<sup>0</sup>1 is considered a power of 2 for this 
problem For example<BR /><var>p</var>13  13 40 20 10 5 <BR/><var>p
</var>8  <BR />Any number invalidating the conjecture would have an 
infinite length sequence prefix</P><P>Let <var>S<sub>m</sub></var> be 
the set of all sequence prefixes of length <var>m</var> Two sequences 
a<sub>1</sub> a<sub>2</sub>  a<sub><var>m</var></sub></var> and b<sub>
1</sub> b<sub>2</sub>  b<sub><var>m</var></sub> in <var>S<sub>m</sub>
</var> are said to belong to the same prefix family if a<sub>i</sub> 
< a<sub>j</sub> if and only if b<sub>i</sub> < b<sub>j</sub> for all 1 
le ij le<var> m</var></P><P>For example in <var>S</var><sub>4</sub> 6 
3 10 5 is in the same family as 454 227 682 341 but not 113 340 170 85
<BR />Let <var>fm</var> be the number of distinct prefix families in 
<var>S<sub>m</sub></var><BR />You are given <var>f</var>5  5 <var>f
</var>10  55 <var>f</var>20  6771</P><P>Find f90</P>
"""

def euler494():
    """
    >>> euler494()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()