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

from envs.scheduling_env_simple_reward import SchedulingEnv

env = SchedulingEnv(
    num_ues=15
)

env = Monitor(
    env,
    filename="training_log_simple_reward"
)

model = DQN(
    "MlpPolicy",
    env,
    learning_rate=1e-4,
    gamma=0.99,
    verbose=1
)

model.learn(
    total_timesteps=10000
)

model.save(
    "models/dqn_simple_reward"
)

print("\nTraining complete!")
print(
    "Model saved as: models/dqn_simple_reward.zip"
)