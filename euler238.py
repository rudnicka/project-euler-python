"""
<style type="text/css">tablep238 td  padding 0px 3px 0px 3px </style>

Create a sequence of numbers using the Blum Blum Shub pseudorandom 
number generator<center><table class="p238">  <tr>    
<td style="text-align:right"><var>s</var><sub>0</sub></td>    <td>
</td>    <td>14025256</td>  </tr><tr>    <td><var>s</var><sub><var>n
</var>1</sub></td>    <td></td>    <td><var>s</var><sub><var>n</var>
</sub><sup>2</sup> mod 20300713</td>  </tr></table></center>

Concatenate these numbers thinsp<var>s</var><sub>0</sub><var>s</var>
<sub>1</sub><var>s</var><sub>2</sub>hellip to create a string <var>w
</var> of infinite length
Then <var>w</var>thinspthinsp
<span style='font-family:courier new;font-size:12pt;color:#0000ff;'>
14025256741014958470038053646hellip</span>

For a positive integer <var>k</var> if no substring of <var>w</var> 
exists with a sum of digits equal to <var>k</var> <var>p</var><var>k
</var> is defined to be zero If at least one substring of <var>w</var> 
exists with a sum of digits equal to <var>k</var> we define <var>p
</var><var>k</var>thinspthinsp<var>z</var> where <var>z</var> is the 
starting position of the earliest such substring

For instance

The substrings 
<span style='font-family:courier new;font-size:12pt;color:#0000ff;'>1
</span> 
<span style='font-family:courier new;font-size:12pt;color:#0000ff;'>14
</span> 
<span style='font-family:courier new;font-size:12pt;color:#0000ff;'>
1402</span> hellip 
with respective sums of digits equal to 1 5 7 hellip
start at position <b>1</b> hence <var>p</var>1thinspthinsp<var>p</var>
5thinspthinsp<var>p</var>7thinspthinsphellipthinspthinsp<b>1</b>

The substrings 
<span style='font-family:courier new;font-size:12pt;color:#0000ff;'>4
</span> 
<span style='font-family:courier new;font-size:12pt;color:#0000ff;'>
402</span> 
<span style='font-family:courier new;font-size:12pt;color:#0000ff;'>
4025</span> hellip
with respective sums of digits equal to 4 6 11 hellip
start at position <b>2</b> hence <var>p</var>4thinspthinsp<var>p</var>
6thinspthinsp<var>p</var>11thinspthinsphellipthinspthinsp<b>2</b>

The substrings 
<span style='font-family:courier new;font-size:12pt;color:#0000ff;'>02
</span> 
<span style='font-family:courier new;font-size:12pt;color:#0000ff;'>
0252</span> hellip
with respective sums of digits equal to 2 9 hellip
start at position <b>3</b> hence <var>p</var>2thinspthinsp<var>p</var>
9thinspthinsphellipthinspthinsp<b>3</b>

Note that substring 
<span style='font-family:courier new;font-size:12pt;color:#0000ff;'>
025</span> starting at position <b>3</b> has a sum of digits equal to 
7 but there was an earlier substring starting at position <b>1</b> 
with a sum of digits equal to 7 so <var>p</var>7thinspthinsp1 <i>not
</i> 3

We can verify that for 0thinsp<&thinsp;<var>k</var>thinsplethinsp10
<sup>3</sup> sumthinsp<var>p</var><var>k</var>  4742

Find sumthinsp<var>p</var><var>k</var> for 0thinsp<&thinsp;<var>k
</var>thinsplethinsp2middot10<sup>15</sup>
"""

def euler238():
    """
    >>> euler238()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()