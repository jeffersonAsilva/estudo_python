# Manupulação de strings

# criando uma string
spam = "That is Alice's cat."

# Caracteres de scape
spam = 'Say hi to Bob\'s mother.'

# string pura
print(r'That is Carol\'s cat.')

# Indexação e slicing de strings

'''  
As strings usam índices e slices (fatias) do mesmo modo que as listas.
Podemos pensar na string 'Hello world!' como uma lista e em cada caractere
da string como um item com um índice correspondente.
'''
spam = 'Hello world!'
spam[0]

spam[4]

spam[-1]

spam[0:5]
# Métodos de string upper(), lower(), isupper() e islower()
spam = 'Hello world!'
spam = spam.upper()
spam

spam = spam.lower()
spam

# Métodos de string join() e split()
', '.join(['cats', 'rats', 'bats'])

'My name is Simon'.split()

# Justificando texto com rjust(), ljust() e center()
'Hello'.rjust(10)
'Hello'.ljust(20, '-')
'Hello'.center(20, '=')

# Removendo espaços em branco com strip(), rstrip() e lstrip()

spam = ' Hello World '
spam.strip()
spam.lstrip()
spam.rstrip()

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
