def decide_action(state):

    if state["customer_mood"] in ["angry", "furious"]:
        if "contact_customer" not in state["history"]:
            return "contact_customer"

    if state["order_status"] == "delayed":
        if "check_order" not in state["history"]:
            return "check_order"

    if state["status"] == "open":
        return "refund"

    return "escalate"