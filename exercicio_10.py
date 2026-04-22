""""
Crie um arquivo CSV pessoas.csv 
com colunas Nome, Idade, Cidade. 
Depois leia o arquivo, 
filtre apenas as pessoas com idade >= 18 e salve em pessoas_maiores.csv."""

import csv

dados = [
    {"Nome": "João", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Maria", "Idade": 17, "Cidade": "Rio de Janeiro"},
    {"Nome": "Pedro", "Idade": 30, "Cidade": "Belo Horizonte"},
]

campos = ["Nome", "Idade", "Cidade"]

# escrevendo no arquivo

with open("pessoas.csv", "w", encoding="utf-8", newline="" ) as f:
    writer = csv.DictWriter(f, fieldnames= campos)
    writer.writeheader()
    writer.writerows(dados)

print("Arquivo pessoas.csv criado com sucesso.")

# lendo o arquivo

with open("pessoas.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    pessoas = list(reader)

#filtrando e escrevendo outro csv so com maiores de idade
maiores = [p for p in pessoas if int(p["Idade"]) >= 18]

with open("pessoas_maiores.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames= campos)
    writer.writeheader()
    writer.writerows(maiores)

print(f"Arquivo pessoas_maiores.csv criado com {len(maiores)} registros")