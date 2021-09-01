#   ALGORITMO DE ORDENAÇÃO MERGE SORT
#  
# No processo de ordenação, esse algoritmo "desmonta" o vetor original contendo N elementos até obter 
# N vetores de apenas um elemento cada um. Em seguida, usando a técnica de mesclagem (merge), 
# "remonta" o vetor, dessa vez com os elementos já em ordem.

def merge_sort(lista):
    """
        Função que complementa o algoritmo merge sort usando o método RECURSIVO
    """

    #print(f'Lista recebida: {lista}')

    # Só continua se a lista tiver mais de um elemento
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    # Gerar uma cópia da primeira metade da lista
    lista_esq = lista[:meio] # do início até o meio -1

    # Gerar uma cópia da segunda metade da lista
    lista_dir = lista[meio:] # do meio ao fim

    # Chamamos recursivamente a função para continuar
    # repartindo a lista em metades
    lista_esq = merge_sort(lista_esq)
    lista_dir = merge_sort(lista_dir)

    #print(f'>>> lista_esq: {lista_esq}')
    #print(f'>>> lista_dir: {lista_dir}')

    # Junta as duas metades em uma única lista, ordenada
    pos_esq = 0
    pos_dir = 0
    ordenada = [] # lista vazia

    # Compara os elementos de cada lista entre si 
    # e insere na lista ordenada o que for menor

    while pos_esq < len(lista_esq) and pos_dir < len(lista_dir):
        # O elemento que se encontra na lista da esquerda
        # é menor que o que se encontra na lista da direita
        if lista_esq[pos_esq] < lista_dir[pos_dir]:
            ordenada.append(lista_esq[pos_esq])
            pos_esq += 1
        # O contrário
        else:
            ordenada.append(lista_dir[pos_dir])
            pos_dir += 1

    sobra = None # A sobra da lista que ficou para trás

    if(pos_esq < pos_dir): #Houve sobra à esquerda
        sobra = lista_esq[pos_esq:] # sobra do pos_esq até o final
    else: # houve sobra à direita
        sobra = lista_dir[pos_dir:] # sobra do pos_dir até o final]
    
    #print(f'>>> final ordenada: {ordenada + sobra}')

    # Retornamos a lista final ordenada, composta da ordenada + sobra
    return ordenada + sobra # "soma" de 2 listas

####################################################################################

nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

nums_ord = merge_sort(nums)

print(nums_ord)

#####################################################################################

from data.nomes_desord import nomes
from time import time
import tracemalloc

ini = time()
tracemalloc.start() # inicia a medição de consumo de memória 

nomes_ord = merge_sort(nomes)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

print(nomes_ord)
print(f"Tempo: {fim - ini}")
print(f'Pico de memória: {mem_pico / 1024 / 1024}MB')

tracemalloc.stop() # finaliza a medição do consumo de memória
