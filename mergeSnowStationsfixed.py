#!/usr/bin/env python3

import re

#create the output file
outputFile = open("ridershipWithSnowData.txt","w")

#open the snow data file
snowFile = open("SnowTags.txt")

#compile regex pattern and initialize snow dictionary
snowPattern = re.compile(r'\|([0-9\.]{1,4})\|(-[nlmh])')
snowDict = {}

#for each line in the snow file
for line in snowFile:

    #check for weird text and skip to next line
    if 'PRCP"|0|-n' in line:
        continue
    
    #extracts the date and snow amount for each line
    snowDate = line[:10]
    snowData = re.findall(snowPattern, line)
    amount = snowData[0][0]
    tag = snowData[0][1]

    #sets snow total for each day in dictionary,
    #each key is unique so no need to check if key is already there
    snowDict[snowDate] = str(amount) + "|" + str(tag)
    

#open the station file and compile regex pattern
stationFile = open("totalRidership20172018.txt")
stationPattern = re.compile(r'([0-9]{4}-[0-9]{2}-[0-9]{2})')

#for each line in the station file
for line in stationFile:

    #extract out date
    stationdata = line.split("|")
    stationDate = stationdata[1]

    #check if there is a date in the line
    if re.match(stationPattern, stationDate):

        #check for weird text and skip to next line
    #if "Airport||0" in line or "<U+FEFF>STATION_NAME|DATE|STATION_ENTRIES" in line:
     #   continue
    
    #match the date for each station entry with snowfall date,
    #extract the snowfall amount and tag for each date
        if stationDate in snowDict:
            snowAmountTag = snowDict[stationDate]

            #add the snowfall data to the station data and output to a new file
            outputLine = line.strip() + "|" + snowAmountTag

            #print(outputLine)
            print(outputLine, file=outputFile)
        
  #  except error as e:
 #       print(stationDate, "error is ", e)
        
#print(snowFileContents)

snowFile.close()
stationFile.close()
outputFile.close()
