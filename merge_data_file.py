import pandas as pd
import glob
import os




#apt_merge_2018_byday.csv에서 aptCode별로 disQuantity의 합계를 구하고, aptinfo에서 ctznCnt를 찾아서 나누면, 아파트 단지별 연간 세대당 베출량이 됨.
#이거를 apt_ctznCnt_2018_byyear.csv 로 cityCode와 함께 저장. 연가 지자체별 세대당 배출량 특성을 알 수 있음.
'''
year = "2020"
data = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_merge_" + year + "_byday.csv", encoding='utf-8-sig')
df = data.groupby('aptCode')['disQuantity'].agg(**{'sum_disQuantity_' + year : 'sum'}).reset_index() ## aptCode별 disQuantity의 연간 합계
df = df.round(4) #소수점 4자리로 정리
df = df.replace([np.inf, -np.inf], np.nan) #infinite를 NAN으로 치환

df.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_code_' + year + '.csv', index=False, encoding='utf-8-sig')
print(df.describe())
'''

#2018,2019,2020 aptCode별 disQuantity의 연간 합계를 apt_code_info_merge에 합치고, 연도별 diaQuantity를 ctznCnt로 나누서 정리
'''아파트 단지별 연간 배출량을 세대당 연간 배출량으로 데이터 전처리
df2018 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_code_2018.csv", encoding='utf-8-sig')
df2019 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_code_2019.csv", encoding='utf-8-sig')
df2020 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_code_2020.csv", encoding='utf-8-sig')
df_2018_2019 = pd.merge(df2018,df2019, how='outer',on='aptCode')
df_total = pd.merge(df_2018_2019,df2020, how='outer',on='aptCode')
df_total.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\aptcode_sum_byyear.csv', index=False, encoding='utf-8-sig')
df_total = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\aptcode_sum_byyear.csv", encoding='utf-8-sig')
df_apt_info = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_code_info_merge.csv", encoding='utf-8-sig')
df_apt_info_merge = pd.merge(df_total, df_apt_info, how='outer', on='aptCode')
df_apt_info_merge.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_code_info_toal_merge.csv', index=False, encoding='utf-8-sig')
df_apt_info_total_merge = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_code_info_toal_merge.csv", encoding='utf-8-sig')
df_apt_info_total_merge['sum_disQuantity_2018_ctznCnt'] = df_apt_info_total_merge['sum_disQuantity_2018'] / df_apt_info_total_merge['ctznCnt']
df_apt_info_total_merge['sum_disQuantity_2019_ctznCnt'] = df_apt_info_total_merge['sum_disQuantity_2019'] / df_apt_info_total_merge['ctznCnt']
df_apt_info_total_merge['sum_disQuantity_2020_ctznCnt'] = df_apt_info_total_merge['sum_disQuantity_2020'] / df_apt_info_total_merge['ctznCnt']
df_apt_info_total_merge.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_code_info_toal_merge.csv', index=False, encoding='utf-8-sig')
'''

print(df_apt_info_total_merge.info())
print(df_apt_info_total_merge.head())
print(df_apt_info_total_merge.tail())

'''
#csv에서 시군구명을 시+구 명으로 합치고 데이터 통합

df1 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\sensus_ingu.csv", encoding='utf-8-sig')
df1['create_sido']= df1[['citySidoName','citySggName']].apply(lambda x: '_'.join(x), axis=1)
df2 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\CityList.csv", encoding='utf-8-sig')
df2['create_sido']= df2[['citySidoName','citySggName']].apply(lambda x: '_'.join(x), axis=1)

#df1.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\sensus_ingu_new.csv', index=False, encoding='utf-8-sig')
#df2.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\CityList_new.csv', index=False, encoding='utf-8-sig')
df3 = pd.merge(df1, df2, on="create_sido", how="outer")
df3.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\City_Sensus_data.csv', index=False, encoding='utf-8-sig')
'''

# 인구자료와 배출량 자료 합지고, 인당 일별 배출량 생성하기
'''
data2018 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\city_merge_2018_bydate.csv")
data2018['create_sido']= data2018[['citySidoName','citySggName']].apply(lambda x: '_'.join(x), axis=1)
city_sensus = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\City_Sensus_data.csv")
df2018 = pd.merge(data2018, city_sensus, on="create_sido", how="outer")
df2018['disQuantity_ingu']= df2018.apply(lambda df2018: df2018['disQuantity'] / df2018['2018_total_ingu'] , axis=1)
df2018.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\city_sensus_waste_2018_bydate.csv', index=False, encoding='utf-8-sig')
'''

# 폴더안에 있는 파일 하나로 합치기
'''
input_file = r'C:\\Users\\hogun\\PycharmProjects\\UDS_wastecity_waste_2020_byday' # csv파일들이 있는 디렉토리 위치
output_file = r'C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\city_merge_2020_byday.csv' # 병합하고 저장하려는 파일명

allFile_list = glob.glob(os.path.join(input_file, '*_waste.csv')) # glob함수로 sales_로 시작하는 파일들을 모은다
allData = [] # 읽어 들인 csv파일 내용을 저장할 빈 리스트를 하나 만든다

for file in allFile_list:
    df = pd.read_csv(file) # for구문으로 csv파일들을 읽어 들인다
    allData.append(df) # 빈 리스트에 읽어 들인 내용을 추가한다

dataCombine = pd.concat(allData, axis=0, ignore_index=True) # concat함수를 이용해서 리스트의 내용을 병합
# axis=0은 수직으로 병합함. axis=1은 수평. ignore_index=True는 인데스 값이 기존 순서를 무시하고 순서대로 정렬되도록 한다.
dataCombine.to_csv(output_file, index=False) # to_csv함수로 저장한다. 인데스를 빼려면 False로 설정
print("SUCCESS")
'''
