"""
Build a triangle from all positive integers in the following way

 1
 <span style="color:red;">2</span>  <span style="color:red;">3</span>
 4  <span style="color:red;">5</span>  6
 <span style="color:red;">7</span>  8  9 10
<span style="color:red;">11</span> 12 <span style="color:red;">13
</span> 14 15
16 <span style="color:red;">17</span> 18 <span style="color:red;">19
</span> 20 21
22 <span style="color:red;">23</span> 24 25 26 27 28
<span style="color:red;">29</span> 30 <span style="color:red;">31
</span> 32 33 34 35 36
<span style="color:red;">37</span> 38 39 40 <span style="color:red;">
41</span> 42 <span style="color:red;">43</span> 44 45
46 <span style="color:red;">47</span> 48 49 50 51 52 
<span style="color:red;">53</span> 54 55
56 57 58 <span style="color:red;">59</span> 60 
<span style="color:red;">61</span> 62 63 64 65 66
  

Each positive integer has up to eight neighbours in the triangle

A set of three primes is called a <i>prime triplet</i> if one of the 
three primes has the other two as neighbours in the triangle

For example in the second row the prime numbers 2 and 3 are elements 
of some prime triplet

If row 8 is considered it contains two primes which are elements of 
some prime triplet ie 29 and 31
If row 9 is considered it contains only one prime which is an element 
of some prime triplet 37

Define S<var>n</var> as the sum of the primes in row <var>n</var> 
which are elements of any prime triplet
Then S860 and S937

You are given that S10000950007619

Find  S5678027  S7208785
"""

def euler196():
    """
    >>> euler196()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()