import sqlite3

conexion = sqlite3.connect("inicio_db.db")
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()#creamos cursor

respuesta = cursor.execute('SELECT * FROM persona;')
#print(respuesta.fetchall())
#print(respuesta.description)
#filas = respuesta.fetchall()


resultado = [dict(fila) for fila in respuesta.fetchall()]
print(resultado)