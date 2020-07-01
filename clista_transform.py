employees = [
    {'name': 'Osenias', 'gender': 'M', 'salary': 2000.00},
    {'name': 'Gustavo', 'gender': 'M', 'salary': 3000.00},
    {'name': 'Tatiany', 'gender': 'F', 'salary': 4000.00},
    {'name': 'Monica', 'gender': 'F', 'salary': 2000.00},
    {'name': 'Josimar', 'gender': 'M', 'salary': 5000.00}
]

soma_masculino = [e['salary'] for e in employees if e['gender'] == 'M']
soma_feminino = [e['salary'] for e in employees if e['gender'] == 'F']

print('Soma masculino: {}'.format(sum(soma_masculino)))
print('Soma feminino: {}'.format(sum(soma_feminino)))