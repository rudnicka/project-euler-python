"""
We want to tile a board of length <var>n</var> and height 1 completely 
with either 1 times 2 blocks or 1 times 1 blocks with a single decimal 
digit on top<img src="project/images/p440_tiles.png" />

For example here are some of the ways to tile a board of length <var>n
</var>  8<img src="project/images/p440_some8.png" />

Let T<var>n</var> be the number of ways to tile a board of length 
<var>n</var> as described above

For example T1  10 and T2  101

Let S<var>L</var> be the triple sum sum<sub><var>a</var><var>b</var>
<var>c</var></sub> gcdT<var>c</var><sup><var>a</var></sup> T<var>c
</var><sup><var>b</var></sup> for 1 le <var>a</var> <var>b</var> <var>
c</var> le <var>L</var>
For example
S2  10444
S3  1292115238446807016106539989
S4 mod 987 898 789  670616280

Find S2000 mod 987 898 789
"""

def euler440():
    """
    >>> euler440()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()