import json
import requests

ours_raw = json.load(open('bears.json'))

url = 'http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=true'

def get_state_from_result(result):
	for address_component in result:
		if 'administrative_area_level_1' in address_component['types']:
			print(address_component)
			return address_component['long_name']

for individual in ours_raw:
	if 'Location' in individual:
		location = json.loads(individual['Location'])
		lat, lng = location['latitude'], location['longitude']
		response = requests.get(url % (lat, lng))
		if response.json()['results']:
			individual['state'] = get_state_from_result(response.json()['results'][0]['address_components'])

json.dump(ours_raw, open('bears-with-states.json', 'w'))

