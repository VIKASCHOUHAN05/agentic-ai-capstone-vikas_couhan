BLOCKED_PATTERNS = [
    "ignore instructions",
    "system prompt",
    "bypass",
    "hack",
]


def validate_input(message):

    text = message.lower()

    for pattern in BLOCKED_PATTERNS:

        if pattern in text:

            return False, pattern

    return True, None