# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 22:05:13 2021

@author: srizz
"""
""" exercise week2"""
import math
import numpy as np

def countinversion( array, length ):
    
    if length % 2 == 0:
        mid = math.ceil(length/2) 
    else:
        mid = math.floor(length/2)    
        
    leftA = array[:-mid]
    rightA = array[-mid:]
    
    if length == 1:
        return  list(array), 0
    elif length == 2:
        if array[0] > array[1]:
            
            return [array[1], array[0]], 1        
        else:
            print(array)
            return list(array), 0
    else:
        B, X = countinversion(leftA, len(leftA) )
        C, Y = countinversion(rightA, len(rightA) )
        D, Z = CountSplitInv(B, C, X, length)
     
        print("\n Calc tmp =", X+Z+Y)
        print("X =", X)
        print("Y =", Y)
        print("Z =", Z)
        return D, X+Y+Z
    
def CountSplitInv( B, C , X, n):
    i = 0
    j = 0
    D = [0]*(n)
       
    for k in range(n) :
        
        # if k == n-1:
        #     if B[-1] < C[-1]:
        #         D[k] = C[-1]
        #         j += 1
        #     else:
        #         D[k] = B[-1]
                
        if i == len(B):            
                D[k] = C[len(C)]
                # i += 1
        elif j >= len(C):
                D[k] = B[len(B)]
                # j += 1                
        elif B[i] < C[j]:
            D[k] = B[i]
            i += 1
        elif B[i] > C[j]:
            D[k] = C[j]
            j += 1
        
        print ("k is equal to:" , k)
        print ("B is equal to:" , B)
        print ("C is equal to:" , C)
        print ("n is equal to:" , n)
        print ("i = " , i, "and j =", j)
        print ("D merge is equal to:" , D)
    
    return D, j + X


def sc_inversion_count(array):
    
    length = len(array)   
    if length == 1: 
        return array, 0    
    if length == 2:
        if array[0] > array[1]:
            print("count inversion at start = 1 ", "/ for array ",array,"\n")
            return np.array([array[1], array[0]]), 1
        else:
            print("count inversion at start = 0", "/ for array ",array,"\n")
            return array, 0
    
    elif length > 2:
        array_l = array[:length//2]
        array_r = array[length//2:]
        array_l_df = sc_inversion_count(array_l)
        array_r_df = sc_inversion_count(array_r)
        array_l_sorted = array_l_df[0]
        array_r_sorted = array_r_df[0]        
        
        length_l = len(array_l)
        length_r = len(array_r)        
        
        count = array_l_df[1] + array_r_df[1]   
        print("count inversion at start = ",count, "/ for array ",array,"\n")
        
        l = 0
        r = 0
        
        sorted_list = []
        
        for i in range(length):
            if r == length_r:
                sorted_list.append(array_l_sorted[l])
                l += 1            
            elif l == length_l:
                sorted_list.append(array_r_sorted[r])
                r += 1             
                
            elif array_l_sorted[l] > array_r_sorted[r]:
                sorted_list.append(array_r_sorted[r])
                r += 1
                count += len(array_l_sorted) - l
                
            elif array_l_sorted[l] < array_r_sorted[r]:
                sorted_list.append(array_l_sorted[l])
                l += 1
            print("count i = ",i)                
            print("parameter l = ",l)
            print("parameter r = ",r)
            print("count inversion = ",count)
            print("array left = ",array_l_sorted)
            print("array right = ",array_r_sorted)
            print(sorted_list,"\n")
        
        return np.array(sorted_list), count            
            
# example
# ciao = [3,7,5,4,8,6,9,10,12,11]
# array_sorted, n_inversion = countinversion(ciao, len(ciao))

# read TXT
# data = list(np.loadtxt("Documents\Coursera\Algo_Specialization\Divide_and_conquer\Assignment_Codes\Week2\IntegerArray.txt"
#                   , dtype=int))

data = [5,4,3,2,1]

array_sorted, n_inversion = sc_inversion_count(data)

# array_sorted, n_inversion = countinversion(data, len(data))
print("final n inversion is ",n_inversion)