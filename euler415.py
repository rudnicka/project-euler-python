"""
A set of lattice points S is called a <i>titanic set</i> if there 
exists a line passing through exactly two points in S

An example of a titanic set is S  0 0 0 1 0 2 1 1 2 0 1 0 where the 
line passing through 0 1 and 2 0 does not pass through any other point 
in S

On the other hand the set 0 0 1 1 2 2 4 4 is not a titanic set since 
the line passing through any two points in the set also passes through 
the other two

For any positive integer <var>N</var> let <var>T</var><var>N</var> be 
the number of titanic sets S whose every point <var>x</var> <var>y
</var> satisfies 0 le <var>x</var> <var>y</var> le <var>N</var>It can 
be verified that <var>T</var>1  11 <var>T</var>2  494 <var>T</var>4  
33554178 <var>T</var>111 mod 10<sup>8</sup>  13500401 and <var>T</var>
10<sup>5</sup> mod 10<sup>8</sup>  63259062

Find <var>T</var>10<sup>11</sup> mod 10<sup>8</sup>
"""

def euler415():
    """
    >>> euler415()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()