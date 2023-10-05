__version__ = "0.1.1"

import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print("Informa o nome do arquivo de emails")
    sys.exit(1)
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) # emails.txt
templatepath = os.path.join(path, templatename) # email_tmpl.txt

clientes = []
for line in open(filepath):
    name, email = line.split(",")

    # TODO Substituir por envio de email
    print(f"Enviando email para: {email}")
    print(
        open(templatepath).read() 
            % {
                "nome": name, 
                "product": "Playstation 5",
                "text": "play games",
                "link": "gamesstore.com", 
                "amount": "5", 
                "price":450,
                
            }
        )
    print("-" * 50)
    
