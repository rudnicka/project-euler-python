"""
As we all know the equation <var>x</var><sup>2</sup>1 has no solutions 
for real <var>x</var>
If we however introduce the imaginary number <var>i</var> this 
equation has two solutions <var>xi</var> and <var>xi</var>
If we go a step further the equation <var>x</var>3<sup>2</sup>4 has 
two complex solutions <var>x</var>32<var>i</var> and <var>x</var>32
<var>i</var>
<var>x</var>32<var>i</var> and <var>x</var>32<var>i</var> are called 
each others complex conjugate
Numbers of the form <var>a</var><var>bi</var> are called complex 
numbers
In general <var>a</var><var>bi</var> and <var>a</var>minus<var>bi
</var> are each others complex conjugate

A Gaussian Integer is a complex number <var>a</var><var>bi</var> such 
that both <var>a</var> and <var>b</var> are integers
The regular integers are also Gaussian integers with <var>b</var>0
To distinguish them from Gaussian integers with <var>b</var> ne 0 we 
call such integers quotrational integersquot
A Gaussian integer is called a divisor of a rational integer <var>n
</var> if the result is also a Gaussian integer
If for example we divide 5 by 12<var>i</var> we can simplify 
<img src="project/images/p153_formule1.gif" border="0" style="vertical-align:middle" alt="" /> 
in the following manner
Multiply numerator and denominator by the complex conjugate of 12<var>
i</var> 1minus2<var>i</var>
The result is 
<img src="project/images/p153_formule2.gif" border="0" alt="" style="vertical-align:middle;" />
So 12<var>i</var> is a divisor of 5
Note that 1<var>i</var> is not a divisor of 5 because 
<img src="project/images/p153_formule5.gif" border="0" style="vertical-align:middle;" alt="" />
Note also that if the Gaussian Integer <var>a</var><var>bi</var> is a 
divisor of a rational integer <var>n</var> then its complex conjugate 
<var>a</var>minus<var>bi</var> is also a divisor of <var>n</var>

In fact 5 has six divisors such that the real part is positive 1 1  2
<var>i</var> 1 minus 2<var>i</var> 2  <var>i</var> 2 minus <var>i
</var> 5
The following is a table of all of the divisors for the first five 
positive rational integers<table align="center" border="1"><tr>
<td width="20"><var>n</var></td><td> Gaussian integer divisors
with positive real part</td><td>Sum s<var>n</var> of 
thesedivisors</td></tr><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>
2</td><td>1 1<var>i</var> 1<var>i</var> 2</td><td>5</td></tr><tr><td>3
</td><td>1 3</td><td>4</td></tr><tr><td>4</td><td>1 1<var>i</var> 1
<var>i</var> 2 22<var>i</var> 22<var>i</var>4</td><td>13</td></tr><tr>
<td>5</td><td>1 12<var>i</var> 12<var>i</var> 2<var>i</var> 2<var>i
</var> 5</td><td>12</td></tr></table>

For divisors with positive real parts then we have 
<img src="project/images/p153_formule6.gif" border="0" style="vertical-align:middle" alt="" />

For 1 le <var>n</var> le 10<sup>5</sup> sum s<var>n</var>17924657155

What is sum s<var>n</var> for 1 le <var>n</var> le 10<sup>8</sup>
"""

def euler153():
    """
    >>> euler153()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()