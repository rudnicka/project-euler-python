"""
Each one of the 25 sheep in a flock must be tested for a rare virus 
known to affect 2 of the sheep populationAn accurate and extremely 
sensitive PCR test exists for blood samples producing a clear positive  
negative result but it is very timeconsuming and expensive

Because of the high cost the vetincharge suggests that instead of 
performing 25 separate tests the following procedure can be used 
instead

The sheep are split into 5 groups of 5 sheep in each group For each 
group the 5 samples are mixed together and a single test is performed 
Then<ul><li>If the result is negative all the sheep in that group are 
deemed to be virusfree</li><li>If the result is positive 5 additional 
tests will be performed a separate test for each animal to determine 
the affected individuals</li></ul>

Since the probability of infection for any specific animal is only 002 
the first test on the pooled samples for each group will be<ul><li>
Negative and no more tests needed with probability 098<sup>5</sup>  0
9039207968</li><li>Positive 5 additional tests needed with probability 
1  09039207968  00960792032</li></ul>

Thus the expected number of tests for each group is 1  00960792032 
times 5  1480396016
Consequently all 5 groups can be screened using an average of only 1
480396016 times 5  <b>740198008</b> tests which represents a huge 
saving of more than 70 

Although the scheme we have just described seems to be very efficient 
it can still be improved considerably always assuming that the test is 
sufficiently sensitive and that there are no adverse effects caused by 
mixing different samples Eg<ul><li>We may start by running a test on a 
mixture of all the 25 samples It can be verified that in about 6035 of 
the cases this test will be negative thus no more tests will be needed 
Further testing will only be required for the remaining 3965 of the 
cases</li><li>If we know that at least one animal in a group of 5 is 
infected and the first 4 individual tests come out negative there is 
no need to run a test on the fifth animal we know that it must be 
infected</li><li>We can try a different number of groups  different 
number of animals in each group adjusting those numbers at each level 
so that the total expected number of tests will be minimised</li></ul>
<P>To simplify the very wide range of possibilities there is one 
restriction we place when devising the most costefficient testing 
scheme whenever we start with a mixed sample all the sheep 
contributing to that sample must be fully screened ie a verdict of 
infected  virusfree must be reached for all of them before we start 
examining any other animals</P>For the current example it turns out 
that the most costefficient testing scheme well call it the <i>optimal 
strategy</i> requires an average of just <b>4155452</b> tests

Using the optimal strategy let T<var>s</var><var>p</var> represent the 
average number of tests needed to screen a flock of <var>s</var> sheep 
for a virus having probability <var>p</var> to be present in any 
individual
Thus rounded to six decimal places T25 002  4155452 and T25 010  12
702124

Find SigmaT10000 p for p001 002 003  050
Give your answer rounded to six decimal places
"""

def euler352():
    """
    >>> euler352()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()