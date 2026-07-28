from integrations.weather_service import get_weather

# Delegate tasks

# Example
def process_request(user_text: str) -> str:
    cleaned_text = user_text.lower()

    if "nightwing" in cleaned_text:
        return ("At your service")

    if "weather" in cleaned_text:
        temperature = get_weather("Dallas")
        return(f"The current temperature is {temperature}")

    return "The general AI connection has not been added yet."