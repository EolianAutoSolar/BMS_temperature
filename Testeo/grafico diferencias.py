from datetime import datetime
import matplotlib.pyplot as plt


# convertir a formato datetime
def convert_timestamp(timestamp):
    return datetime.fromtimestamp(float(timestamp))

def procesar_linea(line):
    try: #try porque una de veces sale con este formato bytearray(b'1720805714.9562~\x00.\x10\x86\x00\x13\xa2\x00A')
        if line.startswith("bytearray"): #apartir de la 7759 empiezan a ser bytearrays xd
            line = eval(line).decode('utf-8') #transformar a bytearray y luego decode a string
        
        timestamp, msg_id, data = line.split('#')
    except: return 0
    return timestamp

def leer_archivo(filename):
    diferencias = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    
    for i in range(1, len(lines)-2, 2):
        if i >= 7757: #aqui hay un salto
            i = i+1

        line1 = lines[i].strip()
        timestamp = procesar_linea(line1)
        canTimestamp = convert_timestamp(timestamp)
        
        
        line2 = lines[i + 1].strip()
        pcTimestamp = datetime.strptime(line2, '%Y-%m-%d %H:%M:%S.%f')
        
        diferencia = pcTimestamp - canTimestamp
        if diferencia.total_seconds() > 10:
            continue
        diferencias.append(diferencia.total_seconds())

    return diferencias
        
lista = leer_archivo('Testeo/log.txt')
#graficar
plt.figure(figsize=(10, 6))
plt.plot(lista)
plt.title('Diferencias de tiempo test')
plt.xlabel('Línea') 
plt.ylabel('Diferencia de tiempo (segundos)')
plt.grid(True)
plt.axhline(0, color='red', linestyle='--')  
plt.show()
