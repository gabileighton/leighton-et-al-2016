from collections import defaultdict 
import csv
import json
import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

google_data = json.load(open('sparrowhawks-clusters-google.json'))
field_clusters = list(csv.DictReader(open('new-chosen-clusters.csv')))

buckets = defaultdict(lambda: {'google_dark': 0, 'google_n': 0, 'fieldwork_dark': 0, 'fieldwork_n': 0})

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

plt.xlabel('Confidence', size=14)
plt.ylabel('Difference in proportion of black morph (Google - Fieldwork)', size=14)

xs = []
ys = []

google_ns = []
fieldwork_ns = []

for bucket_name, bucket in buckets.iteritems():
  google_n = int(bucket['google_n'])
  google_ns.append(google_n)
  fieldwork_n = int(bucket['fieldwork_n'])
  fieldwork_ns.append(fieldwork_n)

max_google_n = max(google_ns)
max_fieldwork_n = max(fieldwork_ns)

for bucket_name, bucket in buckets.iteritems():
  google_n = int(bucket['google_n'])
  google_ratio_dark = bucket['google_dark'] / float(bucket['google_n'])
  field_ratio_dark = bucket['fieldwork_dark'] / float(bucket['fieldwork_n'])
  fieldwork_n = int(bucket['fieldwork_n'])

  if google_n <= 5:
    continue

  difference = google_ratio_dark - field_ratio_dark

  confidence = min(google_n / float(max_google_n), fieldwork_n / float(max_fieldwork_n))

  xs.append(confidence)
  ys.append(difference)


difference_std = np.std(np.array(ys))
difference_mean = np.mean(np.array(ys))

plt.axhline(difference_mean, color='k')


plt.axhline(difference_mean + 1 * difference_std, color='k', linestyle='dashed')
plt.axhline(difference_mean - 1 * difference_std, color='k', linestyle='dashed')
plt.axhline(difference_mean + 2 * difference_std, color='k', linestyle='dashed')
plt.axhline(difference_mean - 2 * difference_std, color='k', linestyle='dashed')


plt.scatter(xs, ys, color='k', s=50)
plt.show()
#plt.savefig('sparrowhawks-ba-plot.pdf', bbox_inches='tight')
