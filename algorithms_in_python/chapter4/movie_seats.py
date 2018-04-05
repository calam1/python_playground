def naive_max_perm(M, A=None):
    if A is None:
        A = set(range(len(M)))
    if len(A) == 1: return A
    B = {M[i] for i in A} # pick the A index vals of M and strip out the duplicates
    print('A {}'.format(A))
    print('B {}'.format(B))
    #print('M {}'.format(M))
    C = A - B
    print('C {}'.format(C))
    if C:
        A.remove(C.pop())
        return naive_max_perm(M, A)
    return A

M = [2, 2, 0, 5, 3, 5, 7, 4]
#print('naive_max_perm {}'.format(naive_max_perm(M)))

# the relationship is that the ppl and the seats are directly related
# if there is no demand for the seat , being that count[i] == 0 then you remove that person(Person
# is A array) if you remove that person, which is also the seat, you must decrement the demand for that
# person/seat(which is array M in this case)  If the value of that person/seat in M array is 0 you
# need to add it to the 0/filtered array which happens to be named Q and it goes throuhg that while
# loop, etc, etc
def max_perm(M):
    n = len(M)
    A = set(range(n)) # list of ppl just 0 - 8 in an array
    #A = {range(n)} set literal fails
    count = [0]*n # creates an array of size 8 filled with 0s
    for i in M: # fill in what seat/person is occupied and how many 
        count[i] += 1
    print('initial seats wanted and count of each seat{}'.format(count))
    Q = [i for i in A if count[i] == 0] # filter out the indexes with 0 values
    print('values to be removed due to values being 0 {}'.format(Q))
    while Q:
        i = Q.pop()
        print('i {}'.format(i))
        A.remove(i) # remove the 0 values from the list of persons
        #print(A)
        j = M[i] # first time in the value of i is 6 and j will be 7(person 6 wanted seat 7), since person 6 is gone(and so is seat 6) we will remove their desire to have seat 7 by decrementing the count
        print('j value of index i {}'.format(j))
        count[j] -= 1 # decrement seat count of M[i] i being what we just removed from the ppl list
        if count[j] == 0: # if Q is 0 then remove that also
            Q.append(j)
    return A # return the list of ppl that are left


print('max_perm {}'.format(max_perm(M)))
