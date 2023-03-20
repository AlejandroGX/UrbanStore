import sqlite3 as sql

DB_PATH = "D:\\UrbanStoreCOPIA\\database.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE kart (
        id_user INTEGER, 
        id_cam INTEGER,
        quantity INTEGER,
        FOREIGN KEY(id_user) REFERENCES users(id_user),
        FOREIGN KEY(id_cam) REFERENCES camisetas(id_cam)
        )""")
    conn.commit()
    conn.close()
if __name__ == "__main__":
    createDB()