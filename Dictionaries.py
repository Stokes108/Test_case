# person={'first_name': "Adam", "last_name": "Nelson", "age": 23, "location": "Ypsi"}

# print (person['first_name'])
# print (person['last_name'])
# print (person['age'])
# print (person['location'])

# fav_nums={
#     "loop": "a way to cycle thrtough a list of data",
#     "conditional": "a statment that can be true or false and helps sort things",
#     "function": "a piece of code that can be handed information and return something/or do something",
#     "print statement": "this prints information from the display screen",
#     "list": "an assortment of data that can be moved around and is sorted with indices",
#     "dictionaries": "an infinate amoutn of key-value pairs"
#     }

# print ("The python dictionary is!!!!!!\n")

# for i in fav_nums.keys():
#     print (f"{i} : {fav_nums[i]}")

# rivers={'ganga': 'India', "nile": "Egypt", "mississippi": "USA"}

# # for r in rivers.keys():
# #     print (f"The {r.title()} river runs through {rivers[r].title()}!")

# for r in rivers.keys():
#     print (r.title())
#     print (rivers[r] + "\n")


# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phIl': 'python',
# }

# fav_lang_keys= [x.lower() for x in favorite_languages.keys()]

# should_take={
#     'jEn' : 'python',
#     'jimmy' : 'java',
#     "brooke" : 'c++',
#     "EdwArd" : 'c'
# }

# for person in should_take.keys():
#     if person.lower() in fav_lang_keys:
#         print (f"Thank you {person} for responding to this poll")
#     else:
#         print(f"Dear {person} please take this poll ASAP... or else")

# person1={'first_name': "Adam", "last_name": "Nelson", "age": 23, "location": "Ypsi"}
# person2={'first_name': "Raghav", "last_name": "Bhat", "age": 21, "location": "Ypsi"}
# person3={'first_name': "Harivilasa", "last_name": "Das", "age": 23, "location": "Raleigh"}

# persons=[person1, person2, person3]

# for person in persons:
#     full_name= person["first_name"] + " " + person["last_name"]
#     print(f"\nFull name: {full_name}")
#     print("Age: " + str(person["age"]) + "\nCity: " + person["location"])


# favorite_places={
#     "ignacio": ["Gita Nagari", "New Vrindavan", "Puri"],
#     "bernard" : ["Detroti", "Harmony collective", "Gainsville"],
#     "ruby" : ["bahamas", 'New York', "radha Kund"]
#     }

# for person in favorite_places.keys():
#     print (f"{person.title()}'s favorite places are:")
#     for i in favorite_places[person]:
#         print (f"   {i}")

# I changed things here!

# cities={
#     "Detroit": {"country": "America", "population" : "600k", "fact": "Great Hare Krishna Temple"},
#     "Calcutta": {"country": "India", "population" : "10m", "fact": "Prabhupada's Birthplace"},
#     "Radha Kund": {"country": "India", "population" : "6k", "fact": "Most sacred place in the universe"}
# }

# for city, city_info in cities.items():
#     print (city)
#     country, pop, fact= city_info["country"], city_info["population"], city_info["fact"]
#     print(f"    Country: {country} \n    Population: {pop} \n    Fun Fact: {fact} \n")





