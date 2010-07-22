#also known as nodes

from node import Node
from edge import Edge

class Vertex(Node):
    def __init__(self, id):
        self.id = id
        self.prereqlist = set()
        self.coreqlist = set()
        self.leadstolist = set()
        self.restrictlist = set()
        pass

    def add_prereq(self, vertex):
        vertex.add_leadsto(self)
        self.prereqlist.add(vertex)

    def add_coreq(self, vertex):
        if self not in vertex.coreqlist:
            vertex.add_leadsto(self)
        self.coreqlist.add(vertex)

    def add_leadsto(self, vertex):
        self.leadstolist.add(vertex)

    def add_restriction(self, paper):
        self.restrictlist.add(paper)
