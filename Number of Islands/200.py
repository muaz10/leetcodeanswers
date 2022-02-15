from typing import List
import collections

def numIslands(grid: List[List[str]]) -> int:
  def isValidMove(i,j):
    return i<len(grid) and i>=0 and j<len(grid[0]) and j>=0 and grid[i][j] == "1" 

  islands = 0

  for m in range(len(grid)):
    for n in range(len(grid[m])):
      if grid[m][n] != "1":
        continue
      que = collections.deque([(m,n)])
      islands += 1
      while(que):
        (i,j) = que.popleft()
        grid[i][j] = "0"

        for (dx,dy) in ([(-1,0),(1,0),(0,1),(0,-1)]):
          ni = i+dx
          nj = j+dy
          if isValidMove(ni,nj):
            que.append((ni,nj))  
    
  return islands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))
