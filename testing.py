import googleplaces
from googleplaces import GooglePlaces, types, lang, ranking

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
data = open("placesDump.txt","w")
data.write(str(query_result))
data.close()


for place in query_result.places:
    # Returned places from a query are place summaries.
    print place.name
    print place.geo_location
    print place.place_id

    place.get_details()
    print place.formatted_address

