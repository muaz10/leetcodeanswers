class Position:
    def _init_(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist
 
def minDistance(grid):
    currentPosition = Position(0, 0, 0)
 
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
            
    queue = []
    queue.append(currentPosition)
    visited[currentPosition.row][currentPosition.col] = True
    while len(queue) != 0:
        currentPosition = queue.pop(0)
 
        if (grid[currentPosition.row][currentPosition.col] == 9):
            return currentPosition.dist
 
        if isFlat(currentPosition.row - 1, currentPosition.col, grid, visited):
            queue.append(Position(currentPosition.row - 1, currentPosition.col, currentPosition.dist + 1))
            visited[currentPosition.row - 1][currentPosition.col] = True
 
        if isFlat(currentPosition.row + 1, currentPosition.col, grid, visited):
            queue.append(Position(currentPosition.row + 1, currentPosition.col, currentPosition.dist + 1))
            visited[currentPosition.row + 1][currentPosition.col] = True
 
        if isFlat(currentPosition.row, currentPosition.col - 1, grid, visited):
            queue.append(Position(currentPosition.row, currentPosition.col - 1, currentPosition.dist + 1))
            visited[currentPosition.row][currentPosition.col - 1] = True
 
        if isFlat(currentPosition.row, currentPosition.col + 1, grid, visited):
            queue.append(Position(currentPosition.row, currentPosition.col + 1, currentPosition.dist + 1))
            visited[currentPosition.row][currentPosition.col + 1] = True
 
    return -1

def isFlat(x, y, grid, visited):
    if ((x >= 0 and y >= 0) and
        (x < len(grid) and y < len(grid[0])) and
            (grid[x][y] != 0) and (visited[x][y] == False)):
        return True
    return False
 
if _name_ == '_main_':
    lot = [[1, 0, 0],
            [1, 0, 0],
            [1, 9, 1]]
            
    print(minDistance(lot))