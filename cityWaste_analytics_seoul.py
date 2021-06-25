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

data2018 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\seoul_group_2018.csv", encoding='utf-8-sig')
data2019 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\seoul_group_2019.csv", encoding='utf-8-sig')
data2020 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\seoul_group_2020.csv", encoding='utf-8-sig')

# 결측치 제거
data2018.dropna(inplace= True)
data2019.dropna(inplace= True)
data2020.dropna(inplace= True)

Q1 = data2018['sum_Quantity'].quantile(0.1)
Q3 = data2018['sum_Quantity'].quantile(0.9)
outlier = (data2018['sum_Quantity'] < Q1) | (data2018['sum_Quantity'] > Q3)
data2018.drop(data2018[outlier].index, inplace= True)
#data2018.plot(kind='box', y ='sum_Quantity') #박스 플롯으로 결측치 확인

Q1 = data2019['sum_Quantity'].quantile(0.1)
Q3 = data2019['sum_Quantity'].quantile(0.9)
outlier = (data2019['sum_Quantity'] < Q1) | (data2019['sum_Quantity'] > Q3)
data2019.drop(data2019[outlier].index, inplace= True)

Q1 = data2020['sum_Quantity'].quantile(0.1)
Q3 = data2020['sum_Quantity'].quantile(0.9)
outlier = (data2020['sum_Quantity'] < Q1) | (data2020['sum_Quantity'] > Q3)
data2020.drop(data2020[outlier].index, inplace= True)

plot = sns.distplot(data2018['sum_Quantity']/365, bins=15, color="blue")
plot = sns.distplot(data2019['sum_Quantity']/365, bins=15, color="red")
plot = sns.distplot(data2020['sum_Quantity']/365, bins=15, color="orange")
plt.xlabel('Waste Quantity(/g-day-인)')
plt.ylabel('Distribution Density')
fig = plot.get_figure()
plt.show()
fig.savefig('./visualization/3year_seoul_waste_dist.png', dpi=150, bbox_inches='tight')
print(data2018.describe())
print(data2019.describe())
print(data2020.describe())

'''
       mean_Quantity  min_Quantity  max_Quantity  std_Quantity  sum_Quantity
count      16.000000     16.000000     16.000000     16.000000     16.000000
mean       37.108373     20.765799     60.052693      7.049020  13544.556296
std        19.244479     11.759939     29.024302      3.311630   7024.234735
min        12.716087      7.454238     22.833693      2.424848   4641.371792
25%        18.917493     10.369989     36.485847      4.136644   6904.885007
50%        37.109953     20.732918     62.775017      6.948072  13545.132970
75%        45.954223     26.721068     76.052738      8.968695  16773.291363
max        75.699955     49.053061    116.621180     12.350683  27630.483580
       mean_Quantity  min_Quantity  max_Quantity  std_Quantity  sum_Quantity
count      19.000000     19.000000     19.000000     19.000000     19.000000
mean       37.059812     15.889454    352.176519     21.722494  13526.831285
std        20.098864      9.442787   1282.045497     66.005676   7336.085286
min        11.378882      5.113804     18.963813      2.294984   4153.292001
25%        19.475251      9.309712     33.099433      3.972766   7108.466796
50%        41.648703     16.233384     63.670595      7.154221  15201.776660
75%        46.247596     19.881105     76.344736      9.064285  16880.372655
max        82.309883     44.748085   5644.949418    293.963303  30043.107310
       mean_Quantity  min_Quantity  max_Quantity  std_Quantity  sum_Quantity
count      19.000000     19.000000     19.000000     19.000000     19.000000
mean       41.724696     27.253236     66.221594      6.814842  15271.238797
std        18.984415     14.563894     28.329862      2.904911   6948.295942
min        15.922556      9.527129     28.768431      3.243590   5827.655536
25%        26.126646     15.241281     41.447382      4.437180   9562.352499
50%        43.841104     25.841280     67.831118      6.864000  16045.843960
75%        54.417832     37.539121     88.323958      8.498861  19916.926675
max        82.327687     59.629191    118.103687     12.448386  30131.933280
'''