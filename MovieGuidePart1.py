# Create a dictionary that will display 5 data elements
my_jordans = {
    '1985': 'Air Jordan 1',
    '1986': 'Air Jordan 2',
    '1988': 'Air Jordan 3',
    '1989': 'Air Jordan 4',
    '1990': 'Air Jordan 5'}
for values in my_jordans.values():
    print(values)
print()

# Add a new element to the dictonary
a = my_jordans    
a['1991'] = 'Air Jordan 6'
print(a)
print()

# Delete an element from the dictionary
del a['1985']
print(a)
print()