import pandas as pd
import matplotlib.pyplot as plt

print("Loading CSV...")

df = pd.read_csv("baseline_kpis.csv")
df.columns = df.columns.str.strip()

print(df)

plt.switch_backend('TkAgg')

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].bar(df["Scheduler"], df["Average Allocations per UE"])
axes[0].set_title("Average Allocations per UE")
axes[0].tick_params(axis="x", rotation=15)

axes[1].bar(df["Scheduler"], df["Jain Fairness Index"])
axes[1].set_title("Jain Fairness Index")
axes[1].tick_params(axis="x", rotation=15)

plt.tight_layout()

plt.savefig("rr_vs_pf_comparison.png")
print("Saved image!")

plt.show()