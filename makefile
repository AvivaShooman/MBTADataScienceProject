all: snowPlot.pdf

clean:
	rm snowPlot.pdf XAxis.txt YAxis.txt 3D.txt AllData.txt incomeZipcodes.txt subwayStopZipcode.txt subwayStopDir.txt ridershipWithSnowData.txt SnowTags.txt totalRidership20172018.txt GSE_20172018.txt

snowPlot.pdf: XAxis.txt YAxis.txt 3D.txt plotfixed.py
	python3 plotfixed.py

XAxis.txt YAxis.txt 3D.txt: AllData.txt filesForGraph.py
	python3 filesForGraph.py

AllData.txt: incomeZipcodes.txt ridershipWithSnowData.txt mergeRidershipSnowIncome.py
	python3 mergeRidershipSnowIncome.py 

incomeZipcodes.txt: subwayStopZipcode.txt IncomePop.gz grabIncome.py
	python3 grabIncome.py

subwayStopZipcode.txt subwayStopDir.txt: scrapeStationsv2.py
	python3 scrapeStationsv2.py

ridershipWithSnowData.txt: SnowTags.txt totalRidership20172018.txt mergeSnowStationsfixed.py
	python3 mergeSnowStationsfixed.py

SnowTags.txt: SnowData20172018.csv SnowTags.awk
	gawk -f SnowTags.awk

totalRidership20172018.txt: GSE_20172018.txt SortStations.awk
	gawk -f SortStations.awk

GSE_20172018.txt: gated_station_entries_2018_01.csv gated_station_entries_2017.csv	
	cat gated_station_entries_2017.csv gated_station_entries_2018_0*.csv | sort> GSE_20172018.txt
