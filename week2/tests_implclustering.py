import unittest
import implclustering as ic

class ImplicitClusteringTestCase(unittest.TestCase):
    
    def testGraph1(self):
        nodeList, bitsLabel = ic.getGraph("implclustering_test1.txt")
        maxDist = 3
        k = ic.implicitClustering(nodeList, maxDist, bitsLabel)
        self.assertEqual(k, 1)

    def testGraph2(self):
        nodeList, bitsLabel = ic.getGraph("implclustering_test2.txt")
        maxDist = 3
        k = ic.implicitClustering(nodeList, maxDist, bitsLabel)
        self.assertEqual(k, 3)

    def testGraph3(self):
        nodeList, bitsLabel = ic.getGraph("ictest3.txt")
        maxDist = 3
        k = ic.implicitClustering(nodeList, maxDist, bitsLabel)
        self.assertEqual(k, 4)

    def testGraph4(self):
        nodeList, bitsLabel = ic.getGraph("ictest4.txt")
        maxDist = 3
        k = ic.implicitClustering(nodeList, maxDist, bitsLabel)
        self.assertEqual(k, 11)

if __name__ == '__main__':
   suite = unittest.TestLoader().loadTestsFromTestCase(ImplicitClusteringTestCase)
   unittest.TextTestRunner(verbosity=2).run(suite)
