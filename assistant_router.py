from enum import Enum

from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

from prompts.router_instructions import ROUTER_INSTRUCTIONS

load_dotenv()

class AssistantAction(str, Enum):
    WEATHER = "weather"
    CALENDAR = "calendar"
    TASKS = "tasks"
    AGENDA = "agenda"
    GENERAL = "general"
    CLARIFY = "clarify"


class RouteDecision(BaseModel):
    action: AssistantAction
    clarification: str | None = None


def get_openai_client() -> OpenAI:
    """
    Create and return the OpenAI client.

    Keeping client creation inside a function prevents the module from
    requiring OpenAI credentials just to be imported during tests.
    """
    return OpenAI()


def route_request(user_text: str) -> RouteDecision:
    cleaned_text = user_text.strip()

    if not cleaned_text:
        return RouteDecision(
            action=AssistantAction.CLARIFY,
            clarification="What would you like me to help you with?",
        )

    try:
        client = get_openai_client()

        response = client.responses.parse(
            model="gpt-5-mini",
            instructions=ROUTER_INSTRUCTIONS,
            input=cleaned_text,
            text_format=RouteDecision,
        )

        decision = response.output_parsed

        if decision is None:
            raise RuntimeError(
                "The router did not return a valid decision."
            )

        return decision

    except Exception as error:
        raise RuntimeError(
            f"Assistant routing failed: {error}"
        ) from error