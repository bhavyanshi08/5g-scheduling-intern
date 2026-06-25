import numpy as np
from envs.scheduling_env import SchedulingEnv

<<<<<<< HEAD
print("🚀 RR Evaluation Started...")

env = SchedulingEnv()

num_episodes = 5
=======
env = SchedulingEnv()

num_episodes = 100
>>>>>>> 3efb62cc42d40ab31e21f35c14e571dc9584c2ec

throughputs = []
latencies = []
fairnesses = []

for ep in range(num_episodes):

<<<<<<< HEAD
    print(f"\n👉 Starting Episode {ep+1}")

    obs = env.reset()
    if isinstance(obs, tuple):
        obs = obs[0]
=======
    obs, _ = env.reset()
>>>>>>> 3efb62cc42d40ab31e21f35c14e571dc9584c2ec

    done = False

    episode_throughput = 0
    episode_latency = 0

    allocations = np.zeros(env.num_ues)

    current_ue = 0

    while not done:

<<<<<<< HEAD
        action = current_ue
        current_ue = (current_ue + 1) % env.num_ues

        step_result = env.step(action)

        if len(step_result) == 5:
            obs, reward, terminated, truncated, info = step_result
            done = terminated or truncated
        else:
            obs, reward, done, info = step_result

        if isinstance(obs, tuple):
            obs = obs[0]

        episode_throughput += info.get("throughput", reward)
        episode_latency += info.get("latency", 0)

        if "allocations" in info:
            allocations += info["allocations"]

    fairness = (
        np.sum(allocations) ** 2
        /
        (len(allocations) * np.sum(allocations ** 2) + 1e-8)
=======
        # Round Robin action
        action = current_ue
        current_ue = (current_ue + 1) % env.num_ues

        obs, reward, terminated, truncated, info = env.step(action)

        done = terminated or truncated

        episode_throughput += info["throughput"]
        episode_latency += info["latency"]

        allocations += info["allocations"]

    # Jain's Fairness Index
    fairness = (
        np.sum(allocations) ** 2
        /
        (
            len(allocations)
            * np.sum(allocations ** 2)
            + 1e-8
        )
>>>>>>> 3efb62cc42d40ab31e21f35c14e571dc9584c2ec
    )

    throughputs.append(episode_throughput)
    latencies.append(episode_latency)
    fairnesses.append(fairness)

<<<<<<< HEAD
    print(f"✅ Episode {ep+1} done")

print("\n📊 RR Evaluation Results")
print("-" * 40)

print(f"Throughput: {np.mean(throughputs):.2f} +/- {np.std(throughputs):.2f}")
print(f"Latency: {np.mean(latencies):.2f} +/- {np.std(latencies):.2f}")
print(f"Fairness: {np.mean(fairnesses):.4f} +/- {np.std(fairnesses):.4f}")
=======
print("\nRR Evaluation Results")
print("-" * 30)

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
