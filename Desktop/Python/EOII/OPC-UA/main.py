# -- Contenido del archivo --

import threading # Para crear los objetos Hilo
import time      # Para el 'sleep' del hilo principal

# Importa las funciones 'run' de cada archivo de hilo
from thread_client_prosys import run_client_thread
from thread_server_python import run_server_thread
from thread_bridge_udp import run_udp_thread

# --- Bloque Principal ---
if __name__ == "__main__":
    
    print("--- INICIANDO APLICACIÓN PUENTE ---")
    
    # 1. Crea los 3 objetos Hilo
    # Dales un nombre para depurar más fácil
    # 'daemon=True' significa que los hilos se cerrarán solos si el main.py se cierra
    t1 = threading.Thread(target=run_client_thread, name="ClienteProsys", daemon = True)
    t2 = threading.Thread(target=run_server_thread, name="ServidorPython", daemon = True)
    t3 = threading.Thread(target=run_udp_thread, name="PuenteUDP", daemon = True)
    
    # 2. Inicia los hilos
    t1.start()
    t2.start()
    t3.start()
    
    print("Hilos iniciados. (Pulsa Ctrl+C para detener la aplicación)")
    
    # 3. Bucle infinito para mantener vivo el hilo principal
    try:
        while True:
            print(f"El estado activo de los hilos es: {threading.active_count()}")
            time.sleep(5.0)
    except KeyboardInterrupt:
        print("---CERRANDO LA APLICACION---")
        
        
        


# --- Terminal 1: Lanza la aplicación principal ---
#python3 main.py

#--- INICIANDO APLICACIÓN PUENTE ---
#Hilos iniciados. (Pulsa Ctrl+C para detener la aplicación)
#... (Se quedará corriendo)

# --- Terminal 2: Escucha los datos UDP ---
#nc -lu 9000

#{"counter": 50, "random": -10.5}
#{"counter": 51, "random": 33.2}
#...

# --- Terminal 3: (Opcional) Conecta UaExpert ---
# Abre UaExpert y conéctate a tu servidor Python (Thread 2)
# Ahora deberías ver el valor de "Senoidal" cambiando en tiempo real.