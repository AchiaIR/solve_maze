from setuptools import setup, find_packages

setup(
    name='solve_maze',
    version='0.1',
    author='AchiaIR',
    author_email='achia.rosin19@gmail.com',
    description='A maze solver using Reinforcement Learning methods',
    packages=find_packages(),
    install_requires=[
        'gym',
        'tqdm',
        'numpy',
        'gdown',
        'pygame',
        'pyglet',
        'IPython',
        'imageio',
        'matplotlib',
        'yacs >= 0.1.8',
        'imageio-ffmpeg',
        'imageio == 2.9.0',
    ],
    package_data={
        'algorithms': ['model_based/*.py', 'model_based/__init__.py',
                       'model_free/*.py', 'model_free/__init__.py', '*.py'],
        'environement': ['*py'],
        'configs': ['*.py'],
        'maze_mid': ['*.py', '*.npy'],
        'utils': ['*.py'],
    },
    data_files=[
        ('', ['solve_maze.py']),
    ],
    entry_points={
        'console_scripts': [
            'solve_maze=solve_maze:main',
        ],
    },
)
