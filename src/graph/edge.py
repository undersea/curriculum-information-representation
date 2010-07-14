#edge - line between vertices

from node import Node

class Edge(Node):
    def __init__(self):
        self.vertex1 = None
        self.vertex2 = None

    def get_vertices(self):
        return [self.vertex1, self.vertex2]
