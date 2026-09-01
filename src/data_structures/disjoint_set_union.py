class DisjointSetUnion:
    """
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    """

    def __init__(self, n: int):
        self._parents = [i for i in range(n)]
        self._ranks = [1] * n
    
    def find(self, n: int) -> int:
        if n != self._parents[n]:
            self._parents[n] = self.find(self._parents[n])
        return self._parents[n]
    
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self._ranks[p1] > self._ranks[p2]:
            p1, p2 = p2, p1

        self._parents[p2] = p1
        self._ranks[p1] += self._ranks[p2]
        return True