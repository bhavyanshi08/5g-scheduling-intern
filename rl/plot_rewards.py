import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/monitor.csv", skiprows=1)

plt.figure(figsize=(8, 5))
plt.plot(df["r"], marker="o")

plt.title("DQN Training Reward Curve")
plt.xlabel("Episode")
plt.ylabel("Episode Reward")

plt.grid(True)

plt.savefig("../results/dqn_reward_curve.png")

plt.show()
from stable_baselines3.common.monitor import Monitor

env = Monitor(env, "../results/")