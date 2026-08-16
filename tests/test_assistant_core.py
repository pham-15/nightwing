from unittest.mock import patch

from assistant_core import process_request
from assistant_router import AssistantAction, RouteDecision


@patch("assistant_core.route_request")
@patch("assistant_core.get_weather")
def test_weather_request(mock_get_weather, mock_route_request) -> None:
    mock_route_request.return_value = RouteDecision(
        action=AssistantAction.WEATHER
    )

    mock_get_weather.return_value = 75

    response = process_request("What's the weather?")

    mock_get_weather.assert_called_once_with("Dallas")
    assert response == "The current temperature is 75"


@patch("assistant_core.route_request")
@patch("assistant_core.get_todays_calendar_summary")
def test_calendar_request(
    mock_calendar_summary,
    mock_route_request,
) -> None:
    mock_route_request.return_value = RouteDecision(
        action=AssistantAction.CALENDAR
    )

    mock_calendar_summary.return_value = "You have two events today."

    response = process_request("What meetings do I have today?")

    mock_calendar_summary.assert_called_once()
    assert response == "You have two events today."


@patch("assistant_core.route_request")
@patch("assistant_core.get_todays_tasks_summary")
def test_tasks_request(
    mock_tasks_summary,
    mock_route_request,
) -> None:
    mock_route_request.return_value = RouteDecision(
        action=AssistantAction.TASKS
    )

    mock_tasks_summary.return_value = "You have three tasks today."

    response = process_request("What tasks do I have?")

    mock_tasks_summary.assert_called_once()
    assert response == "You have three tasks today."


@patch("assistant_core.route_request")
@patch("assistant_core.get_daily_agenda_summary")
def test_agenda_request(
    mock_agenda_summary,
    mock_route_request,
) -> None:
    mock_route_request.return_value = RouteDecision(
        action=AssistantAction.AGENDA
    )

    mock_agenda_summary.return_value = "Here is your agenda for today."

    response = process_request("Show me my agenda.")

    mock_agenda_summary.assert_called_once()
    assert response == "Here is your agenda for today."


@patch("assistant_core.route_request")
def test_clarification_request(mock_route_request) -> None:
    mock_route_request.return_value = RouteDecision(
        action=AssistantAction.CLARIFY,
        clarification=(
            "Do you want your calendar events, "
            "tasks, or full daily agenda?"
        ),
    )

    response = process_request("What's happening today?")

    assert response == (
        "Do you want your calendar events, "
        "tasks, or full daily agenda?"
    )


@patch("assistant_core.route_request")
def test_general_request(mock_route_request) -> None:
    mock_route_request.return_value = RouteDecision(
        action=AssistantAction.GENERAL
    )

    response = process_request("Explain what a resistor does.")

    assert response == "The general AI connection has not been added yet."