import numpy as np
from stable_baselines3 import PPO
from envs.scheduling_env import SchedulingEnv

# Create environment
env = SchedulingEnv()

# Load trained PPO model (NO .zip extension)
model = PPO.load("../models/ppo_50k")

num_episodes = 100

throughputs = []
latencies = []
fairnesses = []

for ep in range(num_episodes):

    obs, _ = env.reset()

    done = False
    episode_throughput = 0
    episode_latency = 0

    allocations = np.zeros(env.num_ues)

    while not done:

        action, _ = model.predict(obs, deterministic=True)

        obs, reward, terminated, truncated, info = env.step(action)

        done = terminated or truncated

        # safe accumulation
        episode_throughput += info.get("throughput", reward)
        episode_latency += info.get("latency", 0)

        if "allocations" in info:
            allocations += np.array(info["allocations"])

    # Jain's Fairness Index (safe version)
    denom = np.sum(allocations ** 2) * len(allocations)

    fairness = (np.sum(allocations) ** 2) / (denom + 1e-8)

    throughputs.append(episode_throughput)
    latencies.append(episode_latency)
    fairnesses.append(fairness)

# ===================== RESULTS =====================

print("\nPPO Evaluation Results")
print("-" * 30)

print(
    f"Throughput: {np.mean(throughputs):.2f} +/- {np.std(throughputs):.2f}"
)

print(
    f"Latency: {np.mean(latencies):.2f} +/- {np.std(latencies):.2f}"
)

print(
    f"Fairness: {np.mean(fairnesses):.4f} +/- {np.std(fairnesses):.4f}"
)