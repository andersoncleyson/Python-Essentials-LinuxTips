email_tmpl = """
    ...: Hello, %(nome)s
    ...: 
    ...: Would do you like to buy %(product)s?
    ...: 
    ...: This product is awesome for solving
    ...: %(text)s
    ...: 
    ...: Click now %(link)s
    ...: 
    ...: Only %(amount)s available!
    ...: 
    ...: Promotional price %(price).2f
    ...: """

clientes = ["Elliot", "Shayla", "Darlene"]

for cliente in clientes:
    print(
        email_tmpl 
            % {
                "nome": cliente, 
                "product": "Playstation 5",
                "text": "play games",
                "link": "gamesstore.com", 
                "amount": "5", 
                "price":450
                }
        )
    
