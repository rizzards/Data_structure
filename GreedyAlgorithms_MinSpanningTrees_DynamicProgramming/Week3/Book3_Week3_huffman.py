# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 07:42:28 2023

@author: srizz
"""

import numpy as np


#####################################
file_path = "Documents\Coursera\Algo_Specialization\GreedyAlgorithms_MinSpanningTrees_DynamicProgramming\Week3"
file_in = file_path + "\huffman.txt"

#load the main data for testing
input_data = np.loadtxt(file_in, dtype='int', skiprows=1) 



# Creating tree nodes
class NodeTree(object):
    
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right
        
    def children(self):
        return(self.left, self.right)
    
    def nodes(self):
        return(self.left, self.right)
    
    def __str__(self):
        return '%s_%s' % (self.left, self.right)
    
# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d
  
 
# Example
string = 'BCAADDDCCACACAC'
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
nodes = freq


# Main calc
freq = {}
for i in range(len(input_data)):
    freq.update({str(i): input_data[i]})
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])
# huffmanCode_list = list(huffmanCode.items())
huffmanCode_max = sorted(huffmanCode.items(), key=lambda x: len(x[1]), reverse=True)
huffmanCode_max_len = len(huffmanCode_max[0][1])
 
huffmanCode_min = sorted(huffmanCode.items(), key=lambda x: len(x[1]))
huffmanCode_min_len = len(huffmanCode_min[0][1])

   