"""
Let <b><i>D</i></b><sub>0</sub> be the twoletter string quotFaquot  
For nge1 derive <b><i>D</i></b><sub>n</sub> from <b><i>D</i></b><sub>n
1</sub> by the stringrewriting rules

quotaquot rarr quotaRbFRquot
quotbquot rarr quotLFaLbquot

Thus <b><i>D</i></b><sub>0</sub>  quotFaquot <b><i>D</i></b><sub>1
</sub>  quotFaRbFRquot <b><i>D</i></b><sub>2</sub>  quotFaRbFRRLFaLbFR
quot and so on

These strings can be interpreted as instructions to a computer 
graphics program with quotFquot meaning quotdraw forward one unitquot 
quotLquot meaning quotturn left 90 degreesquot quotRquot meaning quot
turn right 90 degreesquot and quotaquot and quotbquot being ignored  
The initial position of the computer cursor is 00 pointing up towards 
01

Then <b><i>D</i></b><sub>n</sub> is an exotic drawing known as the <i>
Heighway Dragon</i> of order <i>n</i>  For example <b><i>D</i></b>
<sub>10</sub> is shown below counting each quotFquot as one step the 
highlighted spot at 1816 is the position reached after 500 steps
<div style="text-align:center;">
<img src="project/images/p220.gif" alt="" />
"""

def euler220():
    """
    >>> euler220()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()