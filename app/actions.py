from app.settings import employees

def add():
    employee = {}
    employee['name'] = input('Informe o nome: ')
    employee['gender'] = input('Informe o sexo (M - Masculino, F - Feminino): ')
    employee['salary'] = float(input('Informe o salário: '))
    employees.append(employee)

def listar():
    for e in employees:
        print('=========================')
        print('Nome: {}'.format(e.get('name')))
        print('Sexo: {}'.format(e.get('gender')))
        print('Salário: {}'.format(e.get('salary')))
        print('=========================')

def somar_salario_homens():
    return _somar_salarios('M')

def somar_salario_mulheres():
    return _somar_salarios('F')


def _somar_salarios(gender: str):
    return sum([e.get('salary') for e in employees if e.get('gender') == gender])