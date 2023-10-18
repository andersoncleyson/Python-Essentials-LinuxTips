import sys
import logging

quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome, preco = line.strip().split(",")
        quartos[codigo] = {
            "nome": nome,
            "preco": float(preco), #TODO: Decimal
        }
except FileNotFoundError:
    logging.error("Arquivo não existe")
    sys.exit(1)

print(quartos)