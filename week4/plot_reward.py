<<<<<<< HEAD
import os
import pandas as pd
import matplotlib.pyplot as plt

# ✅ create folder automatically
os.makedirs("results", exist_ok=True)

df = pd.read_csv("../results/training_log.monitor.csv", skiprows=1)

plt.figure(figsize=(8, 5))
plt.plot(df["r"])

plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("DQN Training Reward Curve")
plt.grid(True)

plt.savefig("results/reward_curve.png", dpi=300)

plt.show()
=======
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
>>>>>>> 3efb62cc42d40ab31e21f35c14e571dc9584c2ec
