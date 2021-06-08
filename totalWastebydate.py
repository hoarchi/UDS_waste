import urllib.request as request
import urllib.parse as parse
import json
import csv
import pandas as pd
from pandas import json_normalize

body_total = pd.DataFrame()
try:
    for k in range(0, 12):
        k_month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        month = k_month[k]
        year = '2018'
        url = "http://apis.data.go.kr/B552584/RfidFoodWasteServiceNew/getTotalDateList"
        service_key = "6CA3mYDBH4MjNuGnfZf6cbLOODeOsdEEu5ufYjgPu8a18B/DoN9lifD3Q9XUOV33U8G5d/KlBpOGRIf1DptR7Q=="
        queryParams = '?' + parse.urlencode({parse.quote_plus('ServiceKey'): service_key,
                                             parse.quote_plus('type'): 'json',
                                             parse.quote_plus('disYear'): year,
                                             parse.quote_plus('disMonth'): month,
                                             parse.quote_plus('page'): '1',
                                             parse.quote_plus('rowNum'): '500'})
        res = request.urlopen(url + queryParams)
        request.get_method = lambda: 'GET'
        response_body = res.read().decode('utf-8')
        json_object = json.loads(response_body)
        body = json_normalize(json_object['data']['list'])
        df = pd.DataFrame(body)
        body_total = body_total.append(df)
    body_total.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste' + year + '_total_waste_bydate.csv', index=False, encoding='utf-8-sig')
    print("Success")
except:
    print("Fail")
    print(url + queryParams)
    fail = url + queryParams
