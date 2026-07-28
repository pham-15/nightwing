"""Combined daily Calendar and Tasks summary."""

from integrations.calendar_service import (
    get_todays_calendar_summary,
)
from integrations.tasks_service import (
    get_todays_tasks_summary,
)


def get_daily_agenda_summary() -> str:
    """Return today's Calendar events and Google Tasks."""
    calendar_summary = get_todays_calendar_summary()
    tasks_summary = get_todays_tasks_summary()

    return f"{calendar_summary} {tasks_summary}"


if __name__ == "__main__":
    try:
        print(get_daily_agenda_summary())
    except Exception as error:
        print(f"Daily agenda test failed: {error}")