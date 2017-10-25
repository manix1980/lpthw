states = {
    'Queensland': 'QLD',
    'New South Wales': 'NSW',
    'Western Australia': 'WA',
    'South Australia': 'SA'
}

territories = {
    'Australian Capital Territory': 'ACT',
    'Tasmania': 'TAS',
    'Northern Territory': 'NT'
}

state_cities = {
    'WA':'Perth',
    'QLD':'Brisbane',
    'NSW':'Sydney',
    'SA':'Adelaide',
}

territory_cities = {
    'ACT':'Canberra',
    'TAS':'Hobart',
    'NT':'Darwin'
}

# print out some cities

print('-' * 10)
print(f"NSW has: ", state_cities['NSW'])
print(f"QLD has: ", state_cities['QLD'])
print(f"SA has: ", state_cities['SA'])
print(f"TAS has: ", territory_cities['TAS'])

# print out some states

print('-' * 10)
print(f"New South Wales' abbreviation is:", states['New South Wales'])
print(f"Queenslands' abbreviation is:", states['Queensland'])
print(f"Northern territories' abbreviation is:", territories['Northern Territory'])

# do it by using the state then cities dict

print('-' * 10)
print("NSW has: ", state_cities[states['New South Wales']])
print("QLD has: ", state_cities[states['Queensland']])
print("ACT has:", territory_cities[territories['Australian Capital Territory']])

# print every state abbreviation

print('-' * 10)

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

for territory, abbrev in list(territories.items()):
    print(f"{territory} is abbreviated {abbrev}")

# print every city in the states

for abbrev, city in list(state_cities.items()):
    print(f"{abbrev} state has {city}")

# print every city in the territories

for abbrev, city in list(territory_cities.items()):
    print(f"{abbrev} Territory has {city}")

# now do both at the same time

print('-' * 10)

for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {state_cities[abbrev]}")

for territory, abbrev in list(territories.items()):
    print(f"{territory} state is abbreviated {abbrev}")
    print(f"and has city {territory_cities[abbrev]}")

print('-' * 10)

state = states.get('Fiji')

if not state:
    print("Sorry there is no state Fiji")

city = state_cities.get('FIJI', 'Does Not Exist')
print(f"The city for the state 'FIJI' is: {city}")
