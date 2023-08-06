from yacs.config import CfgNode as CN

############################################
# define default configuration for parsing #
############################################

defaultCFG = CN()

# Model Part
defaultCFG.ALGORITHM = CN()
defaultCFG.ALGORITHM.NAME = 'QLearning'
defaultCFG.ALGORITHM.NUM_EPISODS = 500
defaultCFG.ALGORITHM.NUM_STEPS = 500
defaultCFG.ALGORITHM.DISCOUNT_FACTOR = 0.9
defaultCFG.ALGORITHM.EPSILON_GREEDY = 0.99
defaultCFG.ALGORITHM.DECAY = 0.99
defaultCFG.ALGORITHM.ALPHA = 0.9
defaultCFG.ALGORITHM.THETA = 1e-12

# Maze Part
defaultCFG.MAZE = CN()
defaultCFG.MAZE.SIZE = 15



