from random import randrange

seq = [randrange(10**10) for i in range(100)]
dd = float("inf")

def s(seq):
    global dd 
    for x in seq:
        for y in seq:
            if x == y: continue
            d = abs(x-y)
            if d < dd:
                xx, yy, dd = x, y, d
    print (xx)
    print (yy)
    print (dd)

ee = float("inf")
def t(seq):
    global ee
    for i in range(len(seq)-1):
        x, y = seq[i], seq[i+1]
        if x == y: continue
        e = abs(x-y)
        if e < ee:
            xx, yy, ee = x, y, e  
    print (xx)
    print (yy)
    print (ee)

print ('s')
s(seq)

seq.sort()


print ('t')
t(seq)


