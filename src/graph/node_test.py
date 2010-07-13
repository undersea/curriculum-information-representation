import unittest

from node import Node

class NodeTest(unittest.TestCase):
    def test_cannot_be_initialised(self):
        try:
            Node()
            raise Exception("Init should have failed")
        except:
            pass
