# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 21:38:53 2022

@author: srizz
"""

import sys
from heapq import heapify, heappush
# heappop

def dijsktra(graph, src, dest):
    
    inf = sys.maxsize
    node_data = {}
    for i in graph:
        node_data[i] = {}
        node_data[i].update({'cost':inf, 'pred':[]})
    
    node_data[src]['cost'] = 0
    visited = []
    temp = src
    
    for i in range(len(graph)-1):
        if temp not in visited :
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost= node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                    heappush(min_heap, (node_data[j]['cost'], j))
        print(min_heap)
        # heapify(min_heap)
        # print((min_heap))
        temp = min_heap[0][1]
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))
    
    


#load the main data for testing
file_path = "Documents\Coursera\Algo_Specialization\Algo_graphs\Week2\dijkstraData.txt"

# LOAD THE GRAPH        
# with open(file_path) as file:
#     graph = {}
#     for line in file:
#         line_temp= line.split()
#         graph[line_temp[0]] = {}
#         for item in line_temp[1:]:
#             key, value = item.rstrip().split(',', 1)
#             graph[line_temp[0]].update({key:int(value)})


graph = {
    'A':{'B':2,'C':4},
    'B':{'A':2,'C':3, 'D':8},
    'C':{'A':4,'B':3, 'E':5, 'D':2},
    'D':{'B':8,'C':2, 'E':11, 'F':22},
    'E':{'C':5,'D':11, 'F':1},
    'F':{'D':22, 'E':1}
    }


# dijsktra(graph, '1', '7')
dijsktra(graph, 'A', 'F')


    