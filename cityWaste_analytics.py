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
import matplotlib.pyplot as plt

'''
#인구수로 나눈 자료를, 시도 단위로 그룹화 후 그룹별 평균, 최대, 최소, 분산, 합계로 만들어서 저장
data2020 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\city_sensus_waste_2020_bydate.csv", encoding='utf-8-sig', parse_dates =["createDate"], index_col ="createDate")
grouped2020 = data2020.groupby('create_sido')
df = data2020.groupby('create_sido')['disQuantity_ingu'].agg(**{'mean_Quantity':'mean',
                                                   'min_Quantity' : 'min',
                                                   'max_Quantity' : 'max',
                                                   'std_Quantity' : 'std',
                                                   'sum_Quantity' : 'sum'
                                                   }).reset_index() ## 도시별, 최대, 최소, 평균, 표준편차, 합계
df.to_csv('C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\city_group_2020.csv', index=False, encoding='utf-8-sig')
'''


# 결측치 제거
year = "2020"
df = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\city_group_" + year + ".csv", encoding='utf-8-sig')
df.dropna(inplace= True)
Q1 = df['sum_Quantity'].quantile(0.1)
Q3 = df['sum_Quantity'].quantile(0.9)
outlier = (df['sum_Quantity'] < Q1) | (df['sum_Quantity'] > Q3)
df.drop(df[outlier].index, inplace= True)
df.plot(kind='box', y ='sum_Quantity', label='2020 일') #박스 플롯으로 결측치 확인
#print(df.describe())

# plot = sns.distplot(df['sum_Quantity']/365, bins=30, color="orange")
# plt.xlabel('Waste Quantity(/g-day-인)')
# plt.ylabel('Distribution Density')
# plt.legend(title=year)
# fig = plot.get_figure()
# plt.show()
# fig.savefig('./visualization/' + year + '_city_waste_dist.png', dpi=150, bbox_inches='tight')


'''
2018   mean_Quantity  min_Quantity  max_Quantity  std_Quantity  sum_Quantity
count     103.000000    103.000000    103.000000    103.000000    103.000000
mean       44.907656     25.801881     91.383087      9.254303  16282.333697
std        25.192171     16.301612    103.421285      6.897940   9195.986566
min         7.964273      0.007285     13.748928      1.527692   2906.959600
25%        20.863217     10.488571     46.028371      5.219503   7615.074170
50%        40.414898     24.676884     74.323732      8.401030  14711.489085
75%        65.132368     39.005192    114.140233     11.872150  23773.314259
max        96.007834     62.156327    989.041107     52.538611  35042.859566

2019   mean_Quantity  min_Quantity  max_Quantity  std_Quantity  sum_Quantity
count     112.000000    112.000000    112.000000    112.000000    112.000000
mean       45.579002     22.596179    130.756827     11.363437  16541.912742
std        25.716602     14.434111    527.670845     27.396434   9407.953991
min         8.296365      0.119825     16.096228      1.953170   3028.173124
25%        22.214642      9.888770     38.645702      4.575591   8108.344449
50%        43.842392     19.978690     72.491091      8.578721  15850.151679
75%        66.251017     35.140693    114.836594     12.070547  24181.621051
max        98.374206     55.069231   5644.949418    293.963303  35906.585032

2020   mean_Quantity  min_Quantity  max_Quantity  std_Quantity  sum_Quantity
count     114.000000    114.000000    114.000000    114.000000    114.000000
mean       49.084242     30.906036     82.731113      8.572030  17901.088973
std        25.147662     18.152870     41.491711      4.743366   9239.393006
min        10.814542      0.452863     16.662300      1.552155   3958.122398
25%        26.479022     15.323588     44.137231      5.145799   9585.095014
50%        45.799798     30.136158     79.103817      7.894100  16762.725974
75%        69.961265     43.792381    114.563891     11.476011  25605.823071
max       102.472359     71.334342    177.953393     35.966134  37504.883221
'''