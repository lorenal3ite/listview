# Etapa 1 - Crie uma lista com os nomes de 5 objetos
objetos = ["mesa", "cama", "cadeira", "estante", "escrivaninha"]
print("lista de objetos criada")
print("--" * 50)

# Etapa 2 - Adicione mais um objeto ao final da lista
objetos.append("banco")
print("mais um objeto foi adicionado á lista")
print("--" * 50)

# Etapa 3 - Acesse o objeto que está na 2a posição
objeto_dois = objetos[1]
print("objeto na segunda posição acessado: ", objeto_dois)
print("--" * 50)

# Etapa 4  - Remova um objeto da lista
objetos.remove("cadeira")
print("um objeto foi removido da lista")
print("--" * 50)

# Etapa 5 - Exiba o tamanho da lista.
print(f"a lista tem {len(objetos)} elementos")
print("--" * 50)

# Etapa 6 - Mostre todos os itens com um laço for.
for item in objetos:
    print(item)
print("--" * 50)

# Etapa 7 - Verifique se 'cadeira' está na lista. Se sim remova-a, senão adicione.
if "cadeira" in objetos == False:
    objetos.append("banco")
elif "cadeira" in objetos == True:
    objetos.remove("cadeira")
print("objeto cadeira verificado na lista")
print("--" * 50)

# Etapa 8 - Ordene a lista em ordem alfabética.
objetos.sort()
print("lista em ordem alfabética:", objetos)
print("--" * 50)

# Etapa 9 - Exiba o primeiro e o último objeto.
primeiro_objeto = objetos[0]
ultimo_objeto = objetos[-1]
print(f"o primeiro objeto da lista é {primeiro_objeto}, o último objeto da lista é {ultimo_objeto}")
print("--" * 50)

# Etapa 10 - Limpe toda a lista
objetos.clear()
print("lista limpa por completo")