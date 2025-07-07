import pandas as pd

# قراءة الملف
df = pd.read_csv("algerian_coastal_weather_2022_2024.csv")

# طباعة أسماء الأعمدة
print("🧾 Available columns in the CSV:")
print(df.columns.tolist())

# عرض أول 5 صفوف لرؤية القيم
print("\n🔍 Sample data:")
print(df[["city", "date", "temperature_2m_max", "temperature_2m_min", "precipitation_sum", "latitude", "longitude"]].head())
