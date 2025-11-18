# -- Contenido del archivo --

import socket  # Para crear el socket UDP
import json    # Para formatear el mensaje
import time    # Para el 'sleep'

from config import UDP_IP, UDP_PORT, SAMPLE_RATE_SEC
from shared_state import shared_data, data_lock

# --- Función de Arranque (El lanzador del hilo) ---
def run_udp_thread():
    
    # 1. Configura el destino (Ignition)
    target_address = (UDP_IP, UDP_PORT)
    
    # 2. Crea el socket UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"Puente UDP enviando a {UDP_IP}:{UDP_PORT}")
    
    # 3. Bucle infinito para enviar datos

    try:
        while True:
            # 4. Adquiere el semáforo para leer de forma segura
            with data_lock:
                # 5. (Dentro del 'with') Lee los datos
                valor_c = shared_data["counter"]
                valor_r = shared_data["random"]
                # 6. Crea el payload (diccionario)
                payload = {
                    "counter": valor_c,
                    "random": valor_r
                }
            # 7. Convierte el diccionario a un string JSON
            json_string =json.dumps(payload)
            # 8. Convierte el string a bytes (UTF-8)
            data_bytes = json_string.encode('utf-8')
            
            # 9. Envía los bytes por UDP
            udp_socket.sendto(data_bytes, target_address)
            
            # 10. (Opcional) Imprime para depurar
            print(f"UDP Enviado{json_string}")
            
            # 11. Espera el tiempo de muestreo
            time.sleep(SAMPLE_RATE_SEC)
    except:
        print("\nPuente UDP detenido.")
    finally:
        udp_socket.close()
        print("Socket UDP cerrado.")
        
# --- Bloque de Prueba (Para probar solo este archivo) ---
if __name__ == "__main__":
    print("Iniciando puente UDP en modo de prueba (Pulsa Ctrl+C para parar)...")
    # Este modo enviará '0' y '0.0' repetidamente
    run_udp_thread()
    
    
    
# --- Terminal 1: Abre un "oyente" UDP ---
# 'nc' (netcat) es la navaja suiza de redes
# -l (listen), -u (udp), 9000 (port)
#nc -lu 9000

# --- Terminal 2: Lanza el script ---
#python3 thread_bridge_udp.py

#{"counter": 0, "random": 0.0}
#{"counter": 0, "random": 0.0}
#...