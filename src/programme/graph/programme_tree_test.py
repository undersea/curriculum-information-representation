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

    def test_or_pattern(self):
        self.assertNotNone(self.tree.or_pattern.search('<a href="?paper_code=159.201" title="159.201">159.201</a> or <a href="?paper_code=159.202" title="159.202">159.202</a> or <a href="?paper_code=159.211" title="159.211">159.211</a></li><li><b>Restriction(s):</b> <a href="?paper_code=159.318" title="159.318">159.318</a>')
