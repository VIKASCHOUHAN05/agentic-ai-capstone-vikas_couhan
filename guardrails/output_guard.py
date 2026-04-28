import re


def mask_pii(text):

    # mask phone numbers
    text = re.sub(
        r"\b\d{10}\b",
        "***PHONE***",
        text
    )

    # mask email
    text = re.sub(
        r"\S+@\S+",
        "***EMAIL***",
        text
    )

    return text