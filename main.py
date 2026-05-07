"""
Sistema Software FJ - Fase 4 UNAD
SISTEMA MODULAR: Clases en carpeta 'entidades'
"""

import logging
from entidades.cliente import Cliente
from entidades.servicio import ReservaSala, AlquilerEquipo, Asesoria
from entidades.reserva import Reserva

logging.basicConfig(
    filename="sistema_logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    clientes = []
    servicios = []
    reservas = []
    
    servicios.append(ReservaSala("S1", "Conferencias", 50.0))
    servicios.append(AlquilerEquipo("E1", "Proyector", 100.0))
    servicios.append(Asesoria("A1", "Python", 80.0))
    
    print("=" * 60)
    print("=== SISTEMA SOFTWARE FJ - 10 OPERACIONES ===")
    print("May 2026 | Javier Ancizar Mejia Rodriguez | Grupo UNAD")
    print("=" * 60)
    print()
    
    operaciones = [
        lambda: clientes.append(Cliente("C1", "Juan Perez", "juan@email.com", "3001234567")),
        lambda: clientes.append(Cliente("C2", "Maria Lopez", "maria@email.com", "3007654321")),
        lambda: clientes.append(Cliente("C3", "", "ana@email.com", "3001112222")),
        lambda: reservas.append(Reserva("R1", clientes[0], servicios[0], 2.0)),
        lambda: reservas[0].confirmar(),
        lambda: reservas.append(Reserva("R2", clientes[1], servicios[1], 1.0)),
        lambda: reservas.append(Reserva("R3", clientes[0], servicios[2], -1.0)),
        lambda: reservas[1].cancelar(),
        lambda: print("Op9: Cliente inválida simulada (C3 no válida)"),
        lambda: print("Op10: Servicio no disponible simulado")
    ]
    
    for i, op in enumerate(operaciones, 1):
        print(f"--- Operación {i} ---")
        try:
            op()
        except Exception as error:
            logger.error(f"Operación {i} falló: {error}")
            print(f"❌ Falló (sistema continua): {error}")
        else:
            print("✅ Exitosa")
        print()
    
    print("=" * 60)
    print("=== RESULTADOS FINALES ===")
    print("=" * 60)
    validos = len([c for c in clientes if c.validar()])
    print(f"Clientes válidos: {validos}")
    print("\nReservas guardadas:")
    for r in reservas:
        print(f"  {r}")
    print("\n✅ ¡Sistema estable! Logs en sistema_logs.txt")


if __name__ == "__main__":
    main()