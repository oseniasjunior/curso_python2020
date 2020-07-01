employees = [
    {'name': 'Osenias', 'gender': 'M', 'salary': 2000.00},
    {'name': 'Gustavo', 'gender': 'M', 'salary': 3000.00},
    {'name': 'Tatiany', 'gender': 'F', 'salary': 4000.00},
    {'name': 'Monica', 'gender': 'F', 'salary': 2000.00},
    {'name': 'Josimar', 'gender': 'M', 'salary': 5000.00}
]

# i = iter(employees)

# print(next(i))
# print(next(i))

mulheres = list(filter(lambda employee: employee['gender'] == 'F', employees))

salario_mulheres = map(
    lambda emp: emp['salary'],
    filter(lambda employee: employee['gender'] == 'F', employees)
)

print(sum(salario_mulheres))

