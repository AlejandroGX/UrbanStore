import sqlite3 as sql

DB_PATH = "D:\\UrbanStoreCOPIA\\database.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE users (
        id_user INTEGER NOT NULL, 
        nom_user TEXT NOT NULL,
        ape_user TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        tel_user NUMERIC NOT NULL,
        ciu_user TEXT NOT NULL,
        dir_user TEXT NOT NULL,
        tipo NUMERIC,
        PRIMARY KEY (id_user)
        )""")
    conn.commit()
    conn.close()
if __name__ == "__main__":
    createDB()