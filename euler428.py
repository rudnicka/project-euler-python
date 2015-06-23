"""
Let <var>a</var> <var>b</var> and <var>c</var> be positive numbers
Let W X Y Z be four collinear points where WX  <var>a</var> XY  <var>b
</var> YZ  <var>c</var> and WZ  <var>a</var>  <var>b</var>  <var>c
</var>
Let C<sub>in</sub> be the circle having the diameter XY
Let C<sub>out</sub> be the circle having the diameter WZ

The triplet <var>a</var> <var>b</var> <var>c</var> is called a <em>
necklace triplet</em> if you can place <var>k</var> ge 3 distinct 
circles C<sub>1</sub> C<sub>2</sub>  C<sub><var>k</var></sub> such 
that<ul><li>C<sub><var>i</var></sub> has no common interior points 
with any C<sub><var>j</var></sub> for 1 le <var>i</var> <var>j</var> 
le <var>k</var> and <var>i</var> ne <var>j</var><li>C<sub><var>i</var>
</sub> is tangent to both C<sub>in</sub> and C<sub>out</sub> for 1 le 
<var>i</var> le <var>k</var><li>C<sub><var>i</var></sub> is tangent to 
C<sub><var>i</var>1</sub> for 1 le <var>i</var> < <var>k</var> and<li>
C<sub><var>k</var></sub> is tangent to C<sub>1</sub></ul>

For example 5 5 5 and 4 3 21 are necklace triplets while it can be 
shown that 2 2 5 is not

<img src=project/images/p428_necklace.png>

Let T<var>n</var> be the number of necklace triplets <var>a</var> 
<var>b</var> <var>c</var> such that <var>a</var> <var>b</var> and 
<var>c</var> are positive integers and <var>b</var> le <var>n</var>For 
example T1  9 T20  732 and T3000  438106

Find T1 000 000 000
"""

def euler428():
    """
    >>> euler428()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()