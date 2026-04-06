This repository contains training data and logs from a humanoid robot simulated in MoJoCo, focusing on learning a stable standing posture. The training process optimizes the robot’s gait control system to maintain balance and remain stationary under simulation dynamics.

Learning about RL and robotics Simultaneously
Concepts --->

# 🧠 Reinforcement Learning — From Basics to ε-Greedy

This repository contains my learning journey through **Reinforcement Learning (RL)** — starting from fundamental concepts to core decision-making strategies like the **k-armed bandit problem** and **ε-greedy algorithm**.

---

# 📌 1. What is Reinforcement Learning?

Reinforcement Learning is a type of machine learning where an **agent learns by interacting with an environment** and receiving feedback in the form of rewards.

👉 Goal:  
Maximize total reward over time through learning.

---

# 🧩 2. Core Concepts of RL

---

## 🤖 Agent
The learner or decision-maker.

Example:
- Robot
- Game AI
- Autonomous system

---

## 🌍 Environment
Everything the agent interacts with.

Example:
- Game world
- Physical robot environment
- Simulation (e.g., Isaac Sim, PyBullet)

---

## 📍 State (S)
Represents the current situation of the agent.

Example:
- Robot position
- Game board configuration

---

## 🎯 Action (A)
Choices the agent can take.

Example:
- Move forward
- Turn left
- Pick object

---

## 🎁 Reward (R)
Feedback from the environment after taking an action.

- Positive → good action  
- Negative → bad action  

👉 Objective:
Maximize cumulative reward

---

## 📜 Policy (π)
Strategy used by the agent to decide actions.

\[
\pi(a | s)
\]

👉 Mapping:
State → Action

---

# 🔁 3. RL Interaction Loop

1. Agent observes state \(S_t\)  
2. Takes action \(A_t\)  
3. Receives reward \(R_t\)  
4. Moves to next state \(S_{t+1}\)  

This loop continues over time.

---

# 🎰 4. k-Armed Bandit Problem

---

## 🧠 Problem Setup

- You have **k actions (slot machines)**  
- Each action gives a **random reward**  
- You must choose actions repeatedly  

👉 Goal:
Maximize total reward over time

---

## ⚙️ Key Idea

Each action has a true value:

\[
q^*(a) = E[R_t | A_t = a]
\]

- Unknown to the agent  
- Must be estimated

---

## 📊 Estimated Value

\[
Q_t(a)
\]

Your current estimate of how good an action is.

---

# ⚔️ 5. Exploration vs Exploitation

---

## 🟢 Exploitation
Choose the best-known action.

✔ High immediate reward  
❌ Might miss better options  

---

## 🔵 Exploration
Try new or less-known actions.

✔ Learn more  
❌ Risky in short term  

---

## ⚡ The Conflict

You cannot do both at the same time.

👉 Trade-off:
- Short-term vs long-term reward

---

# 🎯 6. ε-Greedy Algorithm

---

## 💡 Idea

Balance exploration and exploitation using probability.

---

## ⚙️ Strategy

At each step:

- With probability **ε** → explore (random action)
- With probability **1 - ε** → exploit (best action)

---

## 🧮 Formula

\[
A_t =
\begin{cases}
\text{random action} & \text{with probability } \varepsilon \\
\arg\max_a Q_t(a) & \text{with probability } 1 - \varepsilon
\end{cases}
\]

---

## 🧠 Example

If ε = 0.1:

- 90% → choose best action  
- 10% → explore randomly  

---

## 🔄 Updating Action Values

\[
Q_{t+1}(a) = Q_t(a) + \alpha (R_t - Q_t(a))
\]

Where:
- α = learning rate  
- \(R_t\) = reward received  

---

# 📉 Choosing ε

| ε Value | Behavior |
|--------|---------|
| 0 | Pure greedy (no exploration) |
| 0.1 | Balanced |
| High (0.5) | Too random |

---

## 🔁 Decaying ε (Better Approach)

Start high → reduce over time
ε = 1 → 0.1 → 0.01

# 📊 7. Action-Value Methods

---

## 🧠 What are Action-Value Methods?

These methods estimate how good each action is and use those estimates to make decisions.

---

## 📈 Estimating Action Values

We estimate value of an action using the average of rewards received:

\[
Q_t(a) = \frac{\sum \text{rewards when action a was taken}}{\text{number of times action a was taken}}
\]

---

## 💡 Intuition

> “If an action gave high rewards in the past, it is probably good.”

---

## 🔁 Sample Average Method

Each action value is updated as an average of observed rewards.

As more samples are collected:

\[
Q_t(a) \rightarrow q^*(a)
\]

---

## 🟢 Greedy Action Selection

Choose the action with the highest estimated value:

\[
A_t = argmax_a Q_t(a)
\]

---

### ⚠️ Problem with Greedy

- No exploration  
- Can get stuck in suboptimal actions  

---

## 🎯 ε-Greedy Action Selection

To fix greedy limitations:

- With probability ε → choose random action  
- With probability (1 - ε) → choose best action  

---

## ✅ Advantage

- Ensures all actions are explored  
- Improves long-term performance  

---

## 📈 Long-Term Behavior

- Every action gets sampled  
- Estimates become accurate  
- Optimal action is chosen most of the time  

---

## 🧮 Example Calculation

For:
- 2 actions  
- ε = 0.5  

Probability of choosing greedy action:

\[
0.5 + (0.5 \times 0.5) = 0.75
\]

---

## ⚠️ Note

These guarantees are theoretical (asymptotic).  
In practice, performance depends on:
- ε value  
- Number of steps  
- Reward distribution  

---
