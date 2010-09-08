import unittest

from vertex import Vertex
from programme_tree import Tree
from cStringIO import StringIO

class VertexTest(unittest.TestCase):
    def test_does_vertex_initialise(self):
        try:
            vertex = Vertex()
        except:
            self.fail("could not initialise Vertex")

    def test_eq_works(self):
        
        self.assertEqual(Vertex('1'), Vertex('1'))


    def test_ne_works(self):
        self.assertNotEqual(Vertex('1'), Vertex('2'))


    def test_hash_works(self):
        id = '1'
        #hash of 'vertex:'+id should be the same as hash of Vertex(id) as 'vertex:' and id are concated together used to produce the hash value
        self.assertEqual(hash(Vertex(id)), hash('vertex:'+id))


    def test_cmp_other_vertex_works(self):
        v1 = Vertex('1')
        v2 = Vertex('2')
        self.assertEqual(cmp(v1, v1), 0)
        self.assertEqual(cmp(v1, v2), -1)
        self.assertEqual(cmp(v2, v1), 1)


    def test_cmp_with_id_str(self):
        self.assertEqual(Vertex('1'), '1')


    def test_str_works(self):
        v1 = Vertex('1')
        self.assertEqual(str(v1), 'vertex:1')


    def test_add_prereq(self):
        pre = Vertex('1')
        curr = Vertex('2')
        s1 = curr.prereqlist.copy()
        p1 = pre.leadstolist.copy()
        curr.add_prereq(pre)
        s2 = curr.prereqlist.copy()
        p2 = pre.leadstolist.copy()
        self.assertEqual(len(p1), 0)
        self.assertEqual(len(p2), 1)
        self.assertEqual(set([]), p1)
        self.assertEqual(set([curr]), p2)
        self.assertEqual(len(s1), 0)
        self.assertEqual(len(s2), 1)
        self.assertEqual(set([pre]), s2)
        self.assertTrue(pre in s2)


    def test_add_coreq(self):
        pre = Vertex('1')
        curr = Vertex('2')
        s1 = curr.coreqlist.copy()
        p1 = pre.leadstolist.copy()
        curr.add_coreq(pre)
        p2 = pre.leadstolist.copy()
        s2 = curr.coreqlist.copy()
        self.assertEqual(len(p1), 0)
        self.assertEqual(len(p2), 1)
        self.assertEqual(set([]), p1)
        self.assertEqual(set([curr]), p2)
        self.assertEqual(len(s1), 0)
        self.assertEqual(len(s2), 1)
        self.assertEqual(set([pre]), s2)
        self.assertNotEqual(s1, s2)
        self.assertTrue(pre in s2)


    def test_add_restrict(self):
        pre = Vertex('1')
        curr = Vertex('2')
        s1 = curr.restrictlist.copy()
        p1 = pre.leadstolist.copy()
        curr.add_restriction(pre)
        s2 = curr.restrictlist.copy()
        p2 = pre.leadstolist.copy()
        self.assertEqual(len(p1), 0)
        self.assertNotEqual(len(p2), 1)
        self.assertEqual(set([]), p1)
        self.assertNotEqual(set([curr]), p2)
        self.assertEqual(len(s1), 0)
        self.assertEqual(len(s2), 1)
        self.assertNotEqual(s1, s2)
        self.assertTrue(pre in s2)


    def test_add_leadsto(self):
        pre = Vertex('1')
        curr = Vertex('2')
        p1 = pre.leadstolist.copy()
        pre.add_leadsto(curr)
        p2 = pre.leadstolist.copy()
        self.assertEqual(len(p1), 0)
        self.assertEqual(len(p2), 1)
        self.assertEqual(set([]), p1)
        self.assertEqual(set([curr]), p2)
        

    def test_pprint(self):
        paper = Tree().add_paper('159.302')
        out = StringIO()
        paper.pprint(out)
        expected = """159.101
159.102
\t159.201
\t159.202
\t159.211
\t\t159.302
"""
        got = out.getvalue()
        out.close()
        self.assertEqual(expected, got)
