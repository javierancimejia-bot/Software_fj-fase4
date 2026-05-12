import logging
from .excepciones import ClienteInvalidoError

logger = logging.getLogger(__name__)


class Cliente:
    def __init__(self, nombre, documento, correo, telefono):
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono
        logger.info("Cliente creado correctamente: %s", self.nombre)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ClienteInvalidoError("El nombre del cliente es inválido.")
        self._nombre = valor.strip()

    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ClienteInvalidoError("El documento del cliente es inválido.")
        self._documento = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or "@" not in valor or not valor.strip():
            raise ClienteInvalidoError("El correo del cliente es inválido.")
        self._correo = valor.strip()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ClienteInvalidoError("El teléfono del cliente es inválido.")
        self._telefono = valor.strip()

    def __str__(self):
        return f"Cliente: {self.nombre} | Documento: {self.documento} | Correo: {self.correo} | Teléfono: {self.telefono}"
