"""
The RSA encryption is based on the following procedure

Generate two distinct primes <var>p</var> and <var>q</var>
Compute <var>npq</var> and phi<var>p</var>1<var>q</var>1
Find an integer <var>e</var> 1lt<var>e</var>ltphi such that gcd<var>e
</var>phi1

A message in this system is a number in the interval 0<var>n</var>1
A text to be encrypted is then somehow converted to messages numbers 
in the interval 0<var>n</var>1
To encrypt the text  for each message <var>m</var> <var>c</var><var>m
</var><sup><var>e</var></sup> mod <var>n</var> is calculated

To decrypt the text the following procedure is needed calculate <var>d
</var> such that <var>ed</var>1 mod phi then for each encrypted 
message <var>c</var> calculate <var>mc<sup>d</sup></var> mod <var>n
</var>

There exist values of <var>e</var> and <var>m</var>  such that <var>m
<sup>e</sup></var> mod <var>nm</var>
We call messages <var>m</var> for which <var>m<sup>e</sup></var> mod 
<var>nm</var> unconcealed messages

An issue when choosing <var>e</var> is that there should not be too 
many unconcealed messages  
For instance let <var>p</var>19 and <var>q</var>37
Then <var>n</var>1937703 and phi1836648
If we choose <var>e</var>181 then although gcd1816481 it turns out 
that all possible messages
 <var>m</var> 0le<var>m</var>le<var>n</var>1 are unconcealed when 
calculating <var>m<sup>e</sup></var> mod <var>n</var>
For any valid choice of <var>e</var> there exist some unconcealed 
messages
Its important that the number of unconcealed messages is at a minimum

Choose <var>p</var>1009 and <var>q</var>3643
Find the sum of all values of <var>e</var> 1lt<var>e</var>ltphi1009
3643 and gcd<var>e</var>phi1 so that the number of unconcealed 
messages for this value of <var>e</var> is at a minimum
"""

def euler182():
    """
    >>> euler182()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()