import unittest

import programme_tree as pt

class ProgrammeTreeTest(unittest.TestCase):
    
    def setUp(cls):
        try:
            
            cls.tree = pt.Tree('')
        except:
            cls.tree = None

    def test_tree_init(self):
        param = ''
        try:
            pt.Tree(param)
        except Exception, e:
            self.fail("Couldn't create a Tree instance with '%s' as it's parameter:\n%s"%(param, str(e)))


    def test_tree_size(self):
        for v in self.tree.tree:
            print v,',',
        self.assertEqual(len(self.tree.tree), 28)
