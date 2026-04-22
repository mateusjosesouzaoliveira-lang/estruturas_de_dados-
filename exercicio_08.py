"""Dado um dicionário de notas 
{"João": 8.5, "Maria": 6.0, "Pedro": 9.0}, 
crie outro dicionário apenas com os aprovados
(nota >= 7) usando compreensão."""

notas = {"João": 8.5, "Maria": 6.0, "Pedro": 9.0}

aprovados = {nome: nota for nome, nota in notas.items() if nota >= 7}

print(aprovados)