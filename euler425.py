"""
<P>Two positive numbers A and B are said to be <i>connected</i> 
denoted by A harr B if one of these conditions holds<BR />1 A and B 
have the same length and differ in exactly one digit for example 123 
harr 173<BR />2 Adding one digit to the left of A or B makes B or A 
for example 23 harr 223 and 123 harr 23</P><P>We call a prime P a <i>2
s relative</i> if there exists a chain of connected primes between 2 
and P and no prime in the chain exceeds P</P><P>For example 127 is a 2
s relative One of the possible chains is shown below<BR />2 harr 3 
harr 13 harr 113 harr 103 harr 107 harr 127<BR />However 11 and 103 
are not 2s relatives</P><P>Let FN be the sum of the primes le N which 
are not 2s relatives<BR />We can verify that F10<sup>3</sup>  431 and 
F10<sup>4</sup>  78728</P><P>Find F10<sup>7</sup></P>
"""

def euler425():
    """
    >>> euler425()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()