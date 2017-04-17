import numpy as np
from collections import defaultdict
import json

def build_key(state, subspecies):
	subspecies = subspecies.replace('U.a.', 'U. a.')
	return '%s-%s' % (state, subspecies)

def bucket_ours(ours_raw):
	buckets = defaultdict(lambda: {'black': 0, 'nonblack': 0})
	for individual in ours_raw:
		if not 'Image Usable?' in individual or not individual['Image Usable?'] == 'yes':
			continue

		if not 'Subspecies' in individual:
			continue

		if not 'state' in individual:
			continue

		if individual['state'] == 'Olomouc Region':
			print(individual)

		bucket = buckets[build_key(individual['state'], individual['Subspecies'])]

		if individual['Colour Morph'] == 'Black':
			bucket['black'] += 1
		elif individual['Colour Morph'] == 'Non-black':
			bucket['nonblack'] += 1
		else:
			raise Exception('Encountered neither black nor nonblack %s' % individual)

	return buckets

def get_ours():
	ours_raw = json.load(open('final-blackbear-results/final-bear-results.json'))
	return bucket_ours(ours_raw)

def parse_country(raw):
	region = raw.strip().split('\n')
	region_name = region[0]
	for region in region[1:]:
		raw_line = region.strip().split(' ')
		n, bfn, bfp, nbfn, nbfp = raw_line[:-3]
		data = dict(n=n, bfn=bfn, nbfn=nbfn, nbfp=nbfp)
		species = ' '.join(raw_line[-3:])
		yield {'region_name': region_name, 'species': species, 'data': data}

def bucket_theirs(countries):
	buckets = {}
	for country in countries:
		for region in country:
			buckets[build_key(region['region_name'], region['species'])] = {
				'black': int(region['data']['bfn']),	
				'nonblack': int(region['data']['nbfn']),
			}
	return buckets

def get_theirs():
	raw_countries = open('theirs.txt').read().split('-')
	countries = map(parse_country, raw_countries)
	return bucket_theirs(countries)

our_buckets = get_ours()
their_buckets = get_theirs()

x = []
y = []
area = []

for bucket_key in our_buckets:
	if bucket_key not in their_buckets:
		#print('Throwing away %s' % bucket_key.encode('utf-8'))
		continue

	their_bucket = their_buckets[bucket_key]
	our_bucket = our_buckets[bucket_key]	

	their_n = their_bucket['black'] + their_bucket['nonblack']
	their_ratio = their_bucket['black'] / float(their_n)
	our_n = our_bucket['black'] + our_bucket['nonblack']
	our_ratio = our_bucket['black'] / float(our_n)

	x.append((our_ratio + their_ratio) / 2.0)
	area.append((our_ratio + their_ratio) / 2.0)

	difference = our_ratio - their_ratio
	y.append(difference)

import matplotlib.pyplot as plt

difference_std = np.std(np.array(y))
difference_mean = np.mean(np.array(y))

plt.axhline(difference_mean)

plt.axhline(difference_mean + 2 * difference_std)
plt.axhline(difference_mean - 2 * difference_std)

plt.scatter(x, y)
plt.show()