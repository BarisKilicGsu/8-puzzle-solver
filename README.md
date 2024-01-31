# Sliding Puzzle Solver

This Python code contains an agent class developed to solve the sliding puzzle, a type of puzzle where tiles are rearranged in a matrix to achieve a sorted order. The code utilizes the A* algorithm to solve the puzzle effectively.

## Key Features:

- A* Algorithm: The code employs the A* search algorithm to compute the shortest path.
- Heuristic Function: A heuristic function based on Manhattan distance is used to estimate the number of steps.
- Priority Queue: A priority queue data structure assists in selecting the path with the lowest cost.
- Initial and Target Matrices: The initial and target states of the puzzle are represented through matrices.
- Solution Path: Upon solving the puzzle, a list of moves is obtained, indicating the order of tile movements.

## How to Use:

```python
from agent.agent import myAgent

# Define your initial matrix
tiles_grid = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

# Create an agent using the myAgent class
agent = myAgent(tiles_grid)

# Solve the puzzle
moves = agent.solve_puzzle()

# When a solution path is obtained, it shows the sequence of tile movements
print("Solution Path:", moves)

# View performance information of the agent
agent.print_info()

```

This code example begins by defining the initial matrix and creating an agent using the myAgent class. Then, the puzzle is solved using the solve_puzzle method, and a solution path is obtained. Additionally, you can use the print_info method to view performance details of the agent.

This code provides a foundation for automatically solving sliding puzzles. You can use it to customize and work on different puzzles.[Title](<../../dersler/yapay zela/skeleton/agent/agent.py>)