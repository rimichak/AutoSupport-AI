# 🚀 AutoSupport AI – OpenEnv Agent Training Environment

### 🧠 Real-World AI Simulation for Customer Support

---

## 📌 Overview

AutoSupport AI is a real-world simulation environment designed to train and evaluate AI agents for customer support workflows.

It follows the OpenEnv standard API (`step()`, `reset()`, `state()`) and enables agents to learn decision-making through rewards and feedback.

---

## 💡 Problem Statement

Customer support systems often struggle with:
- Inconsistent decision-making  
- Slow response handling  
- Lack of intelligent automation  

Training AI for such real-world scenarios requires a structured simulation environment.

---

## ✅ Solution

AutoSupport AI simulates customer support situations like:
- Delayed orders  
- Refund requests  
- Fraud disputes  

AI agents interact with the environment by taking actions such as:
- Checking order status  
- Contacting the customer  
- Issuing a refund  
- Escalating the issue  

Each action updates the system state and provides a reward signal, enabling learning through reinforcement.

---

## ⚙️ Key Features

- 🧠 OpenEnv-compliant environment  
- 🔄 Standard API: `step()`, `reset()`, `state()`  
- 📊 Typed state models using Pydantic  
- 🎯 3 difficulty levels (easy, medium, hard)  
- 🎁 Reward-based learning system  
- 🏆 Scoring system (0.0 – 1.0)  
- 🤖 Baseline AI agent (deterministic)  
- 📈 Interactive UI (Gradio dashboard)  
- 🐳 Docker support for deployment  

---

## 🏗️ Project Structure
autosupport-ai-openenv/
│
├── core/ # Environment logic (state, rewards, actions)
├── agent/ # AI decision logic
├── tasks/ # Task definitions (easy → hard)
├── grader/ # Evaluation system
├── app/ # UI (Gradio dashboard)
├── config/ # openenv.yaml configuration
├── main.py # Run all tasks
├── app.py # HuggingFace entry point
├── Dockerfile
├── requirements.txt
└── README.md

---

## 🔄 OpenEnv API

### `reset(task)`
Initializes a new scenario

### `step(action)`
Executes an action and returns:
- next state  
- reward  
- done flag  

### `state()`
Returns current environment state

---

## 🎮 Tasks

| Level   | Scenario                         |
|--------|---------------------------------|
| Easy   | Damaged product refund          |
| Medium | Late delivery complaint         |
| Hard   | Fraud transaction dispute       |

---

## 🎁 Reward System

| Action              | Reward |
|-------------------|--------|
| Check Order        | +0.2   |
| Contact Customer   | +0.3   |
| Issue Refund       | +0.5   |
| Timeout / Bad Flow | -0.5   |

✔ Encourages optimal decision sequences  
✔ Provides partial progress feedback  

---

## 🏆 Evaluation (Grader)

Agents are scored based on:
- Correct action sequence  
- Problem resolution  
- Customer handling  

Final score range: **0.0 – 1.0**

---

## 🤖 Baseline Agent

A deterministic agent is implemented for reproducibility:

- Uses rule-based policy  
- Produces consistent outputs  
- Helps benchmark performance  

Conclusion

AutoSupport AI provides a realistic and scalable environment for training AI agents in customer support workflows, helping improve automation and decision-making before real-world deployment.

Author
Rimi Chakraborty.