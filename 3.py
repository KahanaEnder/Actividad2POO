from enum import Enum
#definición de clase
class Auto():
    brand = None
    model = None
    motor = None
    class Gas(Enum):
        GASOLINA = "Gasolina"
        BIOETANOL = "Bioetanol"
        DIESEL = "Diesel"
        BIODIESEL = "Biodiesel"
        GASNATURAL = "Gas natural"
    class Car(Enum):
        CARRODECIUDAD = "Carro de ciudad"
        SUBCOMPACTO = "Subcompacto"
        COMPACTO = "Compacto"
        FAMILIAR = "Familiar"
        EJECUTIVO = "Ejecutivo"
        SUV = "Suv"
    doors = None
    free_seats = None
    max_velocity = None
    class Color(Enum):
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
    def __init__(self,brand,model,motor,Gas,Car,doors,free_seats,max_velocity,Color,current_speed):
        self.brand = brand
        self.model = model
        self.motor = motor
        self.Gas = Gas
        self.Car = Car
        self.doors = doors
        self.free_seats = free_seats
        self.max_velocity = max_velocity
        self.Color = Color
        self.current_speed = current_speed
#getters
    def getBrand(self):
        return self.brand
    def getModel(self):
        return self.model
    def getMotor(self):
        return self.motor
    def getGas(self):
        return self.Gas.name
    def getCar(self):
        return self.Car.name
    def getDoors(self):
        return self.doors
    def getFreeSeats(self):
        return self.free_seats
    def getMaxVelocity(self):
        return self.max_velocity
    def getColor(self):
        return self.Color.name
    def getCurrentSpeed(self):
        return self.current_speed
#setters
    def setBrand(self,newBrand):
        self.brand = newBrand
    def setModel(self,newModel):
        self.model = newModel
    def setMotor(self,newMotor):
        self.motor = newMotor
    def setGas(self,newGas):
        self.Gas = newGas
    def setCar(self,newCar):
        self.Car = newCar
    def setDoors(self,newDoors):
        self.doors = newDoors
    def setFreeSeats(self,newFreeSeats):
        self.free_seats = newFreeSeats
    def setMaxVelocity(self,newMaxVelocity):
        self.max_velocity = newMaxVelocity
    def setColor(self,newColor):
        self.Color = newColor
    def setCurrentSpeed(self,newCurrentSpeed):
        self.current_speed = newCurrentSpeed

#metodos de velocidad
    def accelerate(self,increment_speed):
        pass
    def decelerate(self,decrement_speed):
        pass
    def stop(self):
        self.current_speed = 0
    def calculate_time(self):
        pass
    def show_attributes(self):
        print(self.getBrand(),self.getModel(),self.getMotor(),self.getGas(),self.getCar(),self.getDoors(),self.getFreeSeats(),self.getMaxVelocity(),self.getColor(),self.getCurrentSpeed())
        



#ejecución
if __name__ == "__main__":
    auto1 = Auto("Mercedes",2000,80,Auto.Gas.GASOLINA,Auto.Car.CARRODECIUDAD,4,4,100,Auto.Color.NEGRO,100)
    print("GETTERS:")
    print(auto1.getBrand())
    print(auto1.getModel())
    print(auto1.getMotor())
    print(auto1.getGas())
    print(auto1.getCar())
    print(auto1.getDoors())
    print(auto1.getFreeSeats())
    print(auto1.getMaxVelocity())
    print(auto1.getColor())
    print(auto1.getCurrentSpeed())
    print("-----------------------")
    print("SETTERS:")
    auto1.setBrand("Suzuki")
    auto1.show_attributes()
