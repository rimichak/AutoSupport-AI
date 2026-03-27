def compute_score(state):
    score = 0.0

    if "check_order" in state["history"]:
        score += 0.3

    if "contact_customer" in state["history"]:
        score += 0.3

    if state["status"] == "closed":
        score += 0.4

    return min(score, 1.0)