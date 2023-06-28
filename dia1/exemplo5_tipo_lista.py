# Listas, tipo list

# Declaração
instancias = ["i-abcdef", "i-abc123", "i-456def"]
print(instancias)
# Posição da lista inicia com 0
print("Primeiro item: ", instancias[0])
print("Segundo item: ", instancias[1])
instancias[1] = 'i-poi098'
print("Segundo item: ", instancias[1])

numeros = [2,3,5,7,8,4,7,8,5,11]
print("Quantidade de itens: ", len(numeros))
parte_1 = numeros[0:4]
parte_2 = numeros[4:8]
print(parte_1)
print(parte_2)
print("Último: ", numeros[-1])
print(instancias[0][0:3])

# Lista de listas
# matriz_diagonal = [
#     [1, 0, 0],
#     [0, 1, 0],
#     [0, 0, 1]
# ]
# print(matriz_diagonal[1][1])



