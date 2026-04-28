from langgraph.graph import StateGraph

from state.schema import CustomerSupportState

from agents.triage_agent import route_query
from agents.billing_agent import billing_agent
from agents.technical_agent import technical_agent
from agents.refund_agent import refund_agent

from guardrails.middleware import (
    run_input_guardrails,
    run_output_guardrails
)

workflow = StateGraph(CustomerSupportState)

from agents.triage_agent import triage_agent, route_query

workflow.add_node("triage", triage_agent)

workflow.add_node("billing", billing_agent)

workflow.add_node("technical", technical_agent)

workflow.add_node("refund", refund_agent)


workflow.set_entry_point("triage")

workflow.add_conditional_edges(

    "triage",
    route_query,
    {

        "billing": "billing",

        "technical": "technical",

        "refund": "refund"

    }

)

app = workflow.compile()



def run_cli():

    state = {

        "messages": [],

        "customer_id": "CUST123",

        "current_agent": "",

        "ticket_id": None,

        "conversation_summary": "",

        "pending_actions": [],

        "guardrail_flags": []

    }

    while True:

        user_input = input("\nUser: ")

        message = {
            "role": "user",
            "content": user_input
        }

        state["messages"].append(message)

        # INPUT GUARDRAIL

        state, allowed = run_input_guardrails(state)

        if not allowed:

            print(
                "Assistant:",
                state["messages"][-1]["content"]
            )

            continue

        # RUN GRAPH

        state = app.invoke(state)

        # OUTPUT GUARDRAIL

        state = run_output_guardrails(state)

        print(
            "Assistant:",
            state["messages"][-1]["content"]
        )


if __name__ == "__main__":

    run_cli()