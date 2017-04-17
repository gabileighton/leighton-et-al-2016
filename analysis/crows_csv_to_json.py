import csv
import json

csv_file = open('raw-from-gabi.csv', 'rU')

reader = csv.DictReader(csv_file)

results = []
for row in reader:
  results.append(row)


json.dump(results, open('raw-from-gabi.json', 'w'), ensure_ascii=False)