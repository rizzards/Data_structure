# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:43:33 2023

@author: srizz
"""

import sys

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
            
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        return self.nodes
    
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        return self.graph[node1][node2]
    
    
def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    
    shortest_path = {}
    previous_nodes = {}
    
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
        
    shortest_path[start_node] = 0
    
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
                
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path



def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
        
    path.append(start_node)
    
    print("The best path btw {} and {} has value of {}.".format(start_node,target_node,shortest_path[target_node]))
    
    
#####################################
file_path = "Documents\Coursera\Algo_Specialization\Algo_graphs\Week2\dijkstraData.txt"

nodes = []
init_graph = {}
    
with open(file_path) as file:    
    for line in file:
        line_temp= line.split()
        nodes.append(line_temp[0])
        init_graph[line_temp[0]] = {}
        for item in line_temp[1:]:
            key, value = item.rstrip().split(',', 1)
            init_graph[line_temp[0]][key] = int(value)

graph = Graph(nodes, init_graph)
previous_nodes, shortest_path = dijkstra_algorithm(graph = graph, start_node = '1')

print_result(previous_nodes, shortest_path, '1', '7')
print_result(previous_nodes, shortest_path, '1', '37')
print_result(previous_nodes, shortest_path, '1', '59')
print_result(previous_nodes, shortest_path, '1', '82')
print_result(previous_nodes, shortest_path, '1', '99')
print_result(previous_nodes, shortest_path, '1', '115')
print_result(previous_nodes, shortest_path, '1', '133')
print_result(previous_nodes, shortest_path, '1', '165')
print_result(previous_nodes, shortest_path, '1', '188')
print_result(previous_nodes, shortest_path, '1', '197')

