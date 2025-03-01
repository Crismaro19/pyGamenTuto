import pymysql

# Configuración de conexión
conn = pymysql.connect(
    host="localhost",
    user="mi_usuario",
    password="mi_password",
    database="mi_base_de_datos",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor  # Para obtener resultados como diccionarios
)

# Crear un cursor
cursor = conn.cursor()

# Ejecutar una consulta
cursor.execute("SELECT * FROM puntajes where usuario = 'MARO'")

res = cursor.fetchall()

print(res[0])

# Cerrar conexión
cursor.close()
conn.close()
