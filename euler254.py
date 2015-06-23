"""
Define f<var>n</var> as the sum of the factorials of the digits of 
<var>n</var> For example f342  3  4  2  32

Define sf<var>n</var> as the sum of the digits of f<var>n</var> So sf
342  3  2  5

Define g<var>i</var> to be the smallest positive integer <var>n</var> 
such that sf<var>n</var>  <var>i</var> Though sf342 is 5 sf25 is also 
5 and it can be verified that g5 is 25

Define sg<var>i</var> as the sum of the digits of g<var>i</var> So sg5  
2  5  7

Further it can be verified that g20 is 267 and sumthinspsg<var>i</var> 
for 1 le <var>i</var> le 20 is 156

What is sumthinspsg<var>i</var> for 1 le <var>i</var> le 150
"""

def euler254():
    """
    >>> euler254()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()