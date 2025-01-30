import time
import random
import serial

def comunicacion_balanza():
    try:
        # Configuración del puerto serial
        puerto = "COM3"  # Cambia según el puerto asignado en tu sistema
        velocidad_baudios = 9600

        # Abrir el puerto serial
        with serial.Serial(puerto, velocidad_baudios, timeout=1) as dispositivo:
            print(f"Conectado a {puerto}. Enviando solicitud de peso (ENQ)...")

            # Enviar ENQ (0x05)
            dispositivo.write(b'\x05')
            print("ENQ enviado. Esperando respuesta...")

            # Leer respuesta de la balanza
            respuesta = dispositivo.read(100)  # Leer hasta 100 bytes
            if respuesta:
                print(f"Bytes recibidos: {respuesta}")
                if respuesta[0] == 0x02:  # Verificar si comienza con STX (0x02)
                    print("Datos válidos recibidos de la balanza.")
                else:
                    print("Respuesta inesperada recibida.")
            else:
                print("No se recibió respuesta de la balanza.")
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")

if __name__ == "__main__":
    comunicacion_balanza()

def comunicacion_balanza_solopeso():
    try:
        puerto = "COM3"  
        velocidad_baudios = 9600

        with serial.Serial(puerto, velocidad_baudios, timeout=1) as dispositivo:
            dispositivo.write(b'\x05')

            respuesta = dispositivo.read(100)  
            if respuesta and respuesta[0] == 0x02:  
                try:
                    # Extraer el peso ignorando los caracteres de control (STX y ETX)
                    datos = respuesta[1:-1].decode().strip()  
                    peso = float(datos.replace("kg", ""))  
                    print(peso)  
                except ValueError:
                    pass 
    except serial.SerialException:
        pass  

if __name__ == "__main__":
    comunicacion_balanza()

def comunicacion_balanza_simulada():
    time.sleep(1)  

    peso = round(random.uniform(0, 100), 2)

    return peso  

if __name__ == "__main__":
    peso_simulado = comunicacion_balanza_simulada()
    print(peso_simulado)  

