"""
For any positive integer n the <b>nth weak Goodstein sequence</b> g
<sub>1</sub> g<sub>2</sub> g<sub>3</sub>  is defined as<ul><li> g<sub>
1</sub>  <var>n</var><li> for <var>k</var> gt 1 g<sub><var>k</var>
</sub> is obtained by writing g<sub><var>k</var>1</sub> in base <var>k
</var> interpreting it as a base <var>k</var>  1 number and 
subtracting 1</ul>The sequence terminates when g<sub><var>k</var>
</sub> becomes 0

For example the 6th weak Goodstein sequence is 6 11 17 25 <ul><li> g
<sub>1</sub>  6<li> g<sub>2</sub>  11 since 6  110<sub>2</sub> 110
<sub>3</sub>  12 and 12  1  11<li> g<sub>3</sub>  17 since 11  102
<sub>3</sub> 102<sub>4</sub>  18 and 18  1  17<li> g<sub>4</sub>  25 
since 17  101<sub>4</sub> 101<sub>5</sub>  26 and 26  1  25</ul>and so 
on

It can be shown that every weak Goodstein sequence terminates

Let G<var>n</var> be the number of nonzero elements in the <var>n
</var>th weak Goodstein sequence
It can be verified that G2  3 G4  21 and G6  381
It can also be verified that SigmaG<var>n</var>  2517 for 1 le <var>n
</var> lt 8

Find the last 9 digits of SigmaG<var>n</var> for 1 le <var>n</var> lt 
16
"""

def euler396():
    """
    >>> euler396()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()