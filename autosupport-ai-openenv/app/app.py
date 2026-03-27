import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import gradio as gr
import pandas as pd

from core.environment import SupportEnv
from tasks.task_loader import get_tasks
from grader.grader import grade

# Initialize
env = SupportEnv()
tasks = get_tasks()

state = None
history_log = []
step_count = 0
total_reward = 0


# 📊 Format state nicely
def format_state(state):
    return f"""
📌 Ticket: {state['ticket']}

📊 Status: {state['status']}
😊 Mood: {state['customer_mood']}
📦 Order: {state['order_status']}
⏳ Time Left: {state['time_left']}

📝 History:
{', '.join(state['history']) if state['history'] else 'No actions yet'}
"""


# 🚀 Load Task
def load_task(task_level):
    global state, history_log, step_count, total_reward

    task = next(t for t in tasks if t["level"] == task_level)

    state = env.reset(task)
    history_log = []
    step_count = 0
    total_reward = 0

    return format_state(state), "0.0", "0.0", "0", "0.0", "Task Loaded 🚀", pd.DataFrame()


# ⚡ Take Action
def take_action(action):
    global state, history_log, step_count, total_reward

    state, reward, done = env.step(action)

    step_count += 1
    total_reward += reward

    score = grade(state)

    history_log.append({
        "step": step_count,
        "action": action,
        "reward": round(reward, 2),
        "score": round(score, 2)
    })

    df = pd.DataFrame(history_log)

    status = "✅ Completed" if done else "⏳ Running"

    return (
        format_state(state),
        str(round(reward, 2)),
        str(round(score, 2)),
        str(step_count),
        str(round(total_reward, 2)),
        status,
        df
    )


# 🎨 UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("""
    # 🚀 AutoSupport AI
    ### Intelligent Agent Training Environment

    Train AI agents to solve real-world customer support problems using reward-based learning.
    """)

    # Task selection
    with gr.Row():
        task_selector = gr.Dropdown(
            choices=["easy", "medium", "hard"],
            label="🎯 Select Task",
            value="easy"
        )
        load_btn = gr.Button("Load Scenario")

    # State display
    state_box = gr.Textbox(label="📊 Environment State", lines=12)

    # Metrics
    with gr.Row():
        reward_box = gr.Textbox(label="🎁 Reward")
        score_box = gr.Textbox(label="🏆 Score")

    with gr.Row():
        step_box = gr.Textbox(label="🔢 Steps")
        total_reward_box = gr.Textbox(label="💰 Total Reward")

    status_box = gr.Textbox(label="📌 Status")

    # Actions
    gr.Markdown("## ⚡ Actions")

    with gr.Row():
        btn1 = gr.Button("🔍 Check Order")
        btn2 = gr.Button("💬 Contact Customer")
        btn3 = gr.Button("💸 Issue Refund")
        btn4 = gr.Button("🚨 Escalate")

    # Performance table
    gr.Markdown("## 📊 Performance Tracking")
    performance_table = gr.Dataframe()

    # Actions wiring
    load_btn.click(
        load_task,
        inputs=task_selector,
        outputs=[state_box, reward_box, score_box, step_box, total_reward_box, status_box, performance_table]
    )

    btn1.click(lambda: take_action("check_order"),
               outputs=[state_box, reward_box, score_box, step_box, total_reward_box, status_box, performance_table])

    btn2.click(lambda: take_action("contact_customer"),
               outputs=[state_box, reward_box, score_box, step_box, total_reward_box, status_box, performance_table])

    btn3.click(lambda: take_action("refund"),
               outputs=[state_box, reward_box, score_box, step_box, total_reward_box, status_box, performance_table])

    btn4.click(lambda: take_action("escalate"),
               outputs=[state_box, reward_box, score_box, step_box, total_reward_box, status_box, performance_table])


# Run app
demo.launch()