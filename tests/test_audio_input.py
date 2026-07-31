from audio.audio_input import record_audio


def main() -> None:
    try:
        audio_path = record_audio(
            duration=5,
            output_path="data/microphone_test.wav",
        )
    except (ValueError, RuntimeError) as error:
        print(f"Recording test failed: {error}")
        return

    print()
    print("Recording test succeeded.")
    print(f"Your file is located at: {audio_path}")


if __name__ == "__main__":
    main()