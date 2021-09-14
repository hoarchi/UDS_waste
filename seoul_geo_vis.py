import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams["font.family"] = 'NanumGothic'
plt.rcParams["figure.figsize"] = (600,600)

#파일불러오기
# #ax = seoul.convex_hull.plot(color = 'purple', edgecolor="w")
# seoul.geometry = seoul.buffer(0.001)
# seoul = seoul.dissolve(by='SIG_CD')
# ax.set_title("구 별로 묶은 서울의 기초 구역도")
# ax.set_axis_off()
# plt.show()

seoul_file = "C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\seoul_gungu\\seoul_gungu.shp"
seoul = gpd.read_file(seoul_file, encoding='euckr')

data2020 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\seoul_group_2019.csv", encoding='utf-8-sig')

seoul = seoul.merge(data2020, on='sigungu_nm', how='outer').fillna(0)
seoul['mean_Quantity'] = np.round(seoul.mean_Quantity).astype('Int64') / 1000 #배출량을 소수점 제거하고 정수로 치환
print(seoul.columns)

#지도에 시각화
ax = seoul.plot(figsize=(15, 15), column='mean_Quantity', edgecolor="k",
                cmap='OrRd', legend=True, scheme='quantiles', legend_kwds={'loc': 'best'})

'''
#지도에 시각화(기존에 자료)
ax = seoul.plot(figsize=(15, 15), column='mean_Quantity', categorical=True, edgecolor="k", #scheme='equal_interval', k=12,
                cmap='OrRd', legend=True, legend_kwds={'loc': 'best'})
'''

seoul['coords'] = seoul['geometry'].apply(lambda x: x.representative_point().coords[:])
seoul['coords'] = [coords[0] for coords in seoul['coords']]
for idx, row in seoul.iterrows():
    plt.annotate(text=row['sigungu_nm'], xy=row['coords'],horizontalalignment='center')

ax.set_title("2019년 구별 아파트 단지의 평균 세대당 배출원단위(kg/세대-년)", fontsize=24)
ax.set_axis_off()
plt.show()
fig = ax.get_figure()
fig.savefig('./visualization/2019_seoul_geomap.png', dpi=150, bbox_inches='tight')