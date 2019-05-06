#!/usr/bin/env python3

import re
import urllib.request
import googlemaps

#save links in variables
originalLink = "https://www.mbta.com/stops/subway"
linkStart = "https://www.mbta.com/stops/place-"

#open the station page link and read in all of its data
f = urllib.request.urlopen(originalLink)
data = f.read().decode()

#compile regex patterns and open files for writing
patternstop = re.compile(r'href="\/stops\/place-([a-z]+)" data-name="([^\"]+)') #can add , flags=re.DOTALL) to gobble all \n as well                                                              
outstop = open("subwayStopDir.txt", "w")

#if you could collect text from the website                                                                                                                
if data:
    #create a list of all match category tuples found in each line                                                                                         
    found = re.findall(patternstop, data)

    #loop through the list on each tuple                                                                                                                   
    for item in found:

        #output text to a file                                                                                                                             
        print(item[1] + "|" + item[0], file=outstop)

#close subway stop directory        
outstop.close()

#open files for reading and writing
subwayFile = open("subwayStopDir.txt")
outzip = open("subwayStopZipcode.txt", "w")

#compile all regexes
patternzip = re.compile(r'<meta name="description" content=".*?([0-9]{5})')
patternaddress = re.compile(r'<meta name=\"description\" content=\"Station serving MBTA Subway.*?lines at ([^\.]+)')

#for each subway stop in the subway stop directory
for line in subwayFile:

    #split on pipe character
    info = line.split("|")
    
    #visit the link for each subway stop
    f = urllib.request.urlopen(linkStart + info[1])
    data = f.read().decode()

    #if you could collect text from the website                                                                                                               
    if data:
        
        #try to find the zipcode                                                                                     
        found = re.findall(patternzip, data)

        #if the zipcode could be found in the website
        if found:
              
            #output station name and zipcode to a file
            print(info[0] + "|" + found[0], file=outzip)
        
        #account for one case where no address is apparent on the website    
        elif info[0] == "South Street":
            print(info[0] + "|" + "02135", file=outzip)
        
        #otherwise find the zipcode using the googlemaps API   
        else:
            
            #try to find the address
            matchaddress= re.findall(patternaddress, data)
            
            #extract out address
            address = matchaddress[0]
            
            #use google API
            gmaps = googlemaps.Client(key='AIzaSyCjr_8MCdRa601AkKBSRvgdtovv5kepl9Y')
            
            #Geocoding an address, index out the result
            result = gmaps.geocode(address)
            placemark = result[0]['address_components']
            
            #if there is only a postal code, index out the postal code
            if placemark[len(placemark)-1]['types'] == ['postal_code']:
                zipcode = placemark[len(placemark)-1]['long_name']
            
            #otherwise, there is also a postal code suffix, index out the postal code correctly    
            elif placemark[len(placemark)-1]['types'] == ['postal_code_suffix']:
                zipcode = placemark[len(placemark)-2]['long_name']
            
            #output text to a file
            print(info[0] + "|" + zipcode, file=outzip)            
            
#close all files            
subwayFile.close()
outzip.close()
