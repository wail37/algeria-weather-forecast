import streamlit as st
import pandas as pd
import joblib
from xgboost import XGBRegressor

# ========= Load models and data =========
model_df = pd.read_csv("algerian_coastal_weather_2022_2024.csv")
xgb_model = joblib.load("weather_model.pkl")  # درجة الحرارة
rain_model = joblib.load("rain_model.pkl")    # الأمطار

model_df['city_code'] = model_df['city'].astype('category').cat.codes
city_codes = dict(zip(model_df['city'], model_df['city_code']))

# ========= Streamlit UI =========
st.set_page_config(page_title="Algeria Weather Forecast", layout="centered")

st.title("🌤️ Weather Prediction App for Algerian Coastal Cities")

st.markdown("This app predicts **maximum temperature** and **rainfall** for a selected city and month using historical data and AI models.")

city = st.selectbox("🌍 Select City", list(city_codes.keys()))
month = st.selectbox("📅 Select Month", list(range(1, 13)))

# Get historical averages to prefill input
city_month_data = model_df[(model_df['city'] == city) & (model_df['month'] == month)]
avg_min_temp = round(city_month_data['temperature_2m_min'].mean(), 1)
avg_rain = round(city_month_data['precipitation_sum'].mean(), 1)

st.write("⬇️ You can use the suggested average values or adjust manually:")

temp_min = st.slider("🌡️ Min Temperature (°C)", 0.0, 30.0, avg_min_temp)
precip = st.slider("🌧️ Precipitation (mm)", 0.0, 200.0, avg_rain)

if st.button("🔮 Predict"):
    input_data = pd.DataFrame({
        "month": [month],
        "temperature_2m_min": [temp_min],
        "precipitation_sum": [precip],
        "city_code": [city_codes[city]]
    })

    pred_temp = xgb_model.predict(input_data)[0]
    pred_rain = rain_model.predict(input_data)[0]

    st.success(f"📍 **{city} – Month {month}**")
    st.metric("Predicted Max Temperature", f"{pred_temp:.2f} °C")
    st.metric("Predicted Rainfall", f"{pred_rain:.2f} mm")

    st.balloons()
