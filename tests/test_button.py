from gpiozero import Button
from signal import pause


# BCM GPIO number.
# GPIO17 is physical pin 11 on the Raspberry Pi header.
BUTTON_GPIO = 17


def button_pressed() -> None:
    print("Button pressed!")


def button_released() -> None:
    print("Button released!")


def main() -> None:
    print("------------------------------")
    print("Project Nightwing Button Test")
    print("------------------------------")
    print()
    print(f"Using GPIO{BUTTON_GPIO}.")
    print("Waiting for button presses...")
    print("Press Ctrl+C to stop the test.")
    print()

    # pull_up=True means:
    #
    # GPIO17 ---- button ---- GND
    #
    # The Raspberry Pi uses its built-in pull-up resistor,
    # so we do not need an external resistor for this test.
    button = Button(
        BUTTON_GPIO,
        pull_up=True,
        bounce_time=0.05,
    )

    button.when_pressed = button_pressed
    button.when_released = button_released

    # Keep the program running so it can continue detecting presses.
    pause()


if __name__ == "__main__":
    main()