# exemplo 01
lista = [1, 2, 3, 4, 5]

for item in lista:
    print(item)

# exemplo 02
contador = 10

for item in range(0, contador):
    print(item)

# exemplo 02
for index, item in enumerate(lista):
    print('indice: {}, item: {}'.format(index, item))

# exemplo 04
funcionarios = []

funcionario1 = {'name': 'osenias', 'salario': 2000}
funcionario2 = {'name': 'gustavo', 'salario': 2000}
funcionario3 = {'name': 'tatiany', 'salario': 2000}

funcionarios.append(funcionario1)
funcionarios.append(funcionario2)
funcionarios.append(funcionario3)

for index, item in enumerate(funcionarios):
    print('funcionário {}'.format((index + 1)))
    print('nome: {}'.format(item.get('name')))
    print('salario: {}'.format(item.get('salario')))
    print('-----')





contador = 1

while contador <= 10:
    print(contador)
    contador += 1



