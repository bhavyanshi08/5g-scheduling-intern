print("PROGRAM STARTED")
from scheduling_env import SchedulingEnv

env = SchedulingEnv(
    num_ues=5,
    max_steps=20
)

state, info = env.reset()

print("\nInitial State")
print("----------------")
print("UE | Buffer | SINR | QoS")

for i, ue in enumerate(state):
    print(
        f"{i}  | "
        f"{int(ue[0]):6} | "
        f"{int(ue[1]):4} | "
        f"{int(ue[2])}"
    )

print("\nRunning Random Agent...\n")

for step in range(10):

    action = env.action_space.sample()

    state, reward, terminated, truncated, info = env.step(action)

    print(
        f"Step {step+1}: "
        f"Selected UE {action} "
        f"Reward={reward:.2f}"
    )

    if terminated or truncated:
        break