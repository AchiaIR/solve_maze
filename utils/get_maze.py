"""
if you need to create the folder maze_mid
yourself uncomment this func in solve_maze.py
and run it with it, then change the path in
maze_cust.py to maze_mid/maze5x5 etc
"""

import os
import gdown
import zipfile


def get_maze():
    # Specify the URL and output file
    url = 'https://drive.google.com/uc?id=1FeuIx5OVLmfCx0dxxwU-7Xn8gpPc-53D'
    output = 'maze_mid.zip'
    dir_path = 'maze_mid'

    # Only download and extract the file if it hasn't been done already
    if not os.path.isdir(dir_path):
        gdown.download(url, output, quiet=False)

        with zipfile.ZipFile(output, 'r') as zip_ref:
            zip_ref.extractall()
