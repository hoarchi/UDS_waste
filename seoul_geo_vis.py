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

data2020 = pd.read_csv("C:\\Users\\hogun\\PycharmProjects\\UDS_waste\\total_waste\\seoul_group_2020.csv", encoding='utf-8-sig')

seoul = seoul.merge(data2020, on='sigungu_nm', how='outer').fillna(0)
seoul['sum_Quantity'] = np.round(seoul.sum_Quantity).astype('Int64') #배출량을 소수점 제거하고 정수로 치환
print(seoul.columns)

ax = seoul.plot(figsize=(15, 15), column='sum_Quantity', categorical=True, edgecolor="k", #scheme='equal_interval', k=12,
                cmap='OrRd', legend=True, legend_kwds={'loc': 'best'})

seoul['coords'] = seoul['geometry'].apply(lambda x: x.representative_point().coords[:])
seoul['coords'] = [coords[0] for coords in seoul['coords']]
for idx, row in seoul.iterrows():
    plt.annotate(text=row['sigungu_nm'], xy=row['coords'],horizontalalignment='center')

ax.set_title("2020년 구별 1인당 년간 배출 총량(g)", fontsize=24)
ax.set_axis_off()
plt.show()
fig = ax.get_figure()
fig.savefig('./visualization/2020_seoul_geomap.png', dpi=150, bbox_inches='tight')