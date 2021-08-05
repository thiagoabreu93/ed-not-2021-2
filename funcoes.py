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
