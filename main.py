from core.environment import SupportEnv
from tasks.task_loader import get_tasks
from agent.baseline_agent import run_agent
from grader.grader import grade
from config.loader import load_config


def run_all():
    print("🚀 AutoSupport AI - Running All Tasks\n")

    # Load OpenEnv config
    config = load_config()
    print("📄 OpenEnv Config Loaded:")
    print(config)
    print("\n" + "="*50)

    env = SupportEnv()

    for task in get_tasks():
        print(f"\n🎯 TASK LEVEL: {task['level'].upper()}")
        print(f"📝 Scenario: {task['ticket']}")

        # Run baseline agent
        state, total_reward, steps = run_agent(env, task)

        # Evaluate
        score = grade(state)

        print("\n📊 FINAL RESULTS")
        print("-" * 30)
        print(f"✅ Final State: {state}")
        print(f"⚡ Actions Taken: {steps}")
        print(f"💰 Total Reward: {round(total_reward, 2)}")
        print(f"🏆 Score: {round(score, 2)}")
        print("="*50)


if __name__ == "__main__":
    run_all()