from pathlib import Path

import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

SAMPLE_RATE = 16_000
CHANNELS = 1


def record_audio(
    output_path: str | Path = "data/recording.wav",
) -> Path:
    """
    Record audio from the default microphone until Enter is pressed.

    Later, the Enter key can be replaced with your physical button.

    Returns:
        Path to the saved WAV file.
    """

    file_path = Path(output_path)

    if not file_path.is_absolute():
        file_path = PROJECT_ROOT / file_path

    file_path.parent.mkdir(parents=True, exist_ok=True)

    # This list will hold small chunks of recorded audio.
    audio_chunks = []

    def audio_callback(indata, frames, time, status):
        """
        This function is automatically called over and over
        while the microphone stream is open.
        """

        if status:
            print(status)

        # Make a copy because sounddevice reuses its internal buffer.
        audio_chunks.append(indata.copy())

    try:
        print("Recording started.")
        print("Speak now.")
        print("Press Enter to stop recording.")

        with sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="int16",
            callback=audio_callback,
        ):
            # The microphone keeps recording while this InputStream
            # block is open.
            input()

        print("Recording stopped.")

        if not audio_chunks:
            raise RuntimeError("No audio was recorded.")

        # Join all of the little recorded chunks into one large array.
        recording = np.concatenate(audio_chunks, axis=0)

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