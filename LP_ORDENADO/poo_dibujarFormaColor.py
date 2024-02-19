#Explora la herencia múltiple y el uso de super():
#Crea una clase base Forma con un método dibujar() que simplemente imprime "Dibujando forma".

#Crea otra clase base Color con un método pintar() que imprime "Pintando con [color]" donde [color] 
# es un atributo de la clase.

#Crea una clase CuadradoColorido que herede de ambas clases, Forma y
# Color, y utiliza super() para llamar a los métodos de las clases padres de manera 
# adecuada para demostrar cómo se puede trabajar con herencia múltiple.

class Forma:
    
    def dibujar(self):
        print("Dibujando forma")
        
    
class Color:
    def __init__(self,color):
        self.color = color
    
    def pintar(self):
        print(f"Pintando con {self.color}")
        
class CuadradoColorido(Forma,Color):
    def __init__(self,color):
        super(). __init__(color)
        
    def dibujar_pintar(self):
        super().dibujar()
        super().pintar()
        
cuadrado = CuadradoColorido("Amarillo")
cuadrado.dibujar_pintar()