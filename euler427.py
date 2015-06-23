"""
A sequence of integers S  s<sub><var>i</var></sub> is called an <var>n
sequence</var> if it has <var>n</var> elements and each element s<sub>
<var>i</var></sub> satisfies 1 le s<sub><var>i</var></sub> le <var>n
</var> Thus there are <var>n</var><sup><var>n</var></sup> distinct 
<var>n</var>sequences in totalFor example the sequence S  1 5 5 10 7 7 
7 2 3 7 is a 10sequence

For any sequence S let LS be the length of the longest contiguous 
subsequence of S with the same valueFor example for the given sequence 
S above LS  3 because of the three consecutive 7s

Let <var>f</var><var>n</var>  sum LS for all <var>n</var>sequences S

For example <var>f</var>3  45 <var>f</var>7  1403689 and <var>f</var>
11  481496895121

Find <var>f</var>7 500 000 mod 1 000 000 009
"""

def euler427():
    """
    >>> euler427()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()