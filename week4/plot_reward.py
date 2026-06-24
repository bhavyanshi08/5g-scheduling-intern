import pandas as pd
import matplotlib.pyplot as plt

# Read monitor file
df = pd.read_csv("training_log.monitor.csv", skiprows=1)

# Plot rewards
plt.figure(figsize=(8, 5))
plt.plot(df["r"], marker='o')
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("DQN Training Reward Curve")
plt.grid(True)

# Save figure
plt.savefig("results/reward_curve.png", dpi=300)

plt.show()

print("Reward curve saved!")