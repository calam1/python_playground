def sel_sort_rec(seq, i):
    if i==0: return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]: max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]
    sel_sort_rec(seq, i-1)


def sel_sort(seq):
    for i in range(len(seq)-1,0,-1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]: max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]

a = [3, 2, 6, 3, 1, 8]
b = [3, 2, 6, 3, 1, 8]

sel_sort_rec(a, len(a)-1)
print(a)

sel_sort(b)
print(b)
