"""
Model Based Methods - Requires a complete model of the environment,
including the transition probabilities and rewards to solve the problem.
in this case: Policy Iteration Algorithm using Dynamic Programming.
"""

import numpy as np
from tqdm import tqdm


class PolicyIteration():

  def __init__(self, env, num_episodes=100, gamma=0.9, theta=1e-12):
    super().__init__()
    self.env = env
    self.num_episodes = num_episodes
    self.gamma = gamma
    self.theta = theta
    self.π = self.env.π
    self.P = self.env.P
    self.R = self.env.R
    self.values = self.env.values
    self.delta = 0

  def policy_evaluation(self):
    delta = 0
    for state in self.P.keys():
      if state[0] == 4 and state[1] == 4:
        self.values[state] = 0
      else:
        v = 0
        for actual_act in self.P[state][self.π[state]]:
          v += actual_act[0] * (self.R[actual_act[1]] + self.gamma * self.values[actual_act[1]])
        delta = max(delta, abs(v - self.values[state]))
        self.values[state] = v
    return delta

  def policy_improvement(self):
    for state in self.P.keys():
      v_max = 0
      for chosen_act in self.P[state].keys():
        v = 0
        for actual_act in self.P[state][chosen_act]:
          # get the reward of the next state + gamma * the value of the next state
          # for each actual action in the transion model
          v += actual_act[0] * (self.R[actual_act[1]] + self.gamma * self.values[actual_act[1]])
        if v > v_max:
          v_max = v
          self.π[state] = chosen_act

  def train(self):
    evals = []
    for i in tqdm(range(self.num_episodes)):
      cur_policy = np.copy(self.π)
      self.delta = self.policy_evaluation()
      num_eval = 1
      while self.theta < self.delta:
        self.delta = self.policy_evaluation()
        num_eval += 1
      self.policy_improvement()
      evals.append(num_eval)
      print(f'\n number of evaluations for episod {i}: {num_eval}')
      # if there's no change in the policy - stop training
      if np.array_equal(cur_policy, self.π):
        break
    return evals

