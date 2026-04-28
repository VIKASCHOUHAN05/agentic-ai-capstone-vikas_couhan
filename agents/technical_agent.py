from tools.technical_tools import create_ticket
from observability.tracer import trace, end_trace


def technical_agent(state):

    start, trace_data = trace("Technical Agent")

    ticket = create_ticket()

    state["ticket_id"] = ticket

    state["messages"].append({

        "role": "assistant",
        "content": ticket

    })

    state["current_agent"] = "technical"

    end_trace(start, trace_data)

    return state