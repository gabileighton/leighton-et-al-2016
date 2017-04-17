import csv
import json


table_json = '{"Scotland":{"Hooded crow":{"count_correct":42,"count_wrong":0},"Carrion crow":{"count_correct":15,"count_wrong":4}},"Germany":{"Hooded crow":{"count_correct":37,"count_wrong":5},"Carrion crow":{"count_correct":30,"count_wrong":0}},"Italy":{"Hooded crow":{"count_correct":24,"count_wrong":0},"Carrion crow":{"count_correct":2,"count_wrong":0}},"Denmark":{"Hooded crow":{"count_correct":31,"count_wrong":0},"Carrion crow":{"count_correct":0,"count_wrong":15}},"Switzerland":{"Hooded crow":{"count_correct":0,"count_wrong":3},"Carrion crow":{"count_correct":14,"count_wrong":0}},"Czech Republic":{"Hooded crow":{"count_correct":14,"count_wrong":1},"Carrion crow":{"count_correct":4,"count_wrong":10}},"Austria":{"Hooded crow":{"count_correct":17,"count_wrong":0},"Carrion crow":{"count_correct":7,"count_wrong":3}}}'

table = json.loads(table_json)

out_file = open('crows-table-ibis.csv', 'w')

out_file_csv = csv.DictWriter(out_file, fieldnames=['country', 'hooded_crow_count_correct', 'hooded_crow_count_wrong', 'carrion_crow_count_correct', 'carrion_crow_count_wrong'])

out_file_csv.writeheader()

for country, values in table.iteritems():
  out_file_csv.writerow({
    'country': country,
    'hooded_crow_count_correct': values['Hooded crow']['count_correct'],
    'hooded_crow_count_wrong': values['Hooded crow']['count_wrong'],
    'carrion_crow_count_correct': values['Carrion crow']['count_correct'],
    'carrion_crow_count_wrong': values['Carrion crow']['count_wrong'],
  })