"""
Albert chooses a positive integer <var>k</var> then two real numbers 
<var>a</var> <var>b</var> are randomly chosen in the interval 01 with 
uniform distribution
The square root of the sum <var>k</var>middot<var>a</var>1<sup>2</sup>
thinspthinsp<var>k</var>middot<var>b</var>1<sup>2</sup> is then 
computed and rounded to the nearest integer If the result is equal to 
<var>k</var> he scores <var>k</var> points otherwise he scores nothing

For example if <var>k</var>thinspthinsp6 <var>a</var>thinspthinsp02 
and <var>b</var>thinspthinsp085 then <var>k</var>middot<var>a</var>1
<sup>2</sup>thinspthinsp<var>k</var>middot<var>b</var>1<sup>2</sup>
thinspthinsp4205
The square root of 4205 is 6484 and when rounded to the nearest 
integer it becomes 6
This is equal to <var>k</var> so he scores 6 points

It can be shown that if he plays 10 turns with <var>k</var>thinsp
thinsp1 <var>k</var>thinspthinsp2  <var>k</var>thinspthinsp10 the 
expected value of his total score rounded to five decimal places is 10
20914

If he plays 10<sup>5</sup> turns with <var>k</var>thinspthinsp1 <var>k
</var>thinspthinsp2 <var>k</var>thinspthinsp3  <var>k</var>thinsp
thinsp10<sup>5</sup> what is the expected value of his total score 
rounded to five decimal places
"""

def euler285():
    """
    >>> euler285()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()