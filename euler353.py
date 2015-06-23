"""
A moon could be described by the sphere C<var>r</var> with centre 000 
and radius <var>r</var> 

There are stations on the moon at the points on the surface of C<var>r
</var> with integer coordinates The station at 00<var>r</var> is 
called North Pole station the station at 00<var>r</var> is called 
South Pole station

All stations are connected with each other via the shortest road on 
the great arc through the stations A journey between two stations is 
risky If <var>d</var> is the length of the road between two stations 
<var>d</var>pi <var>r</var><sup>2</sup> is a measure for the risk of 
the journey let us call it the risk of the road If the journey 
includes more than two stations the risk of the journey is the sum of 
risks of the used roads

A direct journey from  the North Pole station to the South Pole 
station has the length pi<var>r</var> and risk 1 The journey from the 
North Pole station to the South Pole station via 0<var>r</var>0 has 
the same length but a smaller risk frac12pi<var>r</var>pi<var>r</var>
<sup>2</sup>frac12pi<var>r</var>pi<var>r</var><sup>2</sup>05

The minimal risk of a journey from the North Pole station to the South 
Pole station on C<var>r</var> is M<var>r</var>

You are given that M701784943998  rounded to 10 digits behind the 
decimal point 

Find sumM2<sup>n</sup>1 for 1lenle15

Give your answer rounded to 10 digits behind the decimal point in the 
form abcdefghijk
"""

def euler353():
    """
    >>> euler353()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()