#!/usr/bin/env python3

import gzip

income = gzip.open("IncomePop.gz", "rt")
zipcodes = open("subwayStopZipcode.txt")
out = open("incomeZipcodes.txt","w")

s = set()

#for each line in the zipcode file
for line in zipcodes:
    #split the line of the zipcode file and extract the data
    item = line.split("|")
    stationName = item[0]
    Zip = item[1]

    #add each zipcode and stationname to the set
    s.add((Zip[:-1], stationName))

#close file
zipcodes.close()

#for each line in the income file
for line in income:
    
    #skip weird data
    if "Zip\tMedian\tMean\tPop\n" in line:
        continue
    
    #split the line of the income file and extract the data
    info = line.split("|")
    zipcode = info[0]
    medianSalary = info[1]

    #check each entry in the set
    for data in s:
        #if the zipcode we have matches the zipcode in the file, then add its station name, zipcode and median salary to the output file
        if zipcode == data[0]:
            print(data[1] + "|" + zipcode + "|" + medianSalary, file=out)

#close all files
income.close()
out.close()
