from typing import List
import collections

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
  def isValidMove(i,j):
    return i<len(image) and i>=0 and j<len(image[0]) and j>=0 and image[i][j]==oldColor
  
  visited = set()
  que = collections.deque([(sr,sc)])
  oldColor = image[sr][sc]

  while(que):
    (i,j) = que.popleft()
    visited.add((i,j))
    image[i][j] = newColor
    for (dx,dy) in ([(-1,0),(1,0),(0,1),(0,-1)]):
      ni = i+dx
      nj = j+dy
      if isValidMove(ni,nj) and (ni,nj) not in visited:
        que.append((ni,nj))
  
  return image

image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2
print(floodFill(image, sr, sc, newColor))
