# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 22:19:20 2021

@author: srizz
"""
from statistics import median
import numpy as np


# partition with first item    
def partition_first(A, low, high):
    
    pivot = A[low]
    # print("pivot = ", pivot)
    # print(" low = ", low, " high", high) 
    
    i = low + 1
    for j in range (low+1, high+1):
        # print("j = ", j, " A[j]=", A[j]," low +1 = ", low+1, " high+1", high+1)        
        # print (A)
        if A[j] < pivot:        
            A[i],A[j] = A[j],A[i]
            i+=1
            # print("i = ", i)            
                   
    
    A[i-1],A[low] = A[low],A[i-1]
    # print("end partition: ",A)
    return i-1

# partition with last item
def partition_last(A, low, high):
    
    pivot = A[high]
    # print("pivot = ", pivot)
    # print(" low = ", low, " high", high) 
    
    i = low - 1
    for j in range (low, high):
        # print("j = ", j, " A[j]=", A[j]," low = ", low, " high", high)        
        # print (A)
        if A[j] < pivot:        
            i+=1
            A[i],A[j] = A[j],A[i]
            
            # print("i = ", i)                                
    
    A[i+1],A[high] = A[high],A[i+1]
    # print("end partition: ",A)
    return i+1

def partition_last2(A, low, high):    
    
    A[high],A[low] = A[low],A[high]
    pivot = A[low]
    # print("pivot = ", pivot)
    # print(" low = ", low, " high", high) 
    
    i = low + 1
    for j in range (low+1, high+1):
        # print("j = ", j, " A[j]=", A[j]," low +1 = ", low+1, " high+1", high+1)        
        # print (A)
        if A[j] < pivot:        
            A[i],A[j] = A[j],A[i]
            i+=1
            # print("i = ", i)            
                   
    
    A[i-1],A[low] = A[low],A[i-1]
    # print("end partition: ",A)
    return i-1


# partition with median of three item
def partition_median_of_three(A, low, high):
    
    mid = (low+high)//2
    
    pivot = median([A[high],A[low],A[mid]])
    
    if pivot == A[high]:
        pivot_idx = high
    elif pivot == A[low]:
        pivot_idx = low
    else:
        pivot_idx = mid
    
    # print("pivot = ", pivot)
    # print(" low = ", low, " high", high) 
    
    i = low -1
    for j in range (low, high+1):
        if j != pivot_idx:
            # print("j = ", j, " A[j]=", A[j]," low = ", low, " high", high)        
            # print (A)        
            if A[j] < pivot:        
                i+=1
                A[i],A[j] = A[j],A[i]
                
                # print("i = ", i)                                
    
    if pivot_idx == high:
        A[i+1],A[pivot_idx] = A[pivot_idx],A[i+1]
    # print("end partition: ",A)
    return i+1


def partition_median_of_three2(A, low, high):
    
    mid = (low+high)//2
    
    pivot = median([A[high],A[low],A[mid]])
    
    if pivot == A[high]:
        A[high],A[low] = A[low],A[high]
    elif pivot == A[mid]:
        A[mid],A[low] = A[low],A[mid]

    # print("pivot = ", pivot)
    # print(" low = ", low, " high", high) 
    
    i = low + 1
    for j in range (low+1, high+1):
        # print("j = ", j, " A[j]=", A[j]," low +1 = ", low+1, " high+1", high+1)        
        # print (A)
        if A[j] < pivot:        
            A[i],A[j] = A[j],A[i]
            i+=1
            # print("i = ", i)            
                   
    
    A[i-1],A[low] = A[low],A[i-1]
    # print("end partition: ",A)
    return i-1

    

def quick_sort(array, low, high):
    
    length = len(array[low:high+1]) 
    count = 0
    
    if low < high:
        
        # pi = partition_first(array,low, high)
        # pi = partition_last2(array,low, high)
        pi = partition_median_of_three2(array,low, high)
        
        # print("pi=",pi)
        array, countL = quick_sort(array, low, pi-1)   
        # print("countL ",countL,"print left", array[low:pi-1])
        array, countR = quick_sort(array, pi+1, high)    
        # print("countR ",countR,"print right", array[pi+1:high])
        
        count = length-1+ countL+countR        
        # print("count = " , count)
        
    return    array,count

# prova =  [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]

''' test cases'''
# data = list(np.loadtxt("Documents\Coursera\Algo_Specialization\Divide_and_conquer\Assignment_Codes\Week3\input_dgrcode_16_100000.txt"
#                   , dtype=int))


''' read official TXT '''
data = list(np.loadtxt("Documents\Coursera\Algo_Specialization\Divide_and_conquer\Assignment_Codes\Week3\QuickSort.txt"
                  , dtype=int))        

data_output = quick_sort(data, 0, len(data)-1)
print(data_output[1])



        
        
        
        
    