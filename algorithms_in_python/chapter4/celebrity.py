def naive_celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == v: continue # same person, skip
            if G[u][v]: break # person knows other, break, cause celebs don't know other ppl
            if not G[v][u]: break # if others don't know the person then they are not celebs
        else:
            return u
    return None

# C or number 2 is the celebrity
matrix = [[0]*4 for i in range(4)]
matrix[0][2] = 1
matrix[1][2] = 1
matrix[3][2] = 1

print(matrix)
print(naive_celeb(matrix))

def celeb(G):
    l = len(G)
    p = [i for i in range(l)]

    while len(p) > 1:
        one = p.pop()
        two = p.pop()
        print('one {} two {}'.format(one, two))
        if _knows(one, two):
            p.append(two)
        elif _knows(two, one):
            p.append(one)
            

    return p[0]

            
def _knows(a, b):
    return 1 == matrix[a][b]

print(celeb(matrix))

