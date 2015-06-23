"""
<P>An integer partition of a number <var>n</var> is a way of writing 
<var>n</var> as a sum of positive integers</P><P>Partitions that 
differ only in the order of their summands are considered the sameA 
partition of <var>n</var> into <b>distinct parts</b> is a partition of 
<var>n</var> in which every part occurs at most once</P><P>The 
partitions of 5 into distinct parts are<BR/>5 41 and 32</P><P>Let f
<var>n</var> be the maximum product of the parts of any such partition 
of <var>n</var> into distinct parts and let m<var>n</var> be the 
number of elements of any such partition of <var>n</var> with that 
product</P><P>So f56 and m52</P><P>For <var>n</var>10 the partition 
with the largest product is 10235 which gives f1030 and m103<BR/>And 
their product f10middotm10  30middot3  90</P><P>It can be verified 
that<BR/>sumf<var>n</var>middotm<var>n</var> for 1 le <var>n</var> le 
100  1683550844462</P><P>Find sumf<var>n</var>middotm<var>n</var> for 
1 le <var>n</var> le 10<sup>14</sup><BR/>Give your answer modulo 
982451653 the 50 millionth prime</P>
"""

def euler374():
    """
    >>> euler374()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()