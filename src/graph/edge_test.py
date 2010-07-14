import unittest

from edge import Edge

class EdgeTest(unittest.TestCase):
    def test_edge_initialisation(self):
        try:
            edge = Edge()
        except:
            self.fail("Couldn't init Edge")
