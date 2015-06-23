"""
Let N be a positive integer and let N be split into <var>k</var> equal 
parts <var>r</var>  N<var>k</var> so that N  <var>r</var>  <var>r
</var>    <var>r</var>
Let P be the product of these parts P  <var>r</var> times <var>r</var> 
times  times <var>r</var>  <var>r</var><sup><var>k</var></sup>

For example if 11 is split into five equal parts 11  22  22  22  22  2
2 then P  22<sup>5</sup>  5153632

Let MN  P<sub>max</sub> for a given value of N

It turns out that the maximum for N  11 is found by splitting eleven 
into four equal parts which leads to P<sub>max</sub>  114<sup>4</sup> 
that is M11  14641256  5719140625 which is a terminating decimal

However for N  8 the maximum is achieved by splitting it into three 
equal parts so M8  51227 which is a nonterminating decimal

Let DN  N if MN is a nonterminating decimal and DN  N if MN is a 
terminating decimal

For example SigmaDN for 5 le N le 100 is 2438

Find SigmaDN for 5 le N le 10000
"""

def euler183():
    """
    >>> euler183()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()