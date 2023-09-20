***  A* is an informed search algorithm that balances the cost of the path travelled so far with a heuristic estimate of the cost to reach the goal, guiding the search towards the most promising paths. It is specifically designed for finding the shortest path from a starting point (or node) to a goal point (or node) in a graph ***

** PURPOSE: To perform an A* search to find the optimal path from node A to node G considering both edge weights(actual distance) and heuristic values to estimate the cost of reaching the goal. It prints the optimal path if one exists or a message if no path is found.

heuristic = {}
heuristic["A"] = 5
heuristic["B"] = float('inf')
heuristic["C"] = 4
heuristic["D"] = 3
heuristic["E"] = 3
heuristic["F"] = 1
heuristic["G"] = 0

graph = {}

graph["A"] = {"B": 1, "C": 4}
graph["B"] = {"C": 2, "D": 3}
graph["C"] = {"E": 5}
graph["D"] = {"F": 2, "G": 4}
graph["E"] = {"G": 3}
graph["F"] = {"G": 1}
graph["G"] = {}


def aStar(graph, start, goal, path=[]): # define a function named aStar to perform A* search algorithm. ** path parameter keeps track of the current path.
    print("->" + start, end="") # print the current start node, an arrow symbol -> to represent the path, then end="" parameter ensures that the next print statement is on the same line.
    path = path + [start]  # keeps track of the path from the start node to the current node

    if start == goal:   # if the current start node is equal to the goal node, we have reached the goal, and the function returns the current path as a list containing the solution. 
        return [path]

    if start not in graph: # if the current start node is not in the graph, we cannot proceed further from this node, so the function returns an empty list - there is no path
        return []


    # Initialize min_distance to positive infinity and next_node to None. 
    min_distance = float("inf")  #  will be used to track the minimum estimated distance
    next_node = None  # will be used to track the next node to visit.

    # Iterates over the neighbouring nodes of the current start node using graph[start].items()
    for node, distance in graph[start].items():
	# For each neighbour, it calculates the estimated distance to the goal by adding the actual distance to the heuristic value (distance + heuristic[node]).
        if distance + heuristic[node] < min_distance:
            min_distance = distance + heuristic[node] # If this estimated distance is less than min_distance, it updates min_distance and sets next_node to the current neighbour.
            next_node = node

    # Upon iterating all neighbours, check if a next_node has been selected. If yes, it recursively calls the aStar function with the next_node as the new start node.
    if next_node:
        return aStar(graph, next_node, goal, path)
    else:
        return []     # If next_node is not available, it returns an empty list - there is no path to the goal so far




# Set the start node to A and the goal node to G
start = "A"
goal = "G"

result = aStar(graph, start, goal) # Call the aStar function, with the graph, start node and goal node, and store the result in the variable called result.

# Check if a valid result was obtained. If so, print the optimal path by joining the elements of the result[0] list with this arrow -> symbols. If there is no path, prints a message to show that there is no path.
if result:
    print("\n\nThis is the optimum path from A to G:\n", " -> ".join(result[0]))
else:
    print("\nNo path found from A to G")
