"""
Let SA represent the sum of elements in set A of size <i>n</i> We 
shall call it a special sum set if for any two nonempty disjoint 
subsets B and C the following properties are true
<ol style="list-style-type:lower-roman;"><li>SB ne SC that is sums of 
subsets cannot be equal</li><li>If B contains more elements than C 
then SB gt SC</li></ol>

For example 81 88 75 42 87 84 86 65 is not a special sum set because 
65  87  88  75  81  84 whereas 157 150 164 119 79 159 161 139 158 
satisfies both rules for all possible subset pair combinations and SA  
1286

Using <a href="project/resources/p105_sets.txt">setstxt</a> right 
click and Save LinkTarget As a 4K text file with onehundred sets 
containing seven to twelve elements the two examples given above are 
the first two sets in the file identify all the special sum sets A
<sub>1</sub> A<sub>2</sub>  A<sub><i>k</i></sub> and find the value of 
SA<sub>1</sub>  SA<sub>2</sub>    SA<sub><i>k</i></sub>

NOTE This problem is related to <a href="problem=103">Problem 103</a> 
and <a href="problem=106">Problem 106</a>
"""

def euler105():
    """
    >>> euler105()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()