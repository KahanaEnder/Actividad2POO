from enum import Enum
class Planet():
    name:str = None
    satellites:int = 0
    mass:float = 0
    volume:float = 0
    diameter:int = 0
    avg_distance_sun:int = 0
    class Planet_type(Enum):
        ENANO = "ENANO"
        TERRESTRE = "TERRESTRE"
        GASEOSO = "GASEOSO"
    observable:bool = False
    def __init__(self,name,satellites,mass,volume,diameter,avg_distance_sun,Planet_type,observable):
        self.name = name
        self.satellites = satellites
        self.mass = mass
        self.volume = volume
        self.diameter = diameter
        self.avg_distance_sun = avg_distance_sun
        self.Planet_type = Planet_type
        self.observable = observable
    def show_attributes(self):
        print(self.name)
        print(self.satellites)
        print(self.mass)
        print(self.volume)
        print(self.diameter)
        print(self.avg_distance_sun)
        print(self.Planet_type.name) #Añadimos el metodo .name
        print(self.observable)
    def calculate_density(self):
        density = round((self.mass / self.volume),2)
        print(f"DENSIDAD:{density}")
    def isExterior(self):
        #Si el cinturón de asteroides se encuentra hasta un maximo de 3.4 UA y UA = 149.5 entonces cualquier planeta con avg_distance_sun > 149.5* 3.4 o 508.3 será exterior
        if self.avg_distance_sun > 508.3:
            print("El planeta es exterior")
        else:
            print("El planeta no es exterior")


planeta1 = Planet("Pluton",5,500.3,785.32,543,893,Planet.Planet_type.ENANO,True)
planeta2 = Planet("Santiago",3,20000,34442,4200,403,Planet.Planet_type.ENANO,False)


if __name__ == "__main__":
    planeta1.show_attributes()
    planeta1.calculate_density()
    planeta1.isExterior()
    planeta2.show_attributes()
    planeta2.calculate_density()
    planeta2.isExterior()