import streamlit as st
import pandas as pd
import pydeck as pdk

# إعداد الصفحة
st.set_page_config(page_title="Algerian Weather Map", layout="wide")
st.title("🗺️ Weather Forecast Map for Algerian Coastal Cities")

# تحميل البيانات
try:
    df = pd.read_csv("algerian_coastal_weather_2022_2024.csv")
except FileNotFoundError:
    st.error("❌ File 'algerian_coastal_weather_2022_2024.csv' not found.")
    st.stop()

# التأكد من الأعمدة
required_cols = ["latitude", "longitude", "city", "temperature_2m_max", "precipitation_sum", "month"]
missing_cols = [col for col in required_cols if col not in df.columns]
if missing_cols:
    st.error(f"❌ Missing columns in CSV file: {missing_cols}")
    st.stop()

# اختيار الشهر
month = st.slider("📅 Select a month", 1, 12, 7)

# تصفية البيانات حسب الشهر المختار
filtered_df = df[df["month"] == month]

# التحقق من وجود بيانات
if filtered_df.empty:
    st.warning("⚠️ No data available for the selected month.")
    st.stop()

# عرض الخريطة
st.pydeck_chart(pdk.Deck(
    map_style="light",  # ✅ بدون Mapbox API
    initial_view_state=pdk.ViewState(
        latitude=36.5,
        longitude=3.0,
        zoom=6,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=filtered_df,
            get_position='[longitude, latitude]',
            get_radius=40000,
            get_fill_color='[255, 100, 100, 160]',
            pickable=True,
        )
    ],
    tooltip={
        "text": "📍 {city}\n🌡️ Temp: {temperature_2m_max}°C\n🌧️ Rain: {precipitation_sum} mm"
    }
))
