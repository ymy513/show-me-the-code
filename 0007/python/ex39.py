# create a mapping of state to abbreviation
states = {
	'Oregon':'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
}

# create a basic set of states and some cities in them
cities ={
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
}

# add some more cities
cities['NY']='New York'
cities['OR']='Portland'

# print out some cities
print'-'*10
print "NY State has: ",cities['NY']

# print some states
print '-'*10
print 'Michigan has: ',cities[states['Michigan']]

# print every state abbreviation
print '-'*10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-'*10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-'*10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-'*10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')


if not state:
	print "Sorry, no Texas"
	
# get a city with a default value
city = cities.get('TX','Does not exist')
print "The city for the state 'TX' is: %s" % city