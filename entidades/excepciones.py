class ErrorSistemaFJ(Exception):
    """Excepción base para el sistema Software FJ."""
    pass


class ClienteInvalidoError(ErrorSistemaFJ):
    """Se lanza cuando el cliente no cumple validaciones."""
    pass


class ServicioNoDisponibleError(ErrorSistemaFJ):
    """Se lanza cuando un servicio no está disponible."""
    pass


class ReservaInvalidaError(ErrorSistemaFJ):
    """Se lanza cuando una reserva no es válida."""
    pass


class CostoInconsistenteError(ErrorSistemaFJ):
    """Se lanza cuando el cálculo de costo es inconsistente."""
    pass
