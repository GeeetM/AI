#DFS and BFS
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]
#DFS----------------------------------------------------------
    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')

        if vertex in self.graph:
            neighbors = self.graph[vertex]
            for neighbor in neighbors:
                if neighbor not in visited:
                    self._dfs_recursive(neighbor, visited)
#BFS----------------------------------------------------------
    def bfs(self, start):
        visited = set()
        queue = []
        queue.append(start)
        visited.add(start)
        

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')

            if vertex in self.graph:
                neighbors = self.graph[vertex]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)


# Create a graph based on user input----------------------------------------
g = Graph()
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    u, v = map(int, input("Enter an edge (u v): ").split())
    g.add_edge(u, v)

start_vertex = int(input("Enter the starting vertex: "))

print("\nDFS traversal:")
g.dfs(start_vertex)

print("\nBFS traversal:")
g.bfs(start_vertex)

#End of the code-------------------------------------------------------------

'''This code allows the user to input the number of edges in the graph and the edges themselves, as well as the starting vertex for the DFS and BFS traversals.

The Graph class maintains a dictionary self.graph, where each key represents a vertex, and the corresponding value is a list of its neighboring vertices.

The add_edge method is used to add edges between vertices. It ensures that both vertices are added to each other's adjacency lists.

The dfs method performs a Depth-First Search traversal starting from a given vertex. It uses a set visited to keep track of visited vertices and calls the _dfs_recursive helper function to perform the actual traversal recursively.

The _dfs_recursive function first adds the current vertex to the visited set and prints it. Then, for each neighboring vertex, it recursively calls itself if the neighbor hasn't been visited before.

The bfs method performs a Breadth-First Search traversal starting from a given vertex. It uses a queue to keep track of the vertices to visit next. It iteratively pops vertices from the queue, visits them, and adds their unvisited neighbors to the queue.

You can run the code and input the graph edges and starting vertex according to your requirements. The code will perform the DFS and BFS traversals accordingly.

Note: When entering the edges, make sure to separate the vertices by a space. For example, if there is an edge between vertices 0 and 1, enter it as "0 1".'''
