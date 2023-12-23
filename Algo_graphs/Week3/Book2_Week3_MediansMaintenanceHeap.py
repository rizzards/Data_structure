# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 21:14:20 2023

@author: srizz
"""
import numpy as np
import heapq

def medianOfInt(arr, size):
    # creating a min-heap and a max-heap and a list of medians
    minheap=[]
    maxheap=[]
    medians=[]
    
    if size == 0:
        return None
    
    if size == 1:
        return arr[0]
    
    med = arr[0]
    medians.append(med)
    heapq.heappush(maxheap, -med)
    
    for i in range(1,size):
        x = arr[i]
        
        if len(maxheap) > len(minheap):
            if x < med:
                heapq.heappush(minheap, -heapq.heappop(maxheap))
                heapq.heappush(maxheap, -x)
            else:
                heapq.heappush(minheap, x)
                
            med = - maxheap[0]
                
        elif len(maxheap) < len(minheap):
            if x > med:
                heapq.heappush(maxheap, -heapq.heappop(minheap))
                heapq.heappush(minheap, x)
            else:
                heapq.heappush(maxheap, x)
            
            med = - maxheap[0]
            
        else:
            if x < med:
                heapq.heappush(maxheap, -x)
                med = - maxheap[0]
            else:
                heapq.heappush(minheap, x)
                med = minheap[0]
                
        medians.append(med)
        
    return medians

#####################################
file_path = "Documents\Coursera\Algo_Specialization\Algo_graphs\Week3\Median.txt"

#load the main data for testing
input_data = np.loadtxt( file_path, dtype=int) 

#retrieve medians array
medians = medianOfInt(input_data, len(input_data))

print("total sum of medians is {}".format(sum(medians)))
                