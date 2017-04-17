import csv
import json


sci_json = '{"Scotland":{"Hooded crow":{"count_correct":42,"count_wrong":0},"Carrion crow":{"count_correct":18,"count_wrong":1}},"Germany":{"Hooded crow":{"count_correct":38,"count_wrong":4},"Carrion crow":{"count_correct":29,"count_wrong":1}},"Italy":{"Hooded crow":{"count_correct":22,"count_wrong":2},"Carrion crow":{"count_correct":2,"count_wrong":0}},"Denmark":{"Hooded crow":{"count_correct":30,"count_wrong":1},"Carrion crow":{"count_correct":6,"count_wrong":9}},"Switzerland":{"Hooded crow":{"count_correct":2,"count_wrong":1},"Carrion crow":{"count_correct":14,"count_wrong":0}},"Czech Republic":{"Hooded crow":{"count_correct":1,"count_wrong":14},"Carrion crow":{"count_correct":13,"count_wrong":1}},"Austria":{"Hooded crow":{"count_correct":16,"count_wrong":1},"Carrion crow":{"count_correct":7,"count_wrong":3}}}'

mol_json = '{"Scotland":{"Hooded crow":{"count_correct":34,"count_wrong":8},"Carrion crow":{"count_correct":19,"count_wrong":0}},"Germany":{"Hooded crow":{"count_correct":38,"count_wrong":4},"Carrion crow":{"count_correct":29,"count_wrong":1}},"Italy":{"Hooded crow":{"count_correct":22,"count_wrong":2},"Carrion crow":{"count_correct":2,"count_wrong":0}},"Denmark":{"Hooded crow":{"count_correct":30,"count_wrong":1},"Carrion crow":{"count_correct":5,"count_wrong":10}},"Switzerland":{"Hooded crow":{"count_correct":2,"count_wrong":1},"Carrion crow":{"count_correct":14,"count_wrong":0}},"Czech Republic":{"Hooded crow":{"count_correct":15,"count_wrong":0},"Carrion crow":{"count_correct":1,"count_wrong":13}},"Austria":{"Hooded crow":{"count_correct":17,"count_wrong":0},"Carrion crow":{"count_correct":7,"count_wrong":3}}}'

ibis_json = '{"Scotland":{"Hooded crow":{"count_correct":41,"count_wrong":0},"Carrion crow":{"count_correct":15,"count_wrong":4}},"Germany":{"Hooded crow":{"count_correct":37,"count_wrong":5},"Carrion crow":{"count_correct":29,"count_wrong":0}},"Italy":{"Hooded crow":{"count_correct":24,"count_wrong":0},"Carrion crow":{"count_correct":2,"count_wrong":0}},"Isle of Man":{"Hooded crow":{"count_correct":0,"count_wrong":2},"Carrion crow":{"count_correct":0,"count_wrong":0}},"Denmark":{"Hooded crow":{"count_correct":30,"count_wrong":0},"Carrion crow":{"count_correct":0,"count_wrong":15}},"Switzerland":{"Hooded crow":{"count_correct":0,"count_wrong":3},"Carrion crow":{"count_correct":14,"count_wrong":0}},"Faroe Islands":{"Hooded crow":{"count_correct":0,"count_wrong":0},"Carrion crow":{"count_correct":0,"count_wrong":1}},"Czech Republic":{"Hooded crow":{"count_correct":13,"count_wrong":1},"Carrion crow":{"count_correct":4,"count_wrong":10}},"Austria":{"Hooded crow":{"count_correct":16,"count_wrong":0},"Carrion crow":{"count_correct":7,"count_wrong":3}},"Slovenia":{"Hooded crow":{"count_correct":3,"count_wrong":0},"Carrion crow":{"count_correct":0,"count_wrong":0}}}'

table = json.loads(sci_json)

out_file = open('crows-table-sci.csv', 'w')

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