from tools.billing_tools import get_invoice


from tools.billing_tools import get_invoice
from observability.tracer import trace, end_trace


def billing_agent(state):

    start, trace_data = trace("Billing Agent")

    customer_id = state["customer_id"]

    result = get_invoice(customer_id)

    state["messages"].append({

        "role": "assistant",
        "content": result

    })

    state["current_agent"] = "billing"

    end_trace(start, trace_data)

    return state