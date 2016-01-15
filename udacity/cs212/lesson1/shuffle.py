#shuffle

import random

#knuth method, or fisher-yates
#pythons random.shuffle uses the same algo
def shuffle(deck):
    n = len(deck)
    for i in range(n-1):
        j = random.randrange(i, n)
        deck[i], deck[j] = deck[j], deck[i]
    

deck = [1, 2, 3, 4, 5, 6]
print "BEFORE SHUFFLE"
print deck
shuffle(deck)
print "AFTER SHUFFLE"
print deck







