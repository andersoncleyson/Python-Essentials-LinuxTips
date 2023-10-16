#!/usr/bin/env python3

import logging
import sys

log = logging.Logger("alerta")

while True:
    try:
        temp = float(input("Qual a temperatura no momento? ").strip())
    except ValueError:
        log.error("Temperatura inválida")
        sys.exit(1)

    try:
        umidade = float(input("Qual o indice de umidade do ar? ").strip())
    except ValueError:
        log.error("Umidade inválida")
        sys.exit(1)

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
    if cont != 'y':
        print("TCHAU!\n")
        break
    print("\n")
