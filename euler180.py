"""
For any integer <var>n</var> consider the three functions

<var>f</var><sub>1<var>n</var></sub><var>x</var><var>y</var><var>z
</var>  <var>x</var><sup><var>n</var>1</sup>  <var>y</var><sup><var>n
</var>1</sup> minus <var>z</var><sup><var>n</var>1</sup>
<var>f</var><sub>2<var>n</var></sub><var>x</var><var>y</var><var>z
</var>  <var>xy</var>  <var>yz</var>  <var>zx</var><var>x</var><sup>
<var>n</var>1</sup>  <var>y</var><sup><var>n</var>1</sup> minus <var>z
</var><sup><var>n</var>1</sup>
<var>f</var><sub>3<var>n</var></sub><var>x</var><var>y</var><var>z
</var>  <var>xyz</var><var>x</var><sup><var>n</var>2</sup>  <var>y
</var><sup><var>n</var>2</sup> minus <var>z</var><sup><var>n</var>2
</sup>

and their combination

<var>f</var><sub><var>n</var></sub><var>x</var><var>y</var><var>z
</var>  <var>f</var><sub>1<var>n</var></sub><var>x</var><var>y</var>
<var>z</var>  <var>f</var><sub>2<var>n</var></sub><var>x</var><var>y
</var><var>z</var> minus <var>f</var><sub>3<var>n</var></sub><var>x
</var><var>y</var><var>z</var>

We call <var>x</var><var>y</var><var>z</var> a golden triple of order 
<var>k</var> if <var>x</var> <var>y</var> and <var>z</var> are all 
rational numbers of the form <var>a</var>  <var>b</var> with
0 lt <var>a</var> lt <var>b</var> le <var>k</var> and there is at 
least one integer <var>n</var> so that <var>f</var><sub><var>n</var>
</sub><var>x</var><var>y</var><var>z</var>  0

Let <var>s</var><var>x</var><var>y</var><var>z</var>  <var>x</var>  
<var>y</var>  <var>z</var>
Let <var>t</var>  <var>u</var>  <var>v</var> be the sum of all 
distinct <var>s</var><var>x</var><var>y</var><var>z</var> for all 
golden triples <var>x</var><var>y</var><var>z</var> of order 35
 All the <var>s</var><var>x</var><var>y</var><var>z</var> and <var>t
</var>  must be in reduced form

Find <var>u</var>  <var>v</var>
"""

def euler180():
    """
    >>> euler180()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()