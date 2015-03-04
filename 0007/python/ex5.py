my_name = 'Mengyun Yang'
my_age = 18
my_height = 167
my_weight = 'hahaha'
my_eyes = 'black'
my_teeth = 'White'

print "Let's talk about %s" % my_name
print "She is %d cm tall" % my_height
print "She got %s eyes and %s hair" %(my_eyes,my_teeth)

hilarious = False
joke_evaluation ="Isn't that joke so funny? %r"
print joke_evaluation % hilarious

print "Mary had a little lamb"
print "Its fleece was white as %s." % "snow"
print "And everywhere that Mary went."
print "."*10

end1="C"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"

print end1+end2+end3+end4+end5+end6

formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % ("I had this thing","That you could type up right","But it didn't sing","So I said goodnight")

print """
there is something going on here
with the three double-quotes
we will be able to type as much as we like
even 4 lines
"""

print "How old are you?",
age=raw_input()
print "How tall are you?",
height=raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you are %r old, %r tall and %r heavy" %(
	age,height,weight)


age = raw_input("How old are you")
print age