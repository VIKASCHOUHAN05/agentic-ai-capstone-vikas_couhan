def check_input(message):

    blocked = ["ignore instructions", "system prompt"]

    for word in blocked:

        if word in message.lower():

            return False

    return True