#!/bin/bash

if [ "$#" -eq 0 ]; then
    python solve_maze.py -config_file config.yaml
else
    python solve_maze.py -config_file config.yaml ALGORITHM.NAME $1 MAZE.SIZE $2
fi
