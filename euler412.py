"""
For integers <var>m</var> <var>n</var> 0 le <var>n</var> < <var>m
</var> let L<var>m</var> <var>n</var> be an <var>m</var>times<var>m
</var> grid with the topright <var>n</var>times<var>n</var> grid 
removed

For example L5 3 looks like this

<img src=project/images/p412_table53.png>

We want to number each cell of L<var>m</var> <var>n</var> with 
consecutive integers 1 2 3  such that the number in every cell is 
smaller than the number below it and to the left of it

For example here are two valid numberings of L5 3

<img src=project/images/p412_tablenums.png>

Let LC<var>m</var> <var>n</var> be the number of valid numberings of L
<var>m</var> <var>n</var>
It can be verified that LC3 0  42 LC5 3  250250 LC6 3  406029023400 
and LC10 5 mod 76543217  61251715

Find LC10000 5000 mod 76543217
"""

def euler412():
    """
    >>> euler412()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()