#! usr/bin/env python
# encoding:utf-8

print "type quit() to quit."
txt = open("filtered_words.txt").read()
words = txt.split('\n')

sentence = raw_input("Please type something > ")
while(sentence != "quit()"):
    
    for x in words:
        if sentence.find(x)!=-1:
            sentence = sentence.replace(x,'*'*len(x))
    
    print sentence 
            
    #print ' '.join(word)
    sentence = raw_input("Please type something > ")