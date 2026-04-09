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
# 🧪 8. The 10-Armed Testbed

---

## 🎯 Purpose

To compare the performance of:
- Greedy methods
- ε-greedy methods

---

## ⚙️ Setup

- Number of actions: k = 10  
- True action values:

\[
q^*(a) \sim \mathcal{N}(0, 1)
\]

- Rewards:

\[
R_t \sim \mathcal{N}(q^*(A_t), 1)
\]

---

## 🧪 Experiment Details

- 2000 independent bandit problems  
- Each run = 1000 steps  
- Results averaged  

---

## 📊 Methods Compared

- Greedy (ε = 0)  
- ε-greedy (ε = 0.01)  
- ε-greedy (ε = 0.1)  

---

## 📈 Results

---

### 🟢 Greedy Method

- Learns quickly at start  
- Gets stuck in suboptimal actions  
- Poor long-term performance  

---

### 🔵 ε = 0.1

- Explores more  
- Finds optimal action faster  
- But keeps exploring → slightly suboptimal  

---

### 🟡 ε = 0.01

- Slower learning  
- Best long-term performance  

---

## 🧠 Key Insights

- Exploration is essential  
- Greedy methods fail due to lack of exploration  
- Small ε gives best balance  

---

## 📊 Approximate Performance

| Method | Avg Reward | Optimal Action % |
|--------|-----------|-----------------|
| Greedy | ~1.0 | ~33% |
| ε = 0.1 | ~1.4 | ~91% |
| ε = 0.01 | ~1.5 | ~95%+ |

---

## ⚠️ Effect of Noise

- High noise → more exploration needed  
- Low noise → greedy can work better  

---

## 🔁 Non-Stationary Problems

In real-world RL:
- Environments change over time  
- Exploration is always necessary  

---

## 🧩 Conclusion

> A balance between exploration and exploitation is essential for optimal learning.

---
---

## ⚠️ Note

These guarantees are theoretical (asymptotic).  
In practice, performance depends on:
- ε value  
- Number of steps  
- Reward distribution  
# 🔁 10. Nonstationary Problems

---

## 🎯 Problem

In real-world RL, environments change over time.

---

## ❌ Issue with Sample Average

\[
Q_n = \frac{1}{n} \sum R_i
\]

- Treats all rewards equally  
- Slow to adapt to changes  

---

## 💡 Solution: Constant Step Size

\[
Q_{n+1} = Q_n + \alpha (R_n - Q_n)
\]

---

## 🧠 Intuition

> Recent rewards are more important than older ones

---

## 📉 Exponential Recency Weighting

- Recent rewards → high weight  
- Older rewards → exponentially less weight  

---

## ⚖️ Tradeoff

| Method | Behavior |
|--------|--------|
| Sample Average | Stable, slow |
| Constant α | Adaptive, responsive |

---

---

# 🌟 11. Optimistic Initial Values

---

## 🎯 Idea

Initialize action values optimistically:

\[
Q_1(a) = +5
\]

---

## 🧠 Effect

- Encourages exploration  
- Agent becomes “disappointed” and tries other actions  

---

## ⚠️ Limitations

- Works only at the beginning  
- Not useful for nonstationary problems  

---

## 🧩 Insight

> Initial beliefs can drive exploration

---

---

# 🚀 12. Upper Confidence Bound (UCB)

---

## 🎯 Problem

ε-greedy explores randomly and inefficiently.

---

## 💡 Solution: UCB

\[
A_t = argmax_a \left[ Q_t(a) + c \sqrt{\frac{\ln t}{N_t(a)}} \right]
\]

---

## 🧠 Intuition

Action score = value + uncertainty

---

## 📌 Behavior

- Less tried actions → more exploration  
- Frequently tried actions → less exploration  

---

## ✅ Advantages

- Smart exploration  
- Focuses on uncertain actions  

---

## ⚠️ Limitations

- Hard to scale to large problems  
- Not ideal for nonstationary environments  

---

---

# 🧪 Key Insights

---

## 🔥 Exploration Strategies

- ε-greedy → simple, random  
- Optimistic values → initial exploration  
- UCB → uncertainty-based exploration  

---

## 🧠 Real-World Insight

> In dynamic environments, continuous exploration is necessary.

---

## 🚀 Summary

Reinforcement Learning requires:

- Learning from experience  
- Adapting to change  
- Balancing exploration and exploitation  

# 🤖 13. Agent–Environment Interface (MDP)

---

## 🎯 What is this?

Reinforcement Learning is modeled as an interaction between:

- **Agent** → the learner / decision maker  
- **Environment** → everything the agent interacts with  

---

## 🔁 Interaction Loop

At each time step \( t \):

1. Agent observes **state** \( S_t \)  
2. Agent takes **action** \( A_t \)  
3. Environment returns:
   - **reward** \( R_{t+1} \)  
   - **next state** \( S_{t+1} \)  

---

## 🔄 Trajectory (Experience)

The interaction generates a sequence:

\[
S_0, A_0, R_1, S_1, A_1, R_2, S_2, ...
\]

---

## 📦 Components of MDP

- **S (States):** possible situations  
- **A (Actions):** choices available  
- **R (Rewards):** feedback signal  

---

## 🧠 Dynamics Function

\[
p(s', r \mid s, a)
\]

👉 Meaning:

- Probability of reaching state \( s' \)  
- And receiving reward \( r \)  
- Given current state \( s \) and action \( a \)

---

## ⚡ Markov Property (Very Important)

> The future depends only on the present, not the past.

---

## 🧠 Why This Matters

- Simplifies decision making  
- Forms the mathematical foundation of RL  
- Used in all major RL algorithms  

---

## 🤖 Example (Robot)

- State → robot position  
- Action → move forward  
- Reward → +10 if goal reached  
- Next state → updated position  

---

## 🧩 Summary

> Reinforcement Learning is a continuous interaction where an agent learns from states, actions, and rewards to maximize long-term success.

---

---

---
