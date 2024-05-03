# Author: Kim Brodersen
# email: kbroders@csu.fullerton.edu
# Program information:
# This File: dijkstras_algo.py
# Description: Implementation of Dijkstra's Algorithm for optimized pathfinding.

import heapdict # heapdict acts like a regular dictionary, but designed for use as a priority queue. (Supports efficient priority changes)

def dijkstras_algo(start_location, goal_location, adjacency_list):
    Q = heapdict() 
    dist = dict()
    prev = dict()
    for v in adjacency_list.keys():
    	dist[v] = INFINITY
	    prev[v] = UNDEFINED
	    Q[v] = INFINITY #Add the vertex to the queue

    dist[start_location] = 0
    Q[start_location] = 0
    while len(Q) > 0:
	    u = Q.popitem()[0] #Set u = vertex w/min dist from start_location & remove from queue
        
        # Found optimal route
        if u == goal_location:
            path = [u]
            p = prev(path[0])
            while p != UNDEFINED:
                path.insert(0, p)
            return path, dist[goal_location]
	    
        # Check the distance to neighbors
        for v in adjacency_list[vertex].keys(): #for each neighbor v of u
		    alt = dist[u] + adjacency_list[u][v]
    		if alt < dist[v]:
	    		dist[v] = alt
		    	prev[v] = u[0]
			    if v in Q:
				    Q[v] = alt
    return None
