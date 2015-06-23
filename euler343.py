"""
For any positive integer <var>k</var> a finite sequence a<sub><var>i
</var></sub> of fractions x<sub><var>i</var></sub>y<sub><var>i</var>
</sub> is defined by
a<sub>1</sub>  1<var>k</var> and
a<sub><var>i</var></sub>  x<sub><var>i</var>1</sub>1y<sub><var>i</var>
1</sub>1 reduced to lowest terms for <var>i</var>1
When a<sub><var>i</var></sub> reaches some integer <var>n</var> the 
sequence stops That is when y<sub><var>i</var></sub>1
Define f<var>k</var>  <var>n</var> 
For example for <var>k</var>  20

120 rarr 219 rarr 318  16 rarr 25 rarr 34 rarr 43 rarr 52 rarr 61  6

So f20  6

Also f1  1 f2  2 f3  1 and Sigmaf<var>k</var><sup>3</sup>  118937 for 
1 le <var>k</var> le 100

Find Sigmaf<var>k</var><sup>3</sup> for 1 le <var>k</var> le 2times10
<sup>6</sup>
"""

def euler343():
    """
    >>> euler343()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()