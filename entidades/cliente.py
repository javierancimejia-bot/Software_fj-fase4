"""
Clase Cliente con validaciones.
"""

from .excepciones import ClienteError


class Cliente:
    """Representa un cliente del sistema Software FJ."""
    
    def __init__(self, identificacion, nombre, email, telefono):
        self._identificacion = identificacion
        self._nombre = None
        self._email = None
        self._telefono = None
        
        try:
            self.validar_datos(nombre, email, telefono)
            self._nombre = nombre
            self._email = email
            self._telefono = telefono
        except ClienteError as error:
            print(f"Error creando cliente: {error}")
            raise
    
    def validar_datos(self, nombre, email, telefono):
        """Valida que los datos del cliente sean correctos."""
        if not nombre or not email or not telefono:
            raise ClienteError("Datos incompletos")
        if "@" not in email:
            raise ClienteError("Email inválido")
    
    def validar(self):
        """Retorna True si el cliente es válido."""
        return bool(self._nombre and self._email and self._telefono)
    
    def __str__(self):
        return f"Cliente {self._identificacion}: {self._nombre} ({self._email})"
