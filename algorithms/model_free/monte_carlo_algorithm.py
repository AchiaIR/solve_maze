"""
Model Free Methods - Do Not Require a complete model of the environment,
in this case: Monte Carlo Algorithm.
"""

import numpy as np
from tqdm import tqdm



class MonteCarlo():

  def __init__(self, env, num_episodes=500, num_steps=500, epsilon=0.99, decay=0.99, gamma=0.9, alpha=0.9):
    super().__init__()
    self.env = env
    self.num_episodes = num_episodes
    self.num_steps = num_steps
    self.epsilon = epsilon
    self.decay_rate = decay
    self.gamma = gamma
    self.alpha = alpha
    self.R = self.env.R
    self.Q = np.zeros((env.maze_size[0], env.maze_size[1], env.action_space.n))
    # number of visits for each state-action pair
    self.N = np.zeros((env.maze_size[0], env.maze_size[1], env.action_space.n))
    self.env.reset()

  def epsilon_greedy_policy(self, state):
    # Choose a random action with probability epsilon,
    # otherwise choose the action with the highest Q-value
    if np.random.rand() < self.epsilon:
      return self.env.action_space.sample()
    else:
      return np.argmax(self.Q[state])

  def update_Q(self, states_actions_rewards):
    # Update Q-values using the Monte Carlo update rule
    G = 0
    for s, a, r in reversed(states_actions_rewards):
      G = r + G * self.gamma
      self.N[s[0]][s[1]][a] += 1
      self.Q[s[0]][s[1]][a] += self.alpha * (G - self.Q[s[0]][s[1]][a]) / self.N[s[0]][s[1]][a]

  def train(self):
    rewards = []
    for i in tqdm(range(self.num_episodes)):
      if i == self.num_episodes / 2:
        self.QhalfWay = self.Q.copy()
      self.epsilon = self.epsilon * self.decay_rate if self.epsilon * self.decay_rate > 0.05 else 0.05
      state = self.env.reset()
      if i % 20 != 0:
        state = self.env.set_random_state()
      states_actions_rewards = []
      done = False
      episode_reward = 0
      step = 0
      while not done and step < self.num_steps:
        # Choose an action according to the epsilon-greedy policy
        action = self.epsilon_greedy_policy(tuple(np.int32(state)))
        next_state, reward, done, _ = self.env.step(action)
        states_actions_rewards.append((tuple(np.int32(state)), action, reward))
        episode_reward += reward
        state = next_state.copy()
        step += 1
      self.update_Q(states_actions_rewards)
      if i % 20 == 0:
        # print(f"Episode {i}, total reward: {episode_reward}")
        rewards.append(episode_reward)
    return rewards
