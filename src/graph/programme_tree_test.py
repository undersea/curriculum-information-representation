import unittest

import programme_tree as pt

class ProgrammeTreeTest(unittest.TestCase):
    
    def setUp(self):
        try:    
            self.tree = pt.Tree()
        except:
            self.tree = None

    def test_tree_init(self):
        param = ''
        try:
            pt.Tree()
        except Exception, e:
            self.fail("Couldn't create a Tree instance:\n"%(param, str(e)))


    def test_tree_size(self):
        self.assertEqual(len(self.tree.tree), 0)


    def test_tree_print(self):
        self.tree.add_paper('159.201')
        from cStringIO import StringIO
        out = StringIO()
        self.tree.pprint(output=out)
        expected = """159.101
159.102
\t159.201
"""
        got = out.getvalue()
        out.close()
        self.assertEqual(got, expected) 
