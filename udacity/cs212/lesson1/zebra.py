#incomplete
import itertools

print "BASEC ASSIGNMENT"
houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
print houses
print first
print middle
print "----------------"

print "ITERTOOLS.PERMUTATIONS"
orderings = list((itertools.permutations(houses)))
print orderings
print "----------------"

print "YIELD"
def f123():
    yield 1
    yield 2
    yield 3

for item in f123():
    print item

print "----------------"
#print "?????"
#def c(sequence):
#    c.starts += 1
#    for item in sequence:
#        c.items += 1
#        yield item
