# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 06:42:13 2023

@author: srizz
"""

import numpy as np
import sys

# The Dynamic Programming solution to the knapsack problem
# For 
# items             0,  1,  2,  etc 
# that have values  v0, v1, v2, etc 
# and sizes         s0, s1, s2, etc
# find the items with maximum total value 
# such that the total size is not larger than a given capacity C
# sizes and the capacity are non negative integer values.

def dp_knapsack(vals, sizes, C):
    n = len(vals)
    A = [None] * (n+1)
    for x in range(n+1):
        A[x] = [0] * (C+1)
        
    # A[0][c] has already 0s (using 0 items, for all capacities, the value is 0!)
    for i in range(1, n+1):
        for c in range(C+1):
            if sizes[i-1] > c: # sizes are numbered from 0!
                A[i][c] = A[i-1][c] # there is no other choice!
            else: 
                A[i][c] = max(A[i-1][c], 
                              A[i-1][c - sizes[i-1]] + vals[i-1])
    return A[n][C]


# def MF_knapsack(i, wt, val, j):

#     # global F
#     F = {}
#     if F[i][j] < 0:
#         if j < wt[i - 1]:
#             val = MF_knapsack(i - 1, wt, val, j)
#         else:
#             val = max(
#                 MF_knapsack(i - 1, wt, val, j),
#                 MF_knapsack(i - 1, wt, val, j - wt[i - 1]) + val[i - 1],
#             )
#         F[i][j] = val
#     return F[i][j]



def MF_knapsack2(i, j, weights, values):
    
    V = {}
    
    if i not in V:
        V.update({i:{}})
        
    if j not in V[i]:
        V[i] = {j: -1}
 
    if V[i][j] < 0:
        if j < weights[i-1]:
            val = MF_knapsack2(i-1, j, weights, values)
        else:
            val = max(MF_knapsack2(i-1, j, weights, values), 
                      values[i] + MF_knapsack2(i-1, j-weights[i-1],weights, values)
                      )
        V[i][j] = val
        
    return V[i][j] 


#####################################
file_path = "Documents\Coursera\Algo_Specialization\GreedyAlgorithms_MinSpanningTrees_DynamicProgramming\Week4"
file_in = file_path + "\knapsack1.txt"

#load the main data 
knapsack1 = np.loadtxt(file_in, dtype='int', skiprows=1) 
knapsack_size = np.loadtxt(file_in, dtype='int',max_rows=1)[0]
n_items = np.loadtxt(file_in, dtype='int',max_rows=1)[1]

solution_k1 = dp_knapsack(knapsack1[:,0], knapsack1[:,1], knapsack_size)
print("Total value:", solution_k1)

        