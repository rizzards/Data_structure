# -*- coding: utf-8 -*-
"""
test
"""


num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

# =============================================================================
# x = 5678
# y = 123
# 
# res = x*y
# 
# ac = 56*1
# bd = 78*23
# ab = 56+78
# cd = 1+23
# ab_cd = ab * cd
# diff = ab_cd - ac - bd
# 
# print(res)
# print(ac*(10**4))
# print(bd)
# print(diff*(10**2))
# print(ac*(10**4) + bd + diff*(10**2))
# =============================================================================



""" exercise week1"""

import math

def count_digit (n1 , n2 ):
    min_n = min(n1,n2)
    len_num = math.ceil(len(str(min_n))/2)
    return len_num

def split_num (num, pos):
    return int(str(num)[:-pos]),int(str(num)[-pos:])


def karatsuba(n1, n2):
    if n1 <10 or n2 <10:
        return n1*n2
    mid = count_digit(n1,n2)
    high1, low1 = split_num(n1,mid)
    high2, low2 = split_num(n2,mid)
    
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)
    
    return (z2 * (10 ** (mid * 2))) + ((z1 - z2 - z0) * (10 ** mid)) + z0
    

final_num = karatsuba(num1,num2)    
print(final_num)    



    
    
    