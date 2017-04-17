from collections import defaultdict 
import csv
import json
import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

our_data = json.load(open('sparrowhawks-clusters-google.json'))
their_data = json.load(open('sparrowhawks-clusters-fieldwork.json'))

buckets = defaultdict(lambda: {'our_dark': 0, 'our_n': 0, 'their_dark': 0, 'their_n': 0})


plt.xlabel('Average spottiness score found by Google Images', size=14)
plt.ylabel('Average spottiness score found by fieldwork', size=14)

xs = []
ys = []

for row in our_data:
  if row['Image Usable?'] == 'yes':
    ws = row['closest_ws']['station']

    if row['Colour Morph'] == 'Dark':
      buckets[ws]['our_dark'] += 1

    buckets[ws]['our_n'] += 1

for row in their_data:
  ws = row['closest_ws']['station']

  if row['morph'] == 'dark':
    buckets[ws]['their_dark'] += 1

  buckets[ws]['their_n'] += 1

for bucket_name, bucket in buckets.iteritems():

  if bucket['their_n'] <= 2 or bucket['our_n'] <= 2:
    continue

  our_ratio_dark = bucket['our_dark'] / float(bucket['our_n'])
  their_ratio_dark = bucket['their_dark'] / float(bucket['their_n'])

  print(bucket_name, bucket['our_n'], bucket['their_n'], our_ratio_dark, their_ratio_dark)

  xs.append(our_ratio_dark)
  ys.append(their_ratio_dark)

slope, intercept, r_value, p_value, std_err = stats.linregress(xs, ys)

predict_y = intercept + slope * np.array(xs) 

plt.plot([min(xs), max(xs)], [min(predict_y), max(predict_y)], '--', color='k')

plt.scatter(xs, ys, color='k', s=50)

plt.xlabel('Proportion black morph found by Google Images', size=14)
plt.ylabel('Proportion black morph found by fieldwork', size=14)

plt.show()
#plt.savefig('sparrowhawks-regression.pdf', bbox_inches='tight')
