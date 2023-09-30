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

__version__ = "0.1.2"
__author__ = "Anderson Cleyson"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG")[:5]

msg = {
    "en_US": "Hello, friend",
    "pt_BR": "Olá, amigo",
    "es_SP": "Hola, amigo",
    "fr_FR": "Bonjour monde",
    "it_IT": "Ciao, mondo"
}

print(msg[current_language])