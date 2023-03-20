import sqlite3 as sql

DB_PATH = "C:\\UrbanStore\\database.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE camisetas (
        id_cam INTEGER NOT NULL, 
        nom_cam TEXT NOT NULL,
        det_cam TEXT,
        talla_cam TEXT,
        precio_cam NUMERIC NOT NULL,
        url_cam TEXT NOT NULL,
        PRIMARY KEY (id_cam)
        )""")
    conn.commit()
    conn.close()
    
def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        (1,'Nasa','Camiseta con estampado Nasa color blaca','S',35000,'../static/img/portfolio/hcamisetas/1.jpg'),
        (2,'Thrasher','Camiseta de la marca Thrasher color negra','M',50000,'../static/img/portfolio/hcamisetas/2.jpg'),
        (3,'Kappa','Camiseta de la marca Kappa color blaca','S',40000,'../static/img/portfolio/hcamisetas/3.jpg'),
        (4,'Vans','Camiseta de la marca Vans color verde','L',30000,'../static/img/portfolio/hcamisetas/4.jpg'),
        (5,'Robotic','Camiseta estampada Robotica color gris oscuro','L',55000,'../static/img/portfolio/hcamisetas/5.jpg'),
        (6,'Manga Corta','Camiseta manga corta y estampada color verde','S',60000,'../static/img/portfolio/hcamisetas/6.jpg'),
        (7,'Manga Corta','Camiseta manga corta y estampada','M',30000,'../static/img/portfolio/hcamisetas/7.jpg'),
        (8,'Chicago','Camiseta estampada Chicago color blanca','S',45000,'../static/img/portfolio/hcamisetas/8.jpg'),
        (9,'Supreme','Camiseta de la marca Supreme estampada colores clanco y negro','L',55000,'../static/img/portfolio/hcamisetas/9.jpg'),
        (10,'Diesel','Camiseta de la marca Diesel estampada de color amarillo','S',50000,'../static/img/portfolio/hcamisetas/10.jpg'),
        (11,'Manga Corta','Camiseta manga corta estampada','M',35000,'../static/img/portfolio/hcamisetas/11.jpg'),
        (12,'Moschino','Camiseta de la marca Moschino estampada color negro','S',45000,'../static/img/portfolio/hcamisetas/12.jpg')
    ]
    cursor.executemany("""INSERT INTO camisetas values (?, ?, ?, ?, ?, ?)""", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
    addValues()