#차트 생성
import matplotlib.pyplot as plt

#한글 지원하는 라이브러리 추가
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

#차트 축
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

'''
#세대수와 세대수별 배출량의 상관관계 분석
year = "2020"
aptinfo = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_code_info_merge.csv", encoding='utf-8-sig')
aptdata = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_group_" + year + ".csv", encoding='utf-8-sig')
aptinfo = aptinfo.replace([np.inf, -np.inf], np.nan) #infinite를 NAN으로 치환
aptdata = aptdata.replace([np.inf, -np.inf], np.nan) #infinite를 NAN으로 치환
dataframe = pd.merge(aptinfo, aptdata, on="aptCode", how="outer")
dataframe = dataframe.round(4) #소수점 4자리로 정리
'''

'''
#결측치 정리
Q1 = dataframe['sum_Quantity'].quantile(0.0)
Q3 = dataframe['sum_Quantity'].quantile(0.95)
outlier = (dataframe['ctznCnt'] > 2000) | (dataframe['sum_Quantity'] > Q3)
dataframe.drop(dataframe[outlier].index, inplace= True)
'''

#kdeplot
apt_ctzn = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_code_info_total_merge.csv", encoding='utf-8-sig')
apt_ctzn = apt_ctzn.replace([np.inf, -np.inf], np.nan) #infinite를 NAN으로 치환
Q1 = apt_ctzn['sum_disQuantity_2019_ctznCnt'].quantile(0.1)
Q3 = apt_ctzn['sum_disQuantity_2019_ctznCnt'].quantile(0.9)
outlier = (apt_ctzn['ctznCnt'] > 1000) | (apt_ctzn['sum_disQuantity_2019_ctznCnt'] > Q3)
apt_ctzn.drop(apt_ctzn[outlier].index, inplace= True) #결측치 정리
apt_ctzn['sum_disQuantity_2019_ctznCnt'] = apt_ctzn['sum_disQuantity_2019_ctznCnt'] / 1000

plt.figure(figsize=(15, 15))
sns.set_theme(color_codes=True)
plot = sns.kdeplot(data=apt_ctzn, x="sum_disQuantity_2019_ctznCnt", y="ctznCnt", fill=True)
fig = plot.get_figure()
plt.show()
fig.savefig('./visualization/apt_ctzn_sum_2019_under1000.png', dpi=150, bbox_inches='tight')
print(apt_ctzn['sum_disQuantity_2019_ctznCnt'].describe())

'''
#선형회귀
plt.figure(figsize=(15, 15))
sns.set_theme(color_codes=True)
#plot = sns.lmplot(data=dataframe, x="ctznCnt", y="sum_Quantity", col="citySidoName", hue="citySggName")
plot = sns.lmplot(x="sum_Quantity", y="ctznCnt", data = dataframe)
plt.show()
plot.savefig('./visualization/apt_ctzn_sum_2020_replot.png', dpi=150, bbox_inches='tight')
print("success")
'''

#histogram+hexplot
# plt.figure(figsize=(15, 15))
# plot = sns.jointplot(x=dataframe.sum_Quantity, y=dataframe.ctznCnt, kind="hex", data = dataframe)
# fig = plot.get_figure()
# plt.show()

# 트라이앵글 히트맵 작성
# plt.figure(figsize=(16, 6))
# mask = np.triu(np.ones_like(dataframe.corr(), dtype=np.bool))
# heatmap = sns.heatmap(dataframe.corr(), mask=mask, vmin=-1, vmax=1, annot=True, cmap='BrBG')
# heatmap.set_title('Triangle Correlation Heatmap', fontdict={'fontsize':18}, pad=16);
# fig = heatmap.get_figure()
# plt.show()

'''
#아파트 단위로 그룹화 후 그룹별 평균, 최대, 최소, 분산, 합계  <- 의미 없음. 
year = "2020"
data = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_merge_" + year + "_byday.csv", encoding='utf-8-sig')
df = data.groupby('aptCode')['disQuantity_by_ctznCnt'].agg(**{'mean_Quantity':'mean',
                                                   'min_Quantity' : 'min',
                                                   'max_Quantity' : 'max',
                                                   'std_Quantity' : 'std',
                                                   'sum_Quantity' : 'sum'
                                                   }).reset_index() ## 도시별, 최대, 최소, 평균, 표준편차, 합계
df = df.round(4) #소수점 4자리로 정리
df = df.replace([np.inf, -np.inf], np.nan) #infinite를 NAN으로 치환

df.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_group_' + year + '.csv', index=False, encoding='utf-8-sig') <- 데이터 의미 없어서 삭제함. 코드 만 참고용.
print(df.describe())
'''

'''
# 결측치 제거 후 히스토그램 작성(연도별)
year = "2020"
df = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_group_" + year + ".csv", encoding='utf-8-sig')
df.dropna(inplace= True)
Q1 = df['sum_Quantity'].quantile(0.25)
Q3 = df['sum_Quantity'].quantile(0.75)
IQR = Q3 - Q1
outlier = (df['sum_Quantity'] < Q1 - 1.0 * IQR) | (df['sum_Quantity'] > Q3 + 1.0 * IQR)
df.drop(df[outlier].index, inplace= True)
#df.plot(kind='box', y ='sum_Quantity') #박스 플롯으로 결측치 확인
# plt.show()
# print(df.describe())

plot = sns.distplot(df['sum_Quantity']/365, bins=30, color="orange")
plt.xlabel('Waste Quantity(/g-day-세대)')
plt.ylabel('Distribution Density')
plt.legend(title=year)
fig = plot.get_figure()
plt.show()
fig.savefig('./visualization/' + year + '_apt_waste_dist.png', dpi=150, bbox_inches='tight')
print(df.describe())
'''

'''
2018   mean_Quantity  min_Quantity  max_Quantity  std_Quantity   sum_Quantity
count    3505.000000   3505.000000   3505.000000   3505.000000    3505.000000
mean     1878.080259   1143.759124   3124.569482    429.016255  155177.744461
std       482.876371    340.840559    999.932569    253.897236   31889.439732
min       922.510800      0.259700   1311.209100    138.215900   77490.909100
25%      1613.032000    961.231900   2606.104700    326.105400  134778.617400
50%      1870.474300   1168.849600   3040.724000    387.399600  156535.365900
75%      2116.899500   1373.768500   3469.015300    462.665100  176954.470200
max      6676.777000   2791.262100  13368.421100   3500.659900  227958.409100

2019   mean_Quantity  min_Quantity  max_Quantity  std_Quantity   sum_Quantity
count    4333.000000   4333.000000   4333.000000   4333.000000    4333.000000
mean     1797.731268   1060.030074   2972.271654    406.954442  149575.918994
std       405.804779    321.387484    839.956476    204.321672   31086.916338
min       868.750000      0.088200   1209.209500    123.784400   72975.000000
25%      1556.824400    880.303000   2502.364500    317.875500  129675.000000
50%      1811.615200   1087.934800   2926.133900    374.771500  151425.862100
75%      2044.089800   1283.718700   3350.000000    445.740800  171080.311600
max      7026.896600   2110.000000  14375.000000   3266.727100  221110.000000

2020   mean_Quantity  min_Quantity  max_Quantity  std_Quantity   sum_Quantity
count    5005.000000   5005.000000   5005.000000   5005.000000    5005.000000
mean     1812.561247   1117.212875   2940.567010    401.411867  150621.113488
std       469.719901    365.132198    888.250119    215.385395   34309.117627
min       757.498100      0.231500   1082.940400    120.048400   63629.838700
25%      1548.161100    908.354800   2450.000000    309.973500  129309.837800
50%      1829.238200   1156.172800   2883.874700    369.875400  153014.360900
75%      2082.842300   1372.692300   3350.284100    442.603800  174375.623800
max     11824.959600   2881.465500  19070.043100   5348.962300  229547.404400
'''

'''
#결측치 제거 후 히스토그램 작성(3년 중첩)
df2018 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_group_2018.csv", encoding='utf-8-sig')
df2019 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_group_2019.csv", encoding='utf-8-sig')
df2020 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\apt_group_2020.csv", encoding='utf-8-sig')

df2018.dropna(inplace= True)
df2019.dropna(inplace= True)
df2020.dropna(inplace= True)

Q1 = df2018['sum_Quantity'].quantile(0.25)
Q3 = df2018['sum_Quantity'].quantile(0.75)
IQR = Q3 - Q1
outlier = (df2018['sum_Quantity'] < Q1 - 1.0 * IQR) | (df2018['sum_Quantity'] > Q3 + 1.0 * IQR)
df2018.drop(df2018[outlier].index, inplace= True)

Q1 = df2019['sum_Quantity'].quantile(0.25)
Q3 = df2019['sum_Quantity'].quantile(0.75)
IQR = Q3 - Q1
outlier = (df2019['sum_Quantity'] < Q1 - 1.0 * IQR) | (df2019['sum_Quantity'] > Q3 + 1.0 * IQR)
df2019.drop(df2019[outlier].index, inplace= True)

Q1 = df2020['sum_Quantity'].quantile(0.25)
Q3 = df2020['sum_Quantity'].quantile(0.75)
IQR = Q3 - Q1
outlier = (df2020['sum_Quantity'] < Q1 - 1.0 * IQR) | (df2020['sum_Quantity'] > Q3 + 1.0 * IQR)
df2020.drop(df2020[outlier].index, inplace= True)

plot = sns.distplot(df2018['sum_Quantity']/365, bins=30, color="blue")
plot = sns.distplot(df2019['sum_Quantity']/365, bins=30, color="red")
plot = sns.distplot(df2020['sum_Quantity']/365, bins=30, color="orange")

plt.xlabel('Waste Quantity(/g-day-세대)')
plt.ylabel('Distribution Density')
plt.legend(title="3years")
fig = plot.get_figure()
plt.show()
fig.savefig('./visualization/3years_apt_waste_dist.png', dpi=150, bbox_inches='tight')
print(df2018.describe())
print(df2019.describe())
print(df2020.describe())
'''