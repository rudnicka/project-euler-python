"""
A number chain is created by continuously adding the square of the 
digits in a number to form a new number until it has been seen before

For example

44 rarr 32 rarr 13 rarr 10 rarr <b>1</b> rarr <b>1</b>
85 rarr <b>89</b> rarr 145 rarr 42 rarr 20 rarr 4 rarr 16 rarr 37 rarr 
58 rarr <b>89</b>

Therefore any chain that arrives at 1 or 89 will become stuck in an 
endless loop What is most amazing is that EVERY starting number will 
eventually arrive at 1 or 89

How many starting numbers below ten million will arrive at 89
"""

def euler92():
    """
    >>> euler92()
    'to-do'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()