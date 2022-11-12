from abc import ABCMeta

#Se define la clase para el modelo abstracto
class AbstractModelo(metaclass=ABCMeta):
    def __init__(self, data):
        for llave, valor in data.items():
            setattr(self, llave, valor)
