# SmartNavi
Campus navigation system to find the most optimal path for different locations.

**Overview**
SmartNavi is a Python tool that integrates algorithms for pathfinding and uses an adjacency list to store locations. The adjacency list contains nodes representing locations, which are then plotted onto a graph. Additionally, sub-nodes are implemented to account for valid paths and avoid obstacles such as walls.

The system includes a GUI with several buttons for selecting preferred algorithms, starting and ending nodes, and an option to use an alternative adjacency list containing only accessible locations. When accessibility is selected, the graph is redrawn and updated to reflect the new options. The final output displayed to the user includes the number of stops and the exact path taken.

Algorithm Recommendations:
- BFS: Generally Moderate - Chooses the path with the least amount of stops, but may not be optimal in terms of distance. (Unweighted)
- DFS: Generally Slower - Chooses the farest route but allows access to more scenery or buildings if needed by the user. (Unweighted)
- Dijkstra: Generally Faster - Chooses the most optimal route based on time or distance. (Weighted)

***Run Instructions***
```
Run Python File: python3 main_navi.py
```

***Requirements:***
- Python 3
- matplotlib
- networkx
- tkinter

![Capture](https://github.com/vuvictor1/SmartNavi/assets/78053016/31fb1419-5a82-4292-8a26-1e22d017f0ed)

https://github.com/vuvictor1/SmartNavi/assets/78053016/c3026fa9-3551-43e1-b750-85fc57fcd6bc

[For slides, click here](https://docs.google.com/presentation/d/12oPFUwbcshfpkaKLOAai2ng5_hDARwvK-RRWq237D0c/edit?usp=sharing)





