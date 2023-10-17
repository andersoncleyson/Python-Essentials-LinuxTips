#!/usr/bin/env python3

words = []
while True:
    word = input("Digite uma palavra (ou enter para sair):").strip()
    if not word: # condição de parada
        break
    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        if letter.lower() in "aeiou":
            final_word += letter * 2
        else:
            final_word += letter
        
        final_word += letter

        # If ternário alternativo
        #final_word += letter * 2 if letter.lower() in "aeiou" else letter
    words.append(final_word)

print(*words, sep="\n")