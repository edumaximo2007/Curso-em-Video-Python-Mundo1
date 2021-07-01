print('-=-'*10)
print('''\033[7m         DESAFIO 05         \033[m''')
print('-=-'*10)
saudação = str(input('Olá tudo bem? ')).strip()
p1 = str(input('Qual é o seu nome? ')).strip()
if saudação == 'Sim, é você?':
    print('Estou bem {}, obrigado por perguntar, meu noome e Zoe.'.format(p1))
else:
    print('Que pena espero que seu dia fique melhor, meu nome é Zoe!!')
p3 = str(input('Poderia responder meu questionario {}? '.format(p1)))
if p3 =='Sim':
    print('Então vamos começar.')
else:
    print('Você não tem escolha.')
print('-=-'*30)
print('Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.')
n1 = int(input('Digite um valor: '))
n2 = n1 - 1
n3 = n1 + 1
print('Avaliando o número {} seu antecessor e {} e seu sucessor e {}'.format(n1,(n1-1), (n1+1)))
# print('o número antecessor e {} e seu sucessor e {}'.format(n2, n3))
print('')
print('Obrigado por responder meu questionario, volte sempre {}, até breve!'.format(p1))