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

__version__ = "0.0.1"
__author__ = "Anderson Cleyson"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG")[:5]

msg = "Hello, friend"

if current_language == "pt_BR":
    msg = "Olá, amigo"
elif current_language == "it_IT":
    msg = "Ciao, Mondo"
elif current_language == "es_SP":
    msg = "Hola, mundo"
elif current_language == "fr_FR":
    msg = "Bonjour monde"


print(msg)