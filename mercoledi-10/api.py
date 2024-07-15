# Create un programma python che permette tramite le api
# https://open-meteo.com/en/docs (per le previsioni metereologiche) e
# https://www.bigdatacloud.com/free-api/free-reverse-geocode-tocity-
# api#getStarted (per l’ottenimento in automatico della propria
# langitudine e latitudine tramite l’indirizzo ip), di vedere le previsione
# metereologiche.
# L’utente potrà scegliere se visionarle dei prossimi 1, 3 o 7 giorni e se
# visionare oltre che le temperature anche la velocità del vento e le
# probabili precipitazioni.



import requests
import json

# Funzione per ottenere la posizione dell'utente tramite l'API di BigDataCloud
def get_user_location():
    ip_api_url = "https://api.bigdatacloud.net/data/client-ip"
    response = requests.get(ip_api_url)
    data = response.json()
    latitude = data["latitude"]
    longitude = data["longitude"]
    return latitude, longitude

# Funzione per ottenere le previsioni meteorologiche tramite l'API di Open-Meteo
def get_weather_forecast(latitude, longitude, days):
    weather_api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_mean,windspeed_10m_max&forecast_days={days}&timezone=auto"
    response = requests.get(weather_api_url)
    data = response.json()
    return data

# Funzione per visualizzare le previsioni meteorologiche
def display_weather_forecast(data, days):
    print(f"Previsioni meteorologiche per i prossimi {days} giorni:")
    for i in range(days):
        date = data["daily"]["time"][i]
        max_temp = data["daily"]["temperature_2m_max"][i]
        min_temp = data["daily"]["temperature_2m_min"][i]
        precipitation_probability = data["daily"]["precipitation_probability_mean"][i]
        wind_speed = data["daily"]["windspeed_10m_max"][i]
        print(f"Data: {date}")
        print(f"Temperatura massima: {max_temp}°C")
        print(f"Temperatura minima: {min_temp}°C")
        print(f"Probabilità di precipitazioni: {precipitation_probability}%")
        print(f"Velocità del vento massima: {wind_speed} km/h")
        print()

# Programma principale
latitude, longitude = get_user_location()
print(f"Posizione dell'utente: Latitudine={latitude}, Longitudine={longitude}")

days = int(input("Visualizza le previsioni per i prossimi (1, 3 o 7) giorni: "))
if days not in [1, 3, 7]:
    print("Scelta non valida. Impostazione predefinita a 3 giorni.")
    days = 3

weather_data = get_weather_forecast(latitude, longitude, days)
display_weather_forecast(weather_data, days)