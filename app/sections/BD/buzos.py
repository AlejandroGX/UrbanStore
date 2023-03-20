import sqlite3 as sql

DB_PATH = "D:\\UrbanStoreCOPIA\\database.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE buzos (
        id_buz INTEGER NOT NULL, 
        nom_buz TEXT NOT NULL,
        det_buz TEXT,
        talla_buz TEXT,
        precio_buz NUMERIC NOT NULL,
        url_buz TEXT NOT NULL,
        PRIMARY KEY (id_buz)
        )""")
    conn.commit()
    conn.close()
    
def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        (1,'Believe','Buzo corto con estampado en las mangas y capucha, color blanco','S',75000,'../static/img/portfolio/mbuzos/1.jpg'),
        (2,'Los Angeles','Buzo corto con estampado y cuello elegante, color negro y blanco','M',63000,'../static/img/portfolio/mbuzos/2.jpg'),
        (3,'Forever','Buzo corto, color negro, blaco, palo de rosa','S',80000,'../static/img/portfolio/mbuzos/3.jpg'),
        (4,'Brooklyn','Buzo corto, bordado en el pecho y capucha, color negro','M',70000,'../static/img/portfolio/mbuzos/4.jpg'),
        (5,'Mittelmeer','Buzo corto con estampado y capucha, color azul','L',65000,'../static/img/portfolio/mbuzos/5.jpg'),
        (6,'H&M','Buzo corto con capucha, color beige, rosado, palo de rosa','S',72000,'../static/img/portfolio/mbuzos/6.jpg'),
        (7,'Girl Power','Buzo corto con estampado y capucha, color palo de rosa','M',63000,'../static/img/portfolio/mbuzos/7.jpg'),
        (8,'USA','Buzo corto con estampado en el pecho y en las mangas, con capucha, color blanco','M',85000,'../static/img/portfolio/mbuzos/8.jpg'),
        (9,'Start','Buzo tipo bomber, bordado en el pecho, de color blanco y azul','S',75000,'../static/img/portfolio/mbuzos/9.jpg'),
        (10,'Chicago','Buzo estampado con cuello elegante, de color verde','S',66000,'../static/img/portfolio/mbuzos/10.jpg'),
        (11,'Love','Buzo corto con capucha, de colores blanco y palo de rosa','M',60000,'../static/img/portfolio/mbuzos/11.jpg'),
        (12,'Nike','Buzo de cierre, con capucha, de color palo de rosa','M',70000,'../static/img/portfolio/mbuzos/12.jpg')
    ]
    cursor.executemany("""INSERT INTO buzos values (?, ?, ?, ?, ?, ?)""", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
    addValues()