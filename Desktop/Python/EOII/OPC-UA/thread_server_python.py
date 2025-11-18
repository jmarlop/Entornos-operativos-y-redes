# -- Contenido del archivo --

import asyncio
from asyncua import Server  # Ahora necesitas el Servidor
import logging

from config import PYTHON_SERVER_URL, SAMPLE_RATE_SEC
from shared_state import shared_data, data_lock


# --- Lógica Asíncrona (El núcleo del servidor) ---
async def server_logic_async():
    
    # 1. Inicializa el objeto Servidor
    server =Server()
    await server.init()
    await asyncio.sleep(5.0)   
    # 2. Configura el endpoint (la URL)
    server.set_endpoint(PYTHON_SERVER_URL)
    # 3. Configura el espacio de nombres (para organizar tus variables)
    uri = "http://localhost/MiPuenteNamespace"
    idx = await server.register_namespace(uri)
    # 4. Crea un objeto "Carpeta" para tus variables
    mi_objeto = await server.nodes.objects.add_object(idx, "MiPuenteObjeto")
    # 5. Añade la variable "Senoidal" que Ignition leerá
    var_senoidal = await mi_objeto.add_variable(idx,"Senoidal", 0.0)
    # 6. Haz la variable "escribible" por tu propio script
    await var_senoidal.set_writable()
    # 7. Inicia el servidor
    async with server:
        # 8. (Dentro del 'async with') Bucle infinito para actualizar el valor
        while True:
            # 9. Adquiere el semáforo para leer de forma segura
            with data_lock:
            # 10. (Dentro del 'with') Lee el valor del diccionario
                valor_actual = shared_data["senoidal"]
            # 11. Escribe el valor en tu variable de servidor OPC-UA
            await var_senoidal.write_value(valor_actual)
            # 12. (Opcional) Imprime para depurar
            print(f"Servidor: valor 'Senoidal' actualizado a {valor_actual}")
            # 13. Espera un poco
            await asyncio.sleep(SAMPLE_RATE_SEC)

# --- Función de Arranque (El lanzador del hilo) ---
def run_server_thread():
    logging.basicConfig(level=logging.INFO)
    
    # 14. Ejecuta el bucle de eventos asíncrono
    try:
        asyncio.run(server_logic_async())
    except:
        print("\nServidor detenido.")

# --- Bloque de Prueba (Para probar solo este archivo) ---
if __name__ == "__main__":
    print(f"Iniciando servidor en {PYTHON_SERVER_URL} (Pulsa Ctrl+C para parar)...")
    run_server_thread()
    
    
    
# --- Terminal 1: Lanza el servidor ---
#python3 thread_server_python.py


#Iniciando servidor en opc.tcp://127.0.0.1:4840/mi_puente/ ...
#INFO:asyncua.server.server:Listening on 127.0.0.1:4840
#... (Se quedará corriendo)

# --- Terminal 2: Comprueba que el puerto está abierto ---
# netstat: -a (all), -n (numeric), -p tcp (protocol)
# grep: filtra por el puerto 4840
#netstat -anp tcp | grep 4840

#tcp4       0      0  127.0.0.1.4840         *.* LISTEN