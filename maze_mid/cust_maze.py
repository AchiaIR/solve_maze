from maze_mid.maze_env import MazeEnv

class MazeEnvCast5x5(MazeEnv):
    def __init__(self, enable_render=True):
        super(MazeEnvCast5x5, self).__init__(maze_file="maze_mid/maze2d_5x5.npy", enable_render=enable_render)

class MazeEnvCast15x15(MazeEnv):
    def __init__(self, enable_render=True):
        super(MazeEnvCast15x15, self).__init__(maze_file="maze_mid/maze2d_15x15.npy", enable_render=enable_render)

class MazeEnvCast25x25(MazeEnv):
    def __init__(self, enable_render=True):
        super(MazeEnvCast25x25, self).__init__(maze_file="maze_mid/maze2d_25x25.npy", enable_render=enable_render)

class MazeEnvCast30x30(MazeEnv):
    def __init__(self, enable_render=True):
        super(MazeEnvCast30x30, self).__init__(maze_file="maze_mid/maze2d_30x30.npy", enable_render=enable_render)
