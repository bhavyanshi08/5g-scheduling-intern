import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from stable_baselines3 import DQN
from stable_baselines3.common.monitor import Monitor
from envs.scheduling_env import SchedulingEnv

# ✅ absolute path (important)
results_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "results"))
os.makedirs(results_path, exist_ok=True)

env = SchedulingEnv()

# ✅ give filename prefix
env = Monitor(env, os.path.join(results_path, "training_log"))

model = DQN("MlpPolicy", env, verbose=1)

print("Starting Training...")
model.learn(total_timesteps=5000)

model.save("scheduler_dqn")

print("Training Complete!")