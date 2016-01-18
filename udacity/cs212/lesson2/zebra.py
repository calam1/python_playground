#incomplete
import itertools

print "BASIC ASSIGNMENT"
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
print "When f123() is called, it does not return any of the values in the yield statements! It returns a generator object. "
def f123():
    yield 1
    yield 2
    yield 3

for item in f123():
    print item

print "----------------"

print "CLASS"
def _unmockstr(x):
    "Secret function to convert mockstr back to str, leaves other objects unchaged"
    return str.__str__(x) if isinstance(x, mockstr) else x

class mockstr(str):
    """ An objetct that looks like a str, but counts comparisons and accesses
    Obeys 2 rules:
    (1) Any piece of a mockstr that is returned must be a moctstr not a str
    (2) Any comparison or access increments num_comparisons or num_accesses
    Despite these precautions, the class is not secure against many simple attacks,
    including map(ord, s) or str.__str__(s)
    """

    # Track total number of comparisons and accesses to any mockstr objects
    num_comparisons, num_accesses = 0, 0

    def __getitem__(self, i):
        "s[i] counts as 1 access"
        mockstr.num_accesses += 1
        return mockstr(_unmockstr(self)[i])

    def __getslice__(self, start, end):
        "s[i:i+n] counts as n acessess."
        end = min(len(self), end)
        mockstr.num_accesses += (end - start)
        return mockstr(_unmockstr(self)[start:end])

    # s1 == s2 counts as len(s1) comparisons (so s[i] == s[j] counts as 1)
    def __eq__(self, other): return self._c() == _unmockstr(other)
    def __ne__(self, other): return self._c() != _unmockstr(other)
    def __ge__(self, other): return self._c() >= _unmockstr(other)
    def __le__(self, other): return self._c() <= _unmockstr(other)
    def __gt__(self, other): return self._c() > _unmockstr(other)
    def __lt__(self, other): return self._c() < _unmockstr(other)

    def _c(self):
        "Secret method to convert to str, incrememting num_comparisons by len(self)"
        mockstr.num_comparisons += len(self)
        return _unmockstr(self)

    def _a(self):
        "Secret method to convert to str, incrememting num_accesses by len(self)"
        mockstr.num_accesses += len(self)
        return _unmockstr(self)

    # Any piece of self returned by normal methods should be a mockstr, not a str.
    def upper(self):        return mockstr(self._a().upper())
    def lower(self):        return mockstr(self._a().lower())
    def title(self):        return mockstr(self._a().title())
    def capitalize(self):   return mockstr(self._a().capitalize())
    def swapcase(self):     return mockstr(self._a().swapcase())
    def strip(self):        return mockstr(self._a().strip())
    def lstrip(self):       return mockstr(self._a().lstrip())
    def rstrip(self):       return mockstr(self._a().rstrip())
    def split(self, *args): return map(mockstr, self._a().split(*args))
    def rsplit(self, *args):return map(mockstr, self._a().rsplit(*args))
    def join(self, *args):  return mockstr(self._a().join(*args))## Any piece of self

print "----------------"
