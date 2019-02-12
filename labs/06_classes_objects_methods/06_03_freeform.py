'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

'''
import math
import random


class Muggles:
    '''
    define the muggle aspect of a person
    '''

    # class attributes
    attitude_list = ["friendly", "neutral", "negative"]
    '''
    attitude toward the Wizarding World (0, 1, 2)
    '''
    link_list = ["first degree", "second degree", "third degree", "none"]
    '''
    degree of closeness to a Wizard or Witch (0,1,2,3)
    first degree = children, parents, syblings
    second degree = other blood relationship
    third degree = close vacinity (neigbhour, colleague etc)
    none = other relations
    '''

    def __init__(self, country, gender, age, attitude=1, link=3):
        self.country = country
        self.gender = gender
        self.age = age
        self.attitude = attitude
        self.link = link

    def __str__(self):
        if self.gender.upper() == "F":
            return f"She is a {self.age} year old muggle from {self.country} " \
                f"with {Muggles.link_list[self.link]} relation to the wizarding world."
        elif self.gender.upper() == "M":
            return f"He is a {self.age} year old muggle from {self.country} " \
                f"with {Muggles.link_list[self.link]} relation to the wizarding world."
        else:
            return f"This is a {self.age} year old muggle from {self.country} " \
                f"with {Muggles.link_list[self.link]} relation to the wizarding world. " \
                f"The gender of this person is unknown."

    def change_of_attitude(self):
        if int(self.age) >= 90 and self.gender.upper() == "M":
            print("It's impossible to change his attitude toward the wizarding world!")
        elif self.gender.upper() == "F":
            need_years = math.floor(math.sqrt(len(self.country) * (100 % int(self.age))))
            print(f"She needs {need_years} years to change her attitude toward the wizarding world.")
        else:
            need_years = math.floor(math.sqrt(len(self.country) * (100 % int(self.age)))) + 2
            print(f"He needs {need_years} years to change his attitude toward the wizarding world.")

    def relation_update(self):
        if random.randint(0, 1) == 0:
            self.link = min(0, max(random.randint(0, 3) + self.link, 2))
        else:
            self.link = min(0, max(- random.randint(0, 3) + self.link, 2))


# objects for class Muggles
Martin = Muggles("Austria", "m", 93, 2,3)
Ryan = Muggles("USA", "M", 35, 1, 2)
Kim = Muggles("Canada", "F", 15, 0, 0)
May = Muggles("England", "f", 60, 0, 1)


print(May)
May.relation_update()
print(May)

class Magicals:
    '''

    '''

    # class attribute
    pets = ["owl", "rat", "cat", "toad", "snake", "others"]
    origins = ["muggle-born", "half-blood", "pure-blood"]

    def __init__(self, country, school, gender, age, origin=1, pet=0, marital = False):
        self.country = country
        self.school = school
        self.gender = gender
        self.pet = pet
        self.age = age
        self.origin = origin
        self.marital = marital

    def __str__(self):
        if self.gender.upper() == "F":
            return f"She is a {self.age} year old {Magicals.origins[self.origin]} witch from " \
                f"{self.school} School of Witchcraft and Wizardry, in {self.country}."
        elif self.gender.upper() == "M":
            return f"He is a {self.age} year old {Magicals.origins[self.origin]} wizard from " \
                f"{self.school} School of Witchcraft and Wizardry, in {self.country}."
        else:
            return f"This is a {self.age} year old {Magicals.origins[self.origin]} magical person from" \
                f"{self.school} School of Witchcraft and Wizardry, in {self.country}."\
                f"The gender of this person is unknown."

    def years_to_grad(self): # assume in total 7 years in wizarding schools (11 to 18 years of age)
        if self.gender.upper() == "F":
            if int(self.age) > 18:
                print(f"She has already graduated from {self.school}.")
            elif int(self.age) < 11:
                print(f"She has {11 - int(self.age)} years left before she could enter {self.school},"
                      f"if she receives the letter. ")
            else:
                print(f"She has {18 - int(self.age)} years to graduation.")
        else:
            if int(self.age) > 18:
                print(f"He has already graduated from {self.school}.")
            elif int(self.age) < 11:
                print(f"He has {11 - int(self.age)} years left before he could enter {self.school},"
                      f"if he receives the letter. ")
            else:
                print(f"He has {18 - int(self.age)} years to graduation.")

    def __add__(self, others):
        if self.gender == "M":
            return Magicals(self.country, self.school, "F", 0)
        else:
            return Magicals(others.country, others.school, "M", 0)


# objects for class Magicals
Harris = Magicals("England", "Hogwarts", "M", 15, 2, 3) #  "Slytherin",
Olga = Magicals("Russia", "Pistburgervich", "F", 20, 1, 2) #  "Polarperasky"
Emmanuel = Magicals("France", "Beauxbaton", "M", 21, 0, 0) # "Chapollier"
Akram = Magicals("Iran", "Ramdoondish", "F", 7, 0, 5) # "Farshidarin"


class Animals:

    # class attributes
    book_name = "Fantastic Beasts and Where to find them" # Classic book for magical creatures
    shop_name = "TaoTao" # Amazon in the wizarding world

    def __init__(self, world, skills, powers, life_span, rarity, in_book=False, in_shop=False):
        self.world = world
        self.skills = skills
        self.powers = powers
        self.life_span = life_span
        self.rarity = rarity
        self.in_book = in_book
        self.in_shop = in_shop

    def __str__(self):
        if self.in_shop is True:
            can_ = ""
        else:
            can_ = "not"

        return f"An animal from the {self.world} world which can {self.skills} " \
            f"with a life span of {self.life_span} years, and {self.rarity} to find.\n" \
            f"You can{can_} find it in {Animals.shop_name} shop at the moment."


# objects
phoenix = Animals("Magical", "fly", "reborn", "1,000,000,000", "hard", True, False)
hippo = Animals("Muggle", "swim", "eat mud", "50", "easy", False, True)
nagini = Animals("Magical", "kill", "talk", "1,203,400", "extremely hard", True, False)
mono = Animals("Muggle", "climb", "play", "100", "not hard", False, False)


print(Martin)
Ryan.change_of_attitude()
Olga.years_to_grad()
print(nagini)
Sasha = Olga + Emmanuel
print(Sasha)


