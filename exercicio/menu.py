from exercicio import actions

def menu():

    option = -1
    
    while not option == 0:
        print('1 - Add funcionário')
        print('2 - Listar funcionários')
        print('3 - Soma do salário dos homens')
        print('4 - Soma do salário das mulheres')
        print('0 - Sair')

        option = int(input('Digite sua opção: '))

        if option == 1:
            actions.add()
        elif option == 2:
            actions.listar()
        elif option == 3:
            print('Soma do salário dos homens: {}'.format(actions.somar_salario_homens()))
        elif option == 4:
            print('Soma do salário das mulheres: {}'.format(actions.somar_salario_mulheres()))
        else:
            print('Opção inválida')


menu()

