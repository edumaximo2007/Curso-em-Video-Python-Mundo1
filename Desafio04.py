print('-=-'*10)
print('''\033[7m         DESAFIO 04           \033[m''')
print('-=-'*10)
a = input('Digite algo:')
print('o tipo pimitivo desse valor e', type(a))
print('Só tem espaços?', a.isspace())
print('Contem números?', a.isnumeric())
print('Ele é alfanumerico?', a.isalnum())
print('E alfabetico? {}'.format(a.isalpha()))
print('Está em maiuscula? {}' .format(a.isupper()))
print('Está em minuscula? {}'.format(a.islower()))
print('Esta em decimal? {}'.format(a.isdecimal()))
print('Esta capitalizada?{}'.format(a.istitle()))
print('Parabéns você e nota 10!')
