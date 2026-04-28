from guardrails.input_guard import validate_input
from guardrails.output_guard import mask_pii


def run_input_guardrails(state):

    message = state["messages"][-1]["content"]

    valid, pattern = validate_input(message)

    if not valid:

        state["guardrail_flags"].append(pattern)

        state["messages"].append({

            "role": "assistant",
            "content": "Request blocked by safety guardrails."

        })

        return state, False

    return state, True


def run_output_guardrails(state):

    last = state["messages"][-1]

    masked = mask_pii(last["content"])

    last["content"] = masked

    return state