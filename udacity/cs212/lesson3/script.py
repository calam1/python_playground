text = 'christopher'
match_pattern = 'hri'

#print "all of text: %s" % text
#print "first index of text: %s" % text[0]

def search(pattern, txt):
    for i in range(len(txt)):
        print 'iterate txt:', txt[i:]
        match(pattern, txt[i:])


def match(pattern, txt):
    if txt.startswith(pattern):
        print 'search:', txt

search(match_pattern, text)
