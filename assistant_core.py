# Delegate tasks

# Example
def process_request(user_text: str) -> str:
    cleaned_text = user_text.lower()

    if "nightwing" in cleaned_text:
        return ("At your service")

    return "The general AI connection has not been added yet."