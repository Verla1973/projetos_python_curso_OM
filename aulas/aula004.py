# Script que calcula o imc de uma pessoa


nome = str(input('Digite seu nome completo: '))
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / altura**2
print(f'Olá {nome}!')
print(f'Sua altura é {altura:.2f},seu peso: {peso}')
print(f'Seu imc é: {imc:.2f}')
