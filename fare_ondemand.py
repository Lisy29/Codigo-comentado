#se importa el modulo datetime

import datetime


#se define la funcion para calcular al tarifa por demanda de horas, siendo que de 22hrs a 12m hrs el precio por demanda aumenta
#y en las demas horas se mantiene al tarifa base
def calculate_peak_fare(in_movement):
    current_time = datetime.datetime.now()
    hour = current_time.hour

    # Definir horas pico y el aumento de las tarifas en base a las que ya estaban definidas por el cliente
    if (hour < 12) or (hour >= 22):
        if in_movement:
            return 0.1  # Tarifa en movimiento durante horas pico
        else:
            return   0.04  # Tarifa en espera durante horas pico
    else:
        if in_movement:
            return  0.05  # Tarifa en movimiento durante horas no pico
        else:
            return  0.02  # Tarifa en espera durante horas no pico
        
