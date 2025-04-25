from enum import Enum
#definición de clase
class Auto():
    brand = None
    model = None
    motor = None
    class Gas_type(Enum):
        GASOLINA = "Gasolina"
        BIOETANOL = "Bioetanol"
        DIESEL = "Diesel"
        BIODIESEL = "Biodiesel"
        GASNATURAL = "Gas natural"
    class Car_type(Enum):
        CARRODECIUDAD = "Carro de ciudad"
        SUBCOMPACTO = "Subcompacto"
        COMPACTO = "Compacto"
        FAMILIAR = "Familiar"
        EJECUTIVO = "Ejecutivo"
        SUV = "Suv"
    doors = None
    free_seats = None
    max_velocity = None
    class Color_type(Enum):
        BLANCO = "Blanco"
        NEGRO = "Negro"
        ROJO = "Rojo"
        NARANJA = "Naranja"
        AMARILLO = "Amarillo"
        VERDE = "Verde"
        AZUL = "Azul"
        VIOLETA = "Violeta"
    current_speed = None



#constructor
    def __init__(self,brand,model,motor,Gas_type,Car_type,doors,free_seats,max_velocity,Color_type,current_speed):
        self.brand = brand
        self.model = model
        self.motor = motor
        self.Gas_type = Gas_type
        self.Car_type = Car_type
        self.doors = doors
        self.free_seats = free_seats
        self.max_velocity = max_velocity
        self.Color_type = Color_type
        self.current_speed = current_speed



#getters
    def getBrand(self):
        return self.brand
    def getModel(self):
        return self.model
    def getMotor(self):
        return self.motor
    def getGas_type(self):
        return self.Gas_type.name
    def getCar_type(self):
        return self.Car_type.name
    def getDoors(self):
        return self.doors
    def getFreeSeats(self):
        return self.free_seats
    def getMaxVelocity(self):
        return self.max_velocity
    def getColor_type(self):
        return self.Color_type.name
    def getCurrentSpeed(self):
        return self.current_speed
#setters



    def setBrand(self,newBrand):
        self.brand = newBrand
    def setModel(self,newModel):
        self.model = newModel
    def setMotor(self,newMotor):
        self.motor = newMotor
    def setGas_type(self,newGas):
        self.Gas_type = newGas
    def setCar_type(self,newCar):
        self.Car_type = newCar
    def setDoors(self,newDoors):
        self.doors = newDoors
    def setFreeSeats(self,newFreeSeats):
        self.free_seats = newFreeSeats
    def setMaxVelocity(self,newMaxVelocity):
        self.max_velocity = newMaxVelocity
    def setColor_type(self,newColor):
        self.Color_type = newColor
    def setCurrentSpeed(self,newCurrentSpeed):
        self.current_speed = newCurrentSpeed




#metodos de velocidad
    def accelerate(self,increment_speed):
        if self.current_speed + increment_speed > self.max_velocity:
            print("No se puede acelerar más del limite")
            return
        elif increment_speed < 0:
            print("No se puede acelerar con numeros negativos")
            return
        else:
            self.current_speed += increment_speed
            print(f"Se aceleró hasta {self.current_speed} km/h")




    def decelerate(self,decrement_speed):
        if decrement_speed < 0:
            print("No se puede desacelerar con numeros negativos")
            return
        elif self.current_speed - decrement_speed < 0:
            print("No se puede desacelerar tanto")
            return
        else:
            self.current_speed -= decrement_speed
            print(f"Se frenó hasta {self.current_speed} km/h")



    def stop(self):
        self.current_speed = 0
        print("Se frenó la velocidad es de 0 km/h")



    def calculate_time(self,travel_distance):
        if travel_distance != 0 and travel_distance > 0 and self.current_speed > 0:
            return print(f"El tiempo estimado de llegada es {round(travel_distance/self.current_speed,2)} horas")
        elif self.current_speed == 0:
            print("El vehiculo está detenido")
            return
        else:
            print("Error en la entrada de datos")
            return



    def show_attributes(self):
        print(self.getBrand(),self.getModel(),self.getMotor(),self.getGas_type(),self.getCar_type(),self.getDoors(),self.getFreeSeats(),self.getMaxVelocity(),self.getColor_type(),self.getCurrentSpeed())
        



#ejecución
if __name__ == "__main__":
    auto1 = Auto("Mercedes",2000,80,Auto.Gas_type.GASOLINA,Auto.Car_type.CARRODECIUDAD,4,4,150,Auto.Color_type.NEGRO,100)
    print("GETTERS:")
    print(auto1.getBrand())
    print(auto1.getModel())
    print(auto1.getMotor())
    print(auto1.getGas_type())
    print(auto1.getCar_type())
    print(auto1.getDoors())
    print(auto1.getFreeSeats())
    print(auto1.getMaxVelocity())
    print(auto1.getColor_type())
    print(auto1.getCurrentSpeed())
    print("-----------------------")
    print("SETTERS:")
    auto1.setBrand("Suzuki")
    auto1.show_attributes()
    auto1.accelerate(20)
    auto1.decelerate(50)
    auto1.calculate_time(200)
    auto1.stop()
    auto1.calculate_time(40)
