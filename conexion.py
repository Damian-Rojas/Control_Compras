import psycopg2

# Establecer los parámetros de conexión
parametros = {
    "host": "localhost",
    "database": "ControlVentas",
    "user": "admin",
    "password": "damian79"
}

# Crear la conexión
conexion = psycopg2.connect(**parametros)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Ejecutar una consulta
consulta = "SELECT * FROM clientes order by id asc"
cursor.execute(consulta)

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()