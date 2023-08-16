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

