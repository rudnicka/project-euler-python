"""
<style type="text/css">tablep375 td   padding 0px 3px 0px 3px  
verticalalign bottom  textalign left</style>

Let <var>S</var><sub><var>n</var></sub> be an integer sequence 
produced with the following pseudorandom number generator<center>
<table class="p375">  <tr>    <td style="text-align:right"><var>S
</var><sub>0</sub></td>    <td><sub> </sub></td>    <td>290797<sub> 
</sub></td>  </tr><tr>    <td><var>S</var><sub><var>n</var>1</sub>
</td>    <td><sub> </sub></td>    <td><var>S</var><sub><var>n</var>
</sub><sup>2</sup> mod 50515093</td>  </tr></table></center>

Let A<var>i</var> <var>j</var> be the minimum of the numbers <var>S
</var><sub><var>i</var></sub> <var>S</var><sub><var>i</var>1</sub>   
<var>S</var><sub><var>j</var></sub> for <var>i</var> le <var>j</var>
Let M<var>N</var>  SigmaA<var>i</var> <var>j</var> for 1 le <var>i
</var> le <var>j</var> le <var>N</var>
We can verify that M10  432256955 and M10 000  3264567774119

Find M2 000 000 000
"""

def euler375():
    """
    >>> euler375()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()