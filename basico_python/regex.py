# Obtendo REGEX no Python

import re

# buscando um numero de telefone
celular = re.compile(r'\d\d-\d\d\d\d-\d\d\d\d')

mo = celular.search('My number is 44-9914-4242.')

print('Este é o número do celular: ' + mo.group())

# buscando apenas partes do match

celular = re.compile(r'(\d\d)-(\d\d\d\d)-(\d\d\d\d)')

mo = celular.search('My number is 44-9914-4242.')

print('Este é o DD: ' + mo.group(1))
print('Este é o 4 primeiros digitos: ' + mo.group(2))
print('Este é o 4 ultimos digitos: ' + mo.group(3))

# Fazendo a correspondência de vários grupos com pipe

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()

mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()
