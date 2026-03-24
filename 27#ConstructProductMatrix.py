def productMatrixBruteForce(grid):
    if not grid or not grid[0]:
        return []
    
    n = len(grid)
    m = len(grid[0])
    MOD = 12345
    
    result = [[1] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            product = 1
            for x in range(n):
                for y in range(m):
                    if x != i or y != j:
                        product = (product * grid[x][y]) % MOD
            result[i][j] = product
    
    return result