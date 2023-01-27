# 8-Puzzle-Solver-using-BFS-Algorithm

## Project Description

An instance of the 8-puzzle game consists of a board holding 8 distinct movable tiles ans empty space. For such a board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it. In this project, we are given an initial state of the puzzle, the search problem is to find a sequence of moves that transitions this state to the goal state; that is, the configuration with all tiles arranged in ascending order 0,1,2,3,4,5,6,7,8  or 8,7,6,5,4,3,2,1,0 or anyother user defined goal state.

## Objective

Use the Breadth First Search (BFS) Algorithm to solve the 8 puzzle. The slider should swap the empty space with a number to create a unique state. We need to make sure that no state is repeated so as to avoid infinite looping. 

* **Breadth First Search (BFS)** : It is a traversing algorithm where you should start traversing from a selected node (source or starting node) and traverse the graph layerwise thus exploring the neighbour nodes (nodes which are directly connected to source node).
* **Distance Metric** : Again, an abstract module to allow re-use, it includes the required distance metric that is Manhattan distance. Here Manhattan Distance is used because the slider either moves up, down, right or left for about one unit and not more than that. It also won't slide in any other angles directions i.e; diagonally.
* **Unique State Checker** : We implement a set data structure to store all existing states. We will write an algorithm such that every unique state that is being entered into the set will be compared to all other existing states to avoid repitition.

## Contents

## Instructions for Usage

1. Clone the repository

```
git clone https://github.com/bharadwaj-chukkala/8-Puzzle-Solver-using-BFS-Algorithm.git
```

2. Install Python 3.9 and the libraries mentinoned below prior to running the code
3. Go to the root directory from your IDE.
4. Please mention the path to the datasets wherever necessary.
5. Run the `Solver.py` file as it is.
6. `Nodes.txt` will contain all possible states
7. `nodePath.txt` will contain the generated path to the goal from initial state
8. `NodesInfo.txt` will contain the information about child states, parent states and **cost2come**
9. Note: if dataset and results are not given, please paste the py file in the folder where dataset is present and also create a results folder in the directory where you run the code.

### Dependencies

* NumPy
* argparse

## Results
I have defined the initial state and goal state as follows:
<table style="width:50%">
    <tr>
        <td align="center"> Initial State </td>
        <td align="center"> ➡️</td>
        <td align="center"> Goal State</td>
    <tr>
        <td>
            <table style="width:80%" align="center">
            <tr>
            <td>8</td> <td> </td> <td>6</td>
            </tr>
            <tr>
                <td>5</td> <td>4</td> <td>7</td>
            </tr>
            <tr>
                <td>2</td> <td>3</td> <td>1</td>
            </tr>
            </table>
        </td>
        <td align="center"> should <br> change to </td>
        <td>
            <table style="width:80%" align="center">
            <tr>
            <td>1</td> <td>2</td> <td>3</td>
            </tr>
            <tr>
                <td>4</td> <td>5</td> <td>6</td>
            </tr>
            <tr>
                <td>7</td> <td>8</td> <td></td>
            </tr>
            </table>
        </td>
</table>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Bharadwaj Chukkala** `<br>`
UID: 118341705 `<br>`
Bharadwaj Chukkala is currently a Master's student in Robotics at the University of Maryland, College Park, MD (Batch of 2023). His interests include Machine Learning, Perception and Path Planning for Autonomous Robots.`<br>`
[![Contact](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](bchukkal@umd.edu)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bharadwaj-chukkala/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bharadwaj-chukkala)
