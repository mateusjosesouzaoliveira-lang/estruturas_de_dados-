"""Crie um arquivo notas.txt 
com linhas no formato 
Nome:Nota e depois leia, converta para float
e calcule a média."""

# criando o arquivo
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("Maria:8.5\n")
    f.write("João:7.0\n")
    f.write("Pedro:9.0\n")
    f.write("Ana:6.5\n")

#lendo e claculando media
notas = []
with open("notas.txt", "r", encoding="utf-8") as f:
    for linha in f:
        nome, nota_str = linha.strip().split(":")
        nota = float(nota_str)
        notas.append(nota)
        print(f"{nome}: {nota}")


# media

if notas:
    media = sum(notas) / len(notas)
    print(f"\nA média das notas é: {media:.2f}")

