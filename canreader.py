import can

def can_reader(interface='can1'):
    bus = can.interface.Bus(channel=interface, bustype='socketcan')
    while True:
        mensaje = bus.recv()
        if mensaje is not None:
            mens_id = mensaje.arbitration_id
            mens_data = ' '.join(f"{byte:02x}" for byte in mensaje.data)

            print(f"{hex(mens_id)} # [{mensaje.dlc}] {mens_data:02X}")

if __name__ == "__main__":
    can_reader()
