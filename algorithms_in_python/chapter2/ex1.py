a, b, c, d, e, f, g, h = range(8)

N = [
    set([b, c, d, e, f]),
    set([c, e]),
    set([d]),
    set([e]),
    set([f]),
    set([c, g, h]),
    set([f, h]),
    set([f, g])
]

C = [1, 2, 3, 4]
print (a in N[a])

print (len(N[f]))
