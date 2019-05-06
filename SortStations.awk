#!/usr/bin/gawk -f

BEGIN{

#set field delimiters and file paths
FS = ","
OFS = "|"
filePath = "./GSE_20172018.txt"
command = "cat " filePath

#initialize starting variables
prevStationName = "Airport"
count = 0

while ((command | getline) > 0){
    
    #if it is the same station and the same date, keep adding the amount of people seen, then save the last station name and date
    if ((prevStationName == $1) && (prevDate == $3)){

	count += $5
	prevStationName = $1
	prevDate = $3
	}
    
    #otherwise, either it is a new day and the same station or a new station and a new day,
    #print out the data for the last day or old station and last day, then save all the current data
    else if (prevStationName != $1 || (prevStationName == $1 && prevDate != $3)){
	#print out important data fields to a file
	print(prevStationName, prevDate, count) >> "totalRidership20172018.txt" 

	prevDate = $3
	prevStationName = $1
	count = $5
	
    }
}

#check for errors
if (close(command))
    print("There was an error in closing the command.")

}
