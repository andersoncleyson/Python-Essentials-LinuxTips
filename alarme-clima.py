#!/usr/bin/env python3

import logging
import sys

log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None
}

while True:
    # condição de parada
    # o dicionário está completamente preenchido
    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])
    if info_size == filled_size:
        break # para o while

    if all(info.values()): #[None, None]
        break # para o while
    for key in info.keys(): #["temperatura", "umidade"]
        if info[key] is not None:
            continue
        try:
            info[key] = int(input(f"{key}:").strip())
        except ValueError:
            log.error("%s inválidada, digite números", key)
            break # para o for

    temp, umidade = info.values() #unpacking [30. 90]
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
        break@Sha