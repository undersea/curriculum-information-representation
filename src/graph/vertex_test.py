import unittest

from vertex import Vertex

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
        self.assertEqual(len(s1), 0)
        self.assertEqual(len(s2), 1)
        self.assertNotEqual(s1, s2)
        self.assertTrue(pre in s2)


    def test_add_coreq(self):
        pre = Vertex('1')
        curr = Vertex('2')
        s1 = curr.coreqlist.copy()
        curr.add_coreq(pre)
        s2 = curr.coreqlist.copy()
        self.assertEqual(len(s1), 0)
        self.assertEqual(len(s2), 1)
        self.assertNotEqual(s1, s2)
        self.assertTrue(pre in s2)


    def test_add_restrict(self):
        pre = Vertex('1')
        curr = Vertex('2')
        s1 = curr.restrictlist.copy()
        curr.add_restriction(pre)
        s2 = curr.restrictlist.copy()
        self.assertEqual(len(s1), 0)
        self.assertEqual(len(s2), 1)
        self.assertNotEqual(s1, s2)
        self.assertTrue(pre in s2)

