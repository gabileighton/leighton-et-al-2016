from collections import defaultdict 
import csv
import json
import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

google_data = json.load(open('sparrowhawks-clusters-google.json'))
field_clusters = list(csv.DictReader(open('new-chosen-clusters.csv')))

buckets = defaultdict(lambda: {'google_dark': 0, 'google_n': 0, 'fieldwork_dark': 0, 'fieldwork_n': 0, 'rainfall': 0})

for google_siting in google_data:
  if google_siting['Image Usable?'] != 'yes':
    continue

  cluster = google_siting['nearest_usable_cluster']

  if google_siting['Colour Morph'] == 'Dark':
    buckets[cluster]['google_dark'] += 1

  buckets[cluster]['google_n'] += 1

for field_cluster in field_clusters:
  cluster = field_cluster['site/cluster']
  buckets[cluster]['fieldwork_dark'] += int(field_cluster['darkbirds'])
  buckets[cluster]['fieldwork_n'] += int(field_cluster['total birds'])

  buckets[cluster]['rainfall'] += float(field_cluster['rainfall'])

xs = []
google_ys = []
field_ys = []

google_sizes = []
field_sizes = []

dw = csv.DictWriter(open('for-gabi.csv', 'w'), fieldnames=['place_name', 'google_dark', 'google_light', 'google_n', 'google_proportion_dark', 'field_dark', 'field_light', 'field_n', 'field_proportion_dark', 'rainfall'])
dw.writeheader()

for bucket_name, bucket in buckets.iteritems():
  google_ratio_dark = bucket['google_dark'] / float(bucket['google_n'])
  field_ratio_dark = bucket['fieldwork_dark'] / float(bucket['fieldwork_n'])

  rainfall = bucket['rainfall']

  xs.append(rainfall)
  google_ys.append(google_ratio_dark)
  field_ys.append(field_ratio_dark)

  google_sizes.append(int(bucket['google_n']))
  field_sizes.append(int(bucket['fieldwork_n']))

  dw.writerow({
    'place_name': bucket_name,
    'google_dark': bucket['google_dark'],
    'google_light': bucket['google_n'] - bucket['google_dark'],
    'google_n': bucket['google_n'],
    'google_proportion_dark': bucket['google_dark'] / float(bucket['google_n']),
    'field_dark': bucket['fieldwork_dark'],
    'field_light': bucket['fieldwork_n'] - bucket['fieldwork_dark'],
    'field_n': bucket['fieldwork_n'],
    'field_proportion_dark': bucket['fieldwork_dark'] / float(bucket['fieldwork_n']),
    'rainfall': bucket['rainfall'],
    })