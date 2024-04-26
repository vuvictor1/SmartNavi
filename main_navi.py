"""********************************************************************************  
   Author Information:
   Victor Vu (vuvictor@csu.fullerton.edu)

   Other Authors: 

   Program Information:
   This File: main_navi.py
   Description: Manager for the SmartNavi GPS system. Calls BFS, DFS and Dijkstra's 
   Algorithm for pathfinding. Also incorporates GUI, utilizing a graph model.
********************************************************************************"""  
from algorithms import bfs_search # Import external function BFS
from algorithms import dfs_search # Import external function DFS
import gui # Call the GUI file

# Main function for execution
def main():
    # Placeholder locations (userinput later, will be included in Kiara's GUI) ------------------------- important!!!!
    start_location = "Library"
    goal_location = "Park"
    
    # Placeholder list (will need to rely on Robert's graph model) ---------------------------------------- important!!!!
    adjacency_list = {
    "Library": ["Student Center", "Parking Lot", "Cafeteria"],
    "Student Center": ["Library", "Cafeteria", "Theater"],
    "Cafeteria": ["Student Center", "Library", "Gym", "Computer Science Building"],
    "Gym": ["Cafeteria", "Theater"],
    "Theater": ["Student Center", "Gym", "Coffee Shop"],
    "Computer Science Building": ["Cafeteria", "Museum"],
    "Parking Lot": ["Library", "Park"],
    "Coffee Shop": ["Theater", "Park"],
    "Museum": ["Computer Science Building", "Park"],
    "Park": ["Coffee Shop", "Museum", "Library"]
    }

    gui.show_gui(adjacency_list) # pass adjacency list to the GUI

    # Placeholder paths (once Kiara's GUI is completed, user input will select BFS, DFS or Dijkstra and choose a path) important!!!! 
    path = bfs_search(start_location, goal_location, adjacency_list) # use bfs on path
    if path: # placeholder prints (will be displayed in Kiara's GUI) ------------------------------------ important!!!!
        print("BFS: Path found within", len(path)-1, "stops:", path) # print number of stops
    else:
        print("No path found.")

    path2 = dfs_search(start_location, goal_location, adjacency_list) # use dfs on path
    if path2: # placeholder prints (will be displayed in Kiara's GUI) ------------------------------------ important!!!!
        print("DFS: Path found within", len(path2)-1, "stops:", path2) # print number of stops
    else:
        print("No path found.")

# Call main
if __name__ == "__main__":
    main()
                    


