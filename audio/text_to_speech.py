from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI
import pygame


# Find the main project folder.
#
# This file is inside:
# project-nightwing/audio/text_to_speech.py
#
# .parent gives us the audio folder.
# .parent.parent gives us project-nightwing.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load variables from:
# project-nightwing/.env
load_dotenv(PROJECT_ROOT / ".env")


def text_to_speech(
    text: str,
    output_path: str = "data/speech.mp3",
) -> Path:
    """
    Convert text into spoken audio and save it as an MP3 file.

    Returns the path to the created audio file.
    """

    if not text.strip():
        raise ValueError("Text cannot be empty.")

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY was not found in the .env file."
        )

    client = OpenAI(api_key=api_key)

    # Turn the relative output path into a path
    # starting from the project root.
    audio_path = PROJECT_ROOT / output_path

    # Make sure the folder exists.
    audio_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=text,
        ) as response:
            response.stream_to_file(audio_path)

    except Exception as error:
        raise RuntimeError(
            f"OpenAI text-to-speech failed: {error}"
        ) from error

    return audio_path

def play_audio(audio_path: Path) -> None:
    """
    Play an audio file through the computer's default speaker.
    """

    if not audio_path.exists():
        raise FileNotFoundError(
            f"Audio file was not found: {audio_path}"
        )

    try:
        pygame.mixer.init()

        pygame.mixer.music.load(str(audio_path))
        pygame.mixer.music.play()

        # Keep Python waiting while the audio is playing.
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except pygame.error as error:
        raise RuntimeError(
            f"Audio playback failed: {error}"
        ) from error

    finally:
        pygame.mixer.quit()