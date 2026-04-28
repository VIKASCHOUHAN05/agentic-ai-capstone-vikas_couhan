import json
import os

FILE = "memory/chat_history.json"

MAX_MESSAGES = 6
KEEP_LAST = 2


class ShortTermMemory:

    def __init__(self):

        self.messages = []
        self.summary = ""

        self.load()

    # ------------------------
    # LOAD
    # ------------------------

    def load(self):

        if os.path.exists(FILE):

            with open(FILE, "r") as f:

                data = json.load(f)

                self.messages = data

    # ------------------------
    # SAVE
    # ------------------------

    def save(self):

        with open(FILE, "w") as f:

            json.dump(self.messages, f, indent=2)

    # ------------------------
    # ADD MESSAGE
    # ------------------------

    def add(self, message):

        self.messages.append(message)

        if len(self.messages) > MAX_MESSAGES:

            self.messages = self.messages[-KEEP_LAST:]

        self.save()

    # ------------------------
    # GET
    # ------------------------

    def get_messages(self):

        return self.messages