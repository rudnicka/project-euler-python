"""
<P>Jeff eats a pie in an unusual way<BR />The pie is circular He 
starts with slicing an initial cut in the pie along a radius<BR />
While there is at least a given fraction <var>F</var> of pie left he 
performs the following procedure<BR /> He makes two slices from the 
pie centre to any point of what is remaining of the pie border any 
point on the remaining pie border equally likely This will divide the 
remaining pie into three pieces<BR />  Going counterclockwise from the 
initial cut he takes the first two pie pieces and eats them<BR />When 
less than a fraction <var>F</var> of pie remains he does not repeat 
this procedure Instead he eats all of the remaining pie
<P align=center><img src=project/images/p394_eatpie.gif></P>

For <var>x</var> ge 1 let E<var>x</var> be the expected number of 
times Jeff repeats the procedure above with <var>F</var>  <sup>1</sup>
<sub><var>x</var></sub><BR />It can be verified that  E1  1 E2 asymp 1
2676536759 and E75 asymp 21215732071</P><P>Find E40 rounded to 10 
decimal places behind the decimal point</P>
"""

def euler394():
    """
    >>> euler394()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()