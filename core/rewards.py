def calculate_reward(state, action):
    reward = 0.0

    if action == "check_order":
        reward += 0.2

    if action == "contact_customer":
        reward += 0.3

    if action == "refund":
        reward += 0.5

    if state["time_left"] <= 0:
        reward -= 0.5

    return reward