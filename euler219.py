"""
Let <span style="font-weight:bold">A</span> and 
<span style="font-weight:bold">B</span> be bit strings sequences of 0s 
and 1s
If <span style="font-weight:bold">A</span> is equal to the 
<span style="text-decoration:underline;">left</span>most length
<span style="font-weight:bold">A</span> bits of 
<span style="font-weight:bold">B</span> then 
<span style="font-weight:bold">A</span> is said to be a 
<span style="font-style:italic">prefix</span> of 
<span style="font-weight:bold">B</span>
For example 00110 is a prefix of 
<span style="text-decoration:underline;">00110</span>1001 but not of 
00111 or 100110

A <span style="font-style:italic">prefixfree code of size</span> <var>
n</var> is a collection of <var>n</var> distinct bit strings such that 
no string is a prefix of any other  For example this is a prefixfree 
code of size 6

0000 0001 001 01 10 11

Now suppose that it costs one penny to transmit a 0 bit but four pence 
to transmit a 1
Then the total cost of the prefixfree code shown above is 35 pence 
which happens to be the cheapest possible for the skewed pricing 
scheme in question
In short we write Cost6  35

What is Cost10<sup>9</sup> 
"""

def euler219():
    """
    >>> euler219()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()