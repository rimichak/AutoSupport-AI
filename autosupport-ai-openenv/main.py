from core.environment import SupportEnv
from tasks.task_loader import get_tasks
from agent.baseline_agent import run_agent
from grader.grader import grade

def run_all():
    env = SupportEnv()

    for task in get_tasks():
        state, reward = run_agent(env, task)
        score = grade(state)

        print("\nTask:", task["level"])
        print("Final State:", state)
        print("Reward:", reward)
        print("Score:", score)

if __name__ == "__main__":
    run_all()