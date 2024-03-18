"""
This exercise is useful in creating a Memory game. Randomly generate a 6 × 6 list of assorted
characters such that there are exactly two of each character. An example is shown below.

@ 5 # A A !
5 0 b @ $ z
$ N x ! N z
0 - + # b :
- : + c c x
"""


from string import ascii_letters, punctuation, digits
from random import sample, shuffle
from pprint import pprint
import numpy as np

source = ascii_letters + punctuation + digits

chars = sample(source, 18) * 2 # nhân đôi source (lấy 18 ký tự random)

shuffle(chars) # random vt

L = np.array(chars).reshape(6,6).tolist() # covert series to list
pprint(L)

# L = [j for i in range(11) for j in [1, *([0]*i)]]
# print
l1 = [i for i in input("Enter the list items : ").split()]
print( '+'.join(l1))
