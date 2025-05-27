import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# 서초구 고등학교 데이터 (예시: 학교명, 위도, 경도)
highschools = [
    {"name": "서울고등학교", "lat": 37.4923, "lon": 127.0075},
    {"name": "세화고등학교", "lat": 37.5009, "lon": 126.9973},
    {"name": "세화여자고등학교", "lat": 37.5004, "lon": 126.9951},
    {"name": "상문고등학교", "lat": 37.4746, "lon": 126.9881},
    {"name": "서초고등학교", "lat": 37.4705, "lon": 127.0178},
    {"name": "양재고등학교", "lat": 37.4845, "lon": 127.0384},
    {"name": "반포고등학교", "lat": 37.5080, "lon": 126.9957},
    {"name": "영일고등학교", "lat": 37.4835, "lon": 127.0146}
]

# Streamlit 앱 제목
st.title("📍 서초구 고등학교 위치 지도")

# Folium 지도 생성
map_center = [37.4836, 127.0166]
m = folium.Map(location=map_center, zoom_start=13)

# 마커 추가
for school in highschools:
    folium.Marker(
        location=[school["lat"], school["lon"]],
        popup=school["name"],
        tooltip=school["name"],
        icon=folium.Icon(color="blue", icon="graduation-cap", prefix="fa")
    ).add_to(m)

# Folium 지도 출력
st_folium(m, width=700, height=500)
