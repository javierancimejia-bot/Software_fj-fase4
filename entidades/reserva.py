import logging
from .excepciones import ReservaInvalidaError, ServicioNoDisponibleError, CostoInconsistenteError

logger = logging.getLogger(__name__)


class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def validar_reserva(self):
        if self.cliente is None:
            raise ReservaInvalidaError("La reserva no puede crearse sin cliente.")
        if self.servicio is None:
            raise ReservaInvalidaError("La reserva no puede crearse sin servicio.")
        if not isinstance(self.duracion, int) or self.duracion <= 0:
            raise ReservaInvalidaError("La duración de la reserva debe ser un entero mayor que cero.")

    def confirmar(self):
        try:
            self.validar_reserva()
            self.servicio.validar_disponibilidad()
            costo = self.servicio.calcular_costo()
        except Exception as error:
            raise ReservaInvalidaError("No fue posible confirmar la reserva.") from error
        else:
            self.estado = "Confirmada"
            logger.info(
                "Reserva confirmada para %s con servicio %s. Costo: %s",
                self.cliente.nombre,
                self.servicio.nombre,
                costo
            )
            return costo
        finally:
            logger.info("Proceso de confirmación finalizado para la reserva de %s", self.cliente.nombre if self.cliente else "desconocido")

    def cancelar(self):
        self.estado = "Cancelada"
        logger.info("Reserva cancelada para %s", self.cliente.nombre if self.cliente else "desconocido")

    def procesar_reserva(self):
        try:
            costo = self.confirmar()
            return f"Reserva procesada con éxito. Costo total: {costo}"
        except ReservaInvalidaError as error:
            logger.error("Error al procesar reserva: %s", error)
            raise
