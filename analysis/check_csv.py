import pandas as pd

try:
    df = pd.read_csv("algerian_coastal_weather_2022_2024.csv")
    print("\n📄 Columns found in the CSV:")
    print(df.columns.tolist())
    print("\n🔍 First 3 rows:")
    print(df.head(3))
except FileNotFoundError:
    print("❌ The file 'algerian_coastal_weather_2022_2024.csv' was NOT found in this folder.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")

