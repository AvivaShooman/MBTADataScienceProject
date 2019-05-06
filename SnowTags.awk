#!/usr/bin/gawk -f

BEGIN{

#set field delimiters and file paths    
FS = ","
OFS = "|"
filePath = "./SnowData20172018.csv"
command = "cat " filePath

while ((command | getline) > 0){

    #Finds the numerical value of the snow depth either in 00.0 or 0.0 format, gets rid of quotes and sets equal to field
    if (length($9) == 5)
	field = substr($9, 2, 3) + 0 #add 0 so gawk knows this is a numerical value
    
    else if (length($9) == 6){
	field = substr($9, 2, 4) + 0 #see comment above
    }
    #slice out the date field from each entry
    date = substr($7, 2, 10)
    
    tag = ""

    #negligible snow depth
    if (field >= 0.0 && field < 1.0)
	tag = "-n"
    
    #low snow depth
    else if (field >= 1.0 && field <= 4.0)
	tag = "-l"
    
    #medium snow depth
    else if (field > 4.0 && field <= 9.0)
	tag = "-m"

    #high snow depth
    else if (field > 9.0)
	tag = "-h"

    #output to file
    print(date, field, tag)> "SnowTags.txt"
}
}
