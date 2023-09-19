# The output expected is: ABCEGDF
graph = {
    'A':['B','C'], 'B':['C','D'], 'C':['E'], 'D':['F','G'], 'E':['G'], 'F':['G'], 'G':[]
}

visited = set()

def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited, graph, neighbour)
dfs(visited, graph, 'A')