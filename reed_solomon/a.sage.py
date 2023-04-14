

# This file was *autogenerated* from the file a.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_4 = Integer(4); _sage_const_1 = Integer(1); _sage_const_3 = Integer(3); _sage_const_6 = Integer(6); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7)# ref: https://www.jstage.jst.go.jp/article/essfr/4/3/4_3_183/_pdf
R = PolynomialRing(GF(_sage_const_2 ), names=('x',)); (x,) = R._first_ngens(1)
# K.<a> = GF(2^8, name='x', modulus=x^8+x^4+x^3+x^2+1)
K = GF(_sage_const_2 **_sage_const_4 , modulus=x**_sage_const_4 +x+_sage_const_1 , impl='pari', names=('alpha',)); (alpha,) = K._first_ngens(1)
power_map = {}

for i in range(_sage_const_2 **_sage_const_4 ):
    power_map[alpha**i] = i


# k = 4
t = _sage_const_3 
# n = k+2*t
# 
# I = x^3+x^2+x+1
# 
# G = 0
# for i in range(2*t):
#     G *= (x-(alpha^i))
# P = (x^(n-k) * I) % G
# C = (x^(n-k) * I) + P

y = x + x**_sage_const_4  + x**_sage_const_6 

S = _sage_const_0 
for i in range(_sage_const_1 ,_sage_const_7 ):
    S += x**(i-_sage_const_1 )*y(alpha**i)


def my_gcd(t, lhs, rhs, aprev=_sage_const_1 , aprevprev=_sage_const_0 ):
    if rhs.degree() < t:
        return rhs, aprev
    a = -(lhs//rhs) * aprev + aprevprev
    return my_gcd(t, rhs, lhs%rhs, a, aprev)

r, a = my_gcd(t, x**_sage_const_6 , S)
print(r)
print(a)

gamma = _sage_const_1 /(alpha**power_map[a[_sage_const_0 ]])
sigma = gamma*a 
eta = gamma * r

res = []
for i in range(_sage_const_2 **_sage_const_4 ):
    if sigma(alpha**i) == _sage_const_0 :
        res.append(_sage_const_2 **_sage_const_4 -i-_sage_const_1 )

print(res)

