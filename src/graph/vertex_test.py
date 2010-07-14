import unittest

from vertex import Vertex

class VertexTest(unittest.TestCase):
    def test_does_vertex_initialise(self):
        try:
            vertex = Vertex()
        except:
            self.fail("could not initialise Vertex")


