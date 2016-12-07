import googleplaces
from googleplaces import GooglePlaces, types, lang, ranking
import re, json, itertools

YOUR_API_KEY= 'AIzaSyDFu4TmJ0nqqCl3ZyRRBxe1Pkk8E8Onahs'

google_places = GooglePlaces(YOUR_API_KEY)

def BizHubSearch (KEYWORD, TYPE):

	f = open('cleaning.txt', 'w')
	cities = ["North Bergen, NJ", "Lyndhurst, NJ","Paterson, NJ"]

	for item in cities:
		query_result = google_places.nearby_search(
	    	    location=item, keyword=KEYWORD,
	        	radius=500, rankby=ranking.DISTANCE, types=[TYPE,types.TYPE_ADMINISTRATIVE_AREA_LEVEL_3]) #types.TYPE_DENTIST
		for place in query_result.places:
			loc = place.geo_location
	   		s = str(loc)
	   		f.write(s+"\n")
	return;

def LatLngParsing ():
	
	f=open('cleaning.txt', 'r')
	queryOutput = f.read()
	outputParsed = re.split('(\d+.\d+\d|-\d+.\d+\d)', queryOutput)

	x=[]
	x.extend(outputParsed[1::4])
	
	y=[]
	y.extend(outputParsed[3::4])
	
	for item1,item2 in zip(x,y):
		jsonData = json.dumps({'lat':item1,'lng':item2})
			
	return;

"""	with open('lat.txt','wb') as csvfile:
		writer = csv.writer(csvfile)
	 	for item in x:
	 		writer.writerow([item])

	y=[]
	y.extend(outputParsed[3::4])

	with open('lng.txt','wb') as csvfile:	
	 	writer = csv.writer(csvfile)
	 	for item in y:
	 		writer.writerow([item])
	return;"""

BizHubSearch("Doctor", types.TYPE_DOCTOR)
LatLngParsing()