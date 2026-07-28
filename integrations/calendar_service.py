"""Read-only Google Calendar functions for Project Nightwing."""

from __future__ import annotations

from datetime import datetime, time, timedelta
from typing import Any
from zoneinfo import ZoneInfo

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import TIMEZONE
from integrations.google_auth import get_google_credentials


def get_todays_events() -> list[dict[str, Any]]:
    """
    Return today's events from the personal account's primary calendar.

    This includes:
    - Normal timed events
    - All-day events
    - Individual occurrences of recurring events
    """
    timezone = ZoneInfo(TIMEZONE)
    now = datetime.now(timezone)

    start_of_today = datetime.combine(
        now.date(),
        time.min,
        tzinfo=timezone,
    )

    start_of_tomorrow = start_of_today + timedelta(days=1)

    credentials = get_google_credentials()

    service = build(
        "calendar",
        "v3",
        credentials=credentials,
        cache_discovery=False,
    )

    try:
        response = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=start_of_today.isoformat(),
                timeMax=start_of_tomorrow.isoformat(),
                singleEvents=True,
                orderBy="startTime",
                timeZone=TIMEZONE,
            )
            .execute()
        )
    except HttpError as error:
        raise RuntimeError(
            f"Google Calendar request failed: {error}"
        ) from error

    return response.get("items", [])


def format_event_time(event: dict[str, Any]) -> str:
    """Convert a Google event start value into readable local time."""
    start = event.get("start", {})

    # Google represents all-day events with "date" instead of "dateTime".
    if "date" in start:
        return "All day"

    raw_start = start.get("dateTime")

    if not raw_start:
        return "Time unavailable"

    event_datetime = datetime.fromisoformat(
        raw_start.replace("Z", "+00:00")
    )

    local_datetime = event_datetime.astimezone(
        ZoneInfo(TIMEZONE)
    )

    return local_datetime.strftime("%I:%M %p").lstrip("0")


def format_todays_events(
    events: list[dict[str, Any]],
) -> str:
    """Create a spoken, readable summary of today's events."""
    if not events:
        return "You do not have any calendar events today."

    descriptions: list[str] = []

    for event in events:
        title = event.get("summary", "Untitled event")
        event_time = format_event_time(event)

        if event_time == "All day":
            descriptions.append(f"{title}, all day")
        else:
            descriptions.append(f"{title} at {event_time}")

    count = len(descriptions)
    event_word = "event" if count == 1 else "events"

    return (
        f"You have {count} {event_word} today: "
        + "; ".join(descriptions)
        + "."
    )


def get_todays_calendar_summary() -> str:
    """Fetch and format today's Calendar events."""
    return format_todays_events(get_todays_events())


if __name__ == "__main__":
    try:
        print(get_todays_calendar_summary())
    except Exception as error:
        print(f"Calendar test failed: {error}")