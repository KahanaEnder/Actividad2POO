import math
class Circle():
    radio = 0
    #constructor
    def __init__(self,radio):
        self.radio = radio
    #metodo de area
    def area(self):
        return print(f"El area del circulo es {round(math.pi * (self.radio**2),2)}cm cuadrados")
    #metodo de perimetro
    def perimeter(self):
        return print(f"El perimetro del circulo es {round(2 * math.pi * self.radio,2)}cm")
    


    
class Rectangle():
    base = 0
    altura = 0

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return print(f"El area del rectangulo es {round(self.base * self.altura,2)}cm cuadrados")
    def perimeter(self):
        return print(f"El perimetro del rectangulo es {round((self.base * 2) + (self.altura * 2),2)}cm")
    

        
class Square():
    lado = 0
    def __init__(self,lado):
        self.lado = lado
    def area(self):
        return print(f"El area del cuadrado es {self.lado ** 2}cm cuadrados")
    def perimeter(self):
        return print(f"El perimetro del cuadrado es {self.lado * 4}cm")
    

        
class Triangle():
    base = 0
    altura = 0
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def area(self):
        return print(f"El area del triangulo es {round(((self.base * self.altura) / 2),2)}cm cuadrados")
    

    def hypotenuse(self):
        hypotenuse = (math.sqrt((self.base ** 2 + self.altura ** 2)))
        return hypotenuse
    
    def show_hypotenuse(self):
        return print(f"La hipotenusa es {self.hypotenuse()}cm")


    def perimeter(self):
        return print(f"El perimetro del triangulo es {self.altura + self.base + self.hypotenuse()}cm")
    
    def triangle_type(self):
        if self.altura == self.base and self.base == int(self.hypotenuse()):
            return print("El triangulo es equilatero")
        elif self.altura == self.base or self.base == int(self.hypotenuse()) or self.altura == int(self.hypotenuse()):
            return print("El triangulo es isosceles")
        else:
            return print("El triangulo es escaleno")
        

if __name__ == "__main__":

    circunference1 = Circle(5)
    circunference1.area()
    circunference1.perimeter()
    rectangle1 = Rectangle(8,3)
    rectangle1.area()
    rectangle1.perimeter()
    cuadrado1 = Square(5)
    cuadrado1.area()
    cuadrado1.perimeter()
    triangulo1 = Triangle(3,4)
    triangulo1.area()
    triangulo1.perimeter()
    triangulo1.show_hypotenuse()
    triangulo1.triangle_type()