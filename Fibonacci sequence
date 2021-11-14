"""

I was looking thru some repositories recently and one mentioned a program that listed out the Fibonacci sequence.
I thought that would be a perfect use for a genarator, so here is just a basic solution. 

"""

import sys


def fibGen():
    current = 1
    prev = 0
    # loop controlled with call to function, can be placed with for loop and pass a count to the function for range() to use.
    while True:
        x = current+prev
        prev = current
        current = x
        yield x
        
    

seq = fibGen()

print('\n')
print(f'Memory uesd: {sys.getsizeof(seq)}')
print('\n')

for _ in range(10):
    print(next(seq))
    
