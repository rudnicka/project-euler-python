"""
<P>Two players Anton and Bernhard are playing the following game<BR />
There is one pile of n stones<BR />The first player may remove any 
positive number of stones but not the whole pile<BR />Thereafter each 
player may remove at most twice the number of stones his opponent took 
on the previous move<BR />The player who removes the last stone wins
</P><P>Eg n5<BR />If the first player takes anything more than one 
stone the next player will be able to take all remaining stones<BR />
If the first player takes one stone leaving four his opponent will 
take also one stone leaving three stones<BR />The first player cannot 
take all three because he may take at most 2x12 stones So lets say he 
takes also one stone leaving 2 The second player can take the two 
remaining stones and wins<BR />So 5 is a losing position for the first 
player<BR />For some winning positions there is more than one possible 
move for the first player<BR />Eg when n17 the first player can remove 
one or four stones</P><P>Let Mn be the maximum number of stones the 
first player can take from a winning position <i>at his first turn</i> 
and Mn0 for any other position</P><P>sumMn for nle100 is 728</P><P>
Find  sumMn for nle10<sup>18</sup>Give your answer modulo 10<sup>8
</sup></P>
"""

def euler366():
    """
    >>> euler366()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()