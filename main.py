import logging

from entidades import (
    Cliente,
    Reserva,
    Servicio,
    ClienteInvalidoError,
    ReservaInvalidaError,
    ServicioNoDisponibleError,
    CostoInconsistenteError,
)

logging.basicConfig(
    filename="errores.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)


class SalaServicio(Servicio):
    def __init__(self, nombre, precio_base, disponible=True, capacidad=10):
        super().__init__(nombre, precio_base, disponible)
        self.capacidad = capacidad

    def describir_servicio(self):
        return f"Sala: {self.nombre} | Capacidad: {self.capacidad}"

    def calcular_costo(self, descuento=0):
        self.validar_disponibilidad()
        costo = self.precio_base
        costo_final = costo - (costo * descuento)
        if costo_final < 0:
            raise CostoInconsistenteError("El costo final no puede ser negativo.")
        return costo_final


class EquipoServicio(Servicio):
    def __init__(self, nombre, precio_base, disponible=True, cantidad=1):
        super().__init__(nombre, precio_base, disponible)
        self.cantidad = cantidad

    def describir_servicio(self):
        return f"Equipo: {self.nombre} | Cantidad: {self.cantidad}"

    def calcular_costo(self, descuento=0):
        self.validar_disponibilidad()
        costo = self.precio_base * self.cantidad
        costo_final = costo - (costo * descuento)
        if costo_final < 0:
            raise CostoInconsistenteError("El costo final no puede ser negativo.")
        return costo_final


class AsesoriaServicio(Servicio):
    def __init__(self, nombre, precio_base, disponible=True, horas=1):
        super().__init__(nombre, precio_base, disponible)
        self.horas = horas

    def describir_servicio(self):
        return f"Asesoría: {self.nombre} | Horas: {self.horas}"

    def calcular_costo(self, descuento=0):
        self.validar_disponibilidad()
        costo = self.precio_base * self.horas
        costo_final = costo - (costo * descuento)
        if costo_final < 0:
            raise CostoInconsistenteError("El costo final no puede ser negativo.")
        return costo_final


def registrar_operacion(nombre, funcion):
    try:
        resultado = funcion()
        logger.info("Operación exitosa: %s", nombre)
        return True, resultado
    except Exception as error:
        logger.error("Fallo en %s: %s", nombre, error)
        return False, None
    finally:
        logger.info("Finalizó la operación: %s", nombre)


def main():
    intentos = 0
    exitos = 0

    cliente_valido = None
    sala = None
    equipo = None
    asesoria = None

    operaciones = []

    operaciones.append(
        ("Crear cliente válido", lambda: Cliente("Javier Perez", "1001", "javier@mail.com", "3001234567"))
    )
    operaciones.append(
        ("Crear cliente inválido", lambda: Cliente("", "1002", "correo_invalido", ""))
    )
    operaciones.append(
        ("Crear sala disponible", lambda: SalaServicio("Sala A", 100000, disponible=True, capacidad=15))
    )
    operaciones.append(
        ("Crear equipo disponible", lambda: EquipoServicio("Proyector", 50000, disponible=True, cantidad=2))
    )
    operaciones.append(
        ("Crear asesoría disponible", lambda: AsesoriaServicio("Asesoría Python", 80000, disponible=True, horas=3))
    )
    operaciones.append(
        ("Calcular costo sala con descuento", lambda: sala.calcular_costo(descuento=0.10) if sala else (_ for _ in ()).throw(RuntimeError("Sala no inicializada")))
    )
    operaciones.append(
        ("Calcular costo equipo con descuento", lambda: equipo.calcular_costo(descuento=0.15) if equipo else (_ for _ in ()).throw(RuntimeError("Equipo no inicializado")))
    )
    operaciones.append(
        ("Calcular costo asesoría sin descuento", lambda: asesoria.calcular_costo() if asesoria else (_ for _ in ()).throw(RuntimeError("Asesoría no inicializada")))
    )
    operaciones.append(
        ("Reserva válida de sala", lambda: Reserva(cliente_valido, sala, 2).procesar_reserva() if cliente_valido and sala else (_ for _ in ()).throw(RuntimeError("Datos de reserva no inicializados")))
    )
    operaciones.append(
        ("Reserva inválida con duración negativa", lambda: Reserva(cliente_valido, sala, -1).procesar_reserva() if cliente_valido and sala else (_ for _ in ()).throw(RuntimeError("Datos de reserva no inicializados")))
    )
    operaciones.append(
        ("Reserva con servicio no disponible", lambda: Reserva(cliente_valido, sala_inactiva, 1).procesar_reserva() if cliente_valido and sala_inactiva else (_ for _ in ()).throw(RuntimeError("Servicio no disponible no inicializado")))
    )

    global sala_inactiva
    sala_inactiva = None

    for nombre, accion in operaciones:
        intentos += 1

        if nombre == "Crear cliente válido":
            ok, resultado = registrar_operacion(nombre, accion)
            if ok:
                cliente_valido = resultado
                exitos += 1

        elif nombre == "Crear cliente inválido":
            registrar_operacion(nombre, accion)

        elif nombre == "Crear sala disponible":
            ok, resultado = registrar_operacion(nombre, accion)
            if ok:
                sala = resultado
                exitos += 1

        elif nombre == "Crear equipo disponible":
            ok, resultado = registrar_operacion(nombre, accion)
            if ok:
                equipo = resultado
                exitos += 1

        elif nombre == "Crear asesoría disponible":
            ok, resultado = registrar_operacion(nombre, accion)
            if ok:
                asesoria = resultado
                exitos += 1

        elif nombre == "Calcular costo sala con descuento":
            ok, resultado = registrar_operacion(nombre, accion)
            if ok:
                exitos += 1
                print("Costo sala con descuento:", resultado)

        elif nombre == "Calcular costo equipo con descuento":
            ok, resultado = registrar_operacion(nombre, accion)
            if ok:
                exitos += 1
                print("Costo equipo con descuento:", resultado)

        elif nombre == "Calcular costo asesoría sin descuento":
            ok, resultado = registrar_operacion(nombre, accion)
            if ok:
                exitos += 1
                print("Costo asesoría:", resultado)

        elif nombre == "Reserva válida de sala":
            ok, resultado = registrar_operacion(nombre, accion)
            if ok:
                exitos += 1
                print(resultado)

        elif nombre == "Reserva inválida con duración negativa":
            registrar_operacion(nombre, accion)

        elif nombre == "Reserva con servicio no disponible":
            registrar_operacion(nombre, accion)

    try:
        sala_inactiva = SalaServicio("Sala B", 120000, disponible=False, capacidad=20)
        logger.info("Servicio creado para prueba de no disponibilidad: %s", sala_inactiva.nombre)

        try:
            Reserva(cliente_valido, sala_inactiva, 1).procesar_reserva()
        except Exception as error:
            raise ServicioNoDisponibleError("La reserva falló porque el servicio no está disponible.") from error

    except ServicioNoDisponibleError as error:
        logger.error("Excepción encadenada capturada: %s", error)
        print("Error controlado:", error)

    print("Operaciones intentadas:", intentos)
    print("Operaciones exitosas:", exitos)


if __name__ == "__main__":
    main()
