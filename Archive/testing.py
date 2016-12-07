import googleplaces
from googleplaces import GooglePlaces, types, ranking
import json

a=2

if a==2:
    dynLocation="Hoboken,NJ"

YOUR_API_KEY= 'AIzaSyDFu4TmJ0nqqCl3ZyRRBxe1Pkk8E8Onahs'

google_places = GooglePlaces(YOUR_API_KEY)
query_result = google_places.nearby_search(
        location=dynLocation, keyword='Dentist',
        radius=500, rankby=ranking.DISTANCE, types=[types.TYPE_DENTIST,types.TYPE_ADMINISTRATIVE_AREA_LEVEL_3])

for place in query_result.places:
    print place.name
    print place.geo_location
    place.get_details()
    print place.formatted_address

#with open('placesDump.txt', 'w') as outfile:
 #   json.dump(query_result,outfile)