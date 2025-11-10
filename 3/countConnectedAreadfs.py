
grid = []
move = [[1,0], [0,1], [-1,0], [0,-1]]

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    if grid[i][j] == 0 or check[i][j]:
        return
    check[i][j] = True
    for k in range(4):
        dfs(i + move[k][0], j + move[k][1])

def main():
    global n, m, check, grid, counter
    n, m = map(int, input().split())
    check = [[False]*m for _ in range(n)]
    counter = 0

    for i in range(n):
        grid.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if not check[i][j] and grid[i][j] == 1:
                counter += 1
                dfs(i, j)


    print(counter)

if __name__ == "__main__":
    main()

