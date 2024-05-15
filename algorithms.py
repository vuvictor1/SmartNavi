from collections import deque  # Allow function to deque for BFS
import heapq # Import priority queue for DA

# Choose BFS path between locations by least amount of stops (unweighted)
def bfs_search(start_location, goal_location, adjacency_list):
    queue = deque([start_location]) # add the starting location in the queue
    visited = set() # create set of visited locations
    visited.add(start_location) # mark start location as visited
    parent = {} # create parent to track origins of each node

    while queue: # queue all neighbors by each level before going deeper 
        current_location = queue.popleft() # pop current location off the queue
        
        if current_location == goal_location: # if goal is reached
            path = [] # construct the path
            while current_location != start_location:
                path.append(current_location) # add current location to the new path
                current_location = parent[current_location] # track locations traveled, by going through parents
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

# Choose DFS path between locations, but does not guarantee shortest path (unweighted)
def dfs_search(start_location, goal_location, adjacency_list): 
    stack = [start_location] # add the starting location in the stack
    visited = set() # create set of visited locations
    visited.add(start_location) # mark start location as visited
    parent = {} # create parent to track origins of each node

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

    return None # goal could not be reached

# Dijkstra's Algorithm for finding shortest path between two locations
def da_search(start_location, goal_location, adjacency_list):
    pq = [(0, start_location)] # use priority queue with (distance, location)
    visited = set() # set of visited locations
    distance = {start_location: 0} # shortest distance to each location
    parent = {} # track parent of each node

    while pq:
        dist, current_location = heapq.heappop(pq) # pop the node with the smallest distance
        if current_location == goal_location: # if goal is reached
            path = [] # construct the path
            while current_location != start_location:
                path.append(current_location) # current location is now part of path
                current_location = parent[current_location] # track path traveled
            path.append(start_location) # start is also part of path
            path.reverse() # reverse from goal to find correct start order
            return path, distance[goal_location] # return path and shortest distance

        if current_location in visited: # skip already visited nodes
            continue 
        visited.add(current_location) # continue marking current location as visited

        # Explore neighbors
        for neighbor_location, edge_weight in adjacency_list[current_location].items(): # find neighbors and edge weights
            if neighbor_location in visited: # skip already visited neighbors
                continue
            new_dist = dist + edge_weight # calculate new distance
            if new_dist < distance.get(neighbor_location, float('inf')): # update distance if new distance is smaller
                distance[neighbor_location] = new_dist # update distance
                parent[neighbor_location] = current_location # update parent
                heapq.heappush(pq, (new_dist, neighbor_location)) # push new distance and neighbor onto the priority queue

    return None, float('inf') # goal could not be reached