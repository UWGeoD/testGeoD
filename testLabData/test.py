# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 12:55:14 2023

@author: ellie
"""

# import csv
import pandas as pd

# def process_csv(filename):
#     example_file = open(filename, encoding="utf-8")
#     example_reader = csv.reader(example_file)
#     example_data = list(example_reader)
#     example_file.close()
#     return example_data

# data_csv = process_csv("testData.csv")
# test_name = data_csv[0]
# test_notes = data_csv[1]
# data_header = data_csv[3]
# data_units = data_csv[4]
# data_rows = data_csv[5:]

df = pd.read_csv('testData.csv', header = [3,4])