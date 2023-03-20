import sqlite3 as sql

DB_PATH = "C:\\UrbanStore\\database.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE hpantalon (
        id_ph INTEGER NOT NULL, 
        nom_ph TEXT NOT NULL,
        det_ph TEXT,
        talla_ph NUMERIC,
        precio_ph NUMERIC NOT NULL,
        url_ph TEXT NOT NULL,
        PRIMARY KEY (id_ph)
        )""")
    conn.commit()
    conn.close()
    
def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        (1,'Levis','Pantalon jean clasico, color azul, de la masca Levis',36,120000,'../static/img/portfolio/hjeans/1.jpg'),
        (2,'Kenzo','Pantalon tela con bolsillos laterales, color beige',38,100000,'../static/img/portfolio/hjeans/2.jpg'),
        (3,'Diesel','Pantalon jean con rotos, color azul, de la marca Diesel',34,130000,'../static/img/portfolio/hjeans/3.jpg'),
        (4,'Kentux','Pantalon tela con bolsillos laterales, color gris',36,90000,'../static/img/portfolio/hjeans/4.jpg'),
        (5,'Rifle','Pantalon tela con bolsillos laterales, color verde',40,85000,'../static/img/portfolio/hjeans/5.jpg'),
        (6,'Americanino','Pantalon jean, con rotos y estampados, color azul',38,110000,'../static/img/portfolio/hjeans/6.jpg'),
        (7,'People','Pantalon tela con bolsillos laterales color, beige',34,95000,'../static/img/portfolio/hjeans/7.jpg'),
        (8,'Rifle','Pantalon tela con bolsillos laterales, color negro',36,80000,'../static/img/portfolio/hjeans/8.jpg'),
        (9,'Kenzo','Pantalon tela con bolsillos laterales, color gris',36,75000,'../static/img/portfolio/hjeans/9.jpg'),
        (10,'Diesel','Pantalon jean con rotos y bordados, color negro',38,100000,'../static/img/portfolio/hjeans/10.jpg'),
        (11,'Kentux','Pantalon tela, tipo clasico, color beige',40,85000,'../static/img/portfolio/hjeans/11.jpg'),
        (12,'Levis','Pantalon jean clasico, color negro, de la marca Levis',38,90000,'../static/img/portfolio/hjeans/12.jpg')
    ]
    cursor.executemany("""INSERT INTO hpantalon values (?, ?, ?, ?, ?, ?)""", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
    addValues()