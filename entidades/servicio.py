"""
Clases de servicios: abstracta + especializadas.
"""

from abc import ABC, abstractmethod


class Servicio(ABC):
    """Servicio abstracto base."""
    
    def __init__(self, identificacion, nombre, costo_base):
        self._identificacion = identificacion
        self._nombre = nombre
        self._costo_base = costo_base
    
    @abstractmethod
    def calcular_costo(self, duracion):
        """Calcula costo según tipo de servicio."""
        pass
    
    def calcular_costo_con_impuesto(self, duracion, impuesto=0.19):
        """Sobrecarga: versión con impuesto."""
        return self.calcular_costo(duracion) * (1 + impuesto)
    
    def describir(self):
        """Retorna descripción del servicio."""
        return f"Servicio {self._nombre} (${self._costo_base}/hora)"
    
    def validar(self):
        """Retorna True si el servicio es válido."""
        return self._costo_base > 0


class ReservaSala(Servicio):
    """Reserva de sala por hora."""
    
    def calcular_costo(self, duracion):
        return self._costo_base * duracion
    
    def describir(self):
        return f"Reserva de sala {self._nombre} por hora"


class AlquilerEquipo(Servicio):
    """Alquiler de equipo (costo fijo)."""
    
    def calcular_costo(self, duracion):
        return self._costo_base
    
    def describir(self):
        return f"Alquiler equipo {self._nombre} (fijo)"


class Asesoria(Servicio):
    """Asesoría especializada (premium)."""
    
    def calcular_costo(self, duracion):
        return self._costo_base * duracion * 1.5
    
    def describir(self):
        return f"Asesoría especializada {self._nombre}"
