from assistant_core import process_request
from audio.audio_input import record_audio
from audio.speech_to_text import transcribe_audio
from audio.text_to_speech import (
    play_audio,
    text_to_speech,
)


def main() -> None:
    while True:
        input("Press Enter to start recording...")

        try:
            audio_path = record_audio(
                output_path="data/voice_command.wav"
            )

            print()
            print("Transcribing...")

            user_text = transcribe_audio(audio_path)

            print(f"You: {user_text}")

            if user_text.lower().strip() == "exit":
                break

            print()
            print("Thinking...")

            response = process_request(user_text)

            print(f"Robot: {response}")
            print()

            speech_path = text_to_speech(response)
            play_audio(speech_path)

        except (ValueError, FileNotFoundError, RuntimeError) as error:
            print(f"Assistant failed: {error}")
            print()


if __name__ == "__main__":
    main()