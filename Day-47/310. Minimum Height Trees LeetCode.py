class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        inDegree = defaultdict(list)
        for n1, n2 in edges:
            inDegree[n1].append(n2)
            inDegree[n2].append(n1)

        edgeCount = {}
        leaves = []
        for i, j in inDegree.items():
            if len(j) == 1:
                leaves.append(i)
            edgeCount[i] = len(j)

        while leaves:
            if n <= 2:
                return leaves
            for i in range(len(leaves)):
                node = leaves.pop(0)
                n -= 1
                for j in inDegree[node]:
                    edgeCount[j] -= 1
                    if edgeCount[j] == 1:
                        leaves.append(j)
