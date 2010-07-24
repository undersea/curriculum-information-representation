#also known as nodes

import uuid

from node import Node
from edge import Edge

class Vertex(Node):
    def __init__(self, id=uuid.uuid4().hex):
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

    def __str__(self):
        return "%s"%(self.id)


    def __hash__(self):
        return hash(self.id)


    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.id == other.id
        else:
            return self.id == other


    def __cmp__(self, other):
        if isinstance(other, Vertex):
            return cmp(self.id, other.id)
        else:
            return cmp(self.id, other)

    def __ne__(self, other):
        if isinstance(other, Vertex):
            return self.id != other.id
        else:
            return self.id != other

