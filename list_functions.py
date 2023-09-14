numeros = [3, 4, 11, 7, 8, 9, 1]
amigos = ['Bia', 'Lua', 'Maria', 'Julia', 'Lola']

# Adicionando duas listas como se fossem uma só

print(amigos)
# amigos.extend(numeros)
print(amigos)

# Adicionando itens na lista
amigos.append('Carlos')
print(amigos)

# Adicionando itens na lista e definindo a posição
amigos.insert(1, 'Pedro')
print(amigos)

# Removendo itens da lista
amigos.remove('Lua')
print(amigos)

# Removendo a partir de um index
amigos.pop(3)
print(amigos)

# Verificando se um item existe na lista e retornando a posição dele
print(amigos.index('Pedro'))

# Contando quantos itens tem na lista
print(amigos.count('Carlos'))

# Organizando por ordem alfabética
amigos.sort()
print(amigos)

# Organizando por ordem numérica
numeros.sort()
print(numeros)