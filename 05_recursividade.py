# FATORIAL DE UM NÚMERO n
# É igual ao número n multiplicado por todos os seus antecessores até 1
#
# 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 (5040)
# 6! = 6 * 5 * 4 * 3 * 2 * 1 (720)
# 5! = 5 * 4 * 3 * 2 * 1 (120)
# 4! = 4 * 3 * 2 * 1 (24)
# 3! = 3 * 2 * 1 (6)
# 2! = 2 * 1 (2)
# 1! = 1 
# 0! = 1 (por convenção)
#
# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1 * 0!
#
# n! = n * (n - 1)! p/ n > 1

# Implementação iterativa (iter = caminho)
def fatorial(n):
    resultado = 1
    if(n > 1):
        # range começa no número n e vai descendo até 1
        for i in range(n, 1, -1):
            resultado *= i
            print(f'Resultado: {resultado}, i: {i}')
    return resultado

print(f'5! = {fatorial(5)}')
print(f'7! = {fatorial(7)}')

# n! = n * (n - 1)! p/ n > 1
# Recursividade ocorre quando a definição de uma função inclui a própria função sendo definida.
#
# Em programação, a recursividade se traduz quando uma função efetua chamadas a si própria.

# Implementação recursiva
def fatorial2(n):
    # Em uma função cursiva, condição de saída é aquela em que a função
    # é capaz de retornar um resultado SEM chamar novamente a si mesma.
    if n <= 1: # Condição de Saída
        return 1
    return n * fatorial2(n - 1)

print('------------------------------------------------------------------')
print(f'519! = {fatorial2(519)}')

#import sys
#print(sys.maxsize)
