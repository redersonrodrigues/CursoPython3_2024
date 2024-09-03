"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""
# print('Várias')

# def Falar():
#     print('falar')

# Falar()

# def Print():
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# def imprimir(a,b,c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# imprimir(1,2,3)

# def imprimir(a,b,c):
#     print(a,b,c)

# imprimir(1,2,3)
# imprimir(4,5,6)

def saudacao(nome = 'Sem Nome'):
    print(f'Olá, {nome}!')

saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()