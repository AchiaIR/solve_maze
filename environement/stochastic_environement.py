"""
Create Stochastic environement, which means that when the agent takes a certain action
there is a probability of 0.9 that the environment will allow him to reach the state he intended to reach,
but there is also a probability of 0.1 that he will move to another direction.
"""

import gym
import random
import numpy as np

# Numbers to action mapping
ActionIndex = {0:("UP","N", (0, -1)),
              1:("DOWN","S", (0, 1)),
              2:("RIGHT","E", (1, 0)),
              3:("LEFT","W",(-1, 0))}

# Reward to add artificially to Env
NEG_REWARD = -0.2
POS_REWARD = 0.01

# The reward to start with over the board
START_REWARD = 0.1

# The probability of stochastic env
STOC_PROB = 0.9


class StochasticEnv(gym.Env):

  def __init__(self, env):
    super().__init__()
    self.env = env
    self.maze_size = self.env.maze_size
    self.action_space = self.env.action_space
    self.num_states = self.maze_size[0] * self.maze_size[1]
    self.terminal_state = (self.maze_size[0]-1, self.maze_size[1]-1)
    self.actions = np.arange(self.action_space.n)
    self.maze_map = self.env.unwrapped.maze_view.maze.maze_cells
    self.R = np.ones_like(self.maze_map ,dtype=float) * -(START_REWARD / self.num_states)
    self.R[self.terminal_state] = 1
    self.P = {(i,j): {action : [] for action in self.actions}
              for j in range(self.maze_size[1])
              for i in range(self.maze_size[0])}
    self.π = np.zeros((self.maze_size[0], self.maze_size[1]))
    self.values = np.zeros((self.maze_size[0], self.maze_size[1]))
    self.p = STOC_PROB
    self.transition_model()

  def reset(self):
    return self.env.reset()

  def render(self, mode='rgb_array'):
    return self.env.render(mode)

  def observation_space(self):
    return self.env.observation_space

  def action_space(self):
    return self.env.action_space

  def get_reward(self, state):
    return self.R[tuple(np.int32(state))]

  def step(self, action):
    probs = [(1 - self.p) / 3 for i in range(4)]
    probs[np.int32(action)] = self.p
    actions = [i for i in range(4)]
    action = random.choices(actions, probs)[0]
    obs, _, done, info = self.env.step(action)
    # use the reward we defined
    return obs, self.get_reward(obs), done, info

  def get_available_actions(self, state):
    available_actions = []
    for action in self.actions:
      action_letter = ActionIndex[action][1]
      legit = self.env.unwrapped.maze_view.maze.is_open(state,action_letter)
      if legit:
        available_actions.append(action)
    return available_actions

  def set_random_state(self):
    return random.randint(0, self.maze_size[0]-1), random.randint(0, self.maze_size[1]-1)

  def transition_model(self):
    """update the transition model
    according to the stochastic environement """
    for state in self.P.keys():
      # Get the available actions.
      a_actions = self.get_available_actions(tuple(np.int32(state)))
      next_states = []
      for chosen_action in self.actions:
        # The action the agent actually takes.
        for actual_action in self.actions:
          # Find out if youre staying in place or actually moving.
          next_state = tuple(np.add(state, ActionIndex[actual_action][2])) if actual_action in a_actions else state
          # Append the transition model.
          done = 1 if next_state == self.terminal_state else 0
          if actual_action == chosen_action:
            self.P[state][chosen_action].append([self.p, next_state, self.R[next_state], done])
          else:
            self.P[state][chosen_action].append([(1 - self.p) / 3, next_state, self.R[next_state], done])

  def AddReward(self, state_neg, state_pos):
    self.R[state_neg] = float(NEG_REWARD)
    self.R[state_pos] = float(POS_REWARD)
