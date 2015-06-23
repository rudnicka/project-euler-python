"""
The <b>look and say</b> sequence goes 1 11 21 1211 111221 312211 
13112221 1113213211 
The sequence starts with 1 and all other members are obtained by 
describing the previous member in terms of consecutive digits
It helps to do this out loud
1 is one one rarr 11
11 is two ones rarr 21
21 is one two and one one rarr 1211 
1211 is one one one two and two ones rarr 111221
111221 is three ones two twos and one one rarr 312211

Define An Bn and Cn as the number of ones twos and threes in the nth 
element of the sequence respectively
One can verify that A40  31254 B40  20259 and C40  11625

Find An Bn and Cn for n  10<sup>12</sup>
 Give your answer modulo 2<sup>30</sup> and separate your values for A 
B and C by a comma
 Eg for n  40 the answer would be 312542025911625
"""

def euler419():
    """
    >>> euler419()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()