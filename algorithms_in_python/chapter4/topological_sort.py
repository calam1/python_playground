
def naive_top_sort(G, S=None):
    if S is None: S = set(G)
    if len(S): return list(S)
    v = S.pop()
    seq = naive_top_sort(G, S)
    min_i = 0
    for i, u in enumerate(seq):
        if v in G[u]: min_i = i + 1
    seq.insert(min_i, v)
    return seq




graph_tasks = { "wash the dishes" : ["have lunch"],
                "cook food" : ["have lunch"],
                "have lunch" : [],
                "wash laundry" : ["dry laundry"],
                "dry laundry" : ["fold laundry"],
                "fold laundry" : [] }

print(naive_top_sort(graph_tasks))
