import sqlite3 as sql

DB_PATH = "D:\\UrbanStoreCOPIA\\database.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE mpantalon (
        id_pm INTEGER NOT NULL, 
        nom_pm TEXT NOT NULL,
        det_pm TEXT,
        talla_pm NUMERIC,
        precio_pm NUMERIC NOT NULL,
        url_pm TEXT NOT NULL,
        PRIMARY KEY (id_pm)
        )""")
    conn.commit()
    conn.close()
    
def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        (1,'Love Me','Pantalon jean clasico, color azul claro, de la masca Love Me',8,120000,'../static/img/portfolio/mjeans/1.jpg'),
        (2,'Kenzo','Falda jean, con botones, color cafe',6,100000,'../static/img/portfolio/mjeans/2.jpg'),
        (3,'H&M','Pantalon jean con bolsillos laterales, color beige',10,130000,'../static/img/portfolio/mjeans/3.jpg'),
        (4,'Estudio F','Falda de pana con bolsillos y botones, color mostaza',8,90000,'../static/img/portfolio/mjeans/4.jpg'),
        (5,'FDS','falda jean clasica, con botones laterales, color azul',12,85000,'../static/img/portfolio/mjeans/5.jpg'),
        (6,'Americanino','Pantalon jean, con rotos, color gris claro',10,110000,'../static/img/portfolio/mjeans/6.jpg'),
        (7,'Koaj','Falda jean con bolsillos laterales y botones forma corazon, color azul claro',6,95000,'../static/img/portfolio/mjeans/7.jpg'),
        (8,'ELA','Pantalon jean bota ancha, con estampados, color negro',8,80000,'../static/img/portfolio/mjeans/8.jpg'),
        (9,'H&M','Pantalon jean bota ancha, con rotos, color negro',6,75000,'../static/img/portfolio/mjeans/9.jpg'),
        (10,'FDS','Falda jean con rotos, color azul claro',8,100000,'../static/img/portfolio/mjeans/10.jpg'),
        (11,'ELA','Pantalon jean, bota ancha, con estampados, color azul',10,85000,'../static/img/portfolio/mjeans/11.jpg'),
        (12,'Koaj','Falda jean clasico, color negro, con bolsillos laterales',8,90000,'../static/img/portfolio/mjeans/12.jpg')
    ]
    cursor.executemany("""INSERT INTO mpantalon values (?, ?, ?, ?, ?, ?)""", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
    addValues()