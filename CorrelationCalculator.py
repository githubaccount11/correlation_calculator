# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 19:51:26 2021

@author: Leigh Fair-Smiley
"""



import glob
import csv



csv_file_path = 'E:/stocks data/NASDAQpctChange'
averages = 'E:/stocks data/stockAvgAndStdDev.csv'

"""//array of symbols that have been compared so they are not all done twice"""
beenDone = [] 

startPoint = False

with open('E:/stocks data/stockCorrelation.csv', 'a+', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    with open('E:/stocks data/stockAvgAndStdDev.csv', 'r') as fc:
        readerc = csv.reader(fc)
        stats = list(readerc)
        """select stock one at a time and create list of all ticks"""
        for file in glob.glob(csv_file_path + '/*.csv'):
            with open(file, 'r') as f:
                reader = csv.reader(f)
                readerList = []
                for row in reader:
                    readerList.append(row)
                index = 0
                stockAAvg = 0
                stockAStdDev = 0
                """find avg and stdDev of selected stock"""
                for stat in stats:
                    if stat[0] == f.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", ""):
                        stockAAvg = float(stat[1])
                        stockAStdDev = float(stat[2])
                        print("new stock: " + f.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", "") + " stats: " + str(stat[1]) + "  " + str(stat[2]))
                """select second stock"""
                for file_b in glob.glob(csv_file_path + '/*.csv'):
                    with open(file_b, 'r') as fb:
                        if startPoint:
                            if fb.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", "") != f.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", ""):
                                if beenDone.count(f.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", "") + "_" + fb.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", "")) == 0 and beenDone.count(fb.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", "") + "_" + f.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", "")) == 0:
                                    readerb = csv.reader(fb)
                                    readerbList = []
                                    for row in readerb:
                                        readerbList.append(row)
                                    """find avg and stdDev of second stock"""
                                    with open('E:/stocks data/stockAvgAndStdDev.csv', 'r') as fd:
                                        readerd = csv.reader(fd)
                                        stockBAvg = 0
                                        stockBStdDev = 0
                                        for line in readerd:
                                            if line[0] == fb.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", ""):
                                                stockBAvg = float(line[1])
                                                stockBStdDev = float(line[2])
                                        """find covSum"""
                                        covSum = 0
                                        dataPointsNum = 0
                                        for row in readerList:
                                            while index < len(readerbList) - 1 and readerbList[index][0] != row[0]:
                                                index += 1
                                            if readerbList[index][0] == row[0]:
                                                dataPointsNum += 1
                                                """print("row[1]: " + str(row[1]) + " readerbList[index][1]: " + readerbList[index][1])"""
                                                covSum += (float(row[1]) - stockAAvg) * (float(readerbList[index][1]) - stockBAvg)
                                            index = 0
                                        """find cov and cor"""
                                        covariance = 0
                                        correlation = 0
                                        """print("covSum: " + str(covSum) + " stockAAvg: " + str(stockAAvg) + " stockBAvg: " + str(stockBAvg))"""
                                        if dataPointsNum > 1:
                                            covariance = covSum / float(dataPointsNum - 1)
                                            """print("covariance: " + str(covariance) + " stockAStdDev: " + str(stockAStdDev) + " stockBStdDev: " + str(stockBStdDev))"""
                                            correlation = float(covariance) / float(float(stockAStdDev) * float(stockBStdDev))
                                            """print("correlation: " + str(correlation))"""
                                            spamwriter.writerow([f.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", "") + "_" + fb.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", "")] + [covariance] + [correlation])
                                beenDone.append(f.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", "") + "_" + fb.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", ""))
                                beenDone.append(fb.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", "") + "_" + f.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", ""))
                        if (startPoint == False):
                           if (f.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", "") + "_" + fb.name.replace("E:/stocks data/NASDAQpctChange\\", "").replace(".csv", "") == "CYTK_SUNW"):
                               startPoint = True
                                