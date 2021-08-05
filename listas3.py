frutas = ["laranja", "maçã", "uva", "pêra", "mamão", "abacate", "amora"]

#imprimindo apenas a fruta "uva"
print(frutas[2])

# Substituindo "pêra" por "melão"
frutas[3] = "melão"
print(frutas)

# Descobrindo quantas elementos há na lista
print(len(frutas))

print('-------------------------------------')

# percorrendo e imprimindo cada um dos elementos da lista
for fruta in frutas:
    print(fruta)

print('-------------------------------------')

# percorrendo e imprimindo cada elemento e sua posição
for i in range(len(frutas)):
    print(f"{frutas[i]} está na posição {i}")

print('-------------------------------------')

#percurso em ordem invertida
# 1º argumento: len(frutas) -1: a lista precisa começar no último elemento, que é determinado por len() -1
# 2º argumento: -1, porque o limite final não entra e precisamos terminar em 0
# 3º argumento: -1, porque a lista precisa ser decrescente
for j in range(len(frutas) -1, -1, -1):
    print(frutas[j])

print('-------------------------------------')

#ordenando vetor em ordem alfabética
frutas.sort()
print(frutas)

