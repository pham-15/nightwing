from unittest.mock import patch

from assistant_router import (
    AssistantAction,
    RouteDecision,
    route_request,
)


@patch("assistant_router.get_openai_client")
def test_weather_request(mock_get_client) -> None:
    mock_client = mock_get_client.return_value

    mock_client.responses.parse.return_value.output_parsed = RouteDecision(
        action=AssistantAction.WEATHER,
        clarification=None,
    )

    decision = route_request("What's the weather?")

    assert decision.action == AssistantAction.WEATHER
    assert decision.clarification is None


@patch("assistant_router.get_openai_client")
def test_calendar_request(mock_get_client) -> None:
    mock_client = mock_get_client.return_value

    mock_client.responses.parse.return_value.output_parsed = RouteDecision(
        action=AssistantAction.CALENDAR,
        clarification=None,
    )

    decision = route_request("Do I have any meetings today?")

    assert decision.action == AssistantAction.CALENDAR
    assert decision.clarification is None


@patch("assistant_router.get_openai_client")
def test_tasks_request(mock_get_client) -> None:
    mock_client = mock_get_client.return_value

    mock_client.responses.parse.return_value.output_parsed = RouteDecision(
        action=AssistantAction.TASKS,
        clarification=None,
    )

    decision = route_request("What tasks do I have?")

    assert decision.action == AssistantAction.TASKS
    assert decision.clarification is None


@patch("assistant_router.get_openai_client")
def test_agenda_request(mock_get_client) -> None:
    mock_client = mock_get_client.return_value

    mock_client.responses.parse.return_value.output_parsed = RouteDecision(
        action=AssistantAction.AGENDA,
        clarification=None,
    )

    decision = route_request("Show me my agenda.")

    assert decision.action == AssistantAction.AGENDA
    assert decision.clarification is None


@patch("assistant_router.get_openai_client")
def test_ambiguous_request_asks_for_clarification(
    mock_get_client,
) -> None:
    mock_client = mock_get_client.return_value

    mock_client.responses.parse.return_value.output_parsed = RouteDecision(
        action=AssistantAction.CLARIFY,
        clarification=(
            "Do you want your calendar events, "
            "tasks, or full daily agenda?"
        ),
    )

    decision = route_request("What's happening today?")

    assert decision.action == AssistantAction.CLARIFY
    assert decision.clarification is not None


@patch("assistant_router.get_openai_client")
def test_general_request(mock_get_client) -> None:
    mock_client = mock_get_client.return_value

    mock_client.responses.parse.return_value.output_parsed = RouteDecision(
        action=AssistantAction.GENERAL,
        clarification=None,
    )

    decision = route_request("Explain what a resistor does.")

    assert decision.action == AssistantAction.GENERAL
    assert decision.clarification is None


@patch("assistant_router.get_openai_client")
def test_empty_request_asks_for_clarification(
    mock_get_client,
) -> None:
    decision = route_request("   ")

    assert decision.action == AssistantAction.CLARIFY
    assert decision.clarification is not None

    # An empty request should be handled locally.
    # We should not waste an API call on it.
    mock_get_client.assert_not_called()