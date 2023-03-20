import sqlite3 as sql

DB_PATH = "C:\\UrbanStore\\database.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE admin (
        id_admin INTEGER NOT NULL, 
        nom_admin TEXT NOT NULL,
        ape_admin TEXT NOT NULL,
        email TEXT NOT NULL,
        tel_admin NUMERIC NOT NULL,
        password TEXT NOT NULL,
        tipo numeric,
        PRIMARY KEY (id_admin)
        )""")
    conn.commit()
    conn.close()

def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        (1,'Diana','Gomez','dianagomez99@gmail.com',3185883807,'1111',1),
        (2,'Alejandro','Guerrero','alejandrog@gmail.com',3176949901,'2222',1),
        (3,'Pedro','Perez','pedroperez@gmail.com',3205462328,'3333',1)
    ]
    cursor.executemany("""INSERT INTO admin values (?, ?, ?, ?, ?, ?, ?)""", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
    addValues()