"""
A modified Collatz sequence of integers is obtained from a starting 
value a<sub>1</sub> in the following way

<var>a<sub>n1</sub></var>  <var>a<sub>n</sub></var>3 if <var>a<sub>n
</sub></var> is divisible by 3 We shall denote this as a large 
downward step D

<var>a<sub>n1</sub></var>  4<var>a<sub>n</sub></var>  23 if <var>a
<sub>n</sub></var> divided by 3 gives a remainder of 1 We shall denote 
this as an upward step U

<var>a<sub>n1</sub></var>  2<var>a<sub>n</sub></var>  13 if <var>a
<sub>n</sub></var> divided by 3 gives a remainder of 2 We shall denote 
this as a small downward step d

The sequence terminates when some <var>a<sub>n</sub></var>  1

Given any integer we can list out the sequence of steps
For instance if <var>a</var><sub>1</sub>231 then the sequence <var>a
<sub>n</sub></var>2317751171171014931 corresponds to the steps 
DdDddUUdDD

Of course there are other sequences that begin with that same sequence 
DdDddUUdDD
For instance if <var>a</var><sub>1</sub>1004064 then the sequence is 
DdDddUUdDDDdUDUUUdDdUUDDDUdDD
In fact 1004064 is the smallest possible <var>a</var><sub>1</sub> gt 
10<sup>6</sup> that begins with the sequence DdDddUUdDD

What is the smallest <var>a</var><sub>1</sub> gt 10<sup>15</sup> that 
begins with the sequence UDDDUdddDDUDDddDdDddDDUDDdUUDd
"""

def euler277():
    """
    >>> euler277()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()