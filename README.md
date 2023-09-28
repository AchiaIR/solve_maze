<div align="center">
    <h1>Solve Maze with Reinforcement Learning</h1>
<img src="https://github.com/AchiaIR/solve_maze/blob/master/solvemazeexample.gif" width="500" height="500" />
</div>

## 🔴 Table of Contents

- <a href="#solve-maze-with-reinforcement-learning">Solve Maze with Reinforcement Learning</a>
- <a href="#about-the-project">About The Project</a>
- <a href="#overview">Overview</a>
- <a href="#project-content-description">Project Content Description</a>
  - <a href="#python-content-description">Python Content Description</a>
  - <a href="#other-supporting-content-description">Other Supporting Content Description</a>
- <a href="#getting-started">Getting Started</a>
  - <a href="#prerequisites">Prerequisites</a>
  - <a href="#installation">Installation</a>
    - <a href="#windows">Windows</a>
    - <a href="#linux-and-mac">Linux and Mac</a>
  - <a href="#usage">Usage</a>
    - <a href="#windows">Windows</a>
    - <a href="#linux-and-mac">Linux and Mac</a>
- <a href="#advanced-usage">Advanced Usage</a>
- <a href="#acknowledgments">Acknowledgments</a>

<span> ───────────────────────────────────────────── </span>

<a name="about-the-project"></a>
<h2> 🔴  About The Project </h2>

This project is all about exploring Reinforcement Learning (RL) basic algorithms. We use mazes of different sizes as our playground to see how different RL techniques can find their way out. 

Each RL technique we employ offers a unique approach:

* **Policy Iteration:** A deterministic method, Policy Iteration evaluates and improves a policy until it's optimal. It systematically finds the best action for every position in the maze, ensuring a direct path to the solution.
* **Monte Carlo:** Based on experience, the Monte Carlo method learns from complete episodes. It's like letting a person wander through the entire maze multiple times, learning a little more from each adventure.
* **Q-learning:** A model-free algorithm, Q-learning learns by trial and error. It gauges the value of an action in a particular state and refines its strategy over time, making it adaptable and dynamic.
* **SARSA:** Standing for State-Action-Reward-State-Action, SARSA learns by updating the value of the just-taken action based on the current reward and the value of the next possible action. It's more cautious than Q-learning, always thinking one step ahead.


<span> ───────────────────────────────────────────── </span>

<a name="overview"></a>
<h2> 🔴 Overview </h2>

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
A very detailed explain (including the math) is in solve_maze.pdf attached.

<span> ───────────────────────────────────────────── </span>

<a name="project-content-description"></a>
<h2> 🔴 Project Content Description </h2>

<a name="python-content-description"></a>
<h3> $\color{lime}{Python \ Content  \ Description}$ </h3>


* **algorithms:** A folder contains the implementation of the RL algorithms, divided to 2 folders: 
    - model based
    - model free
* **configs:** A folder contains the files to do with the maze and algorithms configurations.
* **environement:** A folder contains the files define the stochastic environement - an environemnet where there is a random aspect in choosing an action.
* **maze_mid:** A folder contains the maze definitions, with the different sizes
* **utils:** A folder contains the display file, and the file that gets the maze_mid folder (to use once)
* **solve_maze.py:** The main file - the file which runs the project
* **setup.py:** the file to use in installation

<a name="other-supporting-content-description"></a>
<h3>$\color{lime}{Other \ supporting \ Content \ Description}$</h3>

* **comfig.yaml:** A file that defines the configuration to use
* **requirements.txt:** A file that defines the libraris to install for running the project
* **run.bat:** A file which runs the project from command  - windows
* **run.sh:** A file which runs the project from command  - linux / mac

<span> ───────────────────────────────────────────── </span>

<a name="getting-started"></a>
<h2> 🔴 Getting Started </h2>

<a name="prerequisites"></a>
<h3>$\color{lime}{Prerequisites}$</h3>

* pytghon 3.x installed on your machine
* Pip (Python package installer)
* A video tool installed (for example vlc) 

<a name="installation"></a>
<h3>$\color{lime}{Installation}$</h3>

<a name="windows"></a>
* <h3>$\color{cyan}{Windows:}$</h3>

1. Clone this repository or download and extract the ZIP file:

   `git clone https://github.com/AchiaIR/solve_maze.git`

2. Navigate to the directory where you cloned or extracted the project:

   `cd solve_maze`
   
3. Install the necessary dependencies:

   `pip install -r requirements.txt`

   or:

   `pip install .`

   or:

   `python setup.py install` 

<a name="linux-and-mac"></a>   
* <h3>$\color{cyan}{Linux \ and \ Mac:}$</h3>

1. Clone this repository or download and extract the ZIP file:

   `git clone https://github.com/AchiaIR/solve_maze.git`

2. Navigate to the directory where you cloned or extracted the project:

   `cd solve_maze`
   
3. Install the necessary dependencies:

   `pip3 install -r requirements.txt`

   or:

   `pip3 install .`

   or:
   
   `pip3 install setuptools`
   
   `python3 setup.py install`

<a name="usage"></a>
<h3>$\color{lime}{Usage}$</h3>

<a name="windows"></a>
* <h3>$\color{cyan}{Windows:}$</h3>

Run the run.bat script:

`run`

you can also define the main parameters (algorithm and maze size), for example:

`run SARSA 25`

<a name="linux-and-mac"></a>
* <h3>$\color{cyan}{Linux \ and \ Mac:}$</h3>

1. Make the script executable (only need to do this once):

   `chmod +x ./run.sh`

2. Run the file.sh script:

   `./run.sh`

   you can also define the main parameters (algorithm and maze size), for example:

   `./run.sh SARSA 25`

<span> ───────────────────────────────────────────── </span>

<a name="advanced-usage"></a>
<h2> 🔴 Advanced Usage </h2>

The algorithms names to use in the command line are:

- PolicyIteration
- MonteCarlo
- QLearning
- SARSA
  
And the maze sizes are:

- 5
- 15
- 25

Each of those combinations is possible, but it won't always solve the maze. Since the algorithm has exploration part in it (Epsilon Greedy)
And the environement is Stochastic (has a random aspect) not each time you try - the maze will be solved properly.

If you want to explore the project further, you can control each parameter from the config.yaml file, 
then run it via cmd or on a python IDE such as pycharm. By each of the parameters in the yaml it mentioned 
if it's relevant for model free / model based / both. you can play with these parameteres and learn abouth the 
power of these algorithms. 

In addition there is an option to change the rewward manually, to encourage a better reward division for a better results.

Iv'e added the google colab notebook also to get better understanding of how to choose the best parameters.

<span> ───────────────────────────────────────────── </span>

<a name="acknowledgments"></a>
<h2> 🔴 Acknowledgments </h2>

Based on a project in Reinforcement Learning course, Reichman University

