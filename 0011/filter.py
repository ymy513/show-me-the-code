#! usr/bin/env python
# encoding:utf-8
def filter(word):
    txt = open("filtered_words.txt")
    words = []
    for line in txt:
        for x in line.split():
            words.append(x)    
    for i in xrange(len(words)):
        #print words[i]
        if word == words[i]:
            return True
    return False


print "type quit() to quit."
word = raw_input("Please type something > ")
while(word != "quit()"):
    bo = filter(word)
    if bo:
        print "Freedom"
    else:
        print "Human Rights"
    word = raw_input("Please type something > ")