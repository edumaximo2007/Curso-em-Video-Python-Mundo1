import random
print('-=-'*10)
print('''\033[7m           DESAFIO 20          \033[m''')
print('-=-'*10)
print('')
print('\033[1mO mesmo professor do desafio anterio quer sortea a ordem de apresentação de trabalhos dos alunos.\nfaça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.\033[m')
print('')
p = str(input('Nome do primeiro aluno: '))
p1 = str(input('Nome do segundo aluno: '))
p2 = str(input('Nome do terceiro aluno: '))
p3 = str(input('Nome do quarto aluno: '))
li = [p, p1, p2, p3]
random.shuffle(li)
print('')
print('\033[1mA ordem de apresentação sera.\033[m ')
print(li)


#n = choice(['João', 'Pedro', 'Carla', 'Maria'])
#n1 = choice(['João', 'Pedro', 'Carla', 'Maria'])
#n2 = choice(['João', 'Pedro', 'Carla', 'Maria'])
#n3 = choice(['João', 'Pedro', 'Carla', 'Maria'])
#print('O 1º{}'.format(n))
#print('O 2º{}'.format(n1))
#print('O 3º{}'.format(n2))
#print('O 4º{}'.format(n3))



