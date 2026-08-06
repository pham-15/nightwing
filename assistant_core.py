from integrations.weather_service import get_weather

from integrations.calendar_service import (
    get_todays_calendar_summary,
)
from integrations.daily_agenda_service import (
    get_daily_agenda_summary,
)
from integrations.tasks_service import (
    get_todays_tasks_summary,
)

# Delegate tasks

# Example
def process_request(user_text: str) -> str:

    cleaned_text = user_text.lower().strip()

    if "nightwing" in cleaned_text:
        return ("At your service")

    if "weather" in cleaned_text:
        temperature = get_weather("Dallas")
        return(f"The current temperature is {temperature}")

    if "agenda" in cleaned_text:
        return get_daily_agenda_summary()

    if "task" in cleaned_text:
        return get_todays_tasks_summary()

    if "calendar" in cleaned_text:
        return get_todays_calendar_summary()

    return "The general AI connection has not been added yet."