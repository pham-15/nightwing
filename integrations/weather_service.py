import openmeteo_requests
import requests
import requests_cache
from retry_requests import retry


def get_coordinates(city: str) -> tuple[float, float, str]:
    """
    Convert a city name into latitude and longitude.

    Returns:
        latitude, longitude, formatted location name
    """

    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

    geocoding_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    response = requests.get(
        geocoding_url,
        params=geocoding_params,
        timeout=10,
    )

    response.raise_for_status()
    data = response.json()

    results = data.get("results")

    if not results:
        raise ValueError(f'Could not find a location named "{city}".')

    location = results[0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    city_name = location["name"]
    state_name = location.get("admin1")
    country_name = location.get("country")

    location_parts = [
        part for part in [city_name, state_name, country_name] if part
    ]

    formatted_location = ", ".join(location_parts)

    return latitude, longitude, formatted_location


def get_weather(city: str) -> float:
    """Return the current temperature for a city in Fahrenheit."""

    latitude, longitude, location_name = get_coordinates(city)

    cache_session = requests_cache.CachedSession(
        ".cache",
        expire_after=3600,
    )

    retry_session = retry(
        cache_session,
        retries=5,
        backoff_factor=0.2,
    )

    openmeteo = openmeteo_requests.Client(
        session=retry_session,
    )

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m",
        "temperature_unit": "fahrenheit",
        "timezone": "auto",
    }

    responses = openmeteo.weather_api(
        weather_url,
        params=weather_params,
    )

    weather_response = responses[0]
    current = weather_response.Current()

    current_temperature = current.Variables(0).Value()

    print(f"Location: {location_name}")

    return current_temperature