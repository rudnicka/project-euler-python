"""
Let us consider <b>mixtures</b> of three substances <b>A</b> <b>B</b> 
and <b>C</b> A mixture can be described by a ratio of the amounts of 
<b>A</b> <b>B</b> and <b>C</b> in it ie <var>a</var>  <var>b</var>  
<var>c</var> For example a mixture described by the ratio 2  3  5 
contains 20 <b>A</b> 30 <b>B</b> and 50 <b>C</b>

For the purposes of this problem we cannot separate the individual 
components from a mixture However we can combine different amounts of 
different mixtures to form mixtures with new ratios

For example say we have three mixtures with ratios 3  0  2 3  6  11 
and 3  3  4 By mixing 10 units of the first 20 units of the second and 
30 units of the third we get a new mixture with ratio 6  5  9 since
10middot<sup>3</sup><sub>5</sub>  20middot<sup>3</sup><sub>20</sub>  
30middot<sup>3</sup><sub>10</sub>  10middot<sup>0</sup><sub>5</sub>  
20middot<sup>6</sup><sub>20</sub>  30middot<sup>3</sup><sub>10</sub>  
10middot<sup>2</sup><sub>5</sub>  20middot<sup>11</sup><sub>20</sub>  
30middot<sup>4</sup><sub>10</sub> 18  15  27  6  5  9

However with the same three mixtures it is impossible to form the 
ratio 3  2  1 since the amount of <b>B</b> is always less than the 
amount of <b>C</b>

Let <var>n</var> be a positive integer Suppose that for every triple 
of integers <var>a</var> <var>b</var> <var>c</var> with 0 le <var>a
</var> <var>b</var> <var>c</var> le <var>n</var> and gcd<var>a</var> 
<var>b</var> <var>c</var>  1 we have a mixture with ratio <var>a</var>  
<var>b</var>  <var>c</var> Let M<var>n</var> be the set of all such 
mixtures

For example M2 contains the 19 mixtures with the following ratios
0  0  1 0  1  0 0  1  1 0  1  2 0  2  1 
1  0  0 1  0  1 1  0  2 1  1  0 1  1  1 
1  1  2 1  2  0 1  2  1 1  2  2 2  0  1 
2  1  0 2  1  1 2  1  2 2  2  1

Let E<var>n</var> be the number of subsets of M<var>n</var> which can 
produce the mixture with ratio 1  1  1 ie the mixture with equal parts 
<b>A</b> <b>B</b> and <b>C</b> 
We can verify that E1  103 E2  520447 E10 mod 11<sup>8</sup>  82608406 
and E500 mod 11<sup>8</sup>  13801403
Find E10 000 000 mod 11<sup>8</sup>
"""

def euler478():
    """
    >>> euler478()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()