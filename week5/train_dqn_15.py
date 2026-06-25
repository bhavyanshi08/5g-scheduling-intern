import sys
import os

<<<<<<< HEAD
# Add project root to path
=======
>>>>>>> 3efb62cc42d40ab31e21f35c14e571dc9584c2ec
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
<<<<<<< HEAD
from envs.scheduling_env import SchedulingEnv

# -----------------------------
# Environment
# -----------------------------
env = SchedulingEnv(num_ues=15)

# Add logging wrapper
env = Monitor(env, filename="training_log_15ue")

# -----------------------------
# Model
# -----------------------------
=======

from envs.scheduling_env import SchedulingEnv


# Create environment with 15 UEs
env = SchedulingEnv(
    num_ues=15
)

# Add monitor for logging rewards
env = Monitor(
    env,
    filename="training_log_15ue"
)

# Create DQN model
>>>>>>> 3efb62cc42d40ab31e21f35c14e571dc9584c2ec
model = DQN(
    "MlpPolicy",
    env,
    learning_rate=1e-4,
    gamma=0.99,
    verbose=1
)

<<<<<<< HEAD
# -----------------------------
# Training
# -----------------------------
model.learn(total_timesteps=50000)

# -----------------------------
# Save model
# -----------------------------
os.makedirs("models", exist_ok=True)

model.save("models/dqn_15ue")
=======
# Train for 50,000 steps
model.learn(
    total_timesteps=50000
)

# Save model
model.save(
    "models/dqn_15ue"
)
>>>>>>> 3efb62cc42d40ab31e21f35c14e571dc9584c2ec

print("\nTraining complete!")
print("Model saved as: models/dqn_15ue.zip")