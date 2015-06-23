"""
<P>Define the sequence an as the number of adjacent pairs of ones in 
the binary expansion of n possibly overlapping<BR/>Eg a5  a101<sub>2
</sub>  0 a6  a110<sub>2</sub>  1 a7  a111<sub>2</sub>  2</P><P>Define 
the sequence bn  1<sup>an</sup><BR/>This sequence is called the <B>
RudinShapiro</B> sequence</P><P>Also consider the summatory sequence 
of bn 
<img src=project/images/p384_formula.gif style="margin-top:-9px;"></P>
<P>The first couple of values of these sequences are<BR/><TT>n    nbsp
   0 nbsp   1 nbsp   2 nbsp   3 nbsp   4 nbsp   5 nbsp   6 nbsp   7
<BR/>an nbsp   0 nbsp   0 nbsp   0 nbsp   1 nbsp   0 nbsp   0 nbsp   1 
nbsp   2<BR/>bn nbsp   1 nbsp   1 nbsp   1 nbsp  1 nbsp   1 nbsp   1 
nbsp  1 nbsp   1<BR/>sn nbsp   1 nbsp   2 nbsp   3 nbsp   2 nbsp   3 
nbsp   4 nbsp   3 nbsp   4</TT></P><P>The sequence sn has the 
remarkable property that all elements are positive and every positive 
integer k occurs exactly k times</P><P>Define gtc with 1 le c le t as 
the index in sn for which t occurs for the cth time in sn<BR/>Eg g33  
6 g42  7 and g5432112345  1220847710</P><P>Let Fn be the fibonacci 
sequence defined by<BR/>F0F11 and<BR/>FnFn1Fn2 for n1</P><P>Define GFt
gFtFt1</P><P>Find SigmaGFt for 2letle45</P>
"""

def euler384():
    """
    >>> euler384()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()