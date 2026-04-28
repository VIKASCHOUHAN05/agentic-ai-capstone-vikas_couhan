import json
import time
import os

LOG_FILE = "observability/logs.json"


def log_event(event):

    if not os.path.exists(LOG_FILE):

        with open(LOG_FILE, "w") as f:
            json.dump([], f)

    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    logs.append(event)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)


def create_trace(agent_name):

    return {

        "agent": agent_name,
        "timestamp": time.time(),
        "latency": None,
        "tokens": 0,
        "cost": 0

    }