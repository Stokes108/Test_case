def favorite_book(title):
    print (f"My favorite book is {title}!")

# favorite_book("Srimad bhagavatam")



def describe_pet(pet_name, animal_type='dog'):

    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


def make_shirt(size="large", text="I love Python"):
    print (f"The size of the shirt is {size} and it says {text}")

# make_shirt("medium", "babies r cool")
# make_shirt(size="medium",text="booyah")
# # make_shirt(text= "This is how we do it now", "small")

# make_shirt()
# make_shirt("medium")
# make_shirt("small", text="hommies in the land")

def describe_city(name, country="USA"):
    print (f"{name.title()} is in {country.title()}")

# describe_city("Oakland")
# describe_city("Paris", "France")
# describe_city("calcutta", "India")

def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
# musician = build_person('jimi', 'hendrix', 7)
# print (musician)



def city_names(city, country):

    location = city.title()+ ", " +country.title()
    return location

# print(city_names("Detroit", "america"))
# print(city_names("Bombay", "India"))
# print(city_names("Moscow", "russia"))


def make_album (artist, title, track=''):
    album= {"artist_name": artist, "album_title": title}
    
    if track:
        album["num_tracks"] = track

    return album

# while True:
#     print("Please tell me an album")
#     print("(enter 'q' if you would like to leave)")

#     artist_name= input ("Please input artist's name: ")
#     if artist_name == "q":
#         break

#     album_title= input ("Please input album title: ")
#     if album_title == "q":
#         break

#     print(make_album(artist_name, album_title))

            
    
# magicians=["Amazing Tony", "Spontaneous Chad", "Marvelous Marvin"]

def show_magicians(names):
    for magician in names:
        print (f"Hello {magician}, thank you for coming to the show!")

def make_great(names):

    for i, s in enumerate(names):
        names [i]= "The Great " + s

    return names


# new_magicians= make_great(magicians[:])

# show_magicians(magicians)
# show_magicians(new_magicians)


def make_sandwiches(size, *toppings):
    print(f"\nWe are making your {size.lower()} sandwich with:")
    for topping in toppings:
        print(f"    -{topping}")


# make_sandwiches("Medium","olives", "tomatoes")
# print(make_sandwiches("Small","peppers", "cucumbers", "tomatoes", "celery"))


def do_nothing():
    print("do nothing")

print (do_nothing)

# make_sandwiches("large","olives", "mustard", "broccoli", "love", "carrots")


def make_car(make, model, **car_stats):
    car={}
    car["make"] = make
    car["model"] = model

    for k in car_stats.keys():
        car[k]= car_stats[k]
    return car

# car = make_car('subaru', 'outback', color='blue', tow_package=True, doors= 4, sunroof= True)

# print (car)


# print(make_album("Biggie smalls", "Ready to die", "8"))
# print(make_album("NF", "Perception"))
# print(make_album("Bethovan", "Quartet"))


