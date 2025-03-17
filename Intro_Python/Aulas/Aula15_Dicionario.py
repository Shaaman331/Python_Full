pessoas = {"nome" : "Tarcisio ", "idade" : "32", "cep" : "12345678"}
pessoas ["nome"] = "Lucca"

print(pessoas)

z = {"nomes01": [], "idade": 22}
z["nomes01"].append("Lucca")
z ["nomes01"].append("Raquel")
print(z)


for pessoa in pessoas:
    print(type(pessoa))
    