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
        
    def DFSOrd(self, v, visited, stack):
        #mark the current node as visited
        visited[v] = True
        #recur for all vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSOrd(i, visited, stack)
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
        SCCnum = 0
        
        # mark all the vertices as non visited
        visited = [False]*(self.V)
        
        #run the first DFS
        for i in range(self.V):
            if visited[i] == False:
                self.DFSOrd(i, visited, stack)
                
        # create the reversed graph
        gr = self.getTranspose()
        
        # mark all the vertices as non visited
        visited = [False]*(self.V)

        while stack:
            i = stack.pop()
            if visited[i] == False:
                    SCCnum += 1
                    gr.DFSutil(i, visited)
                    
        print("Strong connected components: "+ str(SCCnum))
        return stack
        


# sys.setrecursionlimit(5000) 
print(sys.getrecursionlimit())
        
#load the main data for testing
input_data = np.loadtxt("Documents\Coursera\Algo_Specialization\Algo_graphs\Week1\SCC.txt"
                  , dtype=int)     
        

# create graph
g = Graph(len(input_data))

for i in range(len(input_data)):
    g.addEdge(input_data[i,0], input_data[i,1])
    
g.printSCC()
    
# g = Graph(5)
# g.addEdge(1, 0)
# g.addEdge(0, 2)
# g.addEdge(2, 1)
# g.addEdge(0, 3)
# g.addEdge(3, 4)

# g.printSCC()   
 
    
    
    
    
    
        
        