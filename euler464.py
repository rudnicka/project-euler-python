"""
The <b>Moumlbius function</b> denoted <var>mu</var><var>n</var> is 
defined as<ul><li><var>mu</var><var>n</var>  1<sup><var>omega</var>
<var>n</var></sup> if <var>n</var> is squarefree where <var>omega
</var><var>n</var> is the number of distinct prime factors of <var>n
</var></li><li><var>mu</var><var>n</var>  0 if <var>n</var> is not 
squarefree</li></ul>

Let P<var>a</var><var>b</var> be the number of integers <var>n</var> 
in the interval <var>a</var><var>b</var> such that <var>mu</var><var>n
</var>  1
Let N<var>a</var><var>b</var> be the number of integers <var>n</var> 
in the interval <var>a</var><var>b</var> such that <var>mu</var><var>n
</var>  1
For example P210  2 and N210  4

Let C<var>n</var> be the number of integer pairs <var>a</var><var>b
</var> such that<ul><li> 1 le <var>a</var> le <var>b</var> le <var>n
</var></li><li> 99middotN<var>a</var><var>b</var> le 100middotP<var>a
</var><var>b</var> and</li><li> 99middotP<var>a</var><var>b</var> le 
100middotN<var>a</var><var>b</var></li></ul>

For example C10  13 C500  16676 and C10 000  20155319

Find C20 000 000
"""

def euler464():
    """
    >>> euler464()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()