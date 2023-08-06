"""
Model Free Methods - Do Not Require a complete model of the environment,
in this case: SARSA Algorithm.
"""

import random
import numpy as np
from tqdm import tqdm


class SARSA():

  def __init__(self, env, num_episodes=500, num_steps=500, epsilon=0.99, decay=0.99, gamma=0.99, alpha=0.9):
    super().__init__()
    self.env = env
    self.num_episodes = num_episodes
    self.num_steps = num_steps
    self.epsilon = epsilon
    self.decay_rate = decay
    self.gamma = gamma
    self.alpha = alpha
    self.Q = np.zeros((env.maze_size[0], env.maze_size[1], env.action_space.n))

  def select_act(self, state):
    # Choose a random action with probability epsilon,
    # otherwise choose the action with the highest Q-value
    if random.random() < self.epsilon:
      return self.env.action_space.sample()
    else:
      return np.argmax(self.Q[state])

  def update_Q(self, next_state, state, action, next_action, reward):
    self.Q[state][action] += self.alpha * (reward + self.gamma * self.Q[next_state][next_action] - self.Q[state][action])

  def train(self, episodes=500, max_steps=500):
    rewards = []
    for i in tqdm(range(episodes)):
      if i == self.num_episodes / 2:
        self.QhalfWay = self.Q.copy()
      self.epsilon *= self.decay_rate
      state = self.env.reset()
      done = False
      episode_reward = 0
      step = 0
      while not done and step < max_steps:
        # Choose an action according to the epsilon-greedy policy
        action = self.select_act(tuple(np.int32(state)))
        next_state, reward, done, _ = self.env.step(action)
        next_action = self.select_act(tuple(np.int32(next_state)))
        self.update_Q(tuple(np.int32(next_state)), tuple(np.int32(state)), action, next_action, reward)
        episode_reward += reward
        state = next_state.copy()
        step += 1
      if i % 20 == 0:
        rewards.append(episode_reward)
        # print(f"Episode {i}, total reward: {episode_reward}")
    return rewards
