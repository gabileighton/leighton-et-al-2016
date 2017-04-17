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


plt.xlabel('Average spottiness score found by Google Images', size=14)
plt.ylabel('Average spottiness score found by fieldwork', size=14)

xs = []
ys = []

for bucket_name, bucket in buckets.iteritems():
  google_ratio_dark = bucket['google_dark'] / float(bucket['google_n'])
  field_ratio_dark = bucket['fieldwork_dark'] / float(bucket['fieldwork_n'])

  if bucket['google_n'] <= 5:
    continue

  xs.append(google_ratio_dark)
  ys.append(field_ratio_dark)

slope, intercept, r_value, p_value, std_err = stats.linregress(xs, ys)

print(slope, intercept, r_value**2)

predict_y = intercept + slope * np.array(xs) 

plt.plot([min(xs), max(xs)], [min(predict_y), max(predict_y)], '--', color='k')

plt.scatter(xs, ys, color='k', s=50)

plt.xlabel('Proportion black morph found by Google Images', size=14)
plt.ylabel('Proportion black morph found by fieldwork', size=14)

plt.show()
#plt.savefig('sparrowhawks-regression.pdf', bbox_inches='tight')
