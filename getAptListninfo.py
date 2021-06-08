import urllib.request as request
import urllib.parse as parse
import json
import csv
import pandas as pd
from pandas import json_normalize

city_code_list = []
city_info_list = []
f = open('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\CityList.csv', encoding='utf-8-sig')
reader = csv.reader(f)
for col in reader:
    code = col[0]
    city_code_list.append(code)

for i in range(1, len(city_code_list) + 1):
    try:
        city_code = city_code_list[i]
        url_01 = "http://apis.data.go.kr/B552584/RfidFoodWasteServiceNew/getAptlist"
        service_key = "6CA3mYDBH4MjNuGnfZf6cbLOODeOsdEEu5ufYjgPu8a18B/DoN9lifD3Q9XUOV33U8G5d/KlBpOGRIf1DptR7Q=="
        queryParams_01 = '?' + parse.urlencode({parse.quote_plus('ServiceKey'): service_key,
                                             parse.quote_plus('type'): 'json',
                                             parse.quote_plus('cityCode'): city_code,
                                             parse.quote_plus('page'): '1',
                                             parse.quote_plus('rowNum'): '300'})
        url_02 = "http://apis.data.go.kr/B552584/RfidFoodWasteServiceNew/getAptLocInfoList"
        queryParams_02 = '?' + parse.urlencode({parse.quote_plus('ServiceKey'): service_key,
                                             parse.quote_plus('type'): 'json',
                                             parse.quote_plus('cityCode'): city_code,
                                             parse.quote_plus('page'): '1',
                                             parse.quote_plus('rowNum'): '300'})

        res_01 = request.urlopen(url_01 + queryParams_01)
        request.get_method = lambda: 'GET'
        response_body_01 = res_01.read().decode('utf-8')
        json_object_01 = json.loads(response_body_01)

        res_02 = request.urlopen(url_02 + queryParams_02)
        request.get_method = lambda: 'GET'
        response_body_02 = res_02.read().decode('utf-8')
        json_object_02 = json.loads(response_body_02)

        body_01 = json_normalize(json_object_01['data']['list'])
        body_02 = json_normalize(json_object_02['data']['list'])
        body = pd.merge(body_01, body_02, on='aptCode', how='outer')
        body.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\apt_code_info_list\\' + city_code + '_city_apt_info.csv', index=False,
                    encoding='utf-8-sig')
        print("Success" + str(city_code))
    except:
        print("Fail next of " + str(city_code))


