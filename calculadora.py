# Criando uma calculadora

numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo número: ')

# O input entende que estou entrando com uma variável, portanto vou converter para um float
resultado = float(numero1) + float(numero2)

# Usando o método capitalize() para tornar a primeira letra maiúscula
print(resultado)
