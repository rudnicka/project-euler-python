"""
For an integer <var>n</var> ge 4 we define the <i>lower prime square 
root</i> of <var>n</var> denoted by lps<var>n</var> as the largest 
prime le radic<var>n</var> and the <i>upper prime square root</i> of 
<var>n</var> ups<var>n</var> as the smallest prime ge radic<var>n
</var>

So for example lps4  2  ups4 lps1000  31 ups1000  37
Let us call an integer <var>n</var> ge 4 <i>semidivisible</i> if one 
of lps<var>n</var> and ups<var>n</var> divides <var>n</var> but not 
both

The sum of the semidivisible numbers not exceeding 15 is 30 the 
numbers are 8 10 and 12
 15 is not semidivisible because it is a multiple of both lps15  3 and 
ups15  5
As a further example the sum of the 92 semidivisible numbers up to 
1000 is 34825

What is the sum of all semidivisible numbers not exceeding 
999966663333 
"""

def euler234():
    """
    >>> euler234()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()