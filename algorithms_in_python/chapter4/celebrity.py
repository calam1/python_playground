def naive_celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == v: continue
            if G[u][v]: break
            if not G[v][u]: break
        else:
            return u
    return None

matrix = [[0]*4 for i in range(4)]
matrix[0][2] = 1
matrix[1][2] = 1
matrix[3][2] = 1

print(matrix)

print(naive_celeb(matrix))
