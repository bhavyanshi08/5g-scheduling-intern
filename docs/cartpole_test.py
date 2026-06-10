import gymnasium as gym

env = gym.make("CartPole-v1")

obs, info = env.reset()

print("Observation:")
print(obs)

print("\nObservation Shape:")
print(env.observation_space)

print("\nAction Space:")
print(env.action_space)
