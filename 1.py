from enum import Enum
#declaración de la clase
class Person():
    name = None
    lastname = None
    id = None
    birth_year = None


#constructor
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



#objetos
persona1 = Person("Juan","Hoyos",190234872,2005)
persona2 = Person("José","Gerardo",212098312,2003)

#ejecución
if __name__ == "__main__":
    persona1.show_attributes()
    persona2.show_attributes()


