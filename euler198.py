"""
A best approximation to a real number <var>x</var> for the denominator 
bound <var>d</var> is a rational number <var>r</var><var>s</var> in 
reduced form with <var>s</var> le <var>d</var> so that any rational 
number <var>p</var><var>q</var> which is closer to <var>x</var> than 
<var>r</var><var>s</var> has <var>q</var> gt <var>d</var>

Usually the best approximation to a real number is uniquely determined 
for all denominator bounds However there are some exceptions eg 940 
has the two best approximations 14 and 15 for the denominator bound 6
We shall call a real number <var>x</var> <i>ambiguous</i> if there is 
at least one denominator bound for which <var>x</var> possesses two 
best approximations Clearly an ambiguous number is necessarily 
rational

How many ambiguous numbers <var>x</var>  <var>p</var><var>q</var>0 lt 
<var>x</var> lt 1100 are there whose denominator <var>q</var> does not 
exceed 10<sup>8</sup>
"""

def euler198():
    """
    >>> euler198()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()