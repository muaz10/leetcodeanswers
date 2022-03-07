import collections
from typing import List

def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    n,m = len(heights), len(heights[0])
    
    def isValid(ni,nj,i,j):
        if ni<0 or ni>=n or nj<0 or nj>=m or heights[i][j]>heights[ni][nj]:
            return False
        return True
    
    def bfs(starting, visited):
        q = collections.deque([starting])
        
        while q:
            ns = q.popleft()
            
            for n in ns:
                visited.add(n)
            newns=[]
            for n in ns:
                (i,j) = n
                for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if (ni,nj) not in visited and isValid(ni,nj,i,j):
                        newns.append((ni,nj))
            if (len(newns)):
                q.append(newns)
            
    toAtlantic = set()
    startingAtlantic = [(i,m-1) for i in range(n-1)]
    startingAtlantic += [(n-1,j) for j in range(m)]
    bfs(startingAtlantic, toAtlantic)
    
    toPacific = set()
    startingPacific = [(0,i) for i in range(m)]
    startingPacific += [(i,0) for i in range(n)]   
    bfs(startingPacific, toPacific)
    
    return toPacific.intersection(toAtlantic)

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(pacificAtlantic(heights))