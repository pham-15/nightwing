from pathlib import Path

import sounddevice as sd
from scipy.io.wavfile import write


# Locate the main project folder.
#
# This file is located at:
# project-nightwing/audio/audio_input.py
#
# .parent       = audio folder
# .parent.parent = project-nightwing folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Store temporary recordings inside:
# project-nightwing/data/
DATA_DIR = PROJECT_ROOT / "data"

# Audio settings
SAMPLE_RATE = 16_000
CHANNELS = 1
DEFAULT_DURATION = 5


def record_audio(
    duration: float = DEFAULT_DURATION,
    output_path: str | Path = "data/recording.wav",
) -> Path:
    """
    Record audio from the computer's default microphone.

    Args:
        duration:
            How many seconds to record.

        output_path:
            Where the WAV file should be saved. A relative path is
            interpreted from the main project folder.

    Returns:
        A Path object pointing to the saved WAV file.

    Raises:
        ValueError:
            If the requested recording duration is invalid.

        RuntimeError:
            If recording or saving fails.
    """

    if duration <= 0:
        raise ValueError("Recording duration must be greater than zero.")

    file_path = Path(output_path)

    # If the caller gives a relative path such as:
    # data/recording.wav
    #
    # place it inside the project folder.
    if not file_path.is_absolute():
        file_path = PROJECT_ROOT / file_path

    # Create the destination folder if it does not already exist.
    file_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        print(f"Recording for {duration} seconds...")
        print("Speak now.")

        # The total number of audio samples is:
        # duration in seconds × samples per second
        frame_count = int(duration * SAMPLE_RATE)

        recording = sd.rec(
            frames=frame_count,
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="int16",
        )

        # Wait until all requested audio has been recorded.
        sd.wait()

        # Save the recording as a standard WAV file.
        write(
            filename=str(file_path),
            rate=SAMPLE_RATE,
            data=recording,
        )

        print(f"Recording saved to: {file_path}")

        return file_path

    except sd.PortAudioError as error:
        raise RuntimeError(
            "The microphone recording failed. "
            "Make sure a microphone is connected and selected as the "
            "default input device."
        ) from error

    except Exception as error:
        raise RuntimeError(
            f"An unexpected audio recording error occurred: {error}"
        ) from error