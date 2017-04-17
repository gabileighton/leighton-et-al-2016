import csv
import scipy
import numpy as np
import matplotlib.pyplot as plt

data = list(csv.DictReader(open('barnowl-data.csv', 'rU')))

roulin_ns = []
google_ns = []

for row in data:
  google_ns.append(float(row['Google n']))
  roulin_ns.append(float(row['Roulin n']))

google_max_n = max(google_ns)
roulin_max_n = max(roulin_ns)

spottiness_y = []
normalized_google_ns = np.array(google_ns) / max(google_ns)

colour_y = []
x = []

for row in data:
  google_n = float(row['Google n'])
  google_colour = float(row['Google colour'])
  google_spottiness = float(row['Google spottiness'])

  roulin_n = float(row['Roulin n'])
  roulin_colour= float(row['Roulin colour'])
  roulin_spottiness = float(row['Roulin spottiness'])

  if google_n <= 10 or roulin_n <= 10:
    continue

  colour_difference = google_colour - roulin_colour
  spottiness_difference = google_spottiness - roulin_spottiness

  confidence = min(google_n / google_max_n, roulin_n / roulin_max_n)

  colour_y.append(colour_difference)
  spottiness_y.append(spottiness_difference)

  x.append(confidence)


plt.xlabel('Confidence', size=14)
plt.ylabel('Difference in average colour score (Google - Fieldwork)', size=14)

plt.scatter(x, colour_y, s=50, c='k')

difference_std = np.std(np.array(colour_y))
difference_mean = np.mean(np.array(colour_y))
print(difference_std, difference_mean)

plt.axhline(difference_mean, color='k')

# cutoff = 5
# plt.axvline(cutoff / float(our_max_n), linestyle=':', color='k')

plt.axhline(difference_mean + 1 * difference_std, color='k', linestyle='dashed')
plt.axhline(difference_mean - 1 * difference_std, color='k', linestyle='dashed')
plt.axhline(difference_mean + 2 * difference_std, color='k', linestyle='dashed')
plt.axhline(difference_mean - 2 * difference_std, color='k', linestyle='dashed')

plt.show()
#plt.savefig('owls-ba-plot-colour.pdf', bbox_inches='tight')

