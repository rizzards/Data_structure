# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:08:13 2023

@author: srizz
"""

import numpy as np
from heapq import heappush,heappop


            

def minimum_spanning_tree_cost(graph):
    """Return the sum of the costs of the edges in the minimum spanning
    tree for the given graph, which must be a mapping from nodes to an
    iterable of (neighbour, edge-cost) pairs.

    """
    total = 0                   # Total cost of edges in tree
    explored = set()            # Set of vertices in tree
    start = next(iter(graph))   # Arbitrary starting vertex
    unexplored = [(0, start)]   # Unexplored edges ordered by cost
    while unexplored:
        cost, winner = heappop(unexplored)
        if winner not in explored:
            explored.add(winner)
            total += cost
            for neighbour, cost in graph[winner]:
                if neighbour not in explored:
                    heappush(unexplored, (cost, neighbour))
    return total


#####################################
file_path = "Documents\Coursera\Algo_Specialization\GreedyAlgorithms_MinSpanningTrees_DynamicProgramming\Week1"
file_in = file_path + "\edges.txt"

#load the main data for testing
# format is [job_weight] [job_length]
input_data = np.loadtxt(file_in, dtype='int', skiprows=1) 
metadata = np.loadtxt(file_in, dtype='int',max_rows=1) 


graph = {}
for i in range(len(input_data)):
    if input_data[i,0] not in graph:
        graph[input_data[i,0]] = []
    graph[input_data[i,0]].append([input_data[i,1],input_data[i,2]])
    
    if input_data[i,1] not in graph:
        graph[input_data[i,1]] = []    
    graph[input_data[i,1]].append([input_data[i,0],input_data[i,2]])
    
#####################################    
    
total_cost = minimum_spanning_tree_cost(graph) 
print("total cost of the MST is {}".format(total_cost))
