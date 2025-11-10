from collections import deque

grid = []
n = m = 0

def bfs():
    global n, m, grid
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    q = deque([(0, 0)])
    dist = [[0]*m for _ in range(n)]
    dist[0][0] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1 and dist[nx][ny] == 0:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1

    return dist[n-1][m-1]

def main():
    global n, m, grid
    n, m = map(int, input().split())
    grid = [list(map(int, input().strip())) for _ in range(n)]
    print(bfs())

if __name__ == "__main__":
    main()
