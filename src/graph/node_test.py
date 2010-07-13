import unittest

from node import Node

class NodeTest(unittest.TestCase):
    def test_cannot_be_initialised(self):
        try:
            node = Node()
        except:
            return
        
        self.fail("Should have failed to Init")
