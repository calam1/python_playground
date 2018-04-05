M = [2, 2, 0, 5, 3, 5, 7, 4]
A = set([0, 1, 2, 3, 4, 5, 6, 7])
A = set([0, 2, 3, 4, 5, 7])

def test(M, A):
    #if A is None:
    #    A = set(range(len(M)))
    B = {M[i] for i in A}
    print('M {}'.format(M))
    print('A {}'.format(A))
    print('B {}'.format(B))
    
test(M, A)
