# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 16:22:27 2023

@author: srizz
"""


import numpy as np
import pandas as pd

#####################################
file_path = "Documents\Coursera\Algo_Specialization\GreedyAlgorithms_MinSpanningTrees_DynamicProgramming\Week1"
file_in = file_path + "\jobs.txt"

#load the main data for testing
# format is [job_weight] [job_length]
input_data = np.loadtxt(file_in, dtype='int', skiprows=1) 

input_data = pd.DataFrame(input_data, columns = ['weight','length'])
input_data['diff_greed'] = input_data["weight"].sub(input_data["length"], axis = 0)
input_data['ratio_greed'] = input_data["weight"]/input_data["length"]

sort_diff = input_data.sort_values(by=['diff_greed','weight'], ascending = [False, False])
sort_diff["cumsum_length"] = sort_diff['length'].cumsum()
diff_greed_job = np.sum(sort_diff["weight"]*sort_diff["cumsum_length"])

sort_ratio = input_data.sort_values(by=['ratio_greed','weight'], ascending = [False, False])
sort_ratio["cumsum_length"] = sort_ratio['length'].cumsum()
ratio_greed_job = np.sum(sort_ratio["weight"]*sort_ratio["cumsum_length"])


print("diff_greed_job final sum {}".format(diff_greed_job))
print("ratio_greed_job final sum {}".format(ratio_greed_job))