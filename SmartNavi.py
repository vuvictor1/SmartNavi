"""********************************************************************************  
   Author Information:
   Victor Vu (vuvictor@csu.fullerton.edu)

   Other Authors: 

   Program Information:
   This File: SmartNavi.py
   Description: GPS system to find the most optimal path for different locations.
   Implements BFS, DFS, and Dijkstra's Algorithm for routing options.
********************************************************************************"""  
from collections import deque # Allow function to deque for BFS

# BFS path between two locations by shortest amount of stops (unweighted)
def bfs_search(start_location, goal_location, adjacency_list):
    queue = deque([start_location]) # add the starting location in the queue
    visited = set() # set of visited locations
    visited.add(start_location) # mark start location as visited
    parent = {} # track parent of each node, goes back if path is not the shortest

    while queue:
        current_location = queue.popleft() # pop current off the queue
        
        if current_location == goal_location: # if goal is reached
            path = [] # construct the path
            while current_location != start_location:
                path.append(current_location) # current location is now part of path
                current_location = parent[current_location] # track path traveled 
            path.append(start_location) # start is also part of path
            path.reverse() # reverse from goal to find correct start order
            return path

        # Find neighboring locations
        for neighbor_location in adjacency_list[current_location]:
            if neighbor_location not in visited: # only visit unvisited locations
                queue.append(neighbor_location) # add neighbors onto the queue
                visited.add(neighbor_location) # mark neighbors as visited 
                parent[neighbor_location] = current_location # move to the new location

    return None # in case goal could not be reached

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
    if path: # Placeholder prints (will be displayed in Kiara's GUI) ------------------------------------ important!!!!
        print("Path found within", len(path)-1, "stops:", path) # print number of stops
    else:
        print("No path found.")

# Call main
if __name__ == "__main__":
    main()

