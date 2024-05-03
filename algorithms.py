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
import heapq

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
def dfs_search(start_location, goal_location, adjacency_list): # (ex: go far but head back if a dead-end is reached and choose another path)
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

    def da(start_location, goal_location, adjacency_list):
        pq = [(0, start_location)]  # Priority queue with (distance, location)
        visited = set()  # Set of visited locations
        distance = {start_location: 0}  # Shortest distance to each location
        parent = {}  # Track parent of each node

        while pq:
            dist, current_location = heapq.heappop(pq)  # Pop the node with the smallest distance
            if current_location == goal_location:  # If goal is reached
                path = []  # Construct the path
                while current_location != start_location:
                    path.append(current_location)  # Current location is now part of path
                    current_location = parent[current_location]  # Track path traveled
                path.append(start_location)  # Start is also part of path
                path.reverse()  # Reverse from goal to find correct start order
                return path, distance[goal_location]  # Return path and shortest distance

            if current_location in visited:  # Skip already visited nodes
                continue
            visited.add(current_location)

            # Explore neighbors
            for neighbor_location, edge_weight in adjacency_list[current_location].items():
                if neighbor_location in visited:  # Skip already visited neighbors
                    continue
                new_dist = dist + edge_weight
                if new_dist < distance.get(neighbor_location, float('inf')):
                    distance[neighbor_location] = new_dist
                    parent[neighbor_location] = current_location
                    heapq.heappush(pq, (new_dist, neighbor_location))

        return None, float('inf')  # In case goal could not be reached

    # Example usage:
    # adjacency_list = {
    #     'A': {'B': 5, 'C': 3},
    #     'B': {'A': 5, 'C': 2, 'D': 6},
    #     'C': {'A': 3, 'B': 2, 'D': 7},
    #     'D': {'B': 6, 'C': 7}
    # }
    # start = 'A'
    # goal = 'D'
    # path, shortest_distance = dijkstra_shortest_path(start, goal, adjacency_list)
    # print("Shortest Path:", path)
    # print("Shortest Distance:", shortest_distance)

    return None # in case goal could not be reached
