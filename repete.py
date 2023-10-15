#!/usr/bin/env python3

# For loops / Laço for
"""
dados = {}
for line in open("post.txt"):
    if line == "----\n":
        break
    key, valor = line.split(":")
    dados[key] = valor.strip()

print(dados)
"""
#Estrutural
"""
nova = []
for n in [1, 2, 3]:
    nova.append(n * 2)
print(nova)
"""

original = [1, 2, 3]
# Funcional
# List comprehension
dobrada = [n * 2 for n in original]
print(dobrada)

# Dict comprehension
dados = {
    line.split(":")[0]: line.split(":")[1]
    for line in open("post.txt")
    if ":" in line
}
print(dados)