#!/usr/bin/env python3

#open all relevant data files
snowRidershipData = open("ridershipWithSnowData.txt")
incomeData = open("incomeZipcodes.txt")
outData = open("AllData.txt", "w")

d = {}

#for each entry in the income and zip codes file
for line in incomeData:

    #extract out the data and split station into first half
    item = line.split("|")
    stationNamedic = item[0].split("/")
    stationNamedic = stationNamedic[0]

    #account for two cases not solved by searching for 1st half of station name or stripping characters
    if stationNamedic == "Massachusetts Avenue":
        stationNamedic = "Mass Ave"

    elif stationNamedic == "Hynes Convention Center":
        stationNamedic = "Hynes"

    #extract zipcode and income, strip away any \n characters    
    zipcodeIncome = item[1] + "|" + item[2][:-1]

    #load the data into a dictionary
    d[stationNamedic] = zipcodeIncome

#close file 
incomeData.close()

#for each line in the snow and ridership data file    
for line in snowRidershipData:

    #extract out data and strip any " or whitespace
    info = line.split("|")
    info[4] = info[4][:-1]
    stationName = info[0].strip('"')
    stationName = stationName.strip()

    #check every station in the station dictionary
    for entry in d:
        
        #if the first word of the station or whole station name is in the full station name
        if entry in stationName:

            #write all data to file
            print(stationName + "|" + d[entry] + "|" + "|".join(info[n] for n in range(1, 5)), file=outData)

#close all files
snowRidershipData.close()
outData.close()
