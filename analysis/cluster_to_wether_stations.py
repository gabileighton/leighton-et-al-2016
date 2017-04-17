import re
import json
import csv
from geopy.distance import great_circle

our_data = list(json.load(open('sparrowhawks.json')))

clusters = list(csv.DictReader(open('new-chosen-clusters.csv', 'rU')))

for individual in our_data:
  closest = None
  closest_distance = 2**32
  our_coords = individual['Latitude'], individual['Longitude']

  for cluster in clusters:
    cluster_coords = cluster['Y'], cluster['X']

    distance = great_circle(our_coords, cluster_coords).km
    if distance < closest_distance:
      closest_distance = distance
      closest = cluster 

  individual['nearest_usable_cluster'] = closest['site/cluster']
  individual['distance_to_cluster'] = closest_distance

json.dump(our_data, open('sparrowhawks-clusters-google.json', 'w'))
