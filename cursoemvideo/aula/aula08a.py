from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

# floor: arredonda pra baixo; ceil: arredonda pra cima;
# import math: importa toda a biblioteca de matemática;
# from math import: importa somente o comando desejado da biblioteca math;
