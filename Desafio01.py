print('-=-'*10)
print('''\033[7;40m         DESAFIO 01           \033[m''')
print('-=-'*10)
print('Preencha o fomulario abaixo')
nome = str(input('Qual é o seu nome? ')).strip()
sobrenome = str(input('Sobrenome? ')).strip()
idade = int(input('Quantos anos você tem?'))
peso = float(input('Quanto você pesa? '))
print('Data de nascimento')
data = int(input('Dia:'))
mes = str(input('Mês:'))
ano = int(input('ano:'))
print('\033[1mObrigado por responder o questionario {} {}'.format(nome, sobrenome))
print('\033[1mVocê tem {} anos e pesa {}Kg nasceu em {} de {} de {}'.format(idade, peso, data, mes, ano))
