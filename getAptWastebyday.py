#데이터 가져오기 - 아파트별 요일별 배출 총량

import urllib.request as request
import urllib.parse as parse
import json
import csv
import pandas as pd
from pandas import json_normalize

#len(apt_code_list) + 1

f_city = open('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\CityList.csv', encoding='utf-8-sig')
reader_city = csv.reader(f_city)

city_code_list = []
for col_city in reader_city:
    code = col_city[0]
    city_code_list.append(code)

for i in range(1, len(city_code_list) + 1):
    city_code = city_code_list[i]
    f_apt = open('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\apt_code_info_list\\' + city_code + '_city_apt_info.csv', encoding='utf-8-sig')
    reader_apt = csv.reader(f_apt)

    apt_code_list = []
    apt_citizen_list = []
    apt_name_list = []
    for col_apt in reader_apt:
        codea = col_apt[0]
        coden = col_apt[2]
        codec = col_apt[16]
        apt_code_list.append(codea)
        apt_name_list.append(coden)
        apt_citizen_list.append(codec)


    for j in range(1, len(apt_code_list)):
        apt_code = apt_code_list[j]
        apt_name = apt_name_list[j]
        apt_citizen = apt_citizen_list[j]
        print(apt_code)

        body_total = pd.DataFrame()
        try:
            for k in range(0, 12):
                k_month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
                month = k_month[k]
                year = '2020'
                url = "http://apis.data.go.kr/B552584/RfidFoodWasteServiceNew/getCityAptDayList"
                service_key = "6CA3mYDBH4MjNuGnfZf6cbLOODeOsdEEu5ufYjgPu8a18B/DoN9lifD3Q9XUOV33U8G5d/KlBpOGRIf1DptR7Q=="
                queryParams = '?' + parse.urlencode({parse.quote_plus('ServiceKey'): service_key,
                                                     parse.quote_plus('type'): 'json',
                                                     parse.quote_plus('disYear'): year,
                                                     parse.quote_plus('disMonth'): month,
                                                     parse.quote_plus('cityCode'): city_code,
                                                     parse.quote_plus('aptCode'): apt_code,
                                                     parse.quote_plus('page'): '1',
                                                     parse.quote_plus('rowNum'): '300'})
                res = request.urlopen(url + queryParams)
                request.get_method = lambda: 'GET'
                response_body = res.read().decode('utf-8')
                json_object = json.loads(response_body)
                body = json_normalize(json_object['data']['list'])
                df = pd.DataFrame(body)
                df['disQuantity_by_ctznCnt'] = df['disQuantity'] / int(apt_citizen)
                body_total = body_total.append(df)
            body_total.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\apt_waste_' + year + '_byday\\' + apt_code + '_' + year + '_waste.csv', index=False, encoding='utf-8-sig')
        except:
            print("Fail")
            print(url + queryParams)
            fail = url + queryParams
            with open('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\apt_waste_' + year + '_byday\\00_fail_list.csv', 'a', encoding='utf-8-sig') as csvfile:
                writer_object = csv.writer(csvfile)
                writer_object.writerow(fail.split(','))
                csvfile.close()
