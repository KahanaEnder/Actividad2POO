from enum import Enum
class Person():
    name = None
    lastname = None
    id = None
    birth_year = None

    def __init__(self,name,lastname,id,birth_year):
        self.name = name
        self.lastname = lastname
        self.id = id
        self.birth_year = birth_year
    def show_attributes(self):
        print(self.name)
        print(self.lastname)
        print(self.id)
        print(self.birth_year)

persona1 = Person("Juan","Hoyos",190234872,2005)
persona2 = Person("José","Gerardo",212098312,2003)
if __name__ == "__main__":
    persona1.show_attributes()
    persona2.show_attributes()


