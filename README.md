# shortest_path_to_prison_gate
Find shortest path to prison gate in each cell for a given nxm matrix.

# Problem Statement:
For any given nxm matrix:
- Each '0' represents empty cells
- Each '-1' represents a wall 
- Each '-2' represents a gate

For each prison cell calculate shortest distance to a gate. One can't pass through a wall ('-1').

Examples:
```
Input:
[
    [0 -1 -2]
    [0  0  0]
]
Output:
[
    [4 -1 -2]
    [3  2  1]
]
```
```
Input:
[
    [0, 0, 0, -1, -2],
    [0, 0, 0,  0,  0],
    [-2, 0, 0,  0,  0],
]
Output:
[
    [2, 3, 4, -1, -2],
    [1, 2, 3, 2, 1],
    [-2, 1, 2, 3, 2]
]
```
# Solution:
- Implemet bfs algorithm to explore prison
- Inrease depth in each iteration
- Don't pass through walls
- Don't pass over matrix boundry
- Terminate and return depth when a gate is reached.