import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import numpy as np
from stable_baselines3 import DQN
from envs.scheduling_env import SchedulingEnv
<<<<<<< HEAD
 
env = SchedulingEnv(num_ues=5)
model = DQN.load("week4/models/dqn_50k")
=======

env = SchedulingEnv(
    num_ues=30
)

model = DQN.load(
    "models/dqn_30ue"
)
>>>>>>> 3efb62cc42d40ab31e21f35c14e571dc9584c2ec

num_episodes = 100

throughputs = []
latencies = []
fairnesses = []

<<<<<<< HEAD
# -----------------------
# Evaluation loop
# -----------------------
for ep in range(num_episodes):

    obs, _ = env.reset()
=======
for ep in range(num_episodes):

    obs, _ = env.reset()

>>>>>>> 3efb62cc42d40ab31e21f35c14e571dc9584c2ec
    done = False

    episode_throughput = 0
    episode_latency = 0

<<<<<<< HEAD
    allocations = np.zeros(env.num_ues)

    while not done:

        action, _ = model.predict(obs, deterministic=True)

        obs, reward, terminated, truncated, info = env.step(action)

        done = terminated or truncated

        episode_throughput += info.get("throughput", 0)
        episode_latency += info.get("latency", 0)
        allocations += info.get("allocations", 0)

    # Jain's Fairness Index
    fairness = (
        np.sum(allocations) ** 2
        / (len(allocations) * np.sum(allocations ** 2) + 1e-8)
    )

    throughputs.append(episode_throughput)
    latencies.append(episode_latency)
    fairnesses.append(fairness)

# -----------------------
# Results
# -----------------------
=======
    allocations = np.zeros(
        env.num_ues
    )

    while not done:

        action, _ = model.predict(
            obs,
            deterministic=True
        )

        obs, reward, terminated, truncated, info = env.step(
            action
        )

        done = terminated or truncated

        episode_throughput += info["throughput"]
        episode_latency += info["latency"]
        allocations += info["allocations"]

    fairness = (
        np.sum(allocations) ** 2
        /
        (
            len(allocations)
            * np.sum(allocations ** 2)
            + 1e-8
        )
    )

    throughputs.append(
        episode_throughput
    )

    latencies.append(
        episode_latency
    )

    fairnesses.append(
        fairness
    )

>>>>>>> 3efb62cc42d40ab31e21f35c14e571dc9584c2ec
print("\n30 UE DQN Evaluation Results")
print("-" * 35)

print(
    f"Throughput: {np.mean(throughputs):.2f} +/- {np.std(throughputs):.2f}"
)

print(
    f"Latency: {np.mean(latencies):.2f} +/- {np.std(latencies):.2f}"
)

print(
    f"Fairness: {np.mean(fairnesses):.4f} +/- {np.std(fairnesses):.4f}"
)