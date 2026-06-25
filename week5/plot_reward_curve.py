import argparse
import os

import pandas as pd
import matplotlib.pyplot as plt


def find_log_file(log_file: str | None, base_dir: str) -> str:
    candidates = [
        "training_log_15ue.monitor.csv",
        "training_log_30ue.monitor.csv",
        "training_log_no_replay.monitor.csv",
        "training_log_no_target.monitor.csv",
        "training_log_simple_reward.monitor.csv",
    ]

    if log_file:
        if os.path.isabs(log_file):
            return log_file
        return os.path.join(base_dir, log_file)

    for candidate in candidates:
        path = os.path.join(base_dir, candidate)
        if os.path.exists(path):
            return path

    raise FileNotFoundError(
        "Could not find a training log file. "
        "Place one of the expected CSV files in the script directory or pass --log <filename>."
    )


script_dir = os.path.dirname(os.path.abspath(__file__))
parser = argparse.ArgumentParser(description="Plot DQN reward curve from a training log CSV.")
parser.add_argument("--log", help="Relative or absolute path to the training log CSV file.")
args = parser.parse_args()

log_path = find_log_file(args.log, script_dir)
os.makedirs(os.path.join(script_dir, "results"), exist_ok=True)


df = pd.read_csv(log_path, skiprows=1)


df["smoothed"] = df["r"].rolling(
    window=5,
    min_periods=1
).mean()


plt.figure(figsize=(8, 5))

plt.plot(
    df.index,
    df["r"],
    alpha=0.3,
    label="Raw Reward"
)

plt.plot(
    df.index,
    df["smoothed"],
    linewidth=3,
    label="Moving Average"
)

plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("DQN Reward Convergence")
plt.legend()
plt.grid(True)


plt.savefig(
    "results/reward_curve_smoothed.png",
    dpi=300,
    bbox_inches="tight"
)

print("Saved: results/reward_curve_smoothed.png")

plt.show()