"""Crie um dicionário alunos no formato: 
chave é o nome do aluno e valor é outro dicionário com idade e nota.
Depois, percorra alunos.items() e imprima cada registro."""

alunos = {
    "Maria": {"idade": 20, "nota": 8.5},
    "João": {"idade" : 19, "nota": 7.0},
    "Pedro": {"idade": 21, "nota": 9.0}
}

# impressão de resultados
for nome, dados in alunos.items():
    print(f"{nome}: {dados['idade']} anos, nota {dados['nota']} ")