# -- Contenido del archivo --

import asyncio  # Para la programación asíncrona de asyncua
from asyncua import Client  # Solo necesitas el Cliente
import logging # Para ver si hay errores de conexión
import time 
# Importa las variables de configuración y los objetos compartidos
from config import PROSYS_URL
from shared_state import shared_data, data_lock
from config import PROSYS_URL, SAMPLE_RATE_SEC

# --- Lógica Asíncrona (El núcleo del cliente) ---
async def client_logic_async():
    # 1. Configura la URL del servidor Prosys
    url = PROSYS_URL
    # 2. Inicia el cliente
    async with Client(url=url) as cliente:    
    # 3. (Dentro del 'async with') Busca los nodos que necesitas
        nodo_counter = cliente.get_node("ns=2;s=Counter")
        nodo_random = cliente.get_node("ns=2;s=Random")
        nodo_senoidal = cliente.get_node("ns=2;s=Sine")
        # 4. Bucle infinito para leer datos
        while True:
            # 5. (Dentro del bucle) Lee los valores de los nodos
            val_c = await nodo_counter.read_value()
            val_r = await nodo_random.read_value()
            val_s = await nodo_senoidal.read_value() 
            # 6. Adquiere el semáforo para escribir de forma segura
            with data_lock:
                # 7. (Dentro del 'with') Actualiza el diccionario global
                shared_data["counter"] = val_c
                shared_data["random"] = val_r
                shared_data["senoidal"] = val_s
            # 8. (Opcional pero recomendado) Imprime para depurar
            print(f"LEIDO: {val_c}, {val_r}, {val_s}")
            # 9. Espera un poco antes de volver a leer
            await asyncio.sleep(SAMPLE_RATE_SEC * 0.8)
# --- Función de Arranque (El lanzador del hilo) ---
def run_client_thread():
    logging.basicConfig(level=logging.INFO)
    # 10. Crea un bucle 'try/except' para capturar errores de conexión
    try:
        # 11. Ejecuta el bucle de eventos asíncrono
        asyncio.run(client_logic_async())
    except Exception as e:
        print(f"Error en el cliente: {e}")
    except KeyboardInterrupt:
        print("Cliente detenido.")
# --- Bloque de Prueba (Para probar solo este archivo) ---
if __name__ == "__main__":
    # Este código solo se ejecuta si lanzas 'python3 thread_client_prosys.py'
    print("Iniciando cliente en modo de prueba (Pulsa Ctrl+C para parar)...")
    # Asume que Prosys ya está ejecutándose en tu Mac
    run_client_thread()
    
    
    
    
# Ejecuta este archivo directamente para probar solo el Thread 1
#python3 thread_client_prosys.py

#Iniciando cliente en modo de prueba (Pulsa Ctrl+C para parar)...
#INFO:asyncua.client.client:Connected to opc.tcp://127.0.0.1:53530...
#LEÍDO: 10, -25.4, 0.88
#LEÍDO: 11, 12.1, 0.95
#...