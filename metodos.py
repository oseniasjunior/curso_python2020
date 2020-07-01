# def somar(a: int, b: int) -> int:
#     return a + b


# if __name__ == '__main__':
#     resultado = somar(10, 20)
#     print(resultado)


# funcao = lambda : print('osenias')
# somar = lambda a, b: a + b
# subtrair = lambda a, b: a - b

# print(type(funcao))

# print(somar(10, 20))
# print(subtrair(10, 20))


# def somar(a, b):
#     return a + b

# def subtrair(a, b, c):
#     return a - b - c

# parametros = {'a': 20, 'b': 30}

# def funcao3(fn, incremento, **kwargs):
#     r = fn(**kwargs)
#     return r + incremento


# a = funcao3(fn=somar, incremento=100, a=10, b=20)
# b = funcao3(fn=subtrair, incremento=100, a=10, b=10, c=50)

# print(a)
# print(b)



# def somar_varios_numeros(*args):
#     acumulador = 0

#     for i in args:
#         acumulador += i

#     return acumulador


# print(somar_varios_numeros(1, 2))
# print(somar_varios_numeros(1, 2, 3))
# print(somar_varios_numeros(1, 2, 3, 4))
# print(somar_varios_numeros(1, 2, 3, 4, 5))




def somar_e_subtrair(a, b):
    soma = a + b
    subtracacao = a - b

    return soma, subtracacao


a, b = somar_e_subtrair(10, 20)


print('a: {}, b: {}'.format(a, b))








