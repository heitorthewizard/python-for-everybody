import urllib.request, urllib.parse, urllib.error
import json

service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    url = service_url + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    coded_url = urllib.request.urlopen(url)
    data = coded_url.read().decode()
    print('Retrived', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure To Retrive ===')
        print(data)
        continue
    latitude = js['results'][0]['geometry']['location']['lat']
    longitude = js['results'][0]['geometry']['location']['lng']
    print('latitude', latitude, 'longitude', longitude)
    location = js['results'][0]['formatted_address']
    print(location)

