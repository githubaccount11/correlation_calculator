# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 23:56:41 2021

@author: User
"""

import glob
import csv

csv_file_path = 'E:/stocks data/NASDAQpctChange'
    

with open('E:/stocks data/stockAvgAndStdDev.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for file in glob.glob(csv_file_path + '/*.csv'):
            with open(file, 'r') as f:
                with open(file, 'r') as fa:
                    index = 0
                    sumPctChange = 0
                    reader = csv.reader(f)
                    avg = 0
                    stdDev = 0
                    for row in reader:
                        sumPctChange += float(row[1])
                        index += 1
                    avg = sumPctChange / index
                    readerb = csv.reader(fa)
                    for row in readerb:
                        stdDev += abs(float(row[1]) - avg)
                    stdDev = stdDev / index
                    spamwriter.writerow([f.name.replace(csv_file_path + "\\", "").replace(".csv", "")] + [avg] + [stdDev])
                    