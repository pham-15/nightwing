from assistant_router import (
    AssistantAction,
    route_request,
)


def test_live_weather_request() -> None:
    """
    Real API smoke test.

    This test makes an actual OpenAI API request.
    It verifies that the live router can understand a natural-language
    weather request and return the WEATHER action.
    """

    decision = route_request("Do I need an umbrella today?")

    print()
    print(f"Action: {decision.action}")
    print(f"Clarification: {decision.clarification}")

    assert decision.action == AssistantAction.WEATHER
    assert decision.clarification is None