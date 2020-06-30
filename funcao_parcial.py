# from functools import partial as p
import functools
# import actions
from actions import multiplicacao


nova_funcao = functools.partial(multiplicacao, 10, 20)

print(nova_funcao(5))
print(nova_funcao(6))
