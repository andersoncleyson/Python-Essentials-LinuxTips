#!/usr/bin/env python3

import logging
import sys

log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None
}


while True:
    for key in info.keys():
        try:
            #temp = float(input("Qual a temperatura no momento? ").strip())
            info[key] = float(input(f"Qual a {key}? ").strip())
        except ValueError:
            log.error(f"{key.capitalize()} inválida")
            sys.exit(1)

    temp = info["temperatura"]
    umidade = info["umidade"]

    if temp > 45:
        print("ALERTA! Perigo calor extremo")
    elif (temp * 3) >= umidade:
        print("ALERTA! Perigo de calor úmido")
    elif temp >= 10 and temp <= 30:
        print("Normal")
    elif temp >= 0 and temp <= 10:
        print("Frio")
    elif temp < 0:
        print("Frio extremo")
    
    cont = input("Deseja informar outra temperatura? [N/y]").strip().lower()
    if cont != 'y' or cont != 'Y':
        print("TCHAU!\n")
        break