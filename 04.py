numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
operacao = input('Digite a operação: ')

if operacao == '+':
    print('Soma é igual {}'.format( (numero1 + numero2) ))
elif operacao == '-':
    print('Subtração é igual {}'.format( (numero1 - numero2) ))
elif operacao == '*':
    print('Multiplicação é igual {}'.format( (numero1 * numero2) ))
elif operacao == '/':
    try:
        print('Divisão é igual {}'.format( (numero1 / numero2) ))
    except ZeroDivisionError:
        print('Divisão por zero inválida')
else:
    print('Operação inválida')