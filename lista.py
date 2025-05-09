# Etapa 1
objetos = ["mesa", "cama", "cadeira", "estante", "escrivaninha"]
print("lista de objetos criada")
print("--" * 50)

# Etapa 2
objetos.append("banco")
print("mais um objeto foi adicionado á lista")
print("--" * 50)

# Etapa 3
objeto_dois = objetos[1]
print("objeto na segunda posição acessado: ", objeto_dois)
print("--" * 50)

# Etapa 4
objetos.remove("cadeira")
print("um objeto foi removido da lista")
print("--" * 50)

# Etapa 5
print(f"a lista tem {len(objetos)} elementos")
print("--" * 50)

# Etapa 6
for item in objetos:
    print(item)
print("--" * 50)

# Etapa 7
if "cadeira" in objetos == False:
    objetos.append("banco")
elif "cadeira" in objetos == True:
    objetos.remove("cadeira")
print("objeto cadeira verificado na lista")
print("--" * 50)

# Etapa 8
objetos.sort()
print("lista em ordem alfabética:", objetos)
print("--" * 50)

# Etapa 9
primeiro_objeto = objetos[0]
ultimo_objeto = objetos[-1]
print(f"o primeiro objeto da lista é {primeiro_objeto}, o último objeto da lista é {ultimo_objeto}")
print("--" * 50)

# Etapa
objetos.clear()
print("lista limpa por completo")