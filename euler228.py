"""
Let <var>S</var><sub>n</sub> be the regular <var>n</var>sided polygon 
ndash or <i>shape</i> ndash whose vertices <var>v</var><sub><var>k
</var></sub> <var>k</var>thinspthinsp12hellip<var>n</var> have 
coordinates<table>  <tr>    <td width="40"></td>    <td><var>x</var>
<sub><var>k</var></sub> thinsp  thinsp        cos <sup>2<var>k</var>1
</sup><sub><var>n</var></sub> times180degthinsp</td>  </tr><tr>    
<td width="40"></td>    <td><var>y</var><sub><var>k</var></sub> thinsp 
          sin <sup>2<var>k</var>1</sup><sub><var>n</var></sub> times
180degthinsp</td>  </tr></table>

Each <var>S</var><sub><var>n</var></sub> is to be interpreted as a 
filled shape consisting of all points on the perimeter and in the 
interior

The <i>Minkowski sum</i> <var>S</var><var>T</var> of two shapes <var>S
</var> and <var>T</var> is the result of adding every point in <var>S
</var> to every point in <var>T</var> where point addition is 
performed coordinatewise <var>u</var>thinsp<var>v</var>  <var>x</var>
thinsp<var>y</var>  <var>u</var><var>x</var>thinsp<var>v</var><var>y
</var>

For example the sum of <var>S</var><sub>3</sub> and <var>S</var><sub>4
</sub> is the sixsided shape shown in pink below
<div style="text-align:center;">
<img src="project/images/p228.png" alt="picture showing S_3 + S_4" />
"""

def euler228():
    """
    >>> euler228()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()