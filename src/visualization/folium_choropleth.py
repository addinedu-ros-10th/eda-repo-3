import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import folium
from sqlalchemy import create_engine
from shapely.geometry import shape
from io import BytesIO
import base64

from dotenv import load_dotenv
import os
import json

# .env 파일을 찾아 환경 변수로 로드
load_dotenv()

# 환경 변수 가져오기
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# ▶️ MySQL 연결
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

# ▶️ 반려동물 등록 데이터 가져오기
query = """
SELECT *
FROM companion_animal_registration
"""
df = pd.read_sql(query, engine)

# ▶️ 행정구역 명칭을 folium key와 맞추기 위해 하나로 합치기
df['region'] = df['sigungu']

# ▶️ GeoJSON 경로 지정
geo_path = 'DATA/02. skorea_municipalities_geo_simple.json'  # 반드시 'region' 컬럼과 feature.properties.name이 일치해야 함

# ▶️ GeoJSON 로드 (시도+시군구 이름이 properties.name으로 되어 있어야 함)
with open(geo_path, 'r', encoding='utf-8') as f:
    geo = json.load(f)

# ▶️ 지도 시각화
m = folium.Map(location=[36.5, 127.5], zoom_start=8)



folium.Choropleth(
    geo_data=geo_path,
    data=df,
    columns=['region', 'total_registered'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='지역별 반려동물 등록 수'
).add_to(m)


# # ▶️ 5. GeoJSON에 tooltip (지역명 + 등록수)
# # 데이터를 GeoJSON feature에 덧붙이기
# for feature in geo['features']:
#     region_name = feature['properties']['name']
#     matched_row = df[df['region'] == region_name]
#     if not matched_row.empty:
#         total = int(matched_row['total_registered'].values[0])
#         feature['properties']['popup_info'] = f"{region_name}: {total:,}마리 등록"

# # GeoJson에 Tooltip 추가
# folium.GeoJson(
#     geo,
#     style_function=lambda x: {'fillOpacity': 0, 'color': 'black', 'weight': 0.3},
#     tooltip=folium.GeoJsonTooltip(
#         fields=['popup_info'],
#         aliases=[''],
#         localize=True,
#         sticky=False,
#         labels=False,
#         style="""
#             background-color: white;
#             border: 1px solid black;
#             border-radius: 3px;
#             box-shadow: 3px;
#         """
#     )
# ).add_to(m)

# # ▶️ 4. 지역별 고정 막대 차트 생성 (줌 비율 대응 + 투명 배경 + 숫자 표시)
# for feature in geo['features']:
#     region_name = feature['properties']['name']
#     geom = shape(feature['geometry'])
#     centroid = geom.centroid.coords[0]  # (lon, lat)

#     row = df[df['region'] == region_name]
#     if not row.empty:
#         dog = int(row['dog_registered_total'].values[0])
#         cat = int(row['cat_registered_total'].values[0])

#         # ▶️ matplotlib bar chart 생성
#         fig, ax = plt.subplots(figsize=(1.5, 1.2))
#         bars = ax.bar(['Dog', 'Cat'], [dog, cat], color=['blue', 'red'])

#         # 개체 수 텍스트 표시
#         for bar, label in zip(bars, [dog, cat]):
#             ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{label}', 
#                     ha='center', va='bottom', fontsize=6)

#         ax.set_xticks([])
#         ax.set_yticks([])
#         ax.axis('off')
#         plt.tight_layout()

#         # ▶️ 투명 배경 + base64
#         buf = BytesIO()
#         plt.savefig(buf, format='png', dpi=200, transparent=True)
#         plt.close(fig)
#         buf.seek(0)
#         img_base64 = base64.b64encode(buf.read()).decode('utf-8')

#         # ▶️ HTML with CSS transform for zoom responsiveness
#         html = f"""
#         <div class="zoom-marker" style="
#             transform: scale(1);
#             transform-origin: center;
#             transition: transform 0.2s ease;
#             ">
#             <img src="data:image/png;base64,{img_base64}" width="30" style="background: none;">
#         </div>
#         """

#         folium.Marker(
#             location=[centroid[1], centroid[0]],
#             icon=folium.DivIcon(html=html)
#         ).add_to(m)

# # ▶️ 5. JS로 줌 이벤트 감지 후 마커 크기 조정
# # (folium.Html 사용하여 JS 코드 삽입)
# from folium import Html, MacroElement
# from jinja2 import Template

# zoom_script = """
# <script>
# function updateMarkerSize(map) {
#     const zoom = map.getZoom();
#     const scale = Math.pow(zoom / 7, 1.2);  // 줌 레벨에 따른 비율 조정
#     document.querySelectorAll('.zoom-marker').forEach(el => {
#         el.style.transform = `scale(${scale})`;
#     });
# }
# map.on('zoomend', function() {
#     updateMarkerSize(map);
# });
# updateMarkerSize(map);  // 초기 실행
# </script>
# """

# macro = MacroElement()
# macro._template = Template(zoom_script)
# m.get_root().add_child(macro)

# for feature in geo['features']:
#     region_name = feature['properties']['name']
#     geom = shape(feature['geometry'])  # Shapely로 geometry 해석
#     centroid = geom.centroid.coords[0]  # 중심 좌표 (lon, lat)

#     # 데이터 매칭
#     row = df[df['region'] == region_name]
#     print(row)
#     if not row.empty:
#         dog_count = int(row['dog_registered_total'].values[0])
#         cat_count = int(row['cat_registered_total'].values[0])
#         total = int(row['total_registered'].values[0])

#         # CircleMarker for 강아지
#         folium.CircleMarker(
#             location=[centroid[1], centroid[0]],  # lat, lon
#             radius=dog_count**0.5,
#             color='blue',
#             fill=True,
#             fill_opacity=0.1,
#             tooltip=f"[{region_name}] 🐶 개 등록: {dog_count}마리"
#         ).add_to(m)

#         # CircleMarker for 고양이
#         folium.CircleMarker(
#             location=[centroid[1], centroid[0]],  # lat, lon
#             radius=cat_count**0.5,
#             color='red',
#             fill=True,
#             fill_opacity=0.1,
#             tooltip=f"[{region_name}] 🐱 고양이 등록: {cat_count}마리"
#         ).add_to(m)

# for _, row in df.iterrows():
#     folium.Marker(
#         location=[위도, 경도],  # 위도/경도 정보가 있다면
#         popup=f"{row['region']}: {row['total_registered']}건"
#     ).add_to(m)

# ▶️ 결과 저장
m.save('RESULT/visualization/companion_animal_registration_map.html')
