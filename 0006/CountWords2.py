#!/usr/bin/env python
import os,sys
import operator
from collections import Counter


for txtfile in os.listdir(sys.argv[1]):
    txt=open(sys.argv[1]+"/"+txtfile)
    wordcount=Counter(txt.read().split())
    
    print [key for key, val in wordcount.iteritems() if val == max (wordcount.values())] 
