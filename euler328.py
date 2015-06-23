"""
We are trying to find a hidden number selected from the set of 
integers 1 2  <var>n</var> by asking questions Each number question we 
ask has a <u>cost equal to the number asked</u> and we get one of 
three possible answers
<ul><li> Your guess is lower than the hidden number or</li><li> Yes 
thats it or</li><li> Your guess is higher than the hidden number</li>
</ul>

Given the value of <var>n</var> an <i>optimal strategy</i> minimizes 
the total cost ie the sum of all the questions asked <u>for the worst 
possible case</u> Eg

If <var>n</var>3 the best we can do is obviously to ask the number <b>
2</b> The answer will immediately lead us to find the hidden number at 
a total cost  2

If <var>n</var>8 we might decide to use a binary search type of 
strategy Our first question would be <b>4</b> and if the hidden number 
is higher than 4 we will need one or two additional questions
Let our second question be <b>6</b> If the hidden number is still 
higher than 6 we will need a third question in order to discriminate 
between 7 and 8
Thus our third question will be <b>7</b> and the total cost for this 
worstcase scenario will be 467<span style='color:red;'><b>17</b>
</span>

We can improve considerably the worstcase cost for <var>n</var>8 by 
asking <b>5</b> as our first question
If we are told that the hidden number is higher than 5 our second 
question will be <b>7</b> then well know for certain what the hidden 
number is for a total cost of 57<span style='color:blue;'><b>12</b>
</span>
If we are told that the hidden number is lower than 5 our second 
question will be <b>3</b> and if the hidden number is lower than 3 our 
third question will be <b>1</b> giving a total cost of 531
<span style='color:blue;'><b>9</b></span>
Since <span style='color:blue;'><b>12</b></span>
<span style='color:blue;'><b>9</b></span> the worstcase cost for this 
strategy is <span style='color:red;'><b>12</b></span> Thats better 
than what we achieved previously with the binary search strategy it is 
also better than or equal to any other strategy
So in fact we have just described an optimal strategy for <var>n</var>
8

Let C<var>n</var> be the worstcase cost achieved by an optimal 
strategy for <var>n</var> as described above
Thus C1  0 C2  1 C3  2 and C8  12
Similarly C100  400 and 
<img style="vertical-align:middle" src="project/images/p328_sum1.gif" />
C<var>n</var>  17575

Find 
<img style="vertical-align:middle" src="project/images/p328_sum2.gif" />
C<var>n</var>
"""

def euler328():
    """
    >>> euler328()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()