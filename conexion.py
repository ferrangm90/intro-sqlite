import sqlite3


class Conexion:
    def __init__(self,query_sql,parametro=[]):
        self.con =sqlite3.connect("inicio_db.db")
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.res = self.cur.execute(query_sql,parametro)