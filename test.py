import gymnasium as gym
from stable_baselines3 import PPO

# Enable GUI rendering
env = gym.make("CartPole-v1", render_mode="human")

model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    tensorboard_log="./ppo_logs/",
    device="cpu"
)

model.learn(
    total_timesteps=10000,
    tb_log_name="PPO_run"
)

model.save("ppo_cartpole")

print("Training complete!")

# 👇 Run trained agent to see GUI
obs, _ = env.reset()

for _ in range(500):
    action, _ = model.predict(obs)
    obs, reward, terminated, truncated, _ = env.step(action)
    if terminated or truncated:
        obs, _ = env.reset()

env.close()
