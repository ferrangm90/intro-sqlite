from conexion import Conexion
import sqlite3

def formato(respuesta):
    lista_final=[]
    for fila in respuesta.fetchall():
        lista_final.append(dict(fila))
    return lista_final    

def select_all():
    conexionSelect = Conexion('SELECT * FROM persona;')
    respuesta = conexionSelect.res
    resp = formato(respuesta)
    conexionSelect.con.close()
    return resp

def select_by_id(id:int):
    conexionSelectBy = Conexion(f'SELECT * FROM persona WHERE id={id}')
    resp=conexionSelectBy.res
    formato(resp)
    conexionSelectBy.con.close()
    return resp

def insert_data(data):
    try:
        conexionInsert=Conexion('INSERT INTO persona(name,lastname,dni,email) VALUES (?,?,?,?);',data)
        conexionInsert.res
        conexionInsert.con.commit()#para confirmar guardado
    except sqlite3.Error as error:
        print('Error: ',error)

    conexionInsert.con.close()

def update_data(id,data):
    try:
        conexionUpdate=Conexion(f'UPDATE persona SET name=?, lastname=?,dni=?,email=? WHERE id={id};',data)
        conexionUpdate.res
        conexionUpdate.con.commit()#confirmar el update
    except sqlite3.Error as error:
            print('Error: ',error)
    conexionUpdate.con.close()

def delete_data(id:int):
    try:
        conexionDelete=Conexion(f'DELETE FROM persona WHERE id={id};')
        conexionDelete.res
        conexionDelete.con.commit()#confirmar el borrado
    except sqlite3.Error as error:
        print('Error: ',error)    
    conexionDelete.con.close()   