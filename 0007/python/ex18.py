    # this one is like your scripts with argv
def print_two(*args):
	arg1,arg2,arg3=args
	print "arg1: %r, arg2: %r, arg3: %r" %(arg1, arg2, arg3)

# ok, that *args is actually pointless, we can just fo this
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" %arg1

# this one takes no arguments
def print_none():
	print "I got nothing"

print_two("mengyun","yang","Offer!")
print_two_again("mengyun","yang")
print_one("OFFER!")
print_none()