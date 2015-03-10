#! usr/bin/env python
# encoding:utf-8

print "type quit() to quit."
word = raw_input("Please type something > ")
txt = open("filtered_words.txt").read()
words = []
for x in txt.split():
    words.append(x)    

while(word != "quit()"):
    
    if word in words:
        print "Freedom"
    else:
        print "Human Rights"
    word = raw_input("Please type something > ")