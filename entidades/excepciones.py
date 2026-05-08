"""
Excepciones personalizadas para el sistema Software FJ.
"""

class ClienteError(Exception):
    """Error relacionado con datos de cliente."""
    pass

class ServicioError(Exception):
    """Error relacionado con servicios."""
    pass

class ReservaError(Exception):
    """Error relacionado con reservas."""
    pass
