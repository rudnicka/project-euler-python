"""
Let F<sub>5</sub><var>n</var> be the number of strings <var>s</var> 
such that<ul><li><var>s</var> consists only of 0s and 1s<li><var>s
</var> has length at most <var>n</var> and<li><var>s</var> contains a 
palindromic substring of length at least 5</ul>

For example F<sub>5</sub>4  0 F<sub>5</sub>5  8 F<sub>5</sub>6  42 and 
F<sub>5</sub>11  3844

Let D<var>L</var> be the number of integers <var>n</var> such that 5 
le <var>n</var> le <var>L</var> and F<sub>5</sub><var>n</var> is 
divisible by 87654321

For example D10<sup>7</sup>  0 and D5middot10<sup>9</sup>  51

Find D10<sup>18</sup>
"""

def euler486():
    """
    >>> euler486()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()