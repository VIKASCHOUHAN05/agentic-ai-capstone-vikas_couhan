import sys
import os

# Add project root to Python path FIRST
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import json

from agents.triage_agent import route_query


def evaluate():

    with open("evaluation/test_cases.json") as f:
        tests = json.load(f)

    correct = 0

    for test in tests:

        state = {
            "messages": [
                {
                    "role": "user",
                    "content": test["input"]
                }
            ]
        }

        predicted = route_query(state)

        expected = test["expected_agent"]

        if predicted == expected:
            correct += 1

        print(
            test["input"],
            "→",
            predicted,
            "| expected:",
            expected
        )

    accuracy = correct / len(tests)

    print("\nAccuracy:", round(accuracy, 2))


if __name__ == "__main__":
    evaluate()