import unittest
import som

class SomTest(unittest.TestCase):
    def test_som_init(self):
        try:
            map = som.SOM(3,3, [[1,2],[2,3]])
        except Exception, e:
            self.fail("Can't init som: %s"%(str(e)))

