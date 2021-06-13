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

plot = sns.distplot(data2018['mean_Quantity'], bins=30, color="blue")
plot = sns.distplot(data2019['mean_Quantity'], bins=30, color="red")
plot = sns.distplot(data2020['mean_Quantity'], bins=30, color="orange")
plt.xlabel('Waste Quantity(T)')
plt.ylabel('Distribution Density')
fig = plot.get_figure()
plt.show()
fig.savefig('./3year_seoul_waste_dist.png', dpi=150, bbox_inches='tight')
