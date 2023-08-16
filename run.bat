@echo off
IF "%~1"=="" (
    python solve_maze.py -config_file config.yaml
) ELSE (
    python solve_maze.py -config_file config.yaml ALGORITHM.NAME %1 MAZE.SIZE %2
)
