def update_state(state, action):
    if action == "contact_customer":
        state["customer_mood"] = "calm"

    if action == "refund":
        state["status"] = "closed"

    if action == "escalate":
        state["status"] = "escalated"

    return state