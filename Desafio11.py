print('-=-'*10)
print('''\033[7m         DESAFIO 11           \033[m''')
print('-=-'*10)
print('')
print('\033[1mFaça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área \ne a quantidade de tinta necessária para tintá-la, sabendo que cada litro de tinta pinta uma área de 2m²\033[m.')
print('')
p1 = str(input('Podemos começar? '))
if p1 == 'Sim':
    print('Responda abaixo.')
else:
    print('Você não tem essa opção inseto maldito hahahaha')
print('')
la = float(input('Largura da parede: '))
al = float(input('Altura da parede: '))
t1 = la*al
print('A parede tem {}x{} e sua àrea tem {:.3}m²'.format(la, al, t1))
print('='*50)
lt = float(input('Coloque aqui quantos m² 1l de tinta pinta de acordo com o rotulo: '))
print('1l pinta {}m² '.format(lt))
ti = t1 / lt
print('Para pintar essa parede, você precisa de {:.2}l de tinta'.format(ti))
print('='*50)
print('\033[1mParabéns você concluiu esta tarefa!\033[m')
