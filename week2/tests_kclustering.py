import unittest
import kclustering as kc

class KClusteringTestCase(unittest.TestCase):
    
    def setUp(self):
        self.edgeList, self.numNodes = kc.getGraph("kclustering_test.txt")
    
    def testGraph(self):
        n1, n2, maxSpacingEdge = kc.kclustering(4, self.edgeList, self.numNodes)
        self.assertEqual(maxSpacingEdge, 134365)

if __name__ == '__main__':
   suite = unittest.TestLoader().loadTestsFromTestCase(KClusteringTestCase)
   unittest.TextTestRunner(verbosity=2).run(suite)
