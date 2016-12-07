from __future__ import print_function
import os
import string
import googleplaces
from googleplaces import GooglePlaces, types, lang, ranking
import re
import csv

f = open('cleaning.txt', 'w')
x = []
y = []
YOUR_API_KEY= 'AIzaSyDFu4TmJ0nqqCl3ZyRRBxe1Pkk8E8Onahs'

google_places = GooglePlaces(YOUR_API_KEY)
# You may prefer to use the text_search API, instead.
query_result = google_places.nearby_search(
        location='Ewing, New Jersey', keyword='Dentist',
        radius=500, rankby=ranking.DISTANCE, types=[types.TYPE_DENTIST,types.TYPE_ADMINISTRATIVE_AREA_LEVEL_3])
# If types param contains only 1 item the request to Google Places API
# will be send as type param to fullfil:
# http://googlegeodevelopers.blogspot.com.au/2016/02/changes-and-quality-improvements-in_16.html

#if query_result.has_attributions:


for place in query_result.places:
    loc = place.geo_location
    s = str(loc)
    #result = re.sub('[^0-9, ]', '', s)
    f.write(s+"\n")





f=open('cleaning.txt', 'r')
queryOutput = f.read()
outputParsed = re.split('(\d+.\d+\d|-\d+.\d+\d)', queryOutput)
outputParsed.extend(outputParsed[1::5])
#s = str(outputParsed)

with open('latlng','wb') as csvfile:
	writer = csv.writer(csvfile)
 	for item in outputParsed:
 		writer.writerow([item])



    # Returned places from a query are place summaries.
	#data = open("placesDump.txt","w")
	#data.write(str(query_result))
	#data.close()
	#print place.geo_location
	#print > f, "lkasjdflaskdjfh"
#f.write(place.geo_location)
	#place.geo_location
 
    #for item in loc:
	#	f.write(str(item + "\n"))
	


 	
