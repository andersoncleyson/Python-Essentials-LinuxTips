#!/usr/bin/env python3

"""Exibe relatório de crianças por atividade

Nesta versão serão usados os Dicts
"""

__version__ = "0.1.3"

# Dados
escola = {
    "sala1": ["Erik", "Mariana", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["João", "Antonio", "Carlos", "Maria", "Isolada"],
    "aula": {
        "ingles": ["Erik", "Maria", "Joana", "Carlos", "Antonio"],
        "musica": ["Erik", "Carlos", "Maria"],
        "danca": ["Gustavo", "Sofia", "Joana", "Antonio"]
    }
}
# Listar alunos em cada atividade por sala

for nome_Atividade in escola["aula"]:
    # sala1 que tem interseção com atividade
    atividade_Sala1 = set(escola["sala1"]) & set(escola["aula"][nome_Atividade])
    atividade_Sala2 = set(escola["sala2"]) & set(escola["aula"][nome_Atividade])

    print(f"-Alunos da Sala 1 na aula de", nome_Atividade)
    for aluno in atividade_Sala1:
        print("--", aluno)

    print("=" * 15)

    print(f"-Alunos da Sala 2 na aula de", nome_Atividade)
    for aluno in atividade_Sala2:
        print("--", aluno)
    print("=" * 15)