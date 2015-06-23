"""
Let <var>n</var> be a positive integer
A 6sided die is thrown <var>n</var> times Let <var>c</var> be the 
number of pairs of consecutive throws that give the same value

For example if <var>n</var>  7 and the values of the die throws are 11
56663 then the following pairs of consecutive throws give the same 
value
<u>11</u>56663
115<u>66</u>63
1156<u>66</u>3
Therefore <var>c</var>  3 for 1156663

Define C<var>n</var> as the number of outcomes of throwing a 6sided 
die <var>n</var> times such that <var>c</var> does not exceed pi<var>n
</var><sup>1</sup>
For example C3  216 C4  1290 C11  361912500 and C24  
4727547363281250000

Define S<var>L</var> as sum C<var>n</var> for 1 le <var>n</var> le 
<var>L</var>
For example S50 mod 1 000 000 007  832833871

Find S50 000 000 mod 1 000 000 007

<sup>1</sup> pi denotes the <b>primecounting function</b> ie pi<var>n
</var> is the number of primes le <var>n</var>
"""

def euler423():
    """
    >>> euler423()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()