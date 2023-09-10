#!/usr/bin/env python

"""Imprime a tabuada do 1 ao 10."""
__version__ = "0.1.1"
__author__ = "Anderson"

# base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = list(range(1, 11))

for numero in numeros:
    tabuada = "---- Tabuada do {} ----"
    print(tabuada.format(numero))
    for outro_numero in numeros:
        resultado = numero * outro_numero
        calculo = "{:>7} x {} = {}"
        print(calculo.format(numero, outro_numero, resultado))
        
        
        
    print("{:=^23}".format(""))