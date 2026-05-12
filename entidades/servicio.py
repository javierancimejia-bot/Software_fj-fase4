from abc import ABC, abstractmethod
from .excepciones import CostoInconsistenteError


class Servicio(ABC):
    def __init__(self, nombre, precio_base, disponible=True):
        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = disponible

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def calcular_costo(self, descuento=0):
        pass

    def validar_disponibilidad(self):
        if not self.disponible:
            raise RuntimeError(f"El servicio {self.nombre} no está disponible.")

    def calcular_con_impuesto(self, impuesto=0.19):
        costo = self.calcular_costo()
        if costo < 0:
            raise CostoInconsistenteError(
                f"El costo del servicio {self.nombre} no puede ser negativo."
            )
        return costo + (costo * impuesto)
