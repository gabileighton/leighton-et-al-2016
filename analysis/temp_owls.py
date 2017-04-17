import time
import csv
import json
import requests
from sqlalchemy.orm import joinedload
from backend.models import SurveyResult, SurveyField

def get_state_from_result(result):
  for address_component in result:
    if 'administrative_area_level_1' in address_component['types']:
      return address_component['long_name']

def get_country_from_result(result):
  for address_component in result:
    if 'country' in address_component['types']:
      return address_component['long_name']

url = 'http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=true'

survey_id = 4

survey_fields = (SurveyField.query
  .filter(SurveyField.survey_id==survey_id)
  .all())

fieldnames = ['survey_id'] + [sf.label for sf in survey_fields] + ['state', 'country', 'latitude', 'longitude', 'direct_link', 'visible_link', 'search_name', 'search_query', 'search_result_rank', 'search_result_id'] 
fieldnames_by_id = {sf.id_: sf.label for sf in survey_fields}

survey_results = (SurveyResult.query
  .options(joinedload('result_fields'))
  .filter(SurveyResult.survey_id==survey_id)
  .all())

results = []

for survey_result in survey_results:
  result = {fieldnames_by_id[rf.survey_field_id]: rf.value for rf in survey_result.result_fields if rf.survey_field_id}
  result['survey_id'] = survey_result.id_
  result['direct_link'] = survey_result.search_result.link
  result['visible_link'] = survey_result.search_result.visible_link
  result['search_result_id'] = survey_result.search_result.id_
  result['search_name'] = survey_result.search_result.search.name
  result['search_query'] = survey_result.search_result.search.query_string
  result['search_result_rank'] = survey_result.search_result.rank
  if 'Location' in result:
    location = json.loads(result['Location'])
    latitude, longitude = location['latitude'], location['longitude']
    result['latitude'] = latitude
    result['longitude'] = longitude
    response = requests.get(url % (latitude, longitude))
    if response.json()['results']:
      result['state'] = get_state_from_result(response.json()['results'][0]['address_components'])
      result['country'] = get_country_from_result(response.json()['results'][0]['address_components'])
    time.sleep(0.1)
  results.append(result)

csv_file = open('final-owl-results.csv', 'w')

csv_dict_writer = csv.DictWriter(csv_file, fieldnames)
csv_dict_writer.writeheader()

for result in results:
 csv_dict_writer.writerow(result)

json_file = open('final-owl-results.json', 'w')

json.dump(results, json_file)

csv_file.close()
json_file.close()

