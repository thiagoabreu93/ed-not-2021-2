# ALGORITMO DE ORDENAÇÃO BUBBLE SORT
#
# Percorre a lista a ser ordenada em sucessivas passadas,
# trocando elementos adjacentes entre si quando o segundo
# for menor que o primeiro. Efetua tantas passadas quanto
# necessárias até que, na última passada, nenhuma troca seja
# efetuada.

def bubble_sort(lista):
    """
        Função que implementa o algoritmo de ordenação
        bubble sort.
    """
    while True: #loop eterno
        trocou = False
        # loop na lista até o penúltimo elemento:
        # len(lista) - 2
        # Ex. Em uma lista de 10 elementos, len(lista) == 10
        # A última posição estará em len(lista) - , ou seja, 9
        # A penúltima posição estará em len(lista) - 2 (8ºpos)
        for i in range(len(lista) - 2): # inicia nova passada
            if lista[i + 1] < lista[i]:
                # É necessário trocar
                lista[i + 1], lista[i] = lista[i], lista[i + 1] # Faz a troca 
                trocou = True

        # Se houve troca, a lista está ordenada e podemos    # interromper o loop while
        if not trocou: # trocou == False
            break # interrompe o while
