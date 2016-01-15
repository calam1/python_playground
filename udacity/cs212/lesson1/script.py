def sum_numbers_squared(numbers):
    return sum(x **2 for x in numbers)

numbers = [1, 2, 3]
print "SUM NUMBERS SQUARED"
print sum_numbers_squared(numbers)
print "---------------------------"

print "MAX"
print max([3, 4, 5, 0]), max([3, 4, -5, 0], key=abs)
print "---------------------------"

print "NUMBERS COUNT 5"
numbers = [1, 1, 1, 3, 2, 2, 4, 5, 5, 5, 5, 6]
print numbers.count(5)
print "---------------------------"

print "TUPLES OF TOTAL TIMES NUMBER EXIST"
print sorted([(numbers.count(x), x) for x in set(numbers)], reverse = True)
print "---------------------------"

hand = "6 7 8 9 T".split()
#print hand
#for r in hand:
#    print r

print "RETURNS AN ARRAY OF THE VALUE AND ITS POSITION"
print [('--23456789TJQKA'.index(r), r) for r in hand]
print "---------------------------"

cards = "6C$ 7C$ 8C$ 9C$ TC$".split()
print "PRINTS THE SECOND OR 'S' CHARACTER IN CARDS"
print [s for r, s, t in cards]
print "---------------------------"

cards = "6C 7C 8C 9C TC".split()
#for r, s in cards:
#    print s + " " + r
#print "---------------------------"

print "INDEX VALUE OF NUMBERIC VALUE OF CARD"
print ['--23456789TJQKA'.index(r) for r, s in cards]
print "---------------------------"

list_a = [1, 2, 3, 4]
list_b = [9, 8, 7, 6]
list_c = [0, 1, 2, 3]
print "ZIP"
print zip(list_a, list_b, list_c)
a, b, c, d = zip(list_a, list_b, list_c)
print a
print b
print c
print d
print "---------------------------"

print "FLUSH"
print [s for v, s in cards]
suits = set([s for v, s in cards])
print suits
print len(suits)
print "---------------------------"

print "MAX WITH LAMBDA"
num_1 = [3, 4, 1, 7, 2, "9"]
print "max no lambda: ", max(num_1)
print "max with lambda: ", max(num_1, key=lambda x:x)
print "max with lambda that does something: ", max(num_1, key=lambda x:int(x))

print "---------------------------"

print "MORE ADVANCED FOR LOOP"
print [elem for elem in num_1 if elem == "9"]
print [elem for elem in num_1 if elem == "19"] # empty array
print "---------------------------"
