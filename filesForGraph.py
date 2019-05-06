#!/usr/bin/env python3

import datetime

#open all relevant files
data = open("AllData.txt")
outfileX = open("XAxis.txt","w")
outfileY = open("YAxis.txt","w")
outfile3 = open("3D.txt", "w")

#create appropriate dictionarys                                                                                     
d = {}
dTotalRidership = {}

#create variables for knowing when it is a new station
prevStationName = "Airport"
total = 0
count = 0

#for each entry in the data file
for line in data:

    #extract out the proper fields
    item = line.split("|")
    stationName = item[0]
    dateStation = item[3] + "|" + stationName

    #make date, station the key and data the ridership
    d[dateStation] = item[4]

    #if it is the last station and last entry, keep adding to total and count
    #compute total and add to dictionary
    if prevStationName == "Wood Island" and item[3] == "2018-07-26":
        total += int(item[4])
        count += 1
        totalRidership = total/count
        dTotalRidership[stationName] = totalRidership

    #if it is the same station, keep tallying ridership and days seen                                                                                     
    #set previous station name to current station name 
    elif stationName == prevStationName:
        total += int(item[4])
        count += 1
        prevStationName = stationName
        
    #otherwise, it is a new station, compute the total ridership for the last station
    #reset the counter variables for a new station, add to total ridership dictionary
    #set previous station name to current station name
    else:
        totalRidership = total/count
        total = int(item[4])
        count = 1
        dTotalRidership[prevStationName] = totalRidership
        prevStationName = stationName

#close and open data file before reading again
data.close()
data = open("AllData.txt")  

#for all data in the file extract the data
for line in data:
    item = line.split("|")
    
    #if it was a big snowday
    if item[6] == "-h\n" : #or item[6] == "-l\n" or item[6] == "-m\n": # or item[6] == "-n\n":
        
        #extract out date, income, station create key
        date = item[3]
        income = item[2]
        station = item[0]
        stationDate = date + "|" + station

        #extract out daily ridership, convert to int for computations later
        dailyRidership = int(d[stationDate])
        
        #compute days before and days after using date objects
        current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        onebefore_date = (current_date + datetime.timedelta(days=-7)).strftime('%Y-%m-%d')
        oneafter_date = (current_date + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        twobefore_date = (current_date + datetime.timedelta(days=-14)).strftime('%Y-%m-%d')
        twoafter_date = (current_date + datetime.timedelta(days=14)).strftime('%Y-%m-%d')

        #create a tuple of all dates before and after the snowday
        t = (twobefore_date, onebefore_date, oneafter_date, twoafter_date)

        #initialize counter variables
        total = 0
        count = 0

        #for each date
        for day in t:

            #create a key using the date found and the current station
            index = day + "|" + station

            #check if it is in the dictionary, no 2016 dates in dictionary
            if index in d:

                #extract out its ridership, add it to the total as an int for computations
                #incriment the count for number of days found
                ridership = d[index]
                total += int(ridership)
                count += 1

        #divide the total ridership by number of days seen to compute aveRidership
        aveRidership = total/count

        #compute the change, today's ridership minus usual ridership 
        #divide the change by the average ridership and multiply by 100, make positive
        change = dailyRidership-aveRidership
        percentChange = abs((change/aveRidership) * 100)
        
        #output the percent change to y axis file
        print(percentChange, file=outfileY)
        
        #output the income to x axis file
        print(income, file=outfileX)

        #output the total ridership per station from dictionary to 3D file
        print(dTotalRidership[station],file=outfile3)

#       print(station, income, percentChange)
        
#close the file
data.close()
outfileX.close()
outfileY.close()
outfile3.close()
