from assistant_router import (
    AssistantAction,
    route_request,
)

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

from config import DEFAULT_CITY


def process_request(user_text: str) -> str:
    """
    Process a user's request.

    The router first decides what kind of request this is.

    Then this function sends the request to the correct service.
    """

    decision = route_request(user_text)

    if decision.action == AssistantAction.CLARIFY:
        return decision.clarification or (
            "I'm not sure what you mean. Could you clarify?"
        )

    if decision.action == AssistantAction.WEATHER:
        temperature = get_weather(DEFAULT_CITY)

        return (
            f"The current temperature in {DEFAULT_CITY} "
            f"is {round(temperature)} degrees Fahrenheit."
        )
    
    if decision.action == AssistantAction.CALENDAR:
        return get_todays_calendar_summary()

    if decision.action == AssistantAction.TASKS:
        return get_todays_tasks_summary()

    if decision.action == AssistantAction.AGENDA:
        return get_daily_agenda_summary()

    if decision.action == AssistantAction.GENERAL:
        return "The general AI connection has not been added yet."

    return "I could not determine how to handle that request."