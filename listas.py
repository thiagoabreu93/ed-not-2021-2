# Criando uma lista
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Percurso
for num in primos:
    print(num)

# Acrescentar novo elemento no fim da lista: append()
primos.append(31)
print(primos)

# Inserindo um elemento em uma posição específica: insert()
# 1º -> informa a posição de inserção
# 2º -> elemento a ser inserido
primos.insert(0, 1)
print(primos)

# Insere o valor 37 na posição 5
primos.insert(5, 37)
print(primos)

# Retirando o último elemento da lista: pop()
ultimo = primos.pop()
print(f'Último: {ultimo}')
print(primos)

# Removendo por valor: remove()
primos.remove(37)
print(primos)

# Removendo por posição: del()
# Removendo o elemento da posição 4
del primos[4]
print(primos)

# Fatiando uma lista
# Exibindo apenas do elemento da posição 0 (inclusive) à posição 7 (exclusive)
print(primos[0:7])

# Da posição 2 à posição 8
print(primos[2:8])

# Fatiando e criando uma sublista
sub_primos = primos[1:5]
print(sub_primos)
