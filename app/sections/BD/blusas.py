import sqlite3 as sql

DB_PATH = "D:\\UrbanStoreCOPIA\\database.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE blusas (
        id_blu INTEGER NOT NULL, 
        nom_blu TEXT NOT NULL,
        det_blu TEXT,
        talla_blu TEXT,
        precio_blu NUMERIC NOT NULL,
        url_blu TEXT NOT NULL,
        PRIMARY KEY (id_blu)
        )""")
    conn.commit()
    conn.close()
    
def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        (1,'Believe','Blusa corta con estampado Believe, color amarilla','S',35000,'../static/img/portfolio/mblusas/1.jpg'),
        (2,'Baby Girl','Blusa corta con estampado Baby Girl, color morado','M',20000,'../static/img/portfolio/mblusas/2.jpg'),
        (3,'Icon','Blusa corta con estampado Icon, color blaco','S',30000,'../static/img/portfolio/mblusas/3.jpg'),
        (4,'Brooklyn','Blusa corta con estampado Brooklyn, color blaco y negro','M',25000,'../static/img/portfolio/mblusas/4.jpg'),
        (5,'Boston','Blusa corta con estampada Boston, color blanco','L',25000,'../static/img/portfolio/mblusas/5.jpg'),
        (6,'Brooklyn','Blusa corta con estampado Brooklyn, color gris','S',18000,'../static/img/portfolio/mblusas/6.jpg'),
        (7,'Girl Power','Blusa corta con estampado Girl Power, color blanco','M',23000,'../static/img/portfolio/mblusas/7.jpg'),
        (8,'Brooklyn','Blusa corta con estampado Brooklyn 76, color negro y blanco','S',30000,'../static/img/portfolio/mblusas/8.jpg'),
        (9,'Mittelmeer','Blusa corta con capucha, estampada, de color blanco y gris','L',20000,'../static/img/portfolio/mblusas/9.jpg'),
        (10,'Thrasher','Blusa corta de la marca Thrasher, estampada, de color negro y amarillo','S',26000,'../static/img/portfolio/mblusas/10.jpg'),
        (11,'Love','Blusa corta estampada, de colores blanco y negro','M',30000,'../static/img/portfolio/mblusas/11.jpg'),
        (12,'Coca-Cola','Blusa estampada Coca-Cola, de colores rojo y blanco','S',35000,'../static/img/portfolio/mblusas/12.jpg')
    ]
    cursor.executemany("""INSERT INTO blusas values (?, ?, ?, ?, ?, ?)""", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
    addValues()