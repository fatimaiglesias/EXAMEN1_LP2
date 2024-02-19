#Implementa polimorfismo:
#Crea una clase abstracta Animal con un método abstracto hacer_sonido().

#Crea clases concretas que hereden de Animal, por ejemplo, Perro y Gato, e 
#implementa el método hacer_sonido para cada uno de ellos de manera que refleje
# el sonido específico que hace cada animal.

#Demuestra cómo se pueden crear instancias de Perro y Gato y cómo llamar al método 
# hacer_sonido en objetos de ambas clases, mostrando así el polimorfismo.

class Animal:
    def __init__(self, nombreAnimal, sonido):
        self.nombreAnimal = nombreAnimal
        self.sonido = sonido
        
    def hacer_sonido(self): 
        print(f"El animal es: {self.nombreAnimal} y hace: {self.sonido}")
        
        
class Perro(Animal):
    def __init__(self, nombreAnimal, sonido):
        super().__init__(nombreAnimal, sonido)
        
    def hacer_sonido(self): 
        print(f"El perro se llama: {self.nombreAnimal} y ladra: {self.sonido}")
        
class Gato(Animal):
    def __init__(self, nombreAnimal, sonido):
        super().__init__(nombreAnimal, sonido)
        
    def hacer_sonido(self): 
        print(f"El gato se llama: {self.nombreAnimal} y maulla: {self.sonido}")
        

#Creando objetos o instancias
        
perro1 = Perro("Bobby", "WUAU WUAU")
gato1 = Gato("Felix", "MIAU MIAU")
perro2 = Perro("Firulais", "WUAU WUAU")
gato2 = Gato("Lulu", "MIAU MIAU")


#llamando al metodo hacer_sonido

animales = [perro1, gato1, perro2, gato2]
for animal in animales:
    animal.hacer_sonido()