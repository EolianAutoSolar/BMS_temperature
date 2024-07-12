import can
import time
from datetime import datetime, timezone

inicio = time.time()
def tiempo():
    ahora = time.time()
    return ahora - inicio

print("Timestamp |   ID   |  Mensaje")
# Función para imprimir la tabla
def tabla(fila):
    print(" | ".join(map(str, fila)))
    print("\033[F\033[K", end="")


def can_reader(interface='can1'):
    bus = can.interface.Bus(channel=interface, bustype='socketcan')
    while True:
        msg = bus.recv()
        if msg is not None:
            id = msg.arbitration_id
            data = ' '.join(f"{byte:02x}" for byte in msg.data)

            fila = [int(tiempo()), id, data]

            tabla(fila)
            time.sleep(1)
            if str(id)[:3] == 406:
                print("yes")
                

if __name__ == "__main__":
    can_reader()



