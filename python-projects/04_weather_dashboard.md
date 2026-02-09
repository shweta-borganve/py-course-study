# Project 4: Weather Dashboard

**Difficulty:** ⭐⭐⭐ Medium  
**Real-world Use:** Check weather for multiple cities

## Project Overview

Build a **Weather Dashboard** that fetches and displays weather information:
- Get current weather for multiple cities
- Store favorite cities
- Show weather forecasts
- Temperature unit conversion (Celsius/Fahrenheit)
- Weather alerts
- Historical weather data

## Features to Implement

1. **Current Weather Display**:
   - Temperature, feels like, humidity, wind speed
   - Weather condition (sunny, rainy, cloudy)
   - UV index, visibility, pressure
   - Sunrise/sunset times

2. **Multiple Cities**:
   - Search and add cities
   - View weather for all saved cities at once
   - Quick comparison between cities

3. **Forecast**:
   - 5-day or 7-day forecast
   - Hourly forecast
   - Show high/low temperatures

4. **Favorite Cities**:
   - Save favorite locations
   - Quick access dashboard
   - Reorder favorites

5. **Weather Alerts**:
   - Alert if temperature drops below threshold
   - Alert for severe weather
   - Alert for UV danger

6. **Temperature Conversion**:
   - Toggle between Celsius and Fahrenheit
   - Store user preference

7. **Data Storage**:
   - Save favorite cities
   - Save historical weather
   - Cache data to reduce API calls

## Technologies/Concepts Needed
- API calls (requests library) - **NEW CONCEPT**
- JSON parsing
- Data structures
- File I/O
- Date/time handling
- Temperature conversion
- String formatting

## Step-by-Step Guidance

### Step 1: Choose a Weather API
**Free options:**
- OpenWeatherMap (free tier available)
- WeatherAPI (free tier)
- wttr.in (super simple, no key needed)

**For learning: Use wttr.in (simplest)**
```python
import requests

city = "London"
response = requests.get(f"https://wttr.in/{city}?format=j1")
data = response.json()
```

### Step 2: Design Data Structure
```python
favorite_cities = [
    {
        "name": "London",
        "country": "UK",
        "lat": 51.5074,
        "lon": -0.1278,
        "unit": "Celsius"
    }
]

weather_cache = {
    "London": {
        "temp": 15,
        "condition": "Rainy",
        "humidity": 75,
        "wind": 12,
        "updated": "2025-02-09 14:30"
    }
}
```

### Step 3: Create Core Functions
- `fetch_weather(city)` - Get weather from API
- `display_weather(city_data)` - Format and display
- `add_favorite_city(city)`
- `get_all_favorite_weather()`
- `set_temperature_unit(unit)` - Celsius/Fahrenheit
- `convert_temperature(temp, from_unit, to_unit)`
- `check_weather_alerts()`
- `save_favorite_cities()`
- `load_favorite_cities()`

### Step 4: Build Menu System
```
=== Weather Dashboard ===
1. Search Weather by City
2. View Favorite Cities
3. Add Favorite City
4. Remove Favorite City
5. Set Temperature Unit
6. Weather Alerts
7. Compare Cities
8. View Forecast
9. Exit
```

## Example Usage

```
Choose option: 1
Enter city name: London
Fetching weather...

=== Weather in London ===
Temperature: 15°C (feels like 12°C)
Condition: Rainy
Humidity: 75%
Wind Speed: 12 km/h
Pressure: 1013 hPa
Visibility: 8 km
UV Index: 2 (Low)
Sunrise: 07:30 AM
Sunset: 05:45 PM
Last Updated: 2025-02-09 14:30:00

Choose option: 2
=== Favorite Cities Weather ===

London: 15°C - Rainy
Paris: 14°C - Cloudy
New York: 5°C - Snowy

⚠️ Weather Alert: Temperature in New York dropping below 0°C!

Choose option: 7
=== City Comparison ===
Compare between:
1. London vs Paris
2. London vs New York
Choice: 1

City Comparison:
           London    Paris
Temp:      15°C      14°C
Condition: Rainy     Cloudy
Humidity:  75%       68%
Wind:      12 km/h   10 km/h
```

## Real-World Enhancement Ideas
1. **Weather Maps**: Display weather on a map
2. **Pollen Count**: Show allergen levels
3. **Air Quality**: Display AQI (Air Quality Index)
4. **Weather History**: Historical data for trends
5. **Severe Weather Alerts**: Real-time storm warnings
6. **Multiple Languages**: Localization
7. **Push Notifications**: Mobile alerts
8. **Integration**: Connect with calendar (plan outdoor activities)
9. **Climate Data**: Monthly/yearly trends
10. **Weather API Comparison**: Show different forecasts

## Grading Criteria
- ✅ Can fetch weather from API
- ✅ Displays current weather clearly
- ✅ Favorite cities feature works
- ✅ Temperature conversion works
- ✅ Data is cached (don't spam API)
- ✅ Error handling for bad city names
- ✅ User interface is clear
- ✅ Can handle multiple cities efficiently

## Important Notes
- **API Rate Limiting**: Don't make too many requests (use caching)
- **Error Handling**: Handle network errors gracefully
- **Free API Limits**: Most free APIs have request limits
- **Caching**: Store data locally to reduce API calls
