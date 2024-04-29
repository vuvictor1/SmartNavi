"""********************************************************************************  
   Author Information:
   Victor Vu (vuvictor@csu.fullerton.edu)

   Other Authors: 

   Program Information:
   This File: main_navi.py
   Description: Manager for the SmartNavi GPS system. Calls BFS, DFS and Dijkstra's 
   Algorithm for pathfinding. Also incorporates GUI, utilizing a graph model.
********************************************************************************"""  
import gui # Call the GUI file

# Main function for execution
def main():
    # Placeholder list (will need to rely on Robert's graph model) ---------------------------------------- important!!!!
    adjacency_list = { 
    "Library": {"Student Center": 5, "Parking Lot": 3, "Cafeteria": 2},
    "Student Center": {"Library": 5, "Cafeteria": 1, "Theater": 4},
    "Cafeteria": {"Student Center": 1, "Library": 2, "Gym": 3, "Computer Science Building": 6},
    "Gym": {"Cafeteria": 3, "Theater": 2},
    "Theater": {"Student Center": 4, "Gym": 2, "Coffee Shop": 3},
    "Computer Science Building": {"Cafeteria": 6, "Museum": 4},
    "Parking Lot": {"Library": 3, "Park": 5},
    "Coffee Shop": {"Theater": 3, "Park": 4},
    "Museum": {"Computer Science Building": 4, "Park": 6},
    "Park": {"Coffee Shop": 4, "Museum": 6, "Library": 5}
    }
    
    gui.show_gui(adjacency_list) # pass adjacency list to the GUI

# Call main
if __name__ == "__main__":
    main()