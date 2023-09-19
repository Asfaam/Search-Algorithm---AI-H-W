** PURPOSE: To find a path from node A to node G in the graph while looking out for nodes with lower heuristic values, as indicated by Greedy Best-First Search **


heuristic = {}   # initializes an empty dictionary to store heuristic values for each node in the graph.
heuristic["A"] = 5  # Assigns a heuristic value of 5 to node "A.
heuristic["B"] = float('inf') # of positive infinity to node "B." Node "B" is has an unknown heuristic value.
heuristic["C"] = 4   # of 4 to node C
heuristic["D"] = 3   # of 3 to node D
heuristic["E"] = 3   # of 3 to node E
heuristic["F"] = 1   # of 1 to node F
heuristic["G"] = 0   # of 0 to node G

graph = {} # initializes an empty dictionary called graph. Provide graph with information about the connections between nodes.

graph["A"] = {"B": 1, "C": 4}  # define the neighbours of node A along with their edge weights. Node A is connected to node B with an edge weight of 1 and to C with an edge weight of 4.
graph["B"] = {"C": 2, "D": 3}  # B along with their edge weights. Node B is connected to node C with an edge weight of 2 and to D with an edge weight of 3.
graph["C"] = {"E": 5}          # C along with their edge weights. Node C is connected to node E with an edge weight of 5.
graph["D"] = {"F": 2, "G": 4}  # D along with their edge weights. Node D is connected to node F with an edge weight of 2 and to node G with an edge weight of 4.
graph["E"] = {"G": 3}          # E along with their edge weights. Node E is connected to node G with an edge weight of 3.
graph["F"] = {"G": 1}          # F along with their edge weights. Node F is connected to node G with an edge weight of 1.
graph["G"] = {}                # define that node G has no neighbor(s).

def greedy_best_first_search(graph, start, goal, path=[]):
    path = path + [start]  # keeps track of the path from the start node to the current node

    if start == goal:  # if the current start node is equal to the goal node, we have reached the goal, and the function returns the current path as a list containing the solution.
        return [path]

    if start not in graph: # if the current start node is not in the graph, we cannot proceed further from this node, so the function returns an empty list - there is no path
        return []

    # nValue creates a tuple
    nValues = min(graph[start].items()) # find the minimum heuristic value among the neighbors of the current start node by identifying the next node to explore based on greedy best-first search
				

    return greedy_best_first_search(graph, nValues[0], goal, path) # recursion on this line: recursively calls the greedy_best_first_search function with the next node to explore (nValues[0]) as  								   # the new start node and the updated path.

								   # nValues[0] retrieves the first element of nValue which is a minimum value from the graph dictionary. Note: we direct the next 								   # node to explore in Greedy Best-First Search.

print(greedy_best_first_search(graph, 'A', 'G')) # Call the greedy_best_first_search function, with graph, with start node: A and goal node: G and prints the result of the search.

