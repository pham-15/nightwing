"""Read-only Google Tasks functions for Project Nightwing."""

from __future__ import annotations

from datetime import datetime, time, timedelta, timezone
from typing import Any
from zoneinfo import ZoneInfo

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import TIMEZONE
from integrations.google_auth import get_google_credentials


def _get_today_bounds_utc() -> tuple[str, str]:
    """
    Return the beginning of today and tomorrow as UTC RFC 3339 timestamps.

    Google Tasks accepts dueMin and dueMax as RFC 3339 timestamps.
    """
    local_timezone = ZoneInfo(TIMEZONE)
    now = datetime.now(local_timezone)

    start_local = datetime.combine(
        now.date(),
        time.min,
        tzinfo=local_timezone,
    )

    end_local = start_local + timedelta(days=1)

    start_utc = start_local.astimezone(timezone.utc)
    end_utc = end_local.astimezone(timezone.utc)

    return (
        start_utc.isoformat().replace("+00:00", "Z"),
        end_utc.isoformat().replace("+00:00", "Z"),
    )


def get_task_lists() -> list[dict[str, Any]]:
    """Return every Google Tasks list belonging to the authorized user."""
    credentials = get_google_credentials()

    service = build(
        "tasks",
        "v1",
        credentials=credentials,
        cache_discovery=False,
    )

    task_lists: list[dict[str, Any]] = []
    page_token: str | None = None

    try:
        while True:
            response = (
                service.tasklists()
                .list(
                    maxResults=100,
                    pageToken=page_token,
                )
                .execute()
            )

            task_lists.extend(response.get("items", []))
            page_token = response.get("nextPageToken")

            if not page_token:
                break

    except HttpError as error:
        raise RuntimeError(
            f"Google Tasks list request failed: {error}"
        ) from error

    return task_lists


def get_todays_tasks() -> list[dict[str, Any]]:
    """
    Return incomplete tasks due today from every Google Tasks list.

    Each returned item also contains the task-list name.
    """
    credentials = get_google_credentials()

    service = build(
        "tasks",
        "v1",
        credentials=credentials,
        cache_discovery=False,
    )

    due_min, due_max = _get_today_bounds_utc()
    collected_tasks: list[dict[str, Any]] = []

    try:
        task_lists = get_task_lists()

        for task_list in task_lists:
            task_list_id = task_list["id"]
            task_list_title = task_list.get(
                "title",
                "Unnamed task list",
            )

            page_token: str | None = None

            while True:
                response = (
                    service.tasks()
                    .list(
                        tasklist=task_list_id,
                        dueMin=due_min,
                        dueMax=due_max,
                        showCompleted=False,
                        showDeleted=False,
                        showHidden=False,
                        maxResults=100,
                        pageToken=page_token,
                    )
                    .execute()
                )

                for task in response.get("items", []):
                    # This extra check prevents any completed item from
                    # accidentally appearing in the final response.
                    if task.get("status") == "completed":
                        continue

                    task["taskListTitle"] = task_list_title
                    collected_tasks.append(task)

                page_token = response.get("nextPageToken")

                if not page_token:
                    break

    except HttpError as error:
        raise RuntimeError(
            f"Google Tasks request failed: {error}"
        ) from error

    return collected_tasks


def format_todays_tasks(
    tasks: list[dict[str, Any]],
) -> str:
    """Create a spoken summary of today's incomplete tasks."""
    if not tasks:
        return "You do not have any incomplete tasks due today."

    descriptions: list[str] = []

    for task in tasks:
        title = task.get("title", "Untitled task")
        list_title = task.get(
            "taskListTitle",
            "Unknown task list",
        )

        descriptions.append(
            f"{title}, from your {list_title} list"
        )

    count = len(descriptions)
    task_word = "task" if count == 1 else "tasks"

    return (
        f"You have {count} {task_word} due today: "
        + "; ".join(descriptions)
        + "."
    )


def get_todays_tasks_summary() -> str:
    """Fetch and format today's Google Tasks."""
    return format_todays_tasks(get_todays_tasks())


if __name__ == "__main__":
    try:
        print(get_todays_tasks_summary())
    except Exception as error:
        print(f"Tasks test failed: {error}")