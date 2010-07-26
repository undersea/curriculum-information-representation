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


    def test_str_works(self):
        v1 = Vertex('1')
        self.assertEqual(str(v1), 'vertex:1')
