from datetime import date, timedelta
from calendar import monthrange

dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))

data_informada = date(ano, mes, dia)

_, ultimo_dia_do_mes = monthrange(ano, mes)

data_proximo_mes = date(ano, mes, ultimo_dia_do_mes)

diff = data_proximo_mes - data_informada

# if mes == 12:
#     ano += 1
#     mes = 1
# else:
#     mes += 1

# dia = 1

# data_proximo_mes = date(ano, mes, dia)

# diff = (data_proximo_mes - data_informada) - timedelta(days=1)

contador = 0

for item in range(1, diff.days):
    data = data_informada + timedelta(days=item)
    if data.weekday() not in [5, 6]:
        contador += 1


print('Total de dias até o fim do mês sem sábado e domingo: ', contador)
