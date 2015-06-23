"""
Define f01 and f<var>n</var> to be the number of ways to write <var>n
</var> as a sum of powers of 2 where no power occurs more than twice 

For example f105 since there are five different ways to express 10
10  82  811  442  42211  4411

It can be shown that for every fraction <var>pq</var> <var>p</var>gt0 
<var>q</var>gt0 there exists at least one integer <var>n</var> such 
that
 f<var>n</var>f<var>n</var>1<var>pq</var>

For instance the smallest <var>n</var> for which f<var>n</var>f<var>n
</var>11317 is 241
The binary expansion of 241 is 11110001
Reading this binary number from the most significant bit to the least 
significant bit there are 4 ones 3 zeroes and 1 one We shall call the 
string 431 the <span style="font-style: italic">Shortened Binary 
Expansion</span> of 241

Find the Shortened Binary Expansion of the smallest <var>n</var> for 
which
 f<var>n</var>f<var>n</var>1123456789987654321

Give your answer as comma separated integers without any whitespaces
"""

def euler175():
    """
    >>> euler175()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()