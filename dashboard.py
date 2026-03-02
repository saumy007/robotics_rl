import gymnasium as gym
from stable_baselines3 import PPO

model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    tensorboard_log="./ppo_logs/",
    device="cpu"
)

model.learn(total_timesteps=10000, tb_log_name="PPO_run")
