import googlemaps
import urllib, json, ranking

def GoogPlac(lat,lng,radius,types,key):
	AUTH_KEY = key
	LOCATION = str(lat) + "," + str(lng)
	RADIUS = radius
	TYPES = types
	MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
	'?location=%s'
	'&radius=%s'
	'&types=%s'
	'&sensor=false&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)

response = urllib.urlopen(MyUrl)
jsonRaw = response.read()
jsonData = json.loads(jsonRaw)
return jsonData
