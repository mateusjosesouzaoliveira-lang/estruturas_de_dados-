""""Crie um dicionário pessoa = {"nome": "João", "idade": 25}. Acesse o nome diretamente 
e o telefone usando get() com valor padrão "(não informado)"."""

pessoa = {"nome": "João", "idade": 25}


print("nome:", pessoa["nome"])
print("telefone:", pessoa.get("telefone", "(não informado)"))