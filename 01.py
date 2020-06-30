palavra = input('Digite sua palavra: ')

palavra_invertida = palavra[::-1]

print('Sua palavra invertida é ' + palavra_invertida)
print('Sua palavra invertida {} '.format(palavra_invertida))
print('Sua palavra invertida {0} '.format(palavra_invertida))
print('Sua palavra invertida {palavra} '.format(palavra=palavra_invertida))

