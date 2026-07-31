from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI


# Find the main project folder.
# speech_to_text.py is inside:
# project-nightwing/audio/speech_to_text.py
#
# .parent gives us the audio folder.
# .parent.parent gives us the project root folder.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Explicitly load:
# project-nightwing/.env
load_dotenv(PROJECT_ROOT / ".env")


def transcribe_audio(audio_path: str | Path) -> str:
    """
    Convert a recorded audio file into text using OpenAI GPT-Transcribe.

    Args:
        audio_path:
            The location of the audio file, such as
            "data/test_recording.wav".

    Returns:
        The transcribed spoken words as a normal Python string.

    Raises:
        FileNotFoundError:
            If the audio file does not exist.

        RuntimeError:
            If the API key is missing or the API request fails.
    """

    file_path = Path(audio_path)

    # If a relative path was provided, resolve it from the project root.
    if not file_path.is_absolute():
        file_path = PROJECT_ROOT / file_path

    if not file_path.exists():
        raise FileNotFoundError(
            f"Audio file was not found: {file_path}"
        )

    api_key = os.getenv("OPENAI_API_KEY").strip()

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY was not found. "
            "Check that it exists in the project's .env file."
        )

    client = OpenAI(api_key=api_key)

    try:
        # 'rb' means:
        # r = read the file
        # b = read it as binary audio data
        with file_path.open("rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="gpt-transcribe",
                file=audio_file,
            )

        return transcription.text.strip()

    except Exception as error:
        raise RuntimeError(
            f"OpenAI transcription failed: {error}"
        ) from error