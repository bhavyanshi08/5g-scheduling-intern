import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make("CartPole-v1")


BINS = [10, 10, 10, 10]


STATE_BOUNDS = list(zip(
    env.observation_space.low,
    env.observation_space.high
))

STATE_BOUNDS[1] = (-4, 4)
STATE_BOUNDS[3] = (-4, 4)


q_table = np.zeros(BINS + [env.action_space.n])

alpha = 0.1
gamma = 0.99
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01

episodes = 500

rewards = []


def discretize_state(state):
    discrete_state = []

    for i in range(len(state)):
        low, high = STATE_BOUNDS[i]

        value = state[i]

        ratio = (value - low) / (high - low)

        new_value = int(ratio * BINS[i])

        new_value = min(BINS[i] - 1, max(0, new_value))

        discrete_state.append(new_value)

    return tuple(discrete_state)


for episode in range(episodes):

    state, _ = env.reset()
    state = discretize_state(state)

    total_reward = 0
    done = False

    while not done:

        if np.random.random() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])

        next_state, reward, terminated, truncated, _ = env.step(action)

        done = terminated or truncated

        next_state = discretize_state(next_state)

        best_next = np.max(q_table[next_state])

        q_table[state][action] += alpha * (
            reward +
            gamma * best_next -
            q_table[state][action]
        )

        state = next_state
        total_reward += reward

    epsilon = max(epsilon_min, epsilon * epsilon_decay)

    rewards.append(total_reward)

    if (episode + 1) % 50 == 0:
        avg_reward = np.mean(rewards[-50:])
        print(
            f"Episode {episode+1}: Avg Reward (last 50 episodes) = {avg_reward:.2f}"
        )

env.close()

window = 20
moving_avg = np.convolve(
    rewards,
    np.ones(window) / window,
    mode='valid'
)

plt.figure(figsize=(8, 5))
plt.plot(moving_avg)

plt.xlabel("Episode")
plt.ylabel("Average Reward")
plt.title("Q-Learning on CartPole (20-Episode Moving Average)")
plt.grid(True)

plt.savefig("reward_curve.png")
plt.show()