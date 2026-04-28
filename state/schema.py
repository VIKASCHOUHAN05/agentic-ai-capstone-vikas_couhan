from typing import TypedDict, Optional, List


class CustomerSupportState(TypedDict):

    messages: list

    customer_id: str

    current_agent: str

    ticket_id: Optional[str]

    conversation_summary: str

    pending_actions: List[str]

    guardrail_flags: List[str]