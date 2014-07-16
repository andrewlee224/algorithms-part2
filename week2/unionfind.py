"""
Implementation of a Union-Find data structure
"""

class Vertex(object):
    """
    Vertex with a pointer to a leader vertex.
    May point to itself.
    """
    def __init__(self, key, leader=None):
        self.componentCount = 0
        self.key = key
        # if leader, keeps track of vertices pointing to it
        self.outbound = []

        if not leader:
            leader = self
        self.leader = leader
        # leader vertex keeps count of all children vertices
        # => number of vertices in a single component
        leader.componentCount += 1
        leader.outbound.append(self)

class UnionFind(object):
    
    def __init__(self, initList=None):
        self._vdict = {}
        self.totalVertices = 0
        # number of all components in Union-Find
        self.totalComponents = 0
        if initList:
            for el in initList:
                self._vdict[el] = Vertex(el)
            self.totalVertices = len(initList)    
            self.totalComponents = self.totalVertices

    def add(self, vertex):
        self._vdict[vertex.key] = vertex
        self.totalVertices += 1
        self.totalComponents += 1

    def find(self, key):
        """Return leader of the vertex requested by key"""
        vertex = self._vdict[key]
        
        return vertex.leader

    def union(self, key1, key2):
        """
        Perform a union operation on disconnected components c1
        and c2 which contain vertices with key1 and key2.
        """

        if self.find(key1) == self.find(key2):
            # keys in the same component, union already performed
            return False
        
        v1 = self._vdict[key1]
        v2 = self._vdict[key2]

        l1 = v1.leader
        l2 = v2.leader

        if l1.componentCount >= l2.componentCount:
            # change leader of vertices in a smaller component
            for v in l2.outbound:
                v.leader = l1
            l1.componentCount += l2.componentCount
            l1.outbound += l2.outbound
        else:
            for v in l1.outbound:
                v.leader = l2
            l2.componentCount += l1.componentCount
            l2.outbound += l1.outbound

        self.totalComponents -= 1
        
        return True
