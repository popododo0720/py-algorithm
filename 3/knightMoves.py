
from collections import deque

n = 0

def bfs(start, target):
    global n
    move = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
    grid = [[0]*n for _ in range(n)] 
    
    q = deque([(start[0], start[1])])
    grid[start[0]][start[1]] = 1
    while q:
        x, y = q.popleft()
        if(x, y) == (target[0], target[1]):
            return grid[x][y] - 1
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y] + 1
                q.append((nx, ny))

    return -1

def main():
    global n
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        start = list(map(int, input().split()))
        target = list(map(int, input().split()))
        
        if start == target: 
            print(0)
        else: 
            print(bfs(start, target))


if __name__ == "__main__":
    main()
