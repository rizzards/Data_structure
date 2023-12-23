# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 06:18:59 2023

@author: srizz
"""
import numpy as np


def dp_wis_with_reconstruction(wpg):
    
    n = len(wpg)
    solution_weights = [0] * (n + 1)
    
    # For an empty path graph 
    solution_weights[0] = 0
    
    # For a path graph with one nodes
    solution_weights[1] = wpg[0]
      
    # In all other cases pick the best between the solution for the path graph with one less node
    # or the solution fot the path graph with 2 less nodes and add the last node.
    for i in range(2, n + 1):
        solution_weights[i] = max(solution_weights[i - 1], 
                                  solution_weights[i - 2] + wpg[i-1])
    

    # Finally, the solution is the last element!
    
    # Reconstruction ()
    wis = set()
    i = n
    while i >= 1:
        if solution_weights[i-1] >= solution_weights[i-2] + wpg[i-1]:
            i = i - 1
        else:
            wis.add(i-1)
            i = i - 2
    
    # the set and the weight
    return (wis, solution_weights[n])


#####################################
file_path = "Documents\Coursera\Algo_Specialization\GreedyAlgorithms_MinSpanningTrees_DynamicProgramming\Week3"
file_in = file_path + "\mwis.txt"

#load the main data 
input_data = np.loadtxt(file_in, dtype='int', skiprows=1) 

# solution
solution = dp_wis_with_reconstruction(input_data)

solution_bit = []
check_vertex = [1,2,3,4,17,117,517,997]
for i in check_vertex:
    if i in solution[0]:
        solution_bit.append(1)
    else:
        solution_bit.append(0)

print(solution_bit)        


