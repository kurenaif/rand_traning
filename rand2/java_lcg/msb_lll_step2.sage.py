

# This file was *autogenerated* from the file msb_lll_step2.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0x5DEECE66D = Integer(0x5DEECE66D); _sage_const_0xB = Integer(0xB); _sage_const_1 = Integer(1); _sage_const_48 = Integer(48); _sage_const_0 = Integer(0); _sage_const_4 = Integer(4); _sage_const_16 = Integer(16)
import random
# https://crypto.stackexchange.com/questions/37836/problem-with-lll-reduction-on-truncated-lcg-schemes

class LCG:
    multiplier = _sage_const_0x5DEECE66D 
    addend = _sage_const_0xB 
    mask = (_sage_const_1  << _sage_const_48 ) - _sage_const_1 
    seed = _sage_const_0 

    def __init__(self, seed):
        self.seed = (seed ^ self.multiplier) & self.mask
    
    def set_seed(self, seed):
        self.seed = seed

    def next(self, bits):
        self.seed = (self.seed * self.multiplier + self.addend) & self.mask
        return self.seed >> (_sage_const_48 -bits)

N = _sage_const_4 
lcg = LCG(_sage_const_0 )
ans = []
original = []
bits = _sage_const_16 
for i in range(N+_sage_const_1 ):
    ans.append(lcg.next(_sage_const_48 ))
    original.append(((ans[-_sage_const_1 ]) >> (_sage_const_48 -bits)) << (_sage_const_48 -bits))

ys = []
for i in range(N):
    ys.append((original[i+_sage_const_1 ] - original[i]) % (_sage_const_1  << _sage_const_48 ))

a = _sage_const_0x5DEECE66D 
c = _sage_const_0xB 
print(ys[_sage_const_1 ], (ys[_sage_const_0 ] * a) % (_sage_const_1  << _sage_const_48 ))

M = (_sage_const_1  << _sage_const_48 )

ys = vector(ZZ, ys)
mat = -matrix.identity(N)

for i in range(N):
    row = list(mat[i])
    if i == _sage_const_0 :
        row[_sage_const_0 ] = M
    else:
        row[_sage_const_0 ] = (a ** (i))
    mat[i] = vector(ZZ, row)


mat = mat.LLL()

W1 = mat * ys
W2 = vector([ round(RR(w) / M) * M - w for w in W1 ])

Z = mat.solve_right(W2)
print(Z + ys)
print(ans[_sage_const_1 ] - ans[_sage_const_0 ])

z = ans[_sage_const_1 ] - ans[_sage_const_0 ]

print((a*ans[_sage_const_0 ] + c - ans[_sage_const_0 ]) % M == z)
print(((a-_sage_const_1 )*ans[_sage_const_0 ] + c) % M == z)
print(((a-_sage_const_1 )*ans[_sage_const_0 ] ) % M == (z - c) % M)

var('x')
print(solve_mod((a-_sage_const_1 )*x == (z-c), M))
print(ans[_sage_const_0 ])

