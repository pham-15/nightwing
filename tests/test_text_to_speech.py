from audio.text_to_speech import text_to_speech, play_audio


def main() -> None:
    try:
        print("Generating speech...")

        audio_path = text_to_speech(
            "Hello! My name is Nightwing."
        )

        print(f"Audio saved to: {audio_path}")
        print("Playing audio...")

        play_audio(audio_path)

    except (ValueError, FileNotFoundError, RuntimeError) as error:
        print(f"Text-to-speech test failed: {error}")
        return

    print()
    print("Text-to-speech and playback succeeded.")


if __name__ == "__main__":
    main()