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

    daily_agenda_phrases = (
        "what do i have today",
        "what do i need to do today",
        "tell me my agenda",
        "give me my daily agenda",
        "what is my day looking like",
    )

    task_phrases = (
        "what tasks do i have today",
        "what tasks are due today",
        "show me my tasks",
        "tell me my tasks",
    )

    calendar_phrases = (
        "what is on my calendar",
        "what events do i have today",
        "show me today's events",
        "tell me my calendar",
    )

    cleaned_text = user_text.lower().strip()

    if "nightwing" in cleaned_text:
        return ("At your service")

    if "weather" in cleaned_text:
        temperature = get_weather("Dallas")
        return(f"The current temperature is {temperature}")

    if any(
        phrase in cleaned_text
        for phrase in daily_agenda_phrases
    ):
        return get_daily_agenda_summary()

    if any(
        phrase in cleaned_text
        for phrase in task_phrases
    ):
        return get_todays_tasks_summary()

    if any(
        phrase in cleaned_text
        for phrase in calendar_phrases
    ):
        return get_todays_calendar_summary()

    return "The general AI connection has not been added yet."