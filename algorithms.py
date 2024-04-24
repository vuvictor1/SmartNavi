"""********************************************************************************  
   Author Information:
   Victor Vu (vuvictor@csu.fullerton.edu)

   Other Authors: 

   Program Information:
   This File: algorithms.py
   Description: Implementation of BFS, DFS, and Dijkstra's Algorithm for 
   otimal route pathfinding. 
********************************************************************************"""  
from collections import deque # Allow function to deque for BFS

# BFS path between two locations by shortest amount of stops (unweighted)
def bfs_search(start_location, goal_location, adjacency_list): # (ex: throwing a pebble and seeing ripples)
    queue = deque([start_location]) # add the starting location in the queue
    visited = set() # set of visited locations
    visited.add(start_location) # mark start location as visited
    parent = {} # track parent of each node, goes back if path is not the shortest

    while queue: # explore all neighbors by level before going deeper 
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

# DFS path between two locations, but does not guarantee shortest path
def dfs_search(start_location, goal_location, adjacency_list): # (ex: go far but head back if a deadend is reached and choose another path)
    stack = [start_location] # add the starting location in the stack
    visited = set() # set of visited locations
    visited.add(start_location) # mark start location as visited
    parent = {} # track parent of each node, goes back if path is not the shortest

    while stack: # explore all neighbors as deeply as possible
        current_location = stack.pop() # pop current off the stack

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
                stack.append(neighbor_location) # add neighbors onto the stack
                visited.add(neighbor_location) # mark neighbors as visited 
                parent[neighbor_location] = current_location # move to the new location

    return None # in case goal could not be reached
