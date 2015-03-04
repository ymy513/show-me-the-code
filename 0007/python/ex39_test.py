import hashmap

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida','FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities,'CA','San Francisco')
hashmap.set(cities,'MI','Detroit')
hashmap.set(cities,'FL','Jacksonville')

# add some more cities
hashmap.set(cities,'NY','New York')
hashmap.set(cities,'OR','Portland')

# print out some cities
print '-'*10
print "NY State has: %s" % hashmap.get(cities,'NY')
print "OR State has: %s" % hashmap.get(cities,'OR')

# print every state abbreviation
print '-'*10
hashmap.list(states)
