print('-=-'*10)
print('''\033[7m]         DESAFIO 26          \033[m''')
print('='*30)
print('')
print('''\033[1mFaça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.\033[m''')
print('')
n1 = str(input('Digite um nome: ')).strip().upper()
n2 = n1.count('A')
print('Quantas vezes aparece a letra "A":{} '.format(n2))
n3 = n1.find('A') + 1
print('Em que posição a letra "a" aparece a primeira vez: {}'.format(n3))
n4 = n1.rfind('A') + 1
print('Em que posição a letra "a" aparece a última vez: {}'.format(n4))
print('\033[1mParabéns você concluiu esta tarefa!\033[m')
