class Solution:
    def dfs(self, adj, visited, s):
        visited[s] = 1
        count = 0
        
        for i in adj[s]:
            if not visited[i]:
                res = self.dfs(adj, visited, i)
                if res % 2 == 0:
                    self.res += 1
                else:
                    count += 1
        return count + 1
        
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        adj =[[] for i in range(n)]
        
        for i in range(len(edges)):
            adj[edges[i][0] - 1].append(edges[i][1] - 1)
            adj[edges[i][1] - 1].append(edges[i][0] - 1)
        
        self.res = 0
        visited = [0] * n
        self.dfs(adj, visited, 0)
        return self.res
