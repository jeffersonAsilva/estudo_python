# DICIONÁRIO
'''
Assim como uma lista, um dicionário (dictionary) é uma coleção de diversos
valores. Porém, de modo diferente das listas, os índices dos dicionários
podem utilizar vários tipos de dados diferentes, e não apenas inteiros. Os
índices nos dicionários são chamados de chaves (keys), e uma chave
juntamente com seu valor associado é chamada de par chave-valor (key-value
pair)

'''
# EXEMPLO
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

# Métodos keys(), values() e items()

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)
