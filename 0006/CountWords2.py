#!/usr/bin/env python
import os,sys
from collections import Counter


for txtfile in os.listdir(sys.argv[1]):
    txt=open(os.path.join(sys.argv[1],txtfile))
    wordcount=Counter(txt.read().split())
    maxword = max(wordcount.values())
    print [key for key, val in wordcount.iteritems() if val == maxword]    
