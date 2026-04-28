def triage_agent(state):
    # This node does NOT route, just passes state
    return state


def route_query(state):

    text = state["messages"][-1]["content"].lower()

    refund_keywords = [
        "refund",
        "money back",
        "return",
        "cancel",
        "refund request",
        "refund please"
    ]

    billing_keywords = [
        "invoice",
        "billing",
        "payment",
        "statement",
        "charge",
        "payment history",
        "update payment",
        "billing question"
    ]

    technical_keywords = [
        "internet",
        "wifi",
        "network",
        "connection",
        "error",
        "slow",
        "down",
        "not working",
        "issue"
    ]

    # Priority order matters

    if any(k in text for k in refund_keywords):
        return "refund"

    if any(k in text for k in billing_keywords):
        return "billing"

    if any(k in text for k in technical_keywords):
        return "technical"

    # fallback
    return "technical"