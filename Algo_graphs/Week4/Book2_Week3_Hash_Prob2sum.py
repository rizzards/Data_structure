# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:55:13 2023

@author: srizz
"""

import numpy as np


#####################################
file_path = "Documents\Coursera\Algo_Specialization\Algo_graphs\Week4\programming_algo_prob_2sum.txt"

#load the main data for testing
input_data = np.loadtxt(file_path, dtype='int64') 

t = np.arange(-10000,10000+1)
A = {}
count_presensce = 0


def twoNumberSum(array, targetSum):
    matches = {}
    for number in array:
        match = targetSum - number
        if match in matches:
            #return [match, number]
            return 1
        else:
            matches[number] = True
            return 0
    
for j in t:
    res = twoNumberSum(input_data, j)        
    count_presensce += res

print("2sum hash table problem, final count {}".format(count_presensce))
        
    
    