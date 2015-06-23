"""
<style type="text/css">tablep298 tablep298 th tablep298 td   border
width 1px 1px 1px 1px  borderstyle solid solid solid solid  border
color black black black black  textaligncenter  mozborderradius 0px 
0px 0px 0pxtablep298   borderspacing 1px  bordercollapse separate  
backgroundcolor rgb255255255tablep298 th tablep298 td   padding 1px 
6px 1px 6pxtablep298 th  backgroundcolor rgb200220250 tablep298 td  
backgroundcolor rgb255255255 </style>

Larry and Robin play a memory game involving of a sequence of random 
numbers between 1 and 10 inclusive that are called out one at a time 
Each player can remember up to 5 previous numbers When the called 
number is in a players memory that player is awarded a point If its 
not the player adds the called number to his memory removing another 
number if his memory is full

Both players start with empty memories Both players always add new 
missed numbers to their memory but use a different strategy in 
deciding which number to remove
Larrys strategy is to remove the number that hasnt been called in the 
longest time
Robins strategy is to remove the number thats been in the memory the 
longest time

Example game
<center><table class="p298"><tr>  <th>Turn</th>  <th>Called
number</th>  <th style="text-align:right">Larrys
memory</th>  <th>Larrys
score</th>  <th style="text-align:right">Robins
memory</th>  <th>Robins
score</th></tr><tr>  <td>1</td>  <td>1</td>  
<td style="text-align:right">1</td>  <td>0</td>  
<td style="text-align:right">1</td>  <td>0</td></tr><tr>  <td>2</td>  
<td>2</td>  <td style="text-align:right">12</td>  <td>0</td>  
<td style="text-align:right">12</td>  <td>0</td></tr><tr>  <td>3</td>
  <td>4</td>  <td style="text-align:right">124</td>  <td>0</td>  
<td style="text-align:right">124</td>  <td>0</td></tr><tr>  <td>4</td>
  <td>6</td>  <td style="text-align:right">1246</td>  <td>0</td>  
<td style="text-align:right">1246</td>  <td>0</td></tr><tr>  <td>5
</td>  <td>1</td>  <td style="text-align:right">1246</td>  <td>1</td>
  <td style="text-align:right">1246</td>  <td>1</td></tr><tr>  <td>6
</td>  <td>8</td>  <td style="text-align:right">12468</td>  <td>1</td>
  <td style="text-align:right">12468</td>  <td>1</td></tr><tr>  <td>7
</td>  <td>10</td>  <td style="text-align:right">146810</td>  <td>1
</td>  <td style="text-align:right">246810</td>  <td>1</td></tr><tr>  
<td>8</td>  <td>2</td>  <td style="text-align:right">126810</td>  <td>
1</td>  <td style="text-align:right">246810</td>  <td>2</td></tr><tr>
  <td>9</td>  <td>4</td>  <td style="text-align:right">124810</td>  
<td>1</td>  <td style="text-align:right">246810</td>  <td>3</td></tr>
<tr>  <td>10</td>  <td>1</td>  <td style="text-align:right">124810
</td>  <td>2</td>  <td style="text-align:right">146810</td>  <td>3
</td></tr></table></center>

Denoting Larrys score by <var>L</var> and Robins score by <var>R</var> 
what is the expected value of <var>L</var><var>R</var> after 50 turns 
Give your answer rounded to eight decimal places using the format x
xxxxxxxx 
"""

def euler298():
    """
    >>> euler298()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()