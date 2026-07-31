from audio.audio_input import record_audio
from audio.speech_to_text import transcribe_audio


def main() -> None:
    try:
        audio_path = record_audio(
            duration=5,
            output_path="data/voice_command.wav",
        )

        print()
        print("Sending recording for transcription...")

        transcript = transcribe_audio(audio_path)

    except (ValueError, FileNotFoundError, RuntimeError) as error:
        print(f"Voice transcription test failed: {error}")
        return

    print()
    print("Voice transcription succeeded.")
    print("------------------------------")
    print(transcript)


if __name__ == "__main__":
    main()