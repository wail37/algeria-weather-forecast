import requests
import pandas as pd
from time import sleep

cities = [
    {"name": "Algiers", "lat": 36.75, "lon": 3.06},
    {"name": "Oran", "lat": 35.69, "lon": -0.64},
    {"name": "Bejaia", "lat": 36.75, "lon": 5.07},
    {"name": "Annaba", "lat": 36.90, "lon": 7.77},
    {"name": "Mostaganem", "lat": 35.93, "lon": 0.09},
    {"name": "Tipaza", "lat": 36.59, "lon": 2.45},
    {"name": "Skikda", "lat": 36.87, "lon": 6.91},
]

start_date = "2022-01-01"
end_date = "2024-12-31"
all_data = []

for city in cities:
    print(f"📡 Fetching data for {city['name']}...")
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": city["lat"],
        "longitude": city["lon"],
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "Africa/Algiers"
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if "daily" in data:
        df = pd.DataFrame(data["daily"])
        df["date"] = pd.to_datetime(df["time"])
        df["city"] = city["name"]
        df["latitude"] = city["lat"]
        df["longitude"] = city["lon"]
        df["month"] = df["date"].dt.month
        all_data.append(df)
        sleep(1)
    else:
        print(f"⚠️ No data for {city['name']}")

final_df = pd.concat(all_data, ignore_index=True)
final_df.to_csv("algerian_coastal_weather_2022_2024.csv", index=False)
print("✅ Done! Data saved to 'algerian_coastal_weather_2022_2024.csv'")
