"""
<P>A hypocycloid is the curve drawn by a point on a small circle 
rolling inside a larger circle The parametric equations of a 
hypocycloid centered at the origin and starting at the right most 
point is given by</P><P style="text-align:center">xt  R  r cost  r cos
frac R  r r t<BR />yt  R  r sint  r sinfrac R  r r t</P><P>Where <var>
R</var> is the radius of the large circle and <var>r</var> the radius 
of the small circle</P><P>Let CR r be the set of distinct points with 
integer coordinates on the hypocycloid with radius <var>R</var> and 
<var>r</var> and for which there is a corresponding value of <var>t
</var> such that sint and cost are rational numbers</P><P>Let SR r  
sum_xy in CR r x  y be the sum of the absolute values of the <var>x
</var> and <var>y</var> coordinates of the points in CR r</P><P>Let TN  
sum_R  3N sum_r1lfloor frac R  1 2 rfloor SR r be the sum of SR r for 
<var>R</var> and <var>r</var> positive integers Rleq N  and 2r 
< R$.</P><P>You are given<BR /><var>C</var>3 1  3 0 1 2 10 12<BR />
<BR /><var>C</var>2500 1000 <BR /><ul> 2500 0 772 2376 772 2376 516 
1792 516 1792 500 0 68 504 68 504<BR />1356 1088 1356 1088 1500 1000 
1500 1000</ul><i>Note 625 0 is not an element of C2500 1000 because 
sint is not a rational number for the corresponding values of <var>t
</var></i><P><var>S</var>3 1  3  0  1  2  1  0  1  2  10</P><P><var>T
</var>3  10 <var>T</var>10  524 <var>T</var>100  580442 <var>T</var>10
<sup>3</sup>  583108600<P>Find <var>T</var>10<sup>6</sup></P>
"""

def euler450():
    """
    >>> euler450()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()