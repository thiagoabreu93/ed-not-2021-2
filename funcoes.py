# importar valor da constante PI
#math é o nome da biblioteca onde pi se encontra
from math import pi

# função é um trecho de código que tem um nome e pode ter informações externas para fazder seu trabalho. Opcionalmente, uma função pode também produzir um valor de resultado. Uma função definida apenas uma vez e pode ser utilizada (chamada) várias vezes, evitando repetições de códigos. Existem funções já providas pela linguagem, como, por exemplo, len(), range() e sort(), e podemos também definir nossos próprias funções.

# os termos que aparecem entre parenteses são chamados de parâmetros ou argumentos
def imc(peso, altura): #definição ()
    """
        função que calcula o índice de massa corporéa (imc)
    """
    # trechos entre aspas triplas são um tipo especial de comentário chamado docstring, e servem para documentar o propósito de uma função ou uma classe.
    return peso / altura ** 2 # peso / (altura)²

# float(): converte o valor informado em um número com casas decimais (floating point)
    
p = float(input('Informe o peso da pessoa: '))
a = float(input('Informe a altura da pessoa: '))

#fazendo uma chamada à função imc()
resultado = imc(p, a)
print(f"O IMC calculado é {resultado}.")

def area_forma(base, altura, forma = "R"):
    """
        Função que calcula a área de uma das seguintes
        formas geométricas: retângulo, triângulo ou elipse
        Parâmetro forma: 
        "R" == retângulo (parâmetro opcional com valor padrão)
        "T" == triângulo
        "E" == elipse
    """
    area = 0
    if forma == "R": # retângulo
        area = base * altura
    elif forma == "T": # triângulo
        area = base * altura / 2
    elif forma == "E": # elipse
        area = (base / 2) * (altura / 2) * pi
    return area

print('-------------------------------------------------')

print(f"Retângulo 7.5x11: {area_forma(7.5, 11, 'R')}")
print(f"Triângulo 8x12: {area_forma(8, 12, 'T')}")
print(f"Círculo 15x15: {area_forma(15, 15, 'E')}")
print(f"Quadrado 9.5x9.5: {area_forma(9.5, 9.5)}")
