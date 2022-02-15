import collections
def answer(plot):
    def isValidMove(i,j):
        if i<len(plot) and i>=0 and j<len(plot[0]) and j>=0 and plot[i][j]!=0:
            return True
        return False
    
    visited = set()
    que = collections.deque([(0,0,0)])
    while(que):
        (i,j,n) = que.popleft()
        visited.add((i,j))
        if plot[i][j]==9:
            return n
        for (dx,dy) in ([(-1,0),(1,0),(0,1),(0,-1)]):
            ni = i+dx
            nj = j+dy
            if isValidMove(ni,nj) and (ni,nj) not in visited:
                que.append((ni,nj,n+1))

    return -1

lot = [[1,0,0],[1,0,0],[1,1,9]]
print(answer(lot))
