"""
Clase Reserva que integra cliente + servicio.
"""

from .excepciones import ClienteError, ServicioError, ReservaError
from .cliente import Cliente
from .servicio import Servicio


class Reserva:
    """Representa una reserva de servicio."""
    
    def __init__(self, identificacion, cliente, servicio, duracion):
        self._identificacion = identificacion
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "pendiente"
        
        try:
            self.validar()
        except (ClienteError, ServicioError, ReservaError) as error:
            print(f"Error en reserva: {error}")
            raise
    
    def validar(self):
        """Valida cliente, servicio y duración."""
        if not self._cliente.validar():
            raise ClienteError("Cliente inválido")
        if not self._servicio.validar():
            raise ServicioError("Servicio inválido")
        if self._duracion <= 0:
            raise ReservaError("Duración inválida")
    
    def confirmar(self):
        """Confirma la reserva con cálculo de costo."""
        try:
            costo = self._servicio.calcular_costo_con_impuesto(self._duracion)
            print(f"Reserva confirmada. Costo: ${costo:.2f}")
            self._estado = "confirmada"
        except Exception as error:
            raise ReservaError("No se pudo confirmar") from error
        else:
            print("Confirmación exitosa")
    
    def cancelar(self):
        """Cancela la reserva."""
        self._estado = "cancelada"
    
    def __str__(self):
        return f"Reserva {self._identificacion}: {self._cliente} - {self._servicio.describir()} x{self._duracion}h [{self._estado}]"
