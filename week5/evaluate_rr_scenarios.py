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

print("\nRR Scenario Evaluation")
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

        current_ue = 0

        while not done:

            action = current_ue
            current_ue = (
                current_ue + 1
            ) % env.num_ues

            obs, reward, terminated, truncated, info = env.step(
                action
            )

            done = (
                terminated
                or truncated
            )

            episode_throughput += info.get("avg_throughput", 0)
            episode_latency += info.get("latency", 0)

            allocations += np.array(info.get("allocations", np.zeros(env.num_ues)))
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

print("\nRR Scenario Evaluation")
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

        current_ue = 0

        while not done:

            action = current_ue
            current_ue = (
                current_ue + 1
            ) % env.num_ues

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