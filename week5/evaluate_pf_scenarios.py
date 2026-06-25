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
from envs.scheduling_env import SchedulingEnv

num_episodes = 100
scenarios = [5, 15, 30]

print("\nPF Scenario Evaluation")
print("=" * 50)

for users in scenarios:

    env = SchedulingEnv(num_ues=users)

    throughputs = []
    latencies = []
    fairnesses = []

    for ep in range(num_episodes):

        obs, _ = env.reset()

        done = False

        episode_throughput = 0
        episode_latency = 0

        allocations = np.zeros(env.num_ues)

        avg_throughput = np.ones(env.num_ues)

        while not done:

            pf_metric = []

            for ue in range(env.num_ues):

                try:
                    current_tp = obs[ue][1]
                except:
                    current_tp = 0

                metric = current_tp / (avg_throughput[ue] + 1e-8)
                pf_metric.append(metric)

            action = np.argmax(pf_metric)

            obs, reward, terminated, truncated, info = env.step(action)

            done = terminated or truncated

            episode_throughput += info.get("throughput", info.get("avg_throughput", 0))
            episode_latency += info.get("latency", info.get("delay", 0))

            allocations += np.array(info.get("allocations", np.zeros(env.num_ues)))

            tp = info.get("throughput", info.get("avg_throughput", 0))
            avg_throughput[action] = (
                0.9 * avg_throughput[action] + 0.1 * tp
            )

        fairness = (
            np.sum(allocations) ** 2
            / (len(allocations) * np.sum(allocations ** 2) + 1e-8)
        )

        throughputs.append(episode_throughput)
        latencies.append(episode_latency)
        fairnesses.append(fairness)

    print(f"\nScenario: {users} UEs")
    print("-" * 30)

    print(
        f"Throughput: {np.mean(throughputs):.2f} +/- {np.std(throughputs):.2f}"
    )

    print(
        f"Latency: {np.mean(latencies):.2f} +/- {np.std(latencies):.2f}"
    )

    print(
        f"Fairness: {np.mean(fairnesses):.4f} +/- {np.std(fairnesses):.4f}"
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
from envs.scheduling_env import SchedulingEnv

num_episodes = 100

scenarios = [5, 15, 30]

print("\nPF Scenario Evaluation")
print("=" * 50)

for users in scenarios:

    env = SchedulingEnv(num_ues=users)

    throughputs = []
    latencies = []
    fairnesses = []

    for ep in range(num_episodes):

        obs, _ = env.reset()

        done = False

        episode_throughput = 0
        episode_latency = 0

        allocations = np.zeros(env.num_ues)

        avg_throughput = np.ones(env.num_ues)

        while not done:

            pf_metric = []

            for ue in range(env.num_ues):

                current_tp = obs[ue][1]

                metric = (
                    current_tp
                    / avg_throughput[ue]
                )

                pf_metric.append(metric)

            action = np.argmax(
                pf_metric
            )

            obs, reward, terminated, truncated, info = env.step(
                action
            )

            done = (
                terminated
                or truncated
            )

            episode_throughput += info[
                "throughput"
            ]

            episode_latency += info[
                "latency"
            ]

            allocations += info[
                "allocations"
            ]

            avg_throughput[action] = (
                0.9
                * avg_throughput[action]
                + 0.1
                * info["throughput"]
            )

        fairness = (
            np.sum(allocations) ** 2
            /
            (
                len(allocations)
                * np.sum(
                    allocations ** 2
                )
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
        f"\nScenario: {users} UEs"
    )

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
>>>>>>> 3efb62cc42d40ab31e21f35c14e571dc9584c2ec
    )