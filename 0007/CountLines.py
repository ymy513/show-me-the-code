#!/usr/bin/env python
import os,sys

total_lines = 0
total_newlines = 0
total_comments = 0

for pyfile in os.listdir(sys.argv[1]):
    with open(sys.argv[1]+"/"+pyfile) as py:
        newlines = 0
        comments = 0
        for lines, item in enumerate(py):
            if item=='\n':
                newlines += 1
            if item.lstrip().startswith('#'):
                comments += 1
            pass
        total_comments += comments
        total_newlines += newlines
        total_lines += lines  
    print "%r has %d lines, including %d newlines and %d comments" %(pyfile,(lines+1),newlines,comments)

print "\nThere are %d lines, including %d newlines and %d comments in total" %(total_lines,total_newlines,total_comments)
