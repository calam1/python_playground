from collections import defaultdict

def counting_sort(A, key=lambda x: x):
    B, C = [], defaultdict(list)
    for x in A:
        # create a dictionary of number as key, and each number as value, and if more than one, then
        # it appears multiple times in the value, since is is a list
        C[key(x)].append(x)
        #print(C)

    print('min C {} and max C {}'.format(min(C), max(C)))
    for k in range(min(C), max(C)+1): # min and max gets the smallest and largest values of the dictionary
        B.extend(C[k]) # use extend because it will flatten the values in C(the value of key/value), getting the values of the keys from min to max
        print(B)
    return B

mixed = [2, 1, 1, 2, 4, 3, 0]

print(counting_sort(mixed))

