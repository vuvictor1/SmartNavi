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

# Main function for execution
def main():
    # Placeholder locations (userinput later, will be included in Kiara's GUI) ------------------------- important!!!!
    start_location = "Library"
    goal_location = "Computer Science Building"
    
    # Placeholder list (will need to rely on Robert's graph model) ---------------------------------------- important!!!!
    adjacency_list = {
        "Library": ["Student Center", "Parking Lot"],
        "Student Center": ["Library", "Cafeteria"],
        "Cafeteria": ["Student Center", "Computer Science Building"],
        "Computer Science Building": ["Cafeteria", "Parking Lot"],
        "Parking Lot": ["Library", "Computer Science Building"]
    }

    path = bfs_search(start_location, goal_location, adjacency_list) # use bfs on path
    if path: # placeholder prints (will be displayed in Kiara's GUI) ------------------------------------ important!!!!
        print("Path found within", len(path)-1, "stops:", path) # print number of stops
    else:
        print("No path found.")

# Call main
if __name__ == "__main__":
    main()
                    


