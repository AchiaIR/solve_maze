<div align="center">
    <h1>Solve Maze with Reinforcement Learning</h1>
<img src="https://github.com/AchiaIR/solve_maze/blob/master/solvemazeexample.gif" width="500" height="500" />
</div>



<h2>About The Project</h2>
This project is all about exploring Reinforcement Learning (RL) basic algorithms. We use mazes of different sizes as our playground to see how different RL techniques can find their way out. 

Each RL technique we employ offers a unique approach:

* **Policy Iteration:** A deterministic method, Policy Iteration evaluates and improves a policy until it's optimal. It systematically finds the best action for every position in the maze, ensuring a direct path to the solution.
* **Monte Carlo:** Based on experience, the Monte Carlo method learns from complete episodes. It's like letting a person wander through the entire maze multiple times, learning a little more from each adventure.
* **Q-learning:** A model-free algorithm, Q-learning learns by trial and error. It gauges the value of an action in a particular state and refines its strategy over time, making it adaptable and dynamic.
* **SARSA:** Standing for State-Action-Reward-State-Action, SARSA learns by updating the value of the just-taken action based on the current reward and the value of the next possible action. It's more cautious than Q-learning, always thinking one step ahead.

<h2>Overview</h2>
We make use of 4 algorithms: Policy Iteration (Dynamic Programming), Monte-Carlo, Q-Learning (Temporal Difference Method) and SARSA (Temporal Difference Method). 
Policy Iteration is a model based method and the others: Monte-Carlo, Q-Learning and SARSA, are model-free algorithms. 
we applied these algorithms on a 5x5, 15x15 and 25x25 stochastic maze boards.
A deterministic maze is where the outcome an action is certain and predictable.
A stochastic maze, on the other hand, is a maze where the outcome of an action
is uncertain, if the agent takes a certain action in a certain state, it may lead to
different states depending on random factors. Solving a deterministic maze is
generally easier than solving a stochastic maze because the agent can rely on its
past experience to make decisions. However, stochastic mazes are more realistic
and can better represent real-world problems, where the outcome of actions is
often uncertain.
A very detailed explain (including the math) is in solve_maz.pdf attached.

<h2>Project Content Description</h2>
<h3>Python Content Description</h3>

* **algorithms:** A folder contains the implementation of the RL algorithms, divided to 2 folders: 
    - model based
    - model free
* **configs:** A folder contains the files to do with the maze and algorithms configurations.
* **environement:** A folder contains the files define the stochastic environement - an environemnet where there is a random aspect in choosing an action.
* **maze_mid:** A folder contains the maze definitions, with the different sizes
* **utils:** A folder contains the display file, and the file that gets the maze_mid folder (to use once)
* **solve_maze.py:** The main file - the file which runs the project
* **setup.py:** the file to use in installation

<h3>Other supporting Content Description</h3>

* **comfig.yaml:** A file that defines the configuration to use
* **requirements.txt:** A file that defines the libraris to install for running the project
* **run.bat:** A file which runs the project from command  - windows
* **run.sh:** A file which runs the project from command  - linux / mac

<h2>Getting Started</h2>

