#random numbers

import random
print(random.randrange(1,10))

"""
#Error will occur. raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (10, 1, -9)

import random
print(random.randrange(10,1)) 
"""

print(random.randrange(100,1000))
