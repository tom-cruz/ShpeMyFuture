import googleplaces
import json
import urllib, json

def GoogPlac(location,radius,types,key):
	AUTH_KEY = 'AIzaSyDFu4TmJ0nqqCl3ZyRRBxe1Pkk8E8Onahs'
	LOCATION = "Ewing, New Jersey"
	RADIUS = 2000
	TYPES = Dentist
	MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
	'?location=%s'
	'&radius=%s'
	'&types=%s'
	'&sensor=false&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)

	response = urllib.urlopen(MyUrl)
	jsonRaw = response.read()
	jsonData = json.loads(jsonRaw)
	return jsonData

GoogPlac(location="Ewing, New Jersey", radius=2000, type=Dentist)