def ins_sort_rec(seq, i):
    if i==0: return                             # base case -- do nothing
    ins_sort_rec(seq, i-1)                      # sort 0..i-1
    j = i                                       # start walking down
    while j > 0 and seq[j-1] < seq[j]:          # look for OK spot
        seq[j-1], seq[j] = seq[j], seq[j-1]     # keep moving seq[j] down
        j -= 1                                  # decrement j


def ins_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1


a = [3, 2, 6, 3, 1, 8]
b = [3, 2, 6, 3, 1, 8]

ins_sort_rec(a, len(a)-1)
print(a)

ins_sort(b)
print(b)
