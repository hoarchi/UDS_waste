import pandas as pd
from datetime import date

df = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\2018_total_waste_bydate.csv")
df['createDate']= df.apply(lambda df: date(int(df['disYear']), int(df['disMonth']), int(df['disDate'])), axis=1)
df.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\2018_total_waste_bydate.csv', index=False, encoding='utf-8-sig')
print(df['createDate'])