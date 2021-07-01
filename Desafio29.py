print('-=-'*10)
print('''\033[7m          DESAFIO 29          \033[m''')
print('='*30)
print('')
print('''\033[1mEscreva um programa que leia a velocida de um carro.

Se ele ultrapassar 80km/h. mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.\033[m''')
print('')
v1 = int(input('Informe a velocidade nessa rodovia: '))
v2 = (v1 - 80) * 7
if v1 > 80:
   print('Você foi \033[1;31mMULTADO\033[m por excesso de velocidade em {}Km e sua multa ficou em R${:.2f}'.format(v1, v2))
print('\033[1mTenha um bom dia! Dirija com segurança!\033[m')