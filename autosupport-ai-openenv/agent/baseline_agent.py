import random
from agent.policy import decide_action

def run_agent(env, task):
    random.seed(42)  # reproducibility

    state = env.reset(task)

    total_reward = 0
    done = False

    steps = []

    while not done:
        action = decide_action(state)
        steps.append(action)

        state, reward, done = env.step(action)
        total_reward += reward

    return state, total_reward, steps