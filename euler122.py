"""
The most naive way of computing <i>n</i><sup>15</sup> requires 
fourteen multiplications

<i>n</i> times <i>n</i> times  times <i>n</i>  <i>n</i><sup>15</sup>

But using a quotbinaryquot method you can compute it in six 
multiplications

<i>n</i> times <i>n</i>  <i>n</i><sup>2</sup>
<i>n</i><sup>2</sup> times <i>n</i><sup>2</sup>  <i>n</i><sup>4</sup>
<i>n</i><sup>4</sup> times <i>n</i><sup>4</sup>  <i>n</i><sup>8</sup>
<i>n</i><sup>8</sup> times <i>n</i><sup>4</sup>  <i>n</i><sup>12</sup>
<i>n</i><sup>12</sup> times <i>n</i><sup>2</sup>  <i>n</i><sup>14
</sup>
<i>n</i><sup>14</sup> times <i>n</i>  <i>n</i><sup>15</sup>

However it is yet possible to compute it in only five multiplications

<i>n</i> times <i>n</i>  <i>n</i><sup>2</sup>
<i>n</i><sup>2</sup> times <i>n</i>  <i>n</i><sup>3</sup>
<i>n</i><sup>3</sup> times <i>n</i><sup>3</sup>  <i>n</i><sup>6</sup>
<i>n</i><sup>6</sup> times <i>n</i><sup>6</sup>  <i>n</i><sup>12</sup>
<i>n</i><sup>12</sup> times <i>n</i><sup>3</sup>  <i>n</i><sup>15
</sup>

We shall define m<i>k</i> to be the minimum number of multiplications 
to compute <i>n</i><sup><i>k</i></sup> for example m15  5

For 1 le <i>k</i> le 200 find 
<span style='font-family:times new roman;font-size:13pt;'>sum</span> m
<i>k</i>
"""

def euler122():
    """
    >>> euler122()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()