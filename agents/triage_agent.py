def triage_agent(state):
    # This node does NOT route, just passes state
    return state


def route_query(state):

    message = state["messages"][-1]["content"].lower()

    if "invoice" in message:
        return "billing"

    if "refund" in message:
        return "refund"

    if "error" in message:
        return "technical"

    return "technical"