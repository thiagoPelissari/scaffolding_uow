from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def locomover(self) -> str:
        pass
    
    @abstractmethod
    def comunicar(self) -> str:
        pass

        
class Cachorro(IAnimal):
    def locomover(self) -> str:
        return "O cachorro está andando"
    
    def comunicar(self) -> str:
        return "O cachorro está latindo"
    


class Gato(IAnimal):
    def locomover(self) -> str:
        return "O gato está andando suavemente"
    
    def comunicar(self) -> str:
        return "O gato está miando"
    


class Sitio():
    def __init__(self, animal: IAnimal):
        self.animal = animal
        
    def mostrar_qualidades(self):
        print(self.animal.comunicar())
        print(self.animal.locomover())
        


if __name__ == "__main__":
    cachorro = Cachorro()
    sitio = Sitio(cachorro)
    sitio.mostrar_qualidades()
    
    print("Hello World")
