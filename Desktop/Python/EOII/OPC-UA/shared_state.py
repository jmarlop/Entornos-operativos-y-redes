# -- Contenido del archivo --

# Importa la librería para gestionar hilos y semáforos
import threading
# 1. El diccionario que compartirán los 3 hilos
# Inicializa los valores para evitar errores si un hilo lee antes que el otro escriba
shared_data = {
    "counter": 0,
    "random": 0.0,
    "senoidal": 0.0
}
# 2. El semáforo (Lock) que protege el diccionario
# Esto asegura que solo un hilo pueda leer o escribir en 'shared_data' a la vez
data_lock = threading.Lock()



#python3 -c "import shared_state; print(shared_state.data_lock)"
#<locked _thread.lock object at 0x...>