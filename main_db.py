#en este archivo se ejecuta el programa completo, lazando las demas funciones y las bases de datos

from Db_psw import Database
from main import main
import getpass


if __name__ == "__main__":
    db = Database()  # Crea una instancia de la base de datos

    # Añadir un nuevo usuario 
    #db.add_user("admin", "admin123")
    #se inicia la ejecucion del bucle while para autenticarse en la base de datos para iniciar sesion, crear el usuario o salir
while True:
        print("Seleccione una opción:")
        print("1. Iniciar sesión")
        print("2. Crear un nuevo usuario")
        print("3. Salir")
        option = input("Ingrese su opción (1/2/3): ")

        if option == '1':
            user = db.authenticate_user_with_limit()
            if user:
                print("Acceso permitido.")
                # Aquí es donde inicia el programa del taxímetro
                main(user) 
                break

            else:
                print("Acceso denegado.")
        elif option == '2':
            name = input("Ingrese el nombre del nuevo usuario: ")
            pwd = getpass.getpass("Ingrese la contraseña del nuevo usuario: ")
            db.add_user(name, pwd)
        elif option == '3':
            db.close() # Cierra la conexión a la base de datos al final
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

db.close()  # Cierra la conexión a la base de datos al final