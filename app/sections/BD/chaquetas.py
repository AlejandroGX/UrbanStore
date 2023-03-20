import sqlite3 as sql

DB_PATH = "C:\\UrbanStore\\database.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE chaquetas (
        id_cha INTEGER NOT NULL, 
        nom_cha TEXT NOT NULL,
        det_cha TEXT,
        talla_cha TEXT,
        precio_cha NUMERIC NOT NULL,
        url_cha TEXT NOT NULL,
        PRIMARY KEY (id_cha)
        )""")
    conn.commit()
    conn.close()
    
def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        (1,'California','Chaqueta color beige estampada','S',90000,'../static/img/portfolio/hchaquetas/1.jpg'),
        (2,'Kenzo','Chaqueta color negra con beige tipo bomber','M',80000,'../static/img/portfolio/hchaquetas/2.jpg'),
        (3,'Nasa','Chqueta color blanco con capucha y estampado','S',75000,'../static/img/portfolio/hchaquetas/3.jpg'),
        (4,'Tailandia','Chaqueta color beige con capucha y estampado','L',70000,'../static/img/portfolio/hchaquetas/4.jpg'),
        (5,'Beisbolera','Chaqueta color cafe con blanco con capucha','L',85000,'../static/img/portfolio/hchaquetas/5.jpg'),
        (6,'Londres','Chaqueta color blanco y negro con capucha y estampados','M',70000,'../static/img/portfolio/hchaquetas/6.jpeg'),
        (7,'Beisbolera','Chaqueta color negro y gris tipo bomber','M',95000,'../static/img/portfolio/hchaquetas/7.jpg'),
        (8,'Rifle','Chaqueta color azul oscuro, blanco y negro con estampado','S',80000,'../static/img/portfolio/hchaquetas/8.jpg'),
        (9,'Beisbolera','Chaqueta color blanco y negro con bordado','L',75000,'../static/img/portfolio/hchaquetas/9.jpg'),
        (10,'OfBoy','Chaqueta color amarilla con estampados y cuello alto','L',70000,'../static/img/portfolio/hchaquetas/10.jpg'),
        (11,'Beisbolera','Chaqueta color cafe y beige con bordado','M',90000,'../static/img/portfolio/hchaquetas/11.jpg'),
        (12,'Moschino','Chaqueta color negro con estamados','S',95000,'../static/img/portfolio/hchaquetas/12.jpeg')
    ]
    cursor.executemany("""INSERT INTO chaquetas values (?, ?, ?, ?, ?, ?)""", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
    addValues()