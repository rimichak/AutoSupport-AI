from agent.policy import decide_action

def run_agent(env, task):
    state = env.reset(task)

    total_reward = 0
    done = False

    while not done:
        action = decide_action(state)
        state, reward, done = env.step(action)
        total_reward += reward

    return state, total_reward