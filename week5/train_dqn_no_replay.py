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

from stable_baselines3 import DQN
from stable_baselines3.common.monitor import Monitor

from envs.scheduling_env import SchedulingEnv


# Create environment with 15 UEs
env = SchedulingEnv(
    num_ues=15
)

# Add monitor for logging rewards
env = Monitor(
    env,
    filename="training_log_no_replay"
)

# Create DQN model WITHOUT replay buffer
model = DQN(
    "MlpPolicy",
    env,
    learning_rate=1e-4,
    gamma=0.99,
    buffer_size=1,
    verbose=1
)

# Train for 10,000 steps
model.learn(
    total_timesteps=10000
)

# Save model
model.save(
    "models/dqn_no_replay"
)

print("\nTraining complete!")
print("Model saved as: models/dqn_no_replay.zip")