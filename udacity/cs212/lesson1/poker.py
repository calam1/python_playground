
#incomplete

def poker(hands):
    "Returns the best hand: poker([hand, ...]) => hand"
    return max(hands, key=hand_rank)

def hand_rank(hand):
    "Return a value indicating how high the hand ranks."
    # counts is the count of each rank
    # ranks lists corresponding ranks
    # d.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    print group
    return None

def group(items):
    "Return a list  of [(count, x)...], highest count first, the highest x first"
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse = True)

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([fh]) == fh
    assert poker([sf] + 99 * [fh]) == sf
    return "tests pass"

print test()
