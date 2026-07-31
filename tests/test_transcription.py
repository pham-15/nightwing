from audio.speech_to_text import transcribe_audio


def main() -> None:
    audio_file = "data/test_recording.wav"

    print("Sending audio for transcription...")

    try:
        transcript = transcribe_audio(audio_file)
    except (FileNotFoundError, RuntimeError) as error:
        print(f"Transcription test failed: {error}")
        return

    print("\nTranscription succeeded.")
    print("------------------------")
    print(transcript)


if __name__ == "__main__":
    main()