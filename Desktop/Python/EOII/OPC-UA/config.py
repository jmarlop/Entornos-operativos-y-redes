# -- Contenido del archivo --

# --- Configuración del Servidor Prosys (Origen) ---
# OJO: Cambia esto por la URL que te muestre tu servidor Prosys
# Si Prosys está en la misma máquina, será localhost o 127.0.0.1
PROSYS_URL = "opc.tcp://127.0.0.1:53530/OPCUA/SimulationServer"

# --- Configuración de tu Servidor Python (Thread 2) ---
# Esta es la dirección que crearás para que Ignition se conecte a ti
PYTHON_SERVER_URL = "opc.tcp://127.0.0.1:4840/mi_puente/"

# --- Configuración del Puente UDP (Thread 3) ---
# Ignition escuchará en esta IP y puerto
UDP_IP = "127.0.0.1"
UDP_PORT = 9000

# --- Configuración de Muestreo ---
# Tasa de refresco de datos en Prosys (en segundos)
# El PDF dice 100ms
SAMPLE_RATE_SEC = 0.1


# Comprueba que el archivo se puede importar en Python sin errores
# python3 -c "import config; print(config.PYTHON_SERVER_URL)"
# opc.tcp://127.0.0.1:4840/mi_puente/