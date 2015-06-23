"""
We say that a <var>d</var>digit positive number no leading zeros is a 
onechild number if exactly one of its substrings is divisible by <var>
d</var>

For example 5671 is a 4digit onechild number Among all its substrings 
5 6 7 1 56 67 71 567 671 and 5671 only 56 is divisible by 4
Similarly 104 is a 3digit onechild number because only 0 is divisible 
by 3
1132451 is a 7digit onechild number because only 245 is divisible by 7

Let F<var>N</var> be the number of the onechild numbers less than 
<var>N</var>
We can verify that F10  9 F10<sup>3</sup>  389 and F10<sup>7</sup>  
277674

Find F10<sup>19</sup>
"""

def euler413():
    """
    >>> euler413()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()