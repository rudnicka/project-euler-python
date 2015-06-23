"""
A positive integer with <var>k</var> decimal digits is called balanced 
if its first lceil<sup><var>k</var></sup><sub>2</sub>rceil digits sum 
to the same value as its last lceil<sup><var>k</var></sup><sub>2</sub>
rceil digits where lceil<var>x</var>rceil pronounced 
<span style="font-style: italic">ceiling</span> of <var>x</var> is the 
smallest integer ge <var>x</var> thus lceilpirceil  4 and lceil5rceil  
5

So for example all palindromes are balanced as is 13722

Let T<var>n</var> be the sum of all balanced numbers less than 10<sup>
<var>n</var></sup> 
Thus T1  45 T2  540 and T5  334795890 

Find T47 mod 3<sup>15</sup>
"""

def euler217():
    """
    >>> euler217()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()