"""
A <b>cyclic number</b> with <var>n</var> digits has a very interesting 
property
When it is multiplied by 1 2 3 4  <var>n</var> all the products have 
exactly the same digits in the same order but rotated in a circular 
fashion

The smallest cyclic number is the 6digit number 142857 
142857 times 1  142857
142857 times 2  285714
142857 times 3  428571
142857 times 4  571428
142857 times 5  714285
142857 times 6  857142  

The next cyclic number is 0588235294117647 with 16 digits 
0588235294117647 times 1  0588235294117647
0588235294117647 times 2  1176470588235294
0588235294117647 times 3  1764705882352941
0588235294117647 times 16  9411764705882352

Note that for cyclic numbers leading zeros are important

There is only one cyclic number for which the eleven leftmost digits 
are 00000000137 and the five rightmost digits are 56789 ie it has the 
form 0000000013756789 with an unknown number of digits in the middle 
Find the sum of all its digits
"""

def euler358():
    """
    >>> euler358()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()