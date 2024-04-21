class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph =[[] for j in range(n)]
        visited = [0] * n
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(node):
            if visited[node] : return 
            visited[node] = True

            for i in graph[node]:
                dfs(i)

        dfs(source)
        return visited[destination]
