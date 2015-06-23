"""
There are <var>N</var> seats in a row <var>N</var> people come one 
after another to fill the seats according to the following rules<ol>
<li>No person sits beside another</li><li>The first person chooses any 
seat</li><li>Each subsequent person chooses the seat furthest from 
anyone else already seated as long as it does not violate rule 1 If 
there is more than one choice satisfying this condition then the 
person chooses the leftmost choice</li></ol>

Note that due to rule 1 some seats will surely be left unoccupied and 
the maximum number of people that can be seated is less than <var>N
</var> for <var>N</var>  1

Here are the possible seating arrangements for <var>N</var>  15

<img src=project/images/p472_n15.png>

We see that if the first person chooses correctly the 15 seats can 
seat up to 7 people
We can also see that the first person has 9 choices to maximize the 
number of people that may be seated

Let fN be the number of choices the first person has to maximize the 
number of occupants for <var>N</var> seats in a row Thus f1  1 f15  9 
f20  6 and f500  16

Also sumfN  83 for 1 le <var>N</var> le 20 and  sumfN  13343 for 1 le 
<var>N</var> le 500

Find sumfN for 1 le <var>N</var> le 10<sup>12</sup> Give the last 8 
digits of your answer
"""

def euler472():
    """
    >>> euler472()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()