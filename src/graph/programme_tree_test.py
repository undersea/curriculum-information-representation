import unittest

import programme_tree as pt

class ProgrammeTreeTest(unittest.TestCase):
    
    def setUp(cls):
        try:
            cls.tree = pt.Tree('Bachelor of Accountancy (BAcc)')
        except:
            cls.tree = None

    def test_tree_init(self):
        try:
            pt.Tree('Bachelor of Accountancy (BAcc)')
        except Exception, e:
            self.fail("Couldn't create a Tree instance with 'Bachelor of Accountancy (BAcc)' as it's parameter:\n%s"%(str(e)))


    def test_tree_size(self):
        for v in self.tree.tree:
            print v,',',
        self.assertEqual(len(self.tree.tree), 50)
