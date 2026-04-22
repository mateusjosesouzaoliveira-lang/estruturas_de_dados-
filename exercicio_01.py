#Crie uma lista vazia, adicione 3 itens, remova 1 item (se existir) e imprima a lista numerada.

lista_compras = []

# adição de item
lista_compras.append("arroz")
lista_compras.append("feijão")
lista_compras.append("macarrão")

# remoção de item
if "macarrão" in lista_compras:
    lista_compras.remove("macarrão")


# lista numerada

for i, item in enumerate(lista_compras, start=1):
    print(f"{i}. {item}")


