travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, number_visited, cities):
  dictionary ={"Country":country,"visits": number_visited, "cities": cities}

#   or
#   dictionary['country'] = country
#   dictionary['visits'] = number_visited
#   dictionary['cities'] = cities
  travel_log.append(dictionary)


#🚨 Do not change the code below
add_new_country(country="Russia", number_visited= 2, cities= ["Moscow", "Saint Petersburg"])
print(travel_log)



