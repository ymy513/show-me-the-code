#!/usr/bin/env python
import re
from sys import argv
from string import punctuation
from os.path import exists

def file_read():
    filename=raw_input("input your filename > ")
    if exists(filename):
        txt=open(filename)
        print "Here's your file %r:" %filename
        return txt.read()
    else:
        print "There is no file %r." %filename
        exit()

def counter(filename):
    r = re.compile(r'[{}]'.format(punctuation))
    words = r.sub(' ',filename)
    amount = len(words.split())
    return amount

if __name__=="__main__":
    filename = file_read()
    result = counter(filename)
    print "There are %r words in this article." % result
