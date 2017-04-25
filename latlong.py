import googlemaps
gmaps_client = googlemaps.Client(key='')
with open('list_new.txt') as f, open('latlong_values.csv', 'w') as e:
    e.write('place,lat,lon\n')
    for line in f:
        place = line.strip() + ' Karnataka'
        geocode_result = gmaps_client.geocode(place)
        print place
        e.write(
            place
            + ','
            + str(geocode_result[0]['geometry']['location']['lat'])
            + ','
            + str(geocode_result[0]['geometry']['location']['lng'])
            + '\n'
        )

# Output
# <place1>:
#     <lat>: 2.31341
#     <lon>: 24.4442
# <place2>:
#     <lat>: 4.54421
#     <lon>: 113.1141
