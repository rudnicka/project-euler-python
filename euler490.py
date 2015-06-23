"""
There are <var>n</var> stones in a pond numbered 1 to <var>n</var> 
Consecutive stones are spaced one unit apart

A frog sits on stone 1 He wishes to visit each stone exactly once 
stopping on stone <var>n</var> However he can only jump from one stone 
to another if they are at most 3 units apart In other words from stone 
<var>i</var> he can reach a stone <var>j</var> if 1 le <var>j</var> le 
<var>n</var> and <var>j</var> is in the set <var>i</var>3 <var>i</var>
2 <var>i</var>1 <var>i</var>1 <var>i</var>2 <var>i</var>3

Let f<var>n</var> be the number of ways he can do this For example f6  
14 as shown below
1 rarr 2 rarr 3 rarr 4 rarr 5 rarr 6 
1 rarr 2 rarr 3 rarr 5 rarr 4 rarr 6 
1 rarr 2 rarr 4 rarr 3 rarr 5 rarr 6 
1 rarr 2 rarr 4 rarr 5 rarr 3 rarr 6 
1 rarr 2 rarr 5 rarr 3 rarr 4 rarr 6 
1 rarr 2 rarr 5 rarr 4 rarr 3 rarr 6 
1 rarr 3 rarr 2 rarr 4 rarr 5 rarr 6 
1 rarr 3 rarr 2 rarr 5 rarr 4 rarr 6 
1 rarr 3 rarr 4 rarr 2 rarr 5 rarr 6 
1 rarr 3 rarr 5 rarr 2 rarr 4 rarr 6 
1 rarr 4 rarr 2 rarr 3 rarr 5 rarr 6 
1 rarr 4 rarr 2 rarr 5 rarr 3 rarr 6 
1 rarr 4 rarr 3 rarr 2 rarr 5 rarr 6 
1 rarr 4 rarr 5 rarr 2 rarr 3 rarr 6

Other examples are f10  254 and f40  1439682432976

Let S<var>L</var>  sum f<var>n</var><sup>3</sup> for 1 le <var>n</var> 
le <var>L</var>
Examples
S10  18230635
S20  104207881192114219
S1 000 mod 10<sup>9</sup>  225031475
S1 000 000 mod 10<sup>9</sup>  363486179

Find S10<sup>14</sup> mod 10<sup>9</sup>
"""

def euler490():
    """
    >>> euler490()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()