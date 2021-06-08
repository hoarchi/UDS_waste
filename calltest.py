import requests as rq
import urllib.request
import urllib.parse as parse

url = "http://apis.data.go.kr/B552584/RfidFoodWasteServiceNew/getTotalTimeList"
service_key = "6CA3mYDBH4MjNuGnfZf6cbLOODeOsdEEu5ufYjgPu8a18B%2FDoN9lifD3Q9XUOV33U8G5d%2FKlBpOGRIf1DptR7Q%3D%3D"
queryParams = '?' + parse.urlencode({ parse.quote_plus('ServiceKey') : '서비스키' })

res = rq.get(url, queryParams)
print(res)
print(res.status_code)
if res.status_code == 200:
    print("[성공]")
else:
    print("에러")
