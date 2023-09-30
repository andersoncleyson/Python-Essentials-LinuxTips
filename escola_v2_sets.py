#!/usr/bin/env python3

"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""

__version__ = "0.1.2"

# Dados
sala1 = ["Erik", "Maria", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolada"]

aula_ingles = ["Erik", "Maria", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança", aula_danca)
]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:
    # sala1 que tem interseção com atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(set(atividade))


    print(f"---Alunos da sala1 da aula de", nome_atividade)
    for aluno in atividade_sala1:
        print("-", aluno)

    print("=" * 30)

    print(f"---Alunos da sala2 da aula de", nome_atividade)
    for aluno in atividade_sala2:
        print("-", aluno)
    print("=" * 30)