"""
The radical of <i>n</i> rad<i>n</i> is the product of distinct prime 
factors of <i>n</i> For example 504  2<sup>3</sup> times 3<sup>2</sup> 
times 7 so rad504  2 times 3 times 7  42

We shall define the triplet of positive integers <i>a</i> <i>b</i> <i>
c</i> to be an abchit if<ol><li>GCD<i>a</i> <i>b</i>  GCD<i>a</i> <i>c
</i>  GCD<i>b</i> <i>c</i>  1</li><li><i>a</i> lt <i>b</i></li><li><i>
a</i>  <i>b</i>  <i>c</i></li><li>rad<i>abc</i> lt <i>c</i></li></ol>

For example 5 27 32 is an abchit because<ol><li>GCD5 27  GCD5 32  GCD
27 32  1</li><li>5 lt 27</li><li>5  27  32</li><li>rad4320  30 lt 32
</li></ol>

It turns out that abchits are quite rare and there are only thirtyone 
abchits for <i>c</i> lt 1000 with sum<i>c</i>  12523

Find sum<i>c</i> for <i>c</i> lt 120000
"""

def euler127():
    """
    >>> euler127()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()