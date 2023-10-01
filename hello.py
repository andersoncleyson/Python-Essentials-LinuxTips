#!/usr/bin/env python3
"""
Hello friend Multi Linguas.

Dependendo da lingua configurada no
ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução: 

    python3 hello.py
    ou
    ./hello.py
"""

__version__ = "0.1.3"
__author__ = "Anderson Cleyson"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1
}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, friend",
    "pt_BR": "Olá, amigo",
    "es_ES": "Hola, amigo",
    "fr_FR": "Bonjour monde",
    "it_IT": "Ciao, mondo"
}

print(msg[current_language] * int(arguments["count"]))