"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['Asia'] = 'India'
locations['Asia'] ={'India' :['Bangalore']}
locations['North America']['USA'].append('Atlanta')
locations['Africa'] = 'Egypt'
locations['Africa'] = {'Egypt': ['Cairo']}
locations['Asia'].update({'China' :['Shanghai']})

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""
print('1')
for cities in sorted(locations['North America']['USA']):
    print(cities)
print('2')
city = []
for country in locations['Asia']:
    for cities in locations['Asia'][country]:
        city.append(cities + " - " + country)
for cit in sorted(city):
    print(cit)
