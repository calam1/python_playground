# Write a function, `count`
# that returns the units of time
# where each print statement is one unit of time
# and each evaluation of range also takes one unit of time

def count(n):
    return 2 + n + (n * (n - 1))/2


def clique(n):
    print "in a clique..."
    for j in range(n):
        for i in range(j):
            print i, "is friends with", j

print count(4)

