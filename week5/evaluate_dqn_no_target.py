<<<<<<< HEAD
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

env = SchedulingEnv(num_ues=15)

model = DQN.load("models/dqn_no_target")

num_episodes = 100

throughputs = []
latencies = []
fairnesses = []

print("Starting evaluation...", flush=True)

for ep in range(num_episodes):

    print(f"Episode {ep+1}/{num_episodes}", flush=True)

    obs, _ = env.reset()
    done = False

    episode_throughput = 0
    episode_latency = 0

    allocations = np.zeros(env.num_ues)

    step_count = 0

    while not done:

        step_count += 1
        if step_count > 1000:
            print("⚠️ Breaking loop")
            break

        action, _ = model.predict(obs, deterministic=True)

        obs, reward, terminated, truncated, info = env.step(action)

        done = terminated or truncated

        tp = info.get("throughput", info.get("avg_throughput", 0))
        lat = info.get("latency", info.get("delay", 0))
        alloc = np.array(info.get("allocations", np.zeros(env.num_ues)))

        episode_throughput += tp
        episode_latency += lat
        allocations += alloc

    fairness = (
        np.sum(allocations) ** 2
        / (len(allocations) * np.sum(allocations ** 2) + 1e-8)
    )

    throughputs.append(episode_throughput)
    latencies.append(episode_latency)
    fairnesses.append(fairness)

print("\nNo Target Network DQN Results")
print("-" * 35)

print(f"Throughput: {np.mean(throughputs):.2f} +/- {np.std(throughputs):.2f}")
print(f"Latency: {np.mean(latencies):.2f} +/- {np.std(latencies):.2f}")
print(f"Fairness: {np.mean(fairnesses):.4f} +/- {np.std(fairnesses):.4f}")
=======
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

env = SchedulingEnv(
    num_ues=15
)

model = DQN.load(
    "models/dqn_no_target"
)

num_episodes = 100

throughputs = []
latencies = []
fairnesses = []

for ep in range(num_episodes):

    obs, _ = env.reset()

    done = False

    episode_throughput = 0
    episode_latency = 0

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

        done = (
            terminated
            or truncated
        )

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

print(
    "\nNo Target Network DQN Results"
)

print("-" * 35)

print(
    f"Throughput: "
    f"{np.mean(throughputs):.2f} "
    f"+/- {np.std(throughputs):.2f}"
)

print(
    f"Latency: "
    f"{np.mean(latencies):.2f} "
    f"+/- {np.std(latencies):.2f}"
)

print(
    f"Fairness: "
    f"{np.mean(fairnesses):.4f} "
    f"+/- {np.std(fairnesses):.4f}"
)
>>>>>>> 3efb62cc42d40ab31e21f35c14e571dc9584c2ec
