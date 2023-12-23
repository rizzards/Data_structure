# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:50:20 2022

@author: srizz
"""
import sys
import numpy as np
# Implementation of kosaraju's algorith to retrieve SCC

from collections import defaultdict

class Graph:
    
    def __init__(self,vertices):
        self.V = vertices # number of vertices
        self.graph = defaultdict(list) #dictionary to store the graph
        
    #function to add an edge
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
        
    def DFS_iter_ord(self, v, visited, stack):
        stack_b = [v]
        # stack.append(v)
        
        while stack_b:
            # print(stack_b)
            #pop a vertex from stack
            current = stack_b.pop()
            #mark the current node as visited
            visited[current] = True
            stack.insert(0,current)
            # print(current)
            for neighbor in self.graph[current]:
                if visited[neighbor] == False:
                    stack_b.append(neighbor)                                          

    def DFS_iter_util(self, v, visited, SCC_comp):
        comp = 0
        stack_b = [v]        
        
        while stack_b:
            # print(stack_b)
            #pop a vertex from stack
            current = stack_b.pop()
            #mark the current node as visited
            visited[current] = True            
            # print(current)
            comp += 1
            for neighbor in self.graph[current]:
                if visited[neighbor] == False:
                    stack_b.append(neighbor)
        
        SCC_comp.append(comp)
        # SCC_comp = SCC_comp + [comp]
            
                    
    def DFSOrd(self, v, visited, stack):
        #mark the current node as visited
        visited[v] = True
        #recur for all vertices adjacent to this vertex
        # print(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSOrd(i, visited, stack)
        print(v)
        stack = stack.append(v)
        
    def DFSutil(self, v, visited):
        #mark the current node as visited
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSutil(i, visited)

        
    #function that creates the reverse of this graph
    def getTranspose(self):
        g = Graph(self.V)
        
        #recur for all vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
                
        return g
    
    #main function that finds and print all strong connected components
    def printSCC (self):
        stack = []
        SCC_comp = []
        SCCnum = 0
        
        # mark all the vertices as non visited
        visited = [False]*(self.V)
        
        #run the first DFS
        # for i in range(self.V):            
        #     if visited[i] == False:                
        #         self.DFSOrd(i, visited, stack)
        self.DFS_iter_ord(1, visited, stack)
        
        # print(stack)        
        # create the reversed graph
        gr = self.getTranspose()
        
        # mark all the vertices as non visited
        visited = [False]*(self.V)

        while stack:
            i = stack.pop()
            if visited[i] == False:
                    SCCnum += 1
                    # gr.DFSutil(i, visited)
                    gr.DFS_iter_util(1, visited, SCC_comp)
        
        
                    
        print("Strong connected components: "+ str(SCCnum))
                
        return SCC_comp
        # SCC_comp_sorted = SCC_comp.sort(reverse=True)
        # print("Strong connected components composition big 5: "+ str(SCC_comp_sorted[:5]))
        
        


# sys.setrecursionlimit(5000) 
# print(sys.getrecursionlimit())
        
#load the main data for testing
input_data = np.loadtxt("Documents\Coursera\Algo_Specialization\Algo_graphs\Week1\SCC.txt"
                  , dtype=int)     
        

# create graph
g = Graph(len(input_data))

for i in range(len(input_data)):
    g.addEdge(input_data[i,0], input_data[i,1])
    
SCC_list = g.printSCC()
    

# TEST
# g = Graph(5)
# g.addEdge(1, 0)
# g.addEdge(0, 2)
# g.addEdge(2, 1)
# g.addEdge(0, 3)
# g.addEdge(3, 4)

# g.printSCC()   
SCC_list_final = SCC_list.copy()
SCC_list_final.sort(reverse=True)
print(SCC_list_final[:5])
    
    
    
    
        
        