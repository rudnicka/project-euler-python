"""
Define the sequence a<sub>1</sub> a<sub>2</sub> a<sub>3</sub>  as<ul>
<li>a<sub>1</sub>  1</li><li>a<sub><var>n</var>1</sub>  6a<sub><var>n
</var></sub><sup>2</sup>  10a<sub><var>n</var></sub>  3 for <var>n
</var> ge 1</li></ul>

Examples
a<sub>3</sub>  2359
a<sub>6</sub>  269221280981320216750489044576319
a<sub>6</sub> mod 1 000 000 007  203064689
a<sub>100</sub> mod 1 000 000 007  456482974

Define B<var>x</var><var>y</var><var>n</var> as sum a<sub><var>n</var>
</sub> mod <var>p</var> for every prime <var>p</var> such that <var>x
</var> le <var>p</var> le <var>x</var><var>y</var>

Examples
B10<sup>9</sup> 10<sup>3</sup> 10<sup>3</sup>  23674718882
B10<sup>9</sup> 10<sup>3</sup> 10<sup>15</sup>  20731563854

Find B10<sup>9</sup> 10<sup>7</sup> 10<sup>15</sup>
"""

def euler492():
    """
    >>> euler492()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()