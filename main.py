# Get user reqeust

from assistant_core import process_request


def main() -> None:
    while True:
        user_text = input("You: ")

        if user_text.lower() == "exit":
            break

        response = process_request(user_text)
        print(f"Robot: {response}")


if __name__ == "__main__":
    main()