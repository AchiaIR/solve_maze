
import sys
import argparse
from configs import cfg
from utils.get_maze import *
from environement.stochastic_environement import *
from algorithms.model_free.sarsa_algorithm import SARSA
from utils.display_utils import embed_mp4, DisplayVideo
from algorithms.model_free.q_learning_algorithm import QLearning
from algorithms.model_free.monte_carlo_algorithm import MonteCarlo
from algorithms.model_based.policy_iteration_algorithm import PolicyIteration
# get_maze() - change path in cust_maze.py (see utils/get_maze.py) if you use it
from maze_mid.cust_maze import MazeEnvCast5x5, MazeEnvCast15x15, MazeEnvCast25x25

##############################################################
# the main file - run the chosen Algorithm to solve the maze #
##############################################################

env_dict = {
    5: StochasticEnv(MazeEnvCast5x5()),
    15: StochasticEnv(MazeEnvCast15x15()),
    25: StochasticEnv(MazeEnvCast25x25()),
}

algo_dict = {
    'PolicyIteration': (PolicyIteration, True),
    'MonteCarlo': (MonteCarlo, False),
    'QLearning': (QLearning, False),
    'SARSA': (SARSA, False),
}


def parse_args():
    # create parser
    parser = argparse.ArgumentParser(description='Solve Maze')
    # add the cfg file as an argument
    parser.add_argument("-config_file", default="config.yaml", help="path to config file", type=str)
    # parse arguments
    # args = parser.parse_args()
    args, unknown = parser.parse_known_args()
    # override default configurations
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(unknown)
    cfg.freeze()

    return args


def SetEnv(maze_configs):
    global env
    if 'env' in globals():
        env.close()
    env = env_dict.get(maze_configs.SIZE)
    if env is None:
        raise ValueError("Invalid maze size")
    return env


def SetAlgorithm(algorithm_configs, env):
    algo_value = algo_dict.get(algorithm_configs.NAME)
    if algo_value is None:
        print(f"Algorithm name from config: {algorithm_configs.NAME}")
        raise ValueError("Invalid algorithm name")
    AlgoClass, is_model_based = algo_value
    algo = AlgoClass(env)
    algo.train()
    return algo, is_model_based


def main():
    args = parse_args()
    env = SetEnv(cfg.MAZE)
    algo, is_model_based = SetAlgorithm(cfg.ALGORITHM, env)
    DisplayVideo(algo, env, f'{cfg.ALGORITHM.NAME}_{cfg.MAZE.SIZE}x{cfg.MAZE.SIZE}', is_model_based)


if __name__ == "__main__":
    main()