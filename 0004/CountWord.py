#!/usr/bin/env python
import re
import sys
from string import punctuation


def counter(filename):
    r = re.compile(r'[{}]'.format(punctuation))
    words = r.sub(' ',filename)
    amount = len(words.split())
    return amount

if __name__=="__main__":
    txt = open(sys.argv[1]).read()
    result = counter(txt)
    print "There are %r words in this article." % result
