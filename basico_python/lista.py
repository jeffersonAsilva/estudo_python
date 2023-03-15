# LISTA
# Uma lista é um valor que contém diversos valores em uma sequência
# ordenada.
# EXEMPLO
spam = ['cat', 'bat', 'rat', 'elephant']

# Obtendo valores individuais de uma lista por meio de índices

spam[0]
spam[1]
spam[2]
spam[3]
# Índices negativos
spam[-1]
spam[-2]

# Obtendo sublistas com slices
spam[1:4]  # é uma lista com um slice (dois inteiros).

# Obtendo o tamanho de uma lista com len()
len(spam)

# Alterando valores de uma lista usando índices
spam[1] = 'aardvark'

# Removendo valores de listas usando instruções del
del spam[2]
