from model import Taximetro #se importa la clase taximetro con sus funciones del archivo model
import time #se importa el modulo time para poder contabilizar el tiempo
from logger import log_info, log_warning, log_error #se importan modulos de la libreria logger para guardar los loggins

def main(user): #se llama a la funcion main con el argumento user
    taximetro = Taximetro(user) #se define la variable taximetro con  la clase #Taximetro y su argumento user

    log_info("Bienvenido al Taxímetro Digital! Programa iniciado.")  #se llama a la funcion log con mensaje info
    print("Bienvenido al Taxímetro Digital!") #se muestra la bienvenida
    #se explican los comandos de uso del CLI
    print('''Estos son los comandos disponibles:   
          - "E" para empezar 
          - "P" para parar 
          - "C" para continuar
          - "F" para finalizar
          - "H" para visualizar el Historial
          - "X" para salir
            con ellos puede usar el programa.\n''')

#se inicia un bucle while con las condicionales
    while True: #mientras se de este comando 
        comando = input("Ingrese un comando: ").upper() #se usa el modulo .upper para evitar que si se pone la instruccion
        #en minuscula se den errores en la ejecucion 
        if comando == "E":
            taximetro.start() #se llama a la funcion start con la instruccion E de la clase taximetro
            log_info(f"Comando {comando}: Taxímetro iniciado.") #------
        elif comando == "P":
            taximetro.stop() #se llama a la funcion stop con la instruccion P de la clase taximetro
            log_info(f"Comando {comando}: Taxímetro detenido.")#------
        elif comando == "C":
            taximetro.continue_road() #se llama a la funcion continue.road con la instruccion c de la clase taximetro
            log_info(f"Comando {comando}: Taxímetro continuado.")#------
        elif comando == "F":
            taximetro.finish_road() #se llama a la funcion finish.road con la instruccion F de la clase taximetro
            taximetro.clear() #se llama a la funcion clear que limpia el historial, reinicia y deja el taximetro a la espera de nuevas
            #instrucciones
            log_info(f"Comando {comando}: Taxímetro finalizado y reiniciado.")
            print('''Estos son los comandos disponibles: 
                - "E" para empezar 
                - "P" para parar 
                - "C" para continuar
                - "F" para finalizar
                - "H" para visualizar el Historial
                - "X" para salir
                    con ellos puede usar el programa.\n''')
        elif comando == "H":
            taximetro.history_db() #se llama a la funcion history.db que permite visualizar el historial de las carreras
            log_info(f"Comando {comando}: Historial visualizado.")
        elif comando == "X":
            print("Gracias por usar nuestro taximetro.")
            log_info("Programa terminado por el usuario.")
            break #si se da la instruccion X se finaliza el while
        else:
            print("Comando inválido. Intente de nuevo.") #se usa en caso de que ingresen alguna instruccion diferente a la solicitadas
            log_warning("Comando inválido ingresado.")

if __name__ == "__main__": # Este bloque solo se ejecutará si este script es el punto de entrada principal
    user = "Usuario predeterminado"  # Asumiendo que se obtiene el nombre de usuario de alguna manera
    main(user)