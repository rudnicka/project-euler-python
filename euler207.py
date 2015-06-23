"""
For some positive integers <var>k</var> there exists an integer 
partition of the form   4<sup>t</sup>  2<sup>t</sup>  <var>k</var>
where 4<sup>t</sup> 2<sup>t</sup> and <var>k</var> are all positive 
integers and <var>t</var> is a real number

The first two such partitions are 4<sup>1</sup>  2<sup>1</sup>  2 and 
4<sup>15849625</sup>  2<sup>15849625</sup>  6

Partitions where <var>t</var> is also an integer are called <i>perfect
</i>
 For any <var>m</var> ge 1 let P<var>m</var> be the proportion of such 
partitions that are perfect with <var>k</var> le <var>m</var>
Thus P6  12

In the following table are listed some values of P<var>m</var>

   P5  11
   P10  12
   P15  23
   P20  12
   P25  12
   P30  25
   
   P180  14
   P185  313

Find the smallest <var>m</var> for which P<var>m</var> lt 112345
"""

def euler207():
    """
    >>> euler207()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()