class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, new_value):
        self.vertices[new_value] = []

    def add_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].append(end)

    def print_graph(self):
        for vertex, edges in self.vertices.items():
            print(f"{vertex} -> [ ", end="")
            for edge in edges:
                print(edge, end=" ")
            print("]")

    def dfs(self, start, visited=None):
        if visited is None:
            visited = {key: False for key in self.vertices.keys()}

        visited[start] = True
        print(start, end=" ")

        for neighbor in self.vertices[start]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)