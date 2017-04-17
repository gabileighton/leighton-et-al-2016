import csv
import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data = list(csv.DictReader(open('barnowl-data.csv', 'rU')))

def get_axis():
  for row in data:
    google_n = float(row['Google n'])
    google_colour = float(row['Google colour'])
    google_spottiness = float(row['Google spottiness'])

    roulin_n = float(row['Roulin n'])
    roulin_colour= float(row['Roulin colour'])
    roulin_spottiness = float(row['Roulin spottiness'])

    if google_n >= 10:
      yield google_spottiness, roulin_spottiness

plt.xlabel('Average spottiness score found by Google Images', size=14)
plt.ylabel('Average spottiness score found by fieldwork', size=14)

xs = []
ys = []

for x, y in get_axis():
  xs.append(9 - x)
  ys.append(y)

slope, intercept, r_value, p_value, std_err = stats.linregress(xs, ys)

print(slope, intercept, r_value ** 2)

predict_y = intercept + slope * np.array(xs) 

plt.plot([min(xs), max(xs)], [min(predict_y), max(predict_y)], '--', color='k')

plt.scatter(xs, ys, color='k', s=50)

plt.xlabel('Proportion black morph found by Google Images', size=14)
plt.ylabel('Proportion black morph found by fieldwork', size=14)

#plt.show()
plt.savefig('barnowls-spotiness-regression.pdf', bbox_inches='tight')

