import urllib.request as request
import urllib.parse as parse
import json

url = "http://apis.data.go.kr/B552584/RfidFoodWasteServiceNew/getCityAptDayList"
service_key = "6CA3mYDBH4MjNuGnfZf6cbLOODeOsdEEu5ufYjgPu8a18B/DoN9lifD3Q9XUOV33U8G5d/KlBpOGRIf1DptR7Q=="
queryParams = '?' + parse.urlencode({ parse.quote_plus('ServiceKey') : service_key,
                                      parse.quote_plus('type') : 'json',
                                      parse.quote_plus('disYear') : '2020',
                                      parse.quote_plus('disMonth') : '01',
                                      parse.quote_plus('citycode'): 'W34',
                                      parse.quote_plus('aptcode'): 'W34129',
                                      parse.quote_plus('page') : '1',
                                      parse.quote_plus('rowNum') : '10' })

res = request.urlopen(url + queryParams)
request.get_method = lambda: 'GET'
response_body = res.read().decode('utf-8')
json_data = json.loads(response_body)
print(json.dumps(json_data, indent=2, ensure_ascii=False))