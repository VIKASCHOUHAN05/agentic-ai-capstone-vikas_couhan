from tools.refund_tools import calculate_refund, process_refund
from hitl.approval import request_approval
from observability.tracer import trace, end_trace


def refund_agent(state):

    start, trace_data = trace("Refund Agent")

    amount = calculate_refund()

    if amount > 50:

        approved = request_approval(amount)

        if not approved:

            state["messages"].append({

                "role": "assistant",
                "content": "Refund not approved"

            })

            return state

    result = process_refund(amount)

    state["messages"].append({

        "role": "assistant",
        "content": result

    })

    state["current_agent"] = "refund"

    end_trace(start, trace_data)

    return state