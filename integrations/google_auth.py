"""Shared Google OAuth authentication for Project Nightwing."""

from __future__ import annotations

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from config import PROJECT_ROOT


# Read-only access to both Calendar and Tasks.
SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/tasks.readonly",
]

CREDENTIALS_PATH = PROJECT_ROOT / "credentials.json"
TOKEN_PATH = PROJECT_ROOT / "token.json"


def get_google_credentials() -> Credentials:
    """
    Load or create the Google OAuth credentials used by the application.

    credentials.json identifies Project Nightwing.
    token.json contains the permission granted by your personal account.
    """
    credentials: Credentials | None = None

    if TOKEN_PATH.exists():
        credentials = Credentials.from_authorized_user_file(
            str(TOKEN_PATH),
            SCOPES,
        )

    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())

    if not credentials or not credentials.valid:
        if not CREDENTIALS_PATH.exists():
            raise FileNotFoundError(
                "credentials.json was not found in the project root. "
                "Download the Desktop app OAuth credentials from Google Cloud."
            )

        flow = InstalledAppFlow.from_client_secrets_file(
            str(CREDENTIALS_PATH),
            SCOPES,
        )

        credentials = flow.run_local_server(port=0)

    TOKEN_PATH.write_text(
        credentials.to_json(),
        encoding="utf-8",
    )

    return credentials