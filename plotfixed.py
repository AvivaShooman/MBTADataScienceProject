#!/usr/bin/env python3

import matplotlib.pyplot as plt
import random
import numpy as np

#open xaxis, yaxis and 3D file
XAxis = open("XAxis.txt")
YAxis = open("YAxis.txt")
cSize = open("3D.txt")

#create a figure instance that will later be written to a PDF
f = plt.figure()

#create 3 empty lists for compiling data
xList = []
yList = []
aList = []

#read in data from x and y axis files, change strings to floats
for line in XAxis:
    xList += [float(line)]

for line in YAxis:
    yList += [float(line)]

#set the number value based on # of values in list
N = len(xList)

#make a list of random colors, same size as data
colors = [np.random.random() for i in range(N)]

#set circle sizes from 3D file, scale dots so they don't take up the whole graph
for line in cSize:
    aList += [float(line)*0.1]

#make the scatter plot, with specified colors and sizes
plt.scatter(xList, yList, c = colors, s = aList, alpha = 0.5)

#specify the x and y axis labels, graph title
plt.ylabel("Negative Percent Change in Ridership")
plt.xlabel("Income Per Station")
plt.title("Massachusetts Subway Ridership on a Big Snow Day")

#save the plot into a PDF file
f.savefig("snowPlot.pdf")
