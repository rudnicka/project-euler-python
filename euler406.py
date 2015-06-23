"""
We are trying to find a hidden number selected from the set of 
integers 1 2  <var>n</var> by asking questions Each number question we 
ask we get one of three possible answers
<ul><li> Your guess is lower than the hidden number and you incur a 
cost of <var>a</var> or</li><li> Your guess is higher than the hidden 
number and you incur a cost of <var>b</var> or</li><li> Yes thats it 
and the game ends</li></ul>

Given the value of <var>n</var> <var>a</var> and <var>b</var> an <i>
optimal strategy</i> minimizes the total cost <u>for the worst 
possible case</u>

For example if <var>n</var>  5 <var>a</var>  2 and <var>b</var>  3 
then we may begin by asking <b>2</b> as our first question

If we are told that 2 is higher than the hidden number for a cost of 
<var>b</var>3 then we are sure that <b>1</b> is the hidden number for 
a total cost of <span style='color:blue;'><b>3</b></span>
If we are told that 2 is lower than the hidden number for a cost of 
<var>a</var>2 then our next question will be <b>4</b>
If we are told that 4 is higher than the hidden number for a cost of 
<var>b</var>3 then we are sure that <b>3</b> is the hidden number for 
a total cost of 23<span style='color:blue;'><b>5</b></span>
If we are told that 4 is lower than the hidden number for a cost of 
<var>a</var>2 then we are sure that <b>5</b> is the hidden number for 
a total cost of 22<span style='color:blue;'><b>4</b></span>
Thus the worstcase cost achieved by this strategy is 
<span style='color:red;'><b>5</b></span> It can also be shown that 
this is the lowest worstcase cost that can be achieved So in fact we 
have just described an optimal strategy for the given values of <var>n
</var> <var>a</var> and <var>b</var>

Let C<var>n</var> <var>a</var> <var>b</var> be the worstcase cost 
achieved by an optimal strategy for the given values of <var>n</var> 
<var>a</var> and <var>b</var>

Here are a few examples
C5 2 3  5
C500 radic2 radic3  1322073197
C20000 5 7  82
C2000000 radic5 radic7  4963755955

Let F<sub><var>k</var></sub> be the Fibonacci numbers F<sub><var>k
</var></sub>  F<sub><var>k</var>1</sub>  F<sub><var>k</var>2</sub> 
with base cases F<sub>1</sub>  F<sub>2</sub>  1
Find sum<sub>1le<var>k</var>le30</sub> C10<sup>12</sup> radic<var>k
</var> radicF<sub><var>k</var></sub> and give your answer rounded to 8 
decimal places behind the decimal point
"""

def euler406():
    """
    >>> euler406()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()