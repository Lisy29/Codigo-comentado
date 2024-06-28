#se importa la libreria sqlite3 para poder crear base de datos, bcrypt para encriptar las contraseñas, getpass para evitar que se visualizen
#las contraseñas al escribirlas.

import sqlite3
import bcrypt
import getpass


#se define la clase User, con los atributos, name y pwd que corresponden a nombre y contraseña
class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


#se define la clase Database con los atributos db_filename que corresponde al nombre del archivo donde se guardaran los datos de usuario, historial 
#de carreras, se conecta a la base de datos y se crean las tablas
class Database:
    def __init__(self, db_filename="taximetro.db"):
        self.db_filename = db_filename
        self.conn = sqlite3.connect(self.db_filename)
        self.create_table()

#funcion para crear tablas dentro del archivo taximetro.db
    def create_table(self):
        try:
            cursor = self.conn.cursor()
            querys = [
                '''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    pwd TEXT NOT NULL
                );
            ''',
            '''
                CREATE TABLE IF NOT EXISTS trips (
				id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                begin_date TEXT,
                end_date TEXT,
                total REAL,
                FOREIGN KEY (user_id) REFERENCES users (id)
			    );
            '''
            ]
            for q in querys:
                cursor.execute(q)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")
#se crea a funcion de añadir usuario con dos atributos ademas de usar aprametros de consulta para evitar inyecciones SQL, que se alamacenan en la base de datos con la contraseña hasheada con el
# metodo bcrypt , si el usuario ya existe imprime un mensaje.
    def add_user(self, name, pwd):
        hashed_pwd = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO users (name, pwd) VALUES (?, ?)", (name, hashed_pwd.decode('utf-8')))
            self.conn.commit()
            print("Usuario agregado exitosamente.")
            return True
        except sqlite3.IntegrityError:
            print("El usuario ya existe.")
            return False
#se define al funcion de autenticar usuario, se busca en la base de datos y se compara el usuario y la contraseña descodificandola
#buscando coincidencias, devuelve el resultado si los datos coinciden o sino encuentra nada devuelve None
    def authenticate_user(self, name, pwd):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
        result = cursor.fetchone() #recupera la primera fila de al consulta y devuelve none sino encuentra resultados
        if result:
            stored_pwd = result[2] #pwd esta en el indice 2
            if  bcrypt.checkpw(pwd.encode('utf-8'), stored_pwd.encode('utf-8')):
                return result
        return None

#se define la cantidad de veces que se puede intentar autenticar un usuario con contraseña, en este caso 3 veces. Ademàs la 
#contraseña se oculta si coincide la autenticacion permite el acceso al programa taximetro
    def authenticate_user_with_limit(self):
        counter = 3
        while counter > 0:
            n = input("Ingrese su usuario: ")
            p = getpass.getpass("Ingrese su contraseña: ")
            user = self.authenticate_user(n, p)
            if user != None:
                print(f"{n}, ¡Bienvenido al programa!")
                return user
            else:
                counter -= 1
                print("Usuario o contraseña incorrectos. Intentos restantes:", counter)

        print("Has superado el límite de intentos.")
        return 0
  #se define la funcion para agregar los datos del viaje a la base de datos  
    def add_trip_database(self, start_time, end_time, total, user):
        cursor = self.conn.cursor() #Crea un cursor para ejecutar consultas SQL en la conexión self.conn.
        query = """INSERT INTO 
                trips(begin_date, end_date, total, user_id) 
                VALUES(?, ?, ?, ?)"""
        cursor.execute(query, (start_time, end_time, total, user))
        self.conn.commit()
#se define la funcion para mostrar el historial de la base de datos
    def show_history(self, user_id):
        cursor = self.conn.cursor()
        query = """SELECT begin_date, end_date, total 
                FROM trips 
                WHERE user_id = ?"""
        cursor.execute(query, (user_id, ))
        rows = cursor.fetchall() # recupera todas las filas de un conjunto de resultados de una consulta SQL ejecutada previamente
        for row in rows:
            print(row)
#se define la funcion para cerrar la conexión actual con la base de datos SQLite.
    def close(self):
        self.conn.close()