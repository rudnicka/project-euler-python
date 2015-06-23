"""
An <span style="font-style: italic">axisaligned cuboid</span> 
specified by parameters  x<sub>0</sub>y<sub>0</sub>z<sub>0</sub> dxdy
dz  consists of all points XYZ such that x<sub>0</sub> le X le x<sub>0
</sub>dx y<sub>0</sub> le Y le y<sub>0</sub>dy and z<sub>0</sub> le Z 
le z<sub>0</sub>dz  The volume of the cuboid is the product dx times 
dy times dz  The <span style="font-style: italic">combined volume
</span> of a collection of cuboids is the volume of their union and 
will be less than the sum of the individual volumes if any cuboids 
overlap

Let C<sub>1</sub>C<sub>50000</sub> be a collection of 50000 axis
aligned cuboids such that C<sub><var>n</var></sub> has parameters

x<sub>0</sub>  S<sub>6<var>n</var>5</sub> modulo 10000
y<sub>0</sub>  S<sub>6<var>n</var>4</sub> modulo 10000
z<sub>0</sub>  S<sub>6<var>n</var>3</sub> modulo 10000
dx  1  S<sub>6<var>n</var>2</sub> modulo 399
dy  1  S<sub>6<var>n</var>1</sub> modulo 399
dz  1  S<sub>6<var>n</var></sub> modulo 399

where S<sub>1</sub>S<sub>300000</sub> come from the quotLagged 
Fibonacci Generatorquot

For 1 le <var>k</var> le 55 S<sub><var>k</var></sub>  100003  200003
<var>k</var>  300007<var>k</var><sup>3</sup>   modulo 1000000
For 56 le <var>k</var> S<sub><var>k</var></sub>  S<sub><var>k</var>24
</sub>  S<sub><var>k</var>55</sub>   modulo 1000000

Thus C<sub>1</sub> has parameters 7531839436956 C<sub>2</sub> has 
parameters 23833563507942212344 and so on

The combined volume of the first 100 cuboids C<sub>1</sub>C<sub>100
</sub> is 723581599

What is the combined volume of all 50000 cuboids C<sub>1</sub>C<sub>
50000</sub> 
"""

def euler212():
    """
    >>> euler212()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()