<<<<<<< HEAD
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor

from envs.scheduling_env import SchedulingEnv

# Create environment
env = SchedulingEnv()

# Add monitor for logging rewards
env = Monitor(env, filename="ppo_training_log")

# Create PPO model
model = PPO(
    "MlpPolicy",
    env,
    learning_rate=3e-4,
    gamma=0.99,
    verbose=1
)

# Train for 50,000 steps
model.learn(total_timesteps=50000)

# Save model
model.save("models/ppo_50k")

=======
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor

from envs.scheduling_env import SchedulingEnv

# Create environment
env = SchedulingEnv()

# Add monitor for logging rewards
env = Monitor(env, filename="ppo_training_log")

# Create PPO model
model = PPO(
    "MlpPolicy",
    env,
    learning_rate=3e-4,
    gamma=0.99,
    verbose=1
)

# Train for 50,000 steps
model.learn(total_timesteps=50000)

# Save model
model.save("models/ppo_50k")

>>>>>>> 3efb62cc42d40ab31e21f35c14e571dc9584c2ec
print("PPO training complete!")