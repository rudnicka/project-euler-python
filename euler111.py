"""
Considering 4digit primes containing repeated digits it is clear that 
they cannot all be the same 1111 is divisible by 11 2222 is divisible 
by 22 and so on But there are nine 4digit primes containing three ones

1117 1151 1171 1181 1511 1811 2111 4111 8111

We shall say that M<i>n</i> <i>d</i> represents the maximum number of 
repeated digits for an <i>n</i>digit prime where <i>d</i> is the 
repeated digit N<i>n</i> <i>d</i> represents the number of such primes 
and S<i>n</i> <i>d</i> represents the sum of these primes

So M4 1  3 is the maximum number of repeated digits for a 4digit prime 
where one is the repeated digit there are N4 1  9 such primes and the 
sum of these primes is S4 1  22275 It turns out that for <i>d</i>  0 
it is only possible to have M4 0  2 repeated digits but there are N4 0  
13 such cases

In the same way we obtain the following results for 4digit primes
<div style='text-align:center;'>
<table align='center' border='1' cellspacing='0' cellpadding='5'><tr>
<td><b>Digit <i>d</i></b></td><td><b>M4 <i>d</i></b></td><td><b>N4 <i>
d</i></b></td><td><b>S4 <i>d</i></b></td></tr><tr><td>0</td><td>2</td>
<td>13</td><td>67061</td></tr><tr><td>1</td><td>3</td><td>9</td><td>
22275</td></tr><tr><td>2</td><td>3</td><td>1</td><td>2221</td></tr>
<tr><td>3</td><td>3</td><td>12</td><td>46214</td></tr><tr><td>4</td>
<td>3</td><td>2</td><td>8888</td></tr><tr><td>5</td><td>3</td><td>1
</td><td>5557</td></tr><tr><td>6</td><td>3</td><td>1</td><td>6661</td>
</tr><tr><td>7</td><td>3</td><td>9</td><td>57863</td></tr><tr><td>8
</td><td>3</td><td>1</td><td>8887</td></tr><tr><td>9</td><td>3</td>
<td>7</td><td>48073</td></tr></table>
"""

def euler111():
    """
    >>> euler111()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()