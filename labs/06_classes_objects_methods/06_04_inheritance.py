'''
Build on the previous exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercise.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

'''
subclass
Magicals: MOM :Auror Office
Magicals: Azkaban
'''
from datetime import datetime


class Magicals:
    '''
    This class defines the people in Magical world
    '''

    # class attribute
    pets = ("owl", "rat", "cat", "toad", "snake", "others")
    origins = ("muggle-born", "half-blood", "pure-blood")

    def __init__(self, name, country, gender, age, origin=1, pet=0):
        self.name = name
        self.country = country
        self.gender = gender
        self.pet = pet
        self.age = age
        self.origin = origin

    def __str__(self):
        if self.gender.upper() == "F":
            return f"She is a {self.age} year old {Magicals.origins[self.origin]} witch from {self.country}."
        elif self.gender.upper() == "M":
            return f"He is a {self.age} year old {Magicals.origins[self.origin]} wizard from {self.country}."
        else:
            return f"This is a {self.age} year old {Magicals.origins[self.origin]} magical person from {self.country}."\
                f"The gender of this person is unknown."

    def check_student(self): # assume in total 7 years in wizarding schools (11 to 18 years of age)
        if int(self.age) > 18:
            print(f"{self.name.capitalize()} has already graduated and not a student anymore.")
        elif int(self.age) < 11:
            print(f"{self.name} is too young to be a student in the wizarding world.")
        else:
            print(f"{self.name} should be a student, unless is of no magic.")


# objects for class Magicals
Harris = Magicals("Harris","England", "M", 15, 2, 3) #  "Slytherin", "Hogwarts",
Olga = Magicals("Olga","Russia", "F", 20, 1, 2) #  "Polarperasky",  "Pistburger",
Emmanuel = Magicals("Emmanuel","France", "M", 11, 0, 0) # "Chapollier" "Beauxbaton",
Akram = Magicals("Akram","Iran", "F", 7, 0, 5) # "Farshidarin", "Ramdoondish",

Akram.check_student()


# subclass of Magicals
class Azkaban(Magicals):
    '''
    Azkaban is a subclass of Magicals and it defines the prisoners in this highly secured prison.
    '''

    # 6 different types of status predefined (0,1,2,3,4,5)
    status_list = ("unknown", "incarcerated", "escaped", "deceased", "released", "pardoned")

    # 6 different types of crimes predefined (0,1,2,3,4,5)
    crime_list = ("Forbidden curses", "Violation of Wizarding Secrecy", "Death Eater",
                  "Violation of Magical Creature Laws", "Murder", "Attacking muggles")

    def __init__(self, name, country, gender, age, year_of_admission, crimes, conviction, current_status):
        super().__init__(name, country, gender, age)
        self.year_of_admission = year_of_admission
        self.crimes = crimes
        self.conviction = conviction
        self.current_status = current_status

    def __str__(self):
        return f"{self.name} is currently {Azkaban.status_list[self.current_status]} from Azkaban."


Lucius_Malfoy = Azkaban("Malfoy", "England", "M", 40, 1996, 2, "Life", 5)
print(Lucius_Malfoy)


# subclass of Magicals
class MOM(Magicals):
    '''
    MOM stands for Ministry of Magic.
    This class is a subclass of Magicals and it defines the staff of the Ministry.
    Inputs:
    '''

    def __init__(self, name, country, gender, age, start_service, department=""):
        super().__init__(name, country, gender, age)
        self.start_service = start_service
        self.department = department

    def __str__(self):
        service = datetime.now().year - int(self.start_service)
        return f"{self.name} has been working in {self.department} for {service} years."


Arthur_Weasley = MOM("Weasley", "UK", "M", 45, 1970, "Muggle Relation")
print(Arthur_Weasley)


# subclass of MOM
class Aurors(MOM):
    '''
    Auror Office is the main division of Department of Magical Law Enforcement which specifically deals with
    the capture of Dark Witches and Wizards.
    This subclass defines the Aurors had and have worked in Auror Office.
    Inputs:
    '''
    def __init__(self, name, country, gender, age, start_service, number_of_arrest, status):
        super().__init__(name, country, gender, age, start_service)
        self.number_of_arrest = number_of_arrest
        self.status = status

    def __str__(self):
        return f"{self.name} is {self.status} and has made {self.number_of_arrest} arrests as of now."

    def new_arrest(self):
        self.number_of_arrest += 1


Tonks = Aurors("Tonks", "Ireland", "f", 28, 1995, 10, "in-service")
print(Tonks)
Tonks.new_arrest()
print(Tonks)

