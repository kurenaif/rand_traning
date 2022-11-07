

# This file was *autogenerated* from the file msb_lll_step1.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0x5DEECE66D = Integer(0x5DEECE66D); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_48 = Integer(48); _sage_const_4 = Integer(4); _sage_const_32 = Integer(32)
import random
# https://crypto.stackexchange.com/questions/37836/problem-with-lll-reduction-on-truncated-lcg-schemes

class LCG:
    multiplier = _sage_const_0x5DEECE66D 
    # addend = 0xB
    addend = _sage_const_0 
    mask = (_sage_const_1  << _sage_const_48 ) - _sage_const_1 
    seed = _sage_const_0 

    def __init__(self):
        self.seed = random.randint(_sage_const_0 , self.mask)

    def next(self):
        self.seed = (self.seed * self.multiplier + self.addend) & self.mask
        return self.seed

lcg = LCG()

anses = []
ys = []

N = _sage_const_4 
MASK_SIZE = _sage_const_48 
HIDE_SIZE = _sage_const_32 
for i in range(N):
    temp = lcg.next()
    anses.append(temp)
    ys.append(temp & ((_sage_const_1 <<(MASK_SIZE-HIDE_SIZE))-_sage_const_1  << HIDE_SIZE))

print(anses)

a = _sage_const_0x5DEECE66D 
M = (_sage_const_1  << _sage_const_48 )

ans = vector(ZZ, anses)
ys = vector(ZZ, ys)
mat = -matrix.identity(N)

for i in range(N):
    row = list(mat[i])
    if i == _sage_const_0 :
        row[_sage_const_0 ] = M
    else:
        row[_sage_const_0 ] = (a ** (i))
    mat[i] = vector(ZZ, row)


print(mat)
res = mat * ans
print(res)

original_mat = mat
mat = mat.LLL()
res = mat * ans 

W1 = mat * ys
W2 = vector([ round(RR(w) / M) * M - w for w in W1 ])

Z = mat.solve_right(W2)
print("--------------------------------------------------")
print(Z + ys)
print(ans)

print("--------------------------------------------------")
print(mat*ans)
memo = vector([ round(RR(w) / M)*M for w in W1 ])
print(memo)

