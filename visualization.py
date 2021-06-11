#차트 생성
import matplotlib.pyplot as plt

#한글 지원하는 라이브러리 추가
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

#차트 축
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

#차트 데이터 생성
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates

'''
#기술통계량 구하기
data2018 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\2018_total_waste_bydate.csv", parse_dates=['createDate'], index_col= ['createDate'])
data2019 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\2019_total_waste_bydate.csv", parse_dates=['createDate'], index_col= ['createDate'])
data2020 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\2020_total_waste_bydate.csv", parse_dates=['createDate'], index_col= ['createDate'])

sns.distplot(data2018['disQuantity']/1000000, bins=30)
plt.show()
#print(data2018['disQuantity'].describe())
#print(data2018['disQuantity'].sum())
#data2019.describe()
#data2020.describe()
'''

'''
#3년 그래프 이어서 그리기
data2018 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\2018_total_waste_bydate.csv", parse_dates=['createDate'], index_col= ['createDate'])
data2019 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\2019_total_waste_bydate.csv", parse_dates=['createDate'], index_col= ['createDate'])
data2020 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\2020_total_waste_bydate.csv", parse_dates=['createDate'], index_col= ['createDate'])

roll_2018_m7 = pd.Series.rolling(data2018['disQuantity']/1000000, window=7, center = False).mean()
roll_2019_m7 = pd.Series.rolling(data2019['disQuantity']/1000000, window=7, center = False).mean()
roll_2020_m7 = pd.Series.rolling(data2020['disQuantity']/1000000, window=7, center = False).mean()

fig = plt.figure(figsize = (12, 4))
chart = fig.add_subplot(1,1,1)
chart.plot(roll_2018_m7, color='blue' , label='2018')
chart.plot(roll_2019_m7, color='red' , label='2019')
chart.plot(roll_2020_m7, color='orange' , label='2020')
plt.title('Total Waste Trend in 2018, 2019, 2020')
plt.xlabel('Year')
plt.ylabel('Waste Quantity(T)')
plt.legend(loc = 'best')
plt.show()
fig.savefig('./total_waste_3year_001.png', dpi=150, bbox_inches='tight')
'''

'''
#3년 그래프 겹치기 7일 평균선
data2018 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\2018_total_waste_bydate.csv")
data2019 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\2019_total_waste_bydate.csv")
data2020 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\2020_total_waste_bydate.csv")

roll_2018_m7 = pd.Series.rolling(data2018['disQuantity']/1000000, window=7, center = False).mean()
roll_2019_m7 = pd.Series.rolling(data2019['disQuantity']/1000000, window=7, center = False).mean()
roll_2020_m7 = pd.Series.rolling(data2020['disQuantity']/1000000, window=7, center = False).mean()

fig = plt.figure(figsize = (12, 4))
chart = fig.add_subplot(1,1,1)
chart.plot(roll_2018_m7, color='blue' , label='2018')
chart.plot(roll_2019_m7, color='red' , label='2019')
chart.plot(roll_2020_m7, color='orange' , label='2020')
plt.title('Total Waste Trend in 2018, 2019, 2020')
plt.xlabel('DAY')
plt.ylabel('Waste Quantity(T)')
plt.legend(loc = 'best')
plt.show()
fig.savefig('./total_waste_3year_002.png', dpi=150, bbox_inches='tight')
'''

#2018 total graph only
#new_2018['disQuantity'].plot(color='blue', label='High Column')
#plt.show()

#2018 mean7 graph only
#roll_mean7.plot(color='blue', label='7 day rolling mean')
#plt.show()


#plt.title('2018 total Waste in Korea', fontsize=12)
#plt.ylabel('disQuantity', fontsize=10)
#plt.xlabel('createDate', fontsize=10)
#plt.legend(fontsize=10, loc='best')

#시도별 구분할때 좋을 듯
#ax = sns.lineplot(x='Date', y='CumVal', hue='Group',size='Size',data=data2018)
#plt.title('Line Graph of different size w/ Long-form df by seaborn', fontsize=20)
#plt.ylabel('Cummulative Num', fontsize=14)
#plt.xlabel('Date', fontsize=14)
#plt.legend(fontsize=12, loc='best')
#plt.show()

